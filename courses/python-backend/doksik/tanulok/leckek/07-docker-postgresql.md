# Lecke 07 – Docker és PostgreSQL

> **Dokumentáció:** [Docker Getting Started](https://docs.docker.com/get-started/) · [PostgreSQL Docker](https://hub.docker.com/_/postgres) · [Docker Compose](https://docs.docker.com/compose/)

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

### Docker telepítés

**Linux:**

```bash
sudo apt update
sudo apt install docker.io docker-compose-v2
sudo usermod -aG docker $USER
# Jelentkezz ki és be, hogy érvényesüljön!
```

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

### Csatlakozás psql-lel

```bash
docker exec -it postgres-db psql -U kurzus -d backenddb
```

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

---

## Gyakorlat

1. Telepítsd a Dockert (ha még nincs)
2. Indíts egy PostgreSQL konténert
3. Csatlakozz psql-lel és hozz létre egy táblát
4. Készíts `docker-compose.yml`-t FastAPI + PostgreSQL-hez
5. Commitold és pushold
