# 📘 Lecke 07 – Docker és PostgreSQL

> 📚 Dokumentáció:
> https://docs.docker.com/get-started/
> https://hub.docker.com/_/postgres
> https://docs.docker.com/compose/

---

## 43–44. óra: Docker alapok

### Mi az a Docker?

A Docker **konténereket** használ az alkalmazások futtatására. Egy konténer egy könnyű, izolált környezet, ami tartalmazza az alkalmazást és az összes függőségét.

| Fogalom | Leírás |
|---------|--------|
| **Image** | Egy „recept" – megmondja, mit tartalmaz a konténer |
| **Container** | Egy futó példány az image-ből |
| **Dockerfile** | Az image leírása (utasítások) |
| **Volume** | Tartós tárolás (adatok megmaradnak újraindítás után) |

### 🧠 Részletes Magyarázat

- **Konténer vs. virtuális gép** – A konténer az operációs rendszer kernelét osztja meg a gazdagéppel, ezért sokkal könnyebb és gyorsabb, mint egy teljes virtuális gép. Másodpercek alatt indul, és minimális memóriát használ.
- **Image (kép)** – Egy csak olvasható sablon. Gondolj rá úgy, mint egy tortarecept: a recept maga nem ehető, de bármikor süthetünk belőle tortát (konténert). Egy image-ből akárhány konténert indíthatunk.
- **Container (konténer)** – Az image futó példánya. Ha az image a recept, a konténer a sütemény. Mindegyik konténer saját fájlrendszerrel fut, nem látják egymás adatait.
- **Volume (kötet)** – A konténerek alapértelmezetten elveszítik az adataikat leállításkor. A volume-ok külső tárolók, amik megőrzik az adatokat. Adatbázisoknál elengedhetetlen!

### Docker telepítés

**Linux:**

```bash
sudo apt update
sudo apt install docker.io docker-compose-v2
sudo usermod -aG docker $USER
# Jelentkezz ki és be, hogy érvényesüljön!
```

### 🧠 Részletes Magyarázat

- **`docker.io`** – A Docker motor csomagja Linuxon. Ez tartalmazza a `docker` CLI-t és a háttérszolgáltatást (daemon).
- **`docker-compose-v2`** – A Docker Compose v2 plugin, ami a `docker compose` (szóközzel!) parancsot adja. A régi `docker-compose` (kötőjellel) elavult.
- **`usermod -aG docker $USER`** – A `docker` csoportba teszi a felhasználót, hogy ne kelljen `sudo` minden docker parancs elé. A `-aG` jelentése: **a**dd to **G**roup (hozzáadás a csoporthoz, a meglévő csoportok megtartásával).

**Windows:**

1. Töltsd le és telepítsd a [Docker Desktop](https://www.docker.com/products/docker-desktop/)-ot
2. A telepítő bekapcsolja a WSL2 intégrációt (ajánlott) vagy Hyper-V-t
3. Újraindítás után ellenőrizd:

```bash
docker --version
docker compose version
```

### Dockerfile Python alkalmazáshoz

```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### 🧠 Részletes Magyarázat

A Dockerfile utasításonként épít egy image-et. Minden sor egy új „réteget" (layer) hoz létre:

| Utasítás | Mit csinál |
|----------|-----------|
| `FROM python:3.10-slim` | Alap image: Python 3.10 minimális Linuxon (slim = kis méret) |
| `WORKDIR /app` | A konténeren belüli munkakönyvtár (ha nem létezik, létrehozza) |
| `COPY requirements.txt .` | A helyi `requirements.txt`-t bemásolja a konténerbe |
| `RUN pip install ...` | Telepíti a Python csomagokat a konténerbe |
| `COPY . .` | Az összes projektfájlt bemásolja |
| `CMD [...]` | A konténer indulásakor futó parancs |

- **Miért külön `COPY requirements.txt` és `COPY . .`?** – Docker cache optimalizáció! Ha csak a kód változik (nem a requirements), a `pip install` réteg újrahasználódik a cache-ből, és a build percek helyett másodpercek alatt kész.
- **`--no-cache-dir`** – A pip nem menti le a letöltött csomagokat a cache-be. Konténerben nincs szükség rá, és kisebb image-et eredményez.
- **`0.0.0.0`** – A konténeren belül a szerver minden hálózati interfészen figyel. Ha `127.0.0.1`-et írnánk, a konténeren kívülről nem lenne elérhető.

### Docker parancsok

```bash
# Image építése
docker build -t fastapi-app .

# Konténer indítása
docker run -d -p 8000:8000 --name api fastapi-app

# Futó konténerek
docker ps

# Napló
docker logs api

# Leállítás
docker stop api

# Törlés
docker rm api
```

### 🧠 Részletes Magyarázat

| Parancs | Paraméterek | Jelentés |
|---------|------------|----------|
| `docker build` | `-t fastapi-app .` | Image építése, név: `fastapi-app`, kontextus: aktuális mappa (`.`) |
| `docker run` | `-d` | **D**etached mód: háttérben fut |
| | `-p 8000:8000` | **P**ort mapping: `gazda:konténer`. A gép 8000-es portja a konténer 8000-es portjára mutat |
| | `--name api` | A konténer neve (ezzel hivatkozunk rá) |
| `docker ps` | | Futó konténerek listája (hozzáadható `-a` a leállítottakhoz is) |
| `docker logs` | `api` | A megnevezett konténer kimenete (stdout/stderr) |
| `docker stop` | `api` | Graceful leállítás (SIGTERM, majd SIGKILL) |
| `docker rm` | `api` | Konténer törlése (csak leállított konténerre) |

---

## 45–46. óra: PostgreSQL Dockerben

### PostgreSQL indítása

```bash
docker run -d \
  --name postgres-db \
  -e POSTGRES_USER=kurzus \
  -e POSTGRES_PASSWORD=jelszo123 \
  -e POSTGRES_DB=backenddb \
  -p 5432:5432 \
  -v pgdata:/var/lib/postgresql/data \
  postgres:16
```

### 🧠 Részletes Magyarázat

- **`docker run -d`** – Háttérben indítja az adatbázis konténert.
- **`-e` (environment)** – Környezeti változók átadása a konténernek. A PostgreSQL image ezeket használja az inicializáláshoz:

| Változó | Jelentés |
|---------|----------|
| `POSTGRES_USER` | Az adatbázis felhasználó neve |
| `POSTGRES_PASSWORD` | A felhasználó jelszava |
| `POSTGRES_DB` | Az automatikusan létrehozott adatbázis neve |

- **`-p 5432:5432`** – A gép 5432-es portja a konténer 5432-es portjára mutat. Így a Python alkalmazásunk `localhost:5432`-n éri el az adatbázist.
- **`-v pgdata:/var/lib/postgresql/data`** – **Named volume**: a `pgdata` nevű Docker volume a konténer `/var/lib/postgresql/data` mappájára van csatolva. Ez biztosítja, hogy az adatok **megmaradnak** a konténer újraindítása vagy törlése után is.

### Csatlakozás psql-lel

```bash
docker exec -it postgres-db psql -U kurzus -d backenddb
```

### 🧠 Részletes Magyarázat

- **`docker exec`** – Parancs futtatása egy **már futó** konténerben (nem indul új konténer).
- **`-it`** – **I**nteractive + **T**TY: interaktív terminál, ahol gépelhetünk. Nélküle a `psql` azonnal kilépne.
- **`psql`** – A PostgreSQL parancssori kliense. A `-U kurzus` a felhasználót, a `-d backenddb` az adatbázist adja meg.

### Alapszintű SQL

```sql
-- Tábla létrehozása
CREATE TABLE termekek (
    id SERIAL PRIMARY KEY,
    nev VARCHAR(100) NOT NULL,
    ar DECIMAL(10, 2) NOT NULL,
    leiras TEXT
);

-- Adatok beszúrása
INSERT INTO termekek (nev, ar, leiras) VALUES ('Laptop', 299990, 'Erős laptop');
INSERT INTO termekek (nev, ar, leiras) VALUES ('Egér', 5990, 'Vezeték nélküli');

-- Lekérdezés
SELECT * FROM termekek;
SELECT nev, ar FROM termekek WHERE ar > 10000;

-- Módosítás
UPDATE termekek SET ar = 279990 WHERE id = 1;

-- Törlés
DELETE FROM termekek WHERE id = 2;
```

### 🧠 Részletes Magyarázat

| SQL parancs | Jelentés | CRUD művelet |
|-------------|----------|-------------|
| `CREATE TABLE` | Tábla létrehozása oszlop-definíciókkal | – |
| `INSERT INTO` | Új sor beszúrása | **C**reate |
| `SELECT` | Adatok lekérdezése | **R**ead |
| `UPDATE` | Meglévő sor módosítása | **U**pdate |
| `DELETE` | Sor törlése | **D**elete |

- **`SERIAL PRIMARY KEY`** – Automatikusan növekvő egész szám. Minden új sor kap egy egyedi `id`-t anélkül, hogy megadnánk. A `PRIMARY KEY` biztosítja, hogy az érték egyedi és nem lehet NULL.
- **`VARCHAR(100)` vs. `TEXT`** – A `VARCHAR(100)` legfeljebb 100 karakter hosszú szöveg, a `TEXT` korlátlan. A `VARCHAR` validálást ad, a `TEXT` rugalmasabb.
- **`NOT NULL`** – A mező kötelező, nem lehet üres. Ha megpróbálunk NULL-t beszúrni, az adatbázis hibát dob.
- **`DECIMAL(10, 2)`** – Pontos tizedes szám: összesen 10 számjegy, ebből 2 a tizedes vessző után. Pénzügyi adatoknál jobb, mint a `FLOAT` (ami kerekítési hibákat okozhat).
- **`WHERE`** – Szűrési feltétel. Az `ar > 10000` csak azokat a sorokat adja vissza, ahol az ár nagyobb mint 10000. Nélküle az összes sort kapjuk.

---

## 47–48. óra: Docker Compose bevezetés

Egy `docker-compose.yml` fájlban **több szolgáltatást** definiálunk:

```yaml
services:
  db:
    image: postgres:16
    environment:
      POSTGRES_USER: kurzus
      POSTGRES_PASSWORD: jelszo123
      POSTGRES_DB: backenddb
    ports:
      - "5432:5432"
    volumes:
      - pgdata:/var/lib/postgresql/data

  app:
    build: .
    ports:
      - "8000:8000"
    depends_on:
      - db
    environment:
      DATABASE_URL: postgresql://kurzus:jelszo123@db:5432/backenddb

volumes:
  pgdata:
```

### 🧠 Részletes Magyarázat

- **Docker Compose** – Eszköz, amivel egyetlen fájlban definiálunk és kezelünk **több konténert** együtt. Ahelyett, hogy 2-3 `docker run` parancsot futtatnánk kézzel, a `docker compose up` mindent elindít.
- **`services`** – A szolgáltatások (konténerek) listája. Mindegyik szolgáltatásnak van neve (`db`, `app`), ami a Docker belső hálózatán hostnévként is működik.
- **`image: postgres:16`** – A `db` szolgáltatás a hivatalos PostgreSQL 16-os image-et használja a Docker Hub-ról.
- **`build: .`** – Az `app` szolgáltatást az aktuális mappából építi (a `Dockerfile` alapján).
- **`depends_on: [db]`** – Az `app` csak a `db` után indul el. Ez **sorrendet** biztosít, de nem várja meg, hogy az adatbázis teljesen kész legyen (csak az indulást).
- **`@db:5432`** – A `DATABASE_URL`-ben `localhost` helyett `db`-t írunk! Compose-ban a szolgáltatások nevükkel érik el egymást a belső hálózaton. Az `app` konténer a `db` hosztot a PostgreSQL konténerre oldja fel.
- **`volumes: pgdata:`** – A fájl végén deklaráljuk a named volume-ot. Ez a Docker által kezelt tartós tárolás.

### Docker Compose parancsok

```bash
# Indítás
docker compose up -d

# Naplók
docker compose logs -f

# Leállítás
docker compose down

# Újraépítés
docker compose up -d --build
```

### 🧠 Részletes Magyarázat

| Parancs | Mit csinál |
|---------|-----------|
| `docker compose up -d` | Elindítja az összes szolgáltatást háttérben. Ha image nincs, megépíti. |
| `docker compose logs -f` | **F**ollow: a naplókat élőben mutatja (Ctrl+C kilépés) |
| `docker compose down` | Leállítja és **törli** a konténereket (de a volume-ok megmaradnak!) |
| `docker compose up -d --build` | Újraépíti az image-eket (kódváltozás után szükséges) |

- **`down` vs. `stop`** – A `down` törli a konténereket, a `stop` csak leállítja. A `down` után `up`-pal újra kell építeni, a `stop` után `start`-tal folytatható. Volume-okat egyik sem törli (ahhoz `down -v` kell).

---

## Gyakorlat

1. Telepítsd a Dockert (ha még nincs)
2. Indíts egy PostgreSQL konténert
3. Csatlakozz psql-lel és hozz létre egy táblát
4. Készíts `docker-compose.yml`-t FastAPI + PostgreSQL-hez
5. Commitold és pushold
