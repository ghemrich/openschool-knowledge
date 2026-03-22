# 📘 Lecke 15 – Adatbázis mock-olás teszteléshez

> 📚 Dokumentáció:
> https://fastapi.tiangolo.com/advanced/testing-database/
> https://docs.sqlalchemy.org/en/20/dialects/sqlite.html

---

## 91–92. óra: A probléma és a megoldás

### Miért kell mock adatbázis?

A valódi PostgreSQL adatbázis:
- **Nem elérhető** GitHub Actions-ben (CI/CD)
- **Állapotfüggő** – a tesztek egymásra hatnak
- **Lassú** – hálózati kapcsolat kell hozzá

A megoldás: **SQLite in-memory adatbázis** a tesztekhez.

### 🧠 Részletes Magyarázat

- **Mock** – „Ál-objektum", ami a valódi helyettesítése. A mock adatbázis úgy viselkedik, mint a PostgreSQL, de valójában egy könnyű SQLite, ami a memóriában fut (vagy egy ideiglenes fájlban).
- **Miért SQLite?** – (1) Nincs szükség szerverre, (2) nem kell Docker, (3) pillanatok alatt létrejön és törlődik, (4) a GitHub Actions-ben is elérhető. Az SQLAlchemy ORM ugyanazokat a Python műveleteket fordítja SQLite SQL-re, mint PostgreSQL SQL-re.
- **Korlátok** – Az SQLite nem támogat minden PostgreSQL funkciót (pl. `ARRAY`, `JSON` operátorok, `SERIAL`). Alap CRUD-ra tökéletesen megfelel, haladó funkciókra érdemes Docker-based teszt PostgreSQL-t is használni.

### Az elv: Dependency Override

A FastAPI lehetővé teszi, hogy a `Depends()` által használt függvényeket **felülírjuk** a tesztekben:

```
Éles:   get_db → PostgreSQL (docker-compose)
Teszt:  get_db → SQLite in-memory (:memory:)
```

### 🧠 Részletes Magyarázat

- **Dependency Override** – A FastAPI `app.dependency_overrides` dict-je lehetővé teszi, hogy bármely `Depends()` függvényt lecseréljünk a tesztben. A kulcs az eredeti függvény, az érték a helyettesítő.
- **Miért jó ez?** – A végpont kódja **nem változik**: továbbra is `db: Session = Depends(get_db)` a paraméter. Csak a `get_db` mögötti implementáció más: élesben PostgreSQL, tesztben SQLite. Ez a Dependency Injection igazi ereje.

### Teszt adatbázis beállítása

```python
# tests/conftest.py
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient

from app.main import app
from app.database import Base, get_db

# SQLite in-memory adatbázis
SQLALCHEMY_TEST_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_TEST_DATABASE_URL,
    connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

# Dependency felülírás
app.dependency_overrides[get_db] = override_get_db

@pytest.fixture(autouse=True)
def setup_db():
    """Minden teszt előtt: táblákat létrehozza, utána: törli."""
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

@pytest.fixture
def client():
    return TestClient(app)
```

### 🧠 Részletes Magyarázat

Ez a `conftest.py` a teljes teszt-infrastruktúrát beállítja:

1. **Teszt engine** – `create_engine("sqlite:///./test.db")` egy SQLite fájl-alapú adatbázist hoz létre. Az `"sqlite:///:memory:"` változat a memóriában él (még gyorsabb, de nem ellenőrizhető kézzel).
2. **`check_same_thread=False`** – SQLite-specifikus beállítás. Az SQLite alapértelmezetten nem engedélyezi, hogy más szálból érjük el az adatbázist. A FastAPI TestClient más szálat használhat, ezért kikapcsoljuk ezt az ellenőrzést.
3. **`override_get_db()`** – Pontosan ugyanaz a minta, mint az éles `get_db()`, csak `TestingSessionLocal`-t használ az `SessionLocal` helyett.
4. **`app.dependency_overrides[get_db] = override_get_db`** – Ez a sor cseréli ki a valódi adatbázis dependency-t a teszt változatra. Ezután minden `Depends(get_db)` az `override_get_db`-t fogja használni.
5. **`setup_db` fixture (`autouse=True`):**
   - `autouse=True` – Minden tesztre automatikusan érvényes (nem kell paraméterként kérni)
   - `create_all()` – A `Base.metadata` alapján létrehozza az összes táblát
   - `yield` – A teszt lefut
   - `drop_all()` – Az összes táblát törli → következő teszt üres adatbázissal indul

---

## 93–94. óra: Teljes teszt suite mock DB-vel

### Auth fixture mock adatbázissal

```python
# tests/conftest.py (kiegészítés)

@pytest.fixture
def auth_headers(client):
    client.post("/auth/regisztracio", json={
        "nev": "Test User",
        "email": "test@example.com",
        "jelszo": "jelszo123"
    })
    response = client.post("/auth/login", data={
        "username": "test@example.com",
        "password": "jelszo123"
    })
    token = response.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}

@pytest.fixture
def db_session():
    """Közvetlen DB hozzáférés tesztekhez."""
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
```

### 🧠 Részletes Magyarázat

- **`auth_headers` fixture** – A mock adatbázisba regisztrál egy felhasználót, belépteti, és visszaadja a tokenes fejlécet. Mivel a `setup_db` fixture `autouse=True`, az adatbázis üres lesz a fixture futásakor → az előző teszt felhasználója nem zavarhat.
- **`db_session` fixture** – Közvetlen adatbázis hozzáférés tesztekhez. Hasznos, ha a tesztben közvetlenül akarunk adatot beírni az adatbázisba (az API-t megkerülve), vagy ellenőrizni, hogy valóban beíródott-e az adat.

### CRUD tesztek mock DB-vel

```python
# tests/test_items.py

def test_create_item(client, auth_headers):
    response = client.post("/items", json={
        "nev": "Laptop",
        "ar": 350000
    }, headers=auth_headers)
    assert response.status_code == 201
    data = response.json()
    assert data["nev"] == "Laptop"
    assert data["ar"] == 350000
    assert "id" in data

def test_list_items(client, auth_headers):
    # Előkészítés: 3 elem létrehozása
    for i in range(3):
        client.post("/items", json={
            "nev": f"Item {i}",
            "ar": 100 * (i + 1)
        }, headers=auth_headers)

    response = client.get("/items")
    assert response.status_code == 200
    assert len(response.json()) == 3

def test_get_item(client, auth_headers):
    # Létrehozás
    create_resp = client.post("/items", json={
        "nev": "Telefon",
        "ar": 150000
    }, headers=auth_headers)
    item_id = create_resp.json()["id"]

    # Lekérés
    response = client.get(f"/items/{item_id}")
    assert response.status_code == 200
    assert response.json()["nev"] == "Telefon"

def test_get_item_not_found(client):
    response = client.get("/items/9999")
    assert response.status_code == 404

def test_update_item(client, auth_headers):
    create_resp = client.post("/items", json={
        "nev": "Régi név",
        "ar": 100
    }, headers=auth_headers)
    item_id = create_resp.json()["id"]

    response = client.put(f"/items/{item_id}", json={
        "nev": "Új név",
        "ar": 200
    }, headers=auth_headers)
    assert response.status_code == 200
    assert response.json()["nev"] == "Új név"

def test_delete_item(client, auth_headers):
    create_resp = client.post("/items", json={
        "nev": "Törlendő",
        "ar": 100
    }, headers=auth_headers)
    item_id = create_resp.json()["id"]

    response = client.delete(f"/items/{item_id}", headers=auth_headers)
    assert response.status_code == 200

    # Ellenőrzés: már nem létezik
    get_resp = client.get(f"/items/{item_id}")
    assert get_resp.status_code == 404
```

### 🧠 Részletes Magyarázat

Minden teszt a **AAA** (Arrange-Act-Assert) mintát követi:

| Lépés | Mit csinál | Példa |
|-------|-----------|-------|
| **Arrange** | Előkészítés | Item létrehozása, token beszerzés |
| **Act** | A tesztelt művelet | `client.get(f"/items/{item_id}")` |
| **Assert** | Ellenőrzés | `assert response.status_code == 200` |

- **`test_create_item`** – Arrange: semmi (üres DB). Act: POST. Assert: 201 + mezők egyezése.
- **`test_list_items`** – Arrange: 3 elem létrehozása. Act: GET /items. Assert: 200 + 3 elemű lista.
- **`test_get_item`** – Arrange: 1 elem létrehozása. Act: GET /items/{id}. Assert: 200 + név egyezés.
- **`test_get_item_not_found`** – Negatív teszt: nem létező ID → 404.
- **`test_delete_item`** – Kétlépéses: törlés (200), majd lekérés (404 = tényleg törlődött).

Azért működik mindez függetlenül, mert a `setup_db` fixture **minden teszt előtt újra létrehozza** és **utána törli** a táblákat.

---

## 95–96. óra: Tesztek izolálása és CI integráció

### Tesztek izolálása

A `setup_db` fixture (`autouse=True`) gondoskodik arról, hogy **minden teszt tiszta adatbázissal** indul:

```python
@pytest.fixture(autouse=True)
def setup_db():
    Base.metadata.create_all(bind=engine)    # táblákat létrehozza
    yield                                     # teszt fut
    Base.metadata.drop_all(bind=engine)       # táblákat törli
```

### 🧠 Részletes Magyarázat

- **Izoláció** – Minden teszt úgy fut, mintha friss alkalmazást indítottunk volna. Egy teszt létrehozhat 100 elemet, a következő tesztben mégis üres az adatbázis. Ez megakadályozza, hogy a tesztek egymásra hassanak.
- **`create_all` + `drop_all` sorrend:**
  1. `create_all()` — CREATE TABLE IF NOT EXISTS (táblák létrehozása ha nem léteznek)
  2. `yield` — teszt fut (INSERT, SELECT, UPDATE, DELETE)
  3. `drop_all()` — DROP TABLE (táblák AND adatok törlése)
- **Alternatíva: tranzakció rollback** – Egy gyorsabb minta: a `setup_db` tranzakciót indít, és a teszt végén visszagörgeti (`rollback`). Ez gyorsabb, mert nem kell újra létrehozni a táblákat, de bonyolultabb.

### GitHub Actions workflow

```yaml
# .github/workflows/test.yml
name: Tesztek

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - run: pip install -r requirements.txt
      - run: pytest tests/ -v
```

### 🧠 Részletes Magyarázat

- **GitHub Actions** – Automatizált CI/CD platform. Minden `push` és `pull_request` eseményre lefuttatja a teszteket. Ha egy teszt elbukik, a commit „piros pipát" kap.
- **Workflow lépései:**
  1. `actions/checkout@v4` – Klónozza a repót a runner-re
  2. `actions/setup-python@v5` – Telepíti a megadott Python verziót
  3. `pip install -r requirements.txt` – Telepíti a függőségeket
  4. `pytest tests/ -v` – Futtatja a teszteket
- **Nincs Docker szükség** – A mock DB stratégia miatt a GitHub Actions runner-en nincs szükség PostgreSQL-re. Az SQLite a Python beépített modulja, mindig elérhető.
- **GitHub Classroom** – A Classroom autograding pontosan ugyanezt a workflow-t használja. Ha a tesztek SQLite-tal futnak, a tanár beállíthatja, hogy a beadásokat automatikusan értékelje.

A **mock DB** stratégia azért fontos, mert a GitHub Actions-ben **nincs PostgreSQL** – a tesztek SQLite-tal futnak, és így:
- Nincs Docker szükség a CI-ban
- A tesztek gyorsak és megbízhatók
- A GitHub Classroom autograding is működik

### requirements.txt a teszteléshez

```
fastapi
uvicorn
sqlalchemy
alembic
psycopg2-binary
python-jose[cryptography]
passlib[bcrypt]
python-dotenv
pydantic-settings
pytest
httpx
```

---

## Gyakorlat

1. Hozd létre a `tests/conftest.py`-t SQLite mock adatbázissal
2. Írd meg a `setup_db` fixture-t `autouse=True`-val
3. Írj tesztet minden CRUD művelethez (create, list, get, update, delete)
4. Ellenőrizd, hogy a tesztek egymástól függetlenül futnak
5. Hozd létre a `.github/workflows/test.yml` fájlt
6. Commitold és pushold – ellenőrizd a GitHub Actions eredményt
