# Lecke 14 – FastAPI tesztelés

> **Dokumentáció:** [FastAPI Testing](https://fastapi.tiangolo.com/tutorial/testing/) · [httpx](https://www.python-httpx.org/) · [TestClient](https://www.starlette.io/testclient/)

---

## 85–86. óra: TestClient alapok

### API tesztelés

Az API végpontokat a `TestClient` segítségével teszteljük – ez HTTP kéréseket szimulál a szerver elindítása nélkül:

```bash
pip install httpx   # a TestClient ezt használja
```

```python
# tests/test_main.py
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "API fut"}

def test_not_found():
    response = client.get("/nem-letezik")
    assert response.status_code == 404
```

### GET végpontok tesztelése

```python
def test_lista():
    response = client.get("/items")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_query_param():
    response = client.get("/items?skip=0&limit=5")
    assert response.status_code == 200
    data = response.json()
    assert len(data) <= 5
```

### POST végpont tesztelése

```python
def test_create_item():
    uj_item = {"nev": "Teszt item", "ar": 100}
    response = client.post("/items", json=uj_item)
    assert response.status_code == 201
    data = response.json()
    assert data["nev"] == "Teszt item"
    assert "id" in data
```

---

## 87–88. óra: Autentikáció tesztelése

### Regisztráció és login tesztelése

```python
# tests/test_auth.py
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_regisztracio():
    response = client.post("/auth/regisztracio", json={
        "nev": "Test User",
        "email": "test@example.com",
        "jelszo": "teszt123"
    })
    assert response.status_code == 201
    assert response.json()["email"] == "test@example.com"

def test_login():
    response = client.post("/auth/login", data={
        "username": "test@example.com",
        "password": "teszt123"
    })
    assert response.status_code == 200
    assert "access_token" in response.json()
```

### Védett végpont tesztelése

```python
def get_token(client):
    """Segédfüggvény: regisztrál + bejelentkezik, visszaadja a tokent."""
    client.post("/auth/regisztracio", json={
        "nev": "Auth Test",
        "email": "auth@example.com",
        "jelszo": "jelszo123"
    })
    response = client.post("/auth/login", data={
        "username": "auth@example.com",
        "password": "jelszo123"
    })
    return response.json()["access_token"]

def test_vedett_vegpont_token_nelkul():
    response = client.get("/profil")
    assert response.status_code == 401

def test_vedett_vegpont_tokennel():
    token = get_token(client)
    response = client.get(
        "/profil",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    assert response.json()["email"] == "auth@example.com"
```

---

## 89–90. óra: Fixture-ök és conftest.py API teszteléshez

### conftest.py beállítása

```python
# tests/conftest.py
import pytest
from fastapi.testclient import TestClient
from app.main import app

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def auth_headers(client):
    """Bejelentkezett felhasználó headerje."""
    client.post("/auth/regisztracio", json={
        "nev": "Fixture User",
        "email": "fixture@example.com",
        "jelszo": "jelszo123"
    })
    response = client.post("/auth/login", data={
        "username": "fixture@example.com",
        "password": "jelszo123"
    })
    token = response.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}
```

### Fixture használata

```python
# tests/test_items.py

def test_create_item_vedett(client, auth_headers):
    response = client.post(
        "/items",
        json={"nev": "Teszt", "ar": 500},
        headers=auth_headers
    )
    assert response.status_code == 201

def test_create_item_unauthorized(client):
    response = client.post("/items", json={"nev": "Teszt", "ar": 500})
    assert response.status_code == 401
```

### Tesztek futtatása

```bash
pytest tests/ -v                      # összes teszt
pytest tests/test_auth.py -v          # csak auth tesztek
pytest tests/ -v --tb=short           # rövid hibaüzenetek
pytest tests/ -v -x                   # első hibánál megáll
```

---

## Gyakorlat

1. Írj tesztet a `GET /` végpontra
2. Teszteld a regisztráció és login végpontokat
3. Tesztelj egy védett végpontot tokennel és token nélkül
4. Hozz létre `conftest.py`-t `client` és `auth_headers` fixture-ökkel
5. Commitold és pushold
