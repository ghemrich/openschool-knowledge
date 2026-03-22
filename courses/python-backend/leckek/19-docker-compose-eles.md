# 📘 Lecke 19 – Docker Compose éles környezet

> 📚 Dokumentáció:
> https://docs.docker.com/compose/
> https://docs.docker.com/engine/reference/builder/
> https://docs.docker.com/build/building/multi-stage/

---

## 115–116. óra: Production Dockerfile

### Fejlesztői vs. éles Dockerfile

Fejlesztéskor: `uvicorn --reload` (forró újratöltés). Élesben: nincs reload, optimalizált image.

### Multi-stage Dockerfile

```dockerfile
# Dockerfile
FROM python:3.11-slim AS base

WORKDIR /app

# Csak a requirements.txt másolása (cache kihasználás)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Alkalmazás másolása
COPY app/ ./app/
COPY alembic/ ./alembic/
COPY alembic.ini .

# Port
EXPOSE 8000

# Indítás
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### 🧠 Részletes Magyarázat

- **`FROM python:3.11-slim`** – A `slim` verzió kevesebb csomagot tartalmaz, mint a teljes image (~150 MB vs ~900 MB). Éles rendszernél fontos a méret: gyorsabb letöltés, kisebb támadási felület.
- **`WORKDIR /app`** – A konténeren belüli munkakönyvtár. Minden további `COPY` és `RUN` parancs ide vonatkozik.
- **Rétegezés és cache:**
  1. Először csak a `requirements.txt`-t másolja → ha ez nem változik, a `pip install` réteg cache-ből jön
  2. Utána az alkalmazás kódját → ha csak a kód változik, a pip install nem fut újra
- **`--no-cache-dir`** – A pip nem tárolja a letöltött csomagokat. A konténerben nincs szükség cache-re, csak helyet foglalna.
- **`EXPOSE 8000`** – Dokumentáció: jelzi, hogy a konténer a 8000-es porton hallgat. Önmagában nem nyit portot!
- **`CMD` vs. `--reload`** – Élesben **nincs** `--reload`. A reload fejlesztői funkció (fájlváltozás figyelés), ami biztonsági kockázat és teljesítménycsökkenés élesben.

### .dockerignore

```
__pycache__
*.pyc
.env
.git
.venv
tests/
uploads/
*.md
```

### 🧠 Részletes Magyarázat

- **`.dockerignore`** – A `.gitignore` Dockeres megfelelője. Az itt felsorolt fájlokat a `COPY` parancs **nem** másolja be a konténerbe.
- **Miért fontos?**
  - `.env` – Titkos adatokat tartalmaz → a Docker image-be ha bekerülne, bárki kiolvashatná
  - `.git/` – A teljes git történet feleslegesen növelné az image méretét
  - `tests/` – Az éles konténerben nem kell teszt kód
  - `__pycache__/` – Build artifact, a konténerben újra generálódik

---

## 117–118. óra: Docker Compose teljes alkalmazás

### docker-compose.yml

```yaml
services:
  db:
    image: postgres:16-alpine
    environment:
      POSTGRES_DB: backend_db
      POSTGRES_USER: admin
      POSTGRES_PASSWORD: ${DB_PASSWORD}
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U admin -d backend_db"]
      interval: 5s
      timeout: 5s
      retries: 5

  api:
    build: .
    ports:
      - "8000:8000"
    environment:
      DATABASE_URL: postgresql://admin:${DB_PASSWORD}@db:5432/backend_db
      SECRET_KEY: ${SECRET_KEY}
    depends_on:
      db:
        condition: service_healthy
    volumes:
      - uploads_data:/app/uploads

volumes:
  postgres_data:
  uploads_data:
```

### 🧠 Részletes Magyarázat

- **`${DB_PASSWORD}`** – Környezeti változó, amit a Docker Compose a `.env` fájlból olvas. A jelszó **nem** van beégve a YAML-be.
- **`healthcheck`** – A `pg_isready` parancs ellenőrzi, hogy a PostgreSQL fogad-e kapcsolatokat. 5 másodpercenként próbálkozik, max 5-ször. Amíg nem „healthy", az API nem indul el.
- **`depends_on: condition: service_healthy`** – Az API konténer **megvárja**, amíg a DB „healthy" állapotba kerül. Nélküle az API elindulhat a DB előtt, és hibázik.
- **Named volumes (`postgres_data`, `uploads_data`):**
  - `postgres_data` – Az adatbázis fájljai. A `docker compose down` nem törli (csak a `docker compose down -v`).
  - `uploads_data` – A feltöltött fájlok. Szintén megmarad a konténer újraindítása után.
- **`@db:5432`** – A Docker Compose hálózatában a service neve mint DNS hostname működik. Az `api` konténerből a `db` hostnévvel érhető el a PostgreSQL.

### .env fájl (Docker Compose használja)

```env
DB_PASSWORD=biztonsagos_jelszo_123
SECRET_KEY=nagyon_titkos_kulcs_456
```

### 🧠 Részletes Magyarázat

- **`.env`** – A Docker Compose automatikusan beolvassa a `.env` fájlt a projekt gyökeréből. A `${DB_PASSWORD}` hivatkozások a YAML-ben ezekre az értékekre mutatnak.
- **`.env` a `.gitignore`-ban** – A `.env` fájl **soha** nem kerülhet a Git repóba. Ehelyett `.env.example` fájlt hozunk létre placeholder értékekkel:
  ```
  DB_PASSWORD=valtoztasd_meg
  SECRET_KEY=valtoztasd_meg
  ```

### Parancsok

```bash
# Építés és indítás
docker compose up --build

# Háttérben
docker compose up -d --build

# Naplók
docker compose logs -f api
docker compose logs -f db

# Leállítás
docker compose down

# Leállítás + adatok törlése
docker compose down -v
```

### 🧠 Részletes Magyarázat

| Parancs | Mit csinál |
|---------|-----------|
| `docker compose up --build` | Image-eket újraépíti + konténereket indít. **Ez a leggyakrabban használt.** |
| `docker compose up -d --build` | Ugyanaz, de háttérben fut (**d**etached). A terminál szabad marad. |
| `docker compose logs -f api` | Az `api` konténer naplóit mutatja valós időben. `-f` = follow. |
| `docker compose down` | Leállítja és törli a konténereket. Az adatok (volumes) **megmaradnak**. |
| `docker compose down -v` | Leállít + **volumes-t is törli**. **Veszélyes:** az adatbázis tartalma törlődik! |

---

## 119–120. óra: Migrációk és healthcheck

### Alembic futtatás Docker-ben

```yaml
# docker-compose.yml kiegészítés
  migrate:
    build: .
    command: alembic upgrade head
    environment:
      DATABASE_URL: postgresql://admin:${DB_PASSWORD}@db:5432/backend_db
    depends_on:
      db:
        condition: service_healthy
```

```bash
# Migráció futtatás
docker compose run --rm migrate
```

### 🧠 Részletes Magyarázat

- **`migrate` service** – Egy külön konténer, ami csak az Alembic migrációt futtatja, majd kilép. A `command:` felülírja a Dockerfile `CMD`-jét.
- **`docker compose run --rm migrate`** – Egyszer futtatja a `migrate` service-t, majd törli a konténert (`--rm`). Nem indítja el az `api` konténert.
- **Miért külön?** – Így a migráció és a szerver indítás szétválik. Ha a migráció hibázik, a szerver nem indul el „félig migrált" adatbázissal.

### Vagy entrypoint scripttel

```bash
#!/bin/bash
# entrypoint.sh
set -e

echo "Migrációk futtatása..."
alembic upgrade head

echo "Szerver indítása..."
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

```dockerfile
COPY entrypoint.sh .
RUN chmod +x entrypoint.sh
CMD ["./entrypoint.sh"]
```

### 🧠 Részletes Magyarázat

- **`entrypoint.sh`** – Bash script, ami az induláskor automatikusan: (1) migrációkat futtat, (2) elindítja a szervert. Egyszerűbb, mint külön`migrate` service.
- **`set -e`** – Ha bármelyik parancs hibázik (nem-nulla exit code), a script azonnal kilép. Így ha az `alembic upgrade head` elbukik, a szerver nem indul el.
- **`chmod +x`** – Futtatási jogot ad a scriptnek. Nélküle a konténer „Permission denied" hibát ad.
- **Melyiket válasszam?** – Kis projekteknél az entrypoint script egyszerűbb. Nagyobb rendszereknél a külön migrate service jobb, mert a CI/CD pipeline-ban is használható.

### API healthcheck

```python
@app.get("/health")
def health_check(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        return {"status": "healthy", "database": "connected"}
    except Exception:
        raise HTTPException(503, detail="Database unavailable")
```

### 🧠 Részletes Magyarázat

- **`/health` végpont** – Speciális végpont, amit a Docker healthcheck (vagy load balancer) rendszeresen hív. Nem felhasználóknak szól, hanem az infrastruktúrának.
- **`db.execute(text("SELECT 1"))`** – Minimális SQL lekérdezés, ami teszteli, hogy az adatbázis elérhető-e. Ha igen → „healthy". Ha nem → 503 (Service Unavailable).
- **`503`** – HTTP státuszkód: „Service Unavailable". Jelzi, hogy a szerver fut, de nem tud dolgozni (db nem elérhető).

```yaml
# docker-compose.yml
  api:
    ...
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      interval: 10s
      timeout: 5s
      retries: 3
```

### 🧠 Részletes Magyarázat

- **`curl -f`** – A `-f` (fail) flag: ha a HTTP válasz hibakód (4xx/5xx), a `curl` nem-nulla exit code-ot ad → a Docker „unhealthy"-nek tekinti.
- **`interval: 10s`** – 10 másodpercenként ellenőriz.
- **`retries: 3`** – 3 egymás utáni bukás után lesz „unhealthy".
- **Miért fontos?** – Ha a DB elérhetetlen, a Docker automatikusan „unhealthy" állapotba rakja az API-t. A load balancer észreveszi és nem küld több forgalmat.

### Hasznos Docker Compose parancsok

```bash
docker compose ps            # futó konténerek
docker compose exec api bash # shell az API konténerben
docker compose exec db psql -U admin -d backend_db  # psql
docker compose restart api   # újraindítás
docker compose build --no-cache  # cache nélkül újraépítés
```

### 🧠 Részletes Magyarázat

| Parancs | Mit csinál |
|---------|-----------|
| `docker compose ps` | Listázza a futó konténereket, állapotukat és portjaikat |
| `docker compose exec api bash` | Shell-t nyit a futó API konténerben. Hasznos hibakereséshez. |
| `docker compose exec db psql ...` | Közvetlenül a PostgreSQL kliensbe lép. SQL parancsok futtathatók. |
| `docker compose restart api` | Újraindítja az API konténert (a DB marad). |
| `docker compose build --no-cache` | Teljesen újra build-eli az image-et, a layer cache-et figyelmen kívül hagyva. |

---

## Gyakorlat

1. Készíts production Dockerfile-t `.dockerignore`-ral
2. Hozd létre a `docker-compose.yml`-t (api + db)
3. Add hozzá a `/health` végpontot az API-hoz
4. Indítsd el a teljes alkalmazást `docker compose up --build`-del
5. Futtasd a migrációkat Docker-ben
6. Commitold és pushold
