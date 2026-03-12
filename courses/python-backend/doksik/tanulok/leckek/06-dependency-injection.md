# Lecke 06 – Dependency Injection és projektstruktúra

> **Dokumentáció:** [FastAPI Dependencies](https://fastapi.tiangolo.com/tutorial/dependencies/) · [FastAPI Bigger Applications](https://fastapi.tiangolo.com/tutorial/bigger-applications/) · [python-dotenv](https://pypi.org/project/python-dotenv/)

---

## 37–38. óra: Dependency Injection

A **Dependency Injection** (DI) azt jelenti, hogy egy függvény a szükséges erőforrásokat **paraméterként kapja**, nem maga hozza létre. FastAPI-ban a `Depends()` segítségével működik.

### Egyszerű példa: oldalazás

```python
from fastapi import FastAPI, Depends, Query

app = FastAPI()

def oldalazas(skip: int = Query(default=0, ge=0), limit: int = Query(default=10, ge=1, le=100)):
    return {"skip": skip, "limit": limit}

@app.get("/items/")
def list_items(pages: dict = Depends(oldalazas)):
    return {"oldalazas": pages}

@app.get("/users/")
def list_users(pages: dict = Depends(oldalazas)):
    return {"oldalazas": pages}
```

A `oldalazas` függvényt **egyszer írtuk meg**, de több végponton is használjuk!

### Dependency láncolás

```python
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(db = Depends(get_db)):
    # Felhasználó lekérése az adatbázisból
    pass

@app.get("/profile")
def profile(user = Depends(get_current_user)):
    return user
```

---

## 39–40. óra: Projektstruktúra

Ahogy az alkalmazás nő, a `main.py`-ban nem tarthatunk mindent. Használjunk **APIRouter**-t:

```
app/
├── __init__.py
├── main.py              # FastAPI app, include routers
├── config.py            # Beállítások
├── dependencies.py      # Közös dependency-k
├── models.py            # SQLAlchemy modellek (később)
├── schemas.py           # Pydantic sémák
└── routers/
    ├── __init__.py
    ├── items.py          # /items végpontok
    └── users.py          # /users végpontok
```

### APIRouter

```python
# app/routers/items.py
from fastapi import APIRouter

router = APIRouter(prefix="/items", tags=["Termékek"])

@router.get("/")
def list_items():
    return [{"id": 1, "nev": "Laptop"}]

@router.get("/{item_id}")
def get_item(item_id: int):
    return {"id": item_id}

@router.post("/", status_code=201)
def create_item(item: dict):
    return item
```

```python
# app/main.py
from fastapi import FastAPI
from app.routers import items, users

app = FastAPI(title="Backend Kurzus API")

app.include_router(items.router)
app.include_router(users.router)
```

---

## 41–42. óra: Konfigurációkezelés

### .env fájl és python-dotenv

```bash
pip install python-dotenv
```

```
# .env
APP_NAME=Backend Kurzus API
DEBUG=true
DATABASE_URL=postgresql://user:password@localhost:5432/testdb
SECRET_KEY=szupertitkoscode123
```

### Pydantic BaseSettings

```python
# app/config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "My API"
    debug: bool = False
    database_url: str = "sqlite:///./test.db"
    secret_key: str = "changeme"

    class Config:
        env_file = ".env"

settings = Settings()
```

```python
# app/main.py
from app.config import settings

app = FastAPI(title=settings.app_name, debug=settings.debug)
```

### .env.example

A `.env`-t **nem commitoljuk** (benne van a `.gitignore`-ban), de készítünk `.env.example`-t:

```
APP_NAME=Backend Kurzus API
DEBUG=true
DATABASE_URL=postgresql://user:password@localhost:5432/testdb
SECRET_KEY=ide-ird-a-sajat-kulcsod
```

---

## Gyakorlat

1. Alakítsd át az eddigi projektedet a fenti struktúrára:
   - `app/main.py`, `app/schemas.py`, `app/routers/items.py`
   - `app/config.py` Pydantic Settings-szel
   - `.env` és `.env.example`
2. Commitold és pushold
