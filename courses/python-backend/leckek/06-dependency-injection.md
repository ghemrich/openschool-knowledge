# 📘 Lecke 06 – Dependency Injection és projektstruktúra

> 📚 Dokumentáció:
> https://fastapi.tiangolo.com/tutorial/dependencies/
> https://fastapi.tiangolo.com/tutorial/bigger-applications/
> https://pypi.org/project/python-dotenv/

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

### 🧠 Részletes Magyarázat

- **Dependency Injection (DI)** – Tervezési minta, ahol egy függvény nem maga hozza létre a szükséges erőforrásait, hanem kívülről kapja meg. Ez tesztelhetőbb, újrafelhasználhatóbb és tisztább kódot eredményez.
- **`Depends(oldalazas)`** – A FastAPI DI rendszerének kulcsa. Amikor egy végpont meghívódik, a FastAPI automatikusan:
  1. Meghívja az `oldalazas` függvényt (a query paraméterekkel)
  2. Az eredményt átadja a `pages` paraméternek
  3. Majd futtatja a végpont függvényt
- **Újrafelhasználás** – Az `oldalazas` függvényt egyszer írtuk meg, de több végponton is alkalmazzuk (`/items/`, `/users/`). Ha módosítani kell (pl. max limit 100→50), csak egy helyen kell változtatni.
- **`Query(default=0, ge=0)`** – A dependency-ben is használhatunk FastAPI validációt. A `ge=0` (greater or equal) biztosítja, hogy a `skip` nem lehet negatív.

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

### 🧠 Részletes Magyarázat

- **Dependency láncolás** – Egy dependency maga is használhat más dependency-ket. A `get_current_user` függ a `get_db`-től, a `profile` végpont pedig a `get_current_user`-től. A FastAPI automatikusan feloldja a teljes láncot:
```
profile() ← get_current_user() ← get_db()
```
- **`yield` és erőforrás-kezelés** – A `get_db()` függvényben a `yield` különleges: a `yield db` előtti rész a **kérés elején** fut (adatbázis megnyitás), az utána lévő `finally` blokk pedig a **kérés végén** (adatbázis bezárás). Ez biztosítja, hogy a kapcsolat mindig bezáródjon, még hiba esetén is.
- **`try...finally` és `yield` együtt** – A `yield`-es dependency-k a Python generátor-protokollját használják. A `try` blokk védi a `yield`-et, a `finally` garantálja a takarítást. Ez analóg a `with open()` működésével fájloknál.

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

### 🧠 Részletes Magyarázat

- **Miért bontjuk szét?** – Egy 500+ soros `main.py` átláthatatlan. A szétbontás felelősség szerint történik: minden fájlnak egy feladata van. Ez a **Separation of Concerns** (felelősségek szétválasztása) elv.
- **Fájlok szerepe:**

| Fájl | Felelősség |
|------|-----------|
| `main.py` | App létrehozás, routerek összekötése |
| `config.py` | Környezeti változók, beállítások |
| `dependencies.py` | Közös DI függvények (DB, auth) |
| `schemas.py` | Pydantic modellek (input/output) |
| `models.py` | Adatbázis modellek (SQLAlchemy) |
| `routers/*.py` | Végpontok téma szerint csoportosítva |

- **`__init__.py`** – Üres fájl, ami jelzi a Pythonnak, hogy a mappa egy csomag (package). Enélkül az `from app.routers import items` import nem működne.

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

### 🧠 Részletes Magyarázat

- **`APIRouter`** – Egy „mini alkalmazás", ami végpontokat gyűjt, de önmagában nem fut. A `main.py`-ban kell az `app`-hoz csatolni az `include_router()`-rel.
- **`prefix="/items"`** – A routerben definiált összes végpont URL-je ezzel kezdődik. A `@router.get("/")` valójában a `/items/` címre reagál, a `@router.get("/{item_id}")` a `/items/42`-re. Nem kell minden végpontnál kiírni az `/items` részt.
- **`tags=["Termékek"]`** – A Swagger UI-ban ez a címke szerint csoportosítja a végpontokat. Így a dokumentáció áttekinthető lesz, még ha 50+ végpont is van.

```python
# app/main.py
from fastapi import FastAPI
from app.routers import items, users

app = FastAPI(title="Backend Kurzus API")

app.include_router(items.router)
app.include_router(users.router)
```

### 🧠 Részletes Magyarázat

- **`include_router()`** – Ez csatolja a router végpontjait az alkalmazáshoz. A hívás után az összes `items.router`-ben definiált végpont elérhető lesz az alkalmazásban.
- **`from app.routers import items`** – A Python package rendszere: az `app/routers/items.py` fájlból importáljuk az `items` modult, amiből a `.router` objektumot használjuk.
- **Moduláris felépítés előnye** – Ha új témát (pl. `orders`) adunk az API-hoz, csak új fájl kell a `routers/` mappába, és egy `include_router()` sor a `main.py`-ban. A meglévő kód nem változik.

---

## 41–42. óra: Konfigurációkezelés

### .env fájl és python-dotenv

```bash
pip install python-dotenv
```

### 🧠 Részletes Magyarázat

- **`python-dotenv`** – Könyvtár, ami a `.env` fájlból olvassa be a konfigurációt. A Pydantic Settings automatikusan használja, ha telepítve van.

```
# .env
APP_NAME=Backend Kurzus API
DEBUG=true
DATABASE_URL=postgresql://user:password@localhost:5432/testdb
SECRET_KEY=szupertitkoscode123
```

### 🧠 Részletes Magyarázat

- **`.env` fájl** – Környezeti változókat tartalmaz `KULCS=érték` formátumban. Az alkalmazás innen olvassa a beállításokat ahelyett, hogy a kódba lenne beégetve.
- **Miért nem a kódba írjuk?** – A kód Git-ben van, ami nyilvános lehet. A jelszavak, API kulcsok, adatbázis URL-ek érzékeny adatok → `.env` fájlba kerülnek, ami a `.gitignore`-ban van. Így a titkos adatok sosem kerülnek a repository-ba.
- **Környezetenként más beállítás** – Fejlesztésnél `DEBUG=true` és helyi adatbázis, éles szerveren `DEBUG=false` és éles adatbázis. A kód ugyanaz, csak a `.env` más.

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

### 🧠 Részletes Magyarázat

- **`BaseSettings`** – A `pydantic_settings` könyvtár osztálya (Pydantic v2-ben külön csomag: `pip install pydantic-settings`). Működése hasonló a `BaseModel`-hez, de az értékeket **környezeti változókból** is betölti, nem csak kódból.
- **Betöltési sorrend** – A `Settings()` létrehozásakor az értékek a következő sorrendben keresődnek (az utolsó nyer):
  1. Alapértelmezés a kódban (`"My API"`)
  2. `.env` fájl tartalma
  3. Valódi rendszer környezeti változók (`export APP_NAME=...`)
- **`class Config: env_file = ".env"`** – Megmondja a Pydantic-nak, hogy a `.env` fájlból töltse be az értékeket. A mező nevek automatikusan illeszkednek a környezeti változó nevekhez (kis-nagybetű nem számít).
- **Típuskonverzió** – A `.env` fájlban minden szöveg, de a Pydantic automatikusan konvertál: `"true"` → `bool True`, `"5432"` → `int 5432`.
- **`settings = Settings()`** – A modul szintjén létrehozott példány az egész alkalmazásban importálható: `from app.config import settings`.

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

### 🧠 Részletes Magyarázat

- **`.env.example`** – Ez a fájl **commitolva van** a Git-ben, és sablon a `.env` fájlhoz. Amikor valaki klónozza a projektet, lemásolja `.env` néven és kitölti a saját értékeivel.
- **A munkafolyamat:**
  1. `cp .env.example .env` (másolás)
  2. Szerkeszd a `.env` fájlt a saját értékeiddel
  3. A `.gitignore`-ban benne van a `.env`, tehát nem kerül Git-be
  4. A `.env.example` viszont commitolva van, hogy mindenki tudja, milyen beállítások szükségesek

---

## Gyakorlat

1. Alakítsd át az eddigi projektedet a fenti struktúrára:
   - `app/main.py`, `app/schemas.py`, `app/routers/items.py`
   - `app/config.py` Pydantic Settings-szel
   - `.env` és `.env.example`
2. Commitold és pushold
