# Lecke 15 – Adatbázis mock-olás teszteléshez

> **Dokumentáció:** [FastAPI Testing DB](https://fastapi.tiangolo.com/advanced/testing-database/) · [SQLAlchemy SQLite](https://docs.sqlalchemy.org/en/20/dialects/sqlite.html)

---

## 91–92. óra: A probléma és a megoldás

### Miért kell mock adatbázis?

A valódi PostgreSQL adatbázis:
- **Nem elérhető** GitHub Actions-ben (CI/CD)
- **Állapotfüggő** – a tesztek egymásra hatnak
- **Lassú** – hálózati kapcsolat kell hozzá

A megoldás: **SQLite in-memory adatbázis** a tesztekhez.

### Az elv: Dependency Override

A FastAPI lehetővé teszi, hogy a `Depends()` által használt függvényeket **felülírjuk** a tesztekben:

```
Éles:   get_db → PostgreSQL (docker-compose)
Teszt:  get_db → SQLite in-memory (:memory:)
```

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
