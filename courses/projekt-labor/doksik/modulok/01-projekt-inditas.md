# Modul 1 — Projekt indítás

## Cél

Egy üres, de teljesen konfigurált projekt felállítása. A modul végére:

- `docker compose up` → a backend fut, elérhető a health check
- A tesztek zöldek (pytest + TestClient)
- Minden push-ra lefut a CI (GitHub Actions)
- Az adatbázis Alembic-kel migrálható

## 1.1 Repó és mappastruktúra

A `openschool-platform` repó létrehozása és a kiinduló struktúra:

```
openschool-platform/
├── docker-compose.yml
├── docker-compose.prod.yml
├── .env.example
├── .github/
│   └── workflows/
│       └── ci.yml
├── Makefile
├── README.md
├── backend/
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── alembic.ini
│   ├── alembic/
│   │   ├── env.py
│   │   └── versions/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── config.py
│   │   ├── database.py
│   │   ├── models/
│   │   └── routers/
│   └── tests/
│       ├── conftest.py
│       └── test_health.py
└── frontend/           # üres, Modul 5-ben töltjük fel
```

**Feladat:**
- Hozd létre a repót és a mappastruktúrát
- Írd meg a `.env.example` fájlt a szükséges környezeti változókkal
- A `README.md` tartalmazzon futtatási útmutatót

## 1.2 Docker Compose

Három service a fejlesztői környezetben:

```yaml
services:
  backend:
    build: ./backend
    ports:
      - "8000:8000"
    depends_on:
      - db
    env_file: .env
    volumes:
      - ./backend:/app

  db:
    image: postgres:16
    environment:
      POSTGRES_USER: ${DB_USER}
      POSTGRES_PASSWORD: ${DB_PASSWORD}
      POSTGRES_DB: ${DB_NAME}
    ports:
      - "5432:5432"
    volumes:
      - pgdata:/var/lib/postgresql/data

  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
    volumes:
      - ./nginx/nginx.conf:/etc/nginx/nginx.conf
    depends_on:
      - backend

volumes:
  pgdata:
```

**Feladat:**
- Írd meg a `docker-compose.yml` fájlt
- A backend Dockerfile használjon `python:3.12-slim` base image-et
- Teszteld: `docker compose up --build` után elérhető a backend

## 1.3 FastAPI alap

A minimális FastAPI alkalmazás:

```python
# app/main.py
from fastapi import FastAPI

app = FastAPI(title="OpenSchool API")

@app.get("/health")
def health_check():
    return {"status": "ok"}
```

```python
# app/config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str
    secret_key: str
    github_client_id: str = ""
    github_client_secret: str = ""

    class Config:
        env_file = ".env"
```

**Feladat:**
- Írd meg a `main.py`, `config.py`, `database.py` fájlokat
- A `database.py` tartalmazza a SQLAlchemy engine és session konfigurációt
- A health check endpoint-nak működnie kell

## 1.4 Alembic

Adatbázis migráció beállítása:

**Feladat:**
- `alembic init alembic` futtatása a backend mappában
- `env.py` konfigurálása, hogy a `DATABASE_URL`-t a `.env`-ből olvassa
- Az `alembic.ini`-ben a `sqlalchemy.url` legyen üres (az `env.py` felülírja)
- Teszt migráció: üres revision létrehozása és futtatása

**Fogalmak:**
- Mi az a migráció és miért kell?
- `alembic revision --autogenerate` vs manuális revision
- `alembic upgrade head`, `alembic downgrade -1`

## 1.5 Tesztek

Teszt infrastruktúra pytest-tel és in-memory SQLite-tal:

```python
# tests/conftest.py
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.database import Base, get_db

SQLALCHEMY_TEST_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_TEST_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(bind=engine)

@pytest.fixture
def client():
    Base.metadata.create_all(bind=engine)
    def override_get_db():
        db = TestingSessionLocal()
        try:
            yield db
        finally:
            db.close()
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)
    Base.metadata.drop_all(bind=engine)
```

**Feladat:**
- Írd meg a `conftest.py`-t a teszt adatbázis konfigurációval
- Írj egy `test_health.py` tesztet a health check endpoint-ra
- Futtasd: `pytest -v` → zöld

## 1.6 GitHub Actions CI

```yaml
# .github/workflows/ci.yml
name: CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - run: pip install -r backend/requirements.txt
      - run: cd backend && pytest -v
```

**Feladat:**
- Hozd létre a workflow fájlt
- Push-old a kódot → ellenőrizd, hogy a CI zöld

## 1.7 Pre-commit és kódminőség

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.8.0
    hooks:
      - id: ruff
        args: [--fix]
      - id: ruff-format
```

**Feladat:**
- Telepítsd a `pre-commit`-ot és a ruff-ot
- Konfiguráld a `pyproject.toml`-ban a ruff szabályokat
- Futtasd le: `pre-commit run --all-files`

## 1.8 Makefile

Gyakori parancsok rövidítése:

```makefile
.PHONY: up down test migrate lint

up:
	docker compose up --build -d

down:
	docker compose down

test:
	cd backend && pytest -v

migrate:
	cd backend && alembic upgrade head

lint:
	cd backend && ruff check . && ruff format --check .
```

**Feladat:**
- Írd meg a Makefile-t
- Teszteld: `make up`, `make test`, `make lint`

## Háttéranyag

Ezeket nem kell elejétől végig elolvasni — használd referenciaként, amikor az adott témánál tartasz.

| Téma | Link | Miért hasznos |
|------|------|---------------|
| Docker Compose | [docs.docker.com/compose](https://docs.docker.com/compose/) | A `docker-compose.yml` szintaxis és multi-container setup |
| Dockerfile best practices | [docs.docker.com/build/building/best-practices](https://docs.docker.com/build/building/best-practices/) | Hatékony, kis méretű image-ek építése |
| Alembic tutorial | [alembic.sqlalchemy.org/en/latest/tutorial.html](https://alembic.sqlalchemy.org/en/latest/tutorial.html) | Migrációk létrehozása és kezelése |
| Makefile tutorial | [makefiletutorial.com](https://makefiletutorial.com/) | Make alapok — target-ek, phony, változók |
| pre-commit | [pre-commit.com](https://pre-commit.com/) | Hook-ok beállítása és használata |
| Ruff | [docs.astral.sh/ruff](https://docs.astral.sh/ruff/) | Python linter és formatter egyben |
| GitHub Actions | [docs.github.com/en/actions/quickstart](https://docs.github.com/en/actions/quickstart) | CI workflow alapok |
| pydantic-settings | [docs.pydantic.dev/latest/concepts/pydantic_settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/) | Környezeti változók kezelése |

## Verifikációs tesztek

A modul végén futtasd a verifikációs teszteket, hogy ellenőrizd a munkádat:

```bash
# Másold a teszteket az openschool-platform repóba (ha még nem tetted)
cp -r courses/projekt-labor/tesztek/ /path/to/openschool-platform/tesztek/

# Futtasd
cd openschool-platform
pytest tesztek/modul-01/ -v
```

**Mit ellenőriznek a tesztek:**

| Tesztfájl | Ellenőrzések |
|-----------|---------------|
| `test_health.py` | `/health` endpoint létezik és 200-at ad, az app-nak van title-je |
| `test_docker.py` | `docker-compose.yml`, `Dockerfile`, `requirements.txt`, `.env.example`, `Makefile`, `.gitignore`, `README.md` létezik; a compose tartalmaz backend és db service-t; a mappastruktúra helyes |
| `test_alembic.py` | `alembic.ini`, `env.py`, `versions/` létezik; CI workflow, pre-commit config, `database.py`, `config.py`, `conftest.py` létezik |

Ha valamelyik teszt FAILED, a hibaüzenet megmondja, mi hiányzik és mit kell csinálni.

> **Megjegyzés:** Ezek a tesztek a **végeredményt** ellenőrzik kívülről. A modul során írt **saját tesztek** (pl. `test_health.py` a `backend/tests/`-ben) ettől függetlenek — mindkettőnek zöldnek kell lennie.

## Ellenőrzőlista

- [ ] `docker compose up` → backend válaszol a `/health` endpoint-on
- [ ] `pytest -v` → legalább 1 zöld teszt (a saját teszted)
- [ ] GitHub Actions CI → zöld pipeline
- [ ] Alembic migrációk futnak
- [ ] `pre-commit run --all-files` → nincs hiba
- [ ] README tartalmazza a futtatási útmutatót
- [ ] `pytest tesztek/modul-01/ -v` → minden zöld (verifikációs tesztek)
