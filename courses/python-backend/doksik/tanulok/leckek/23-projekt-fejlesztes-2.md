# Lecke 23 – Projekt fejlesztés II.

> **Dokumentáció:** [pytest fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html) · [FastAPI Testing](https://fastapi.tiangolo.com/tutorial/testing/)

---

## 139–140. óra: Tesztek írása a projekthez

### conftest.py a projekthez

```python
# tests/conftest.py
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient

from app.main import app
from app.database import Base, get_db

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

app.dependency_overrides[get_db] = override_get_db

@pytest.fixture(autouse=True)
def setup_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

@pytest.fixture
def client():
    return TestClient(app)

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
def create_user(client):
    def _create(nev="User", email="user@test.com", jelszo="jelszo123"):
        resp = client.post("/auth/regisztracio", json={
            "nev": nev, "email": email, "jelszo": jelszo
        })
        login = client.post("/auth/login", data={
            "username": email, "password": jelszo
        })
        return login.json()["access_token"]
    return _create
```

### Auth tesztek

```python
# tests/test_auth.py

def test_regisztracio(client):
    response = client.post("/auth/regisztracio", json={
        "nev": "Új User",
        "email": "uj@test.com",
        "jelszo": "jelszo123"
    })
    assert response.status_code == 201
    assert response.json()["email"] == "uj@test.com"
    assert "jelszo" not in response.json()

def test_dupla_email(client):
    adat = {"nev": "User", "email": "dupla@test.com", "jelszo": "jelszo123"}
    client.post("/auth/regisztracio", json=adat)
    response = client.post("/auth/regisztracio", json=adat)
    assert response.status_code == 400

def test_login(client):
    client.post("/auth/regisztracio", json={
        "nev": "User", "email": "login@test.com", "jelszo": "jelszo123"
    })
    response = client.post("/auth/login", data={
        "username": "login@test.com", "password": "jelszo123"
    })
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_rossz_jelszo(client):
    client.post("/auth/regisztracio", json={
        "nev": "User", "email": "rossz@test.com", "jelszo": "jelszo123"
    })
    response = client.post("/auth/login", data={
        "username": "rossz@test.com", "password": "rossz"
    })
    assert response.status_code == 401
```

---

## 141–142. óra: CRUD tesztek

```python
# tests/test_posztok.py

def test_poszt_letrehozas(client, auth_headers):
    response = client.post("/posztok", json={
        "cim": "Első poszt",
        "tartalom": "Ez az első poszt tartalma"
    }, headers=auth_headers)
    assert response.status_code == 201
    assert response.json()["cim"] == "Első poszt"

def test_poszt_lista(client, auth_headers):
    for i in range(3):
        client.post("/posztok", json={
            "cim": f"Poszt {i}", "tartalom": f"Tartalom {i}"
        }, headers=auth_headers)
    response = client.get("/posztok")
    assert response.status_code == 200
    assert len(response.json()) == 3

def test_poszt_lekeres(client, auth_headers):
    resp = client.post("/posztok", json={
        "cim": "Keresett", "tartalom": "Tartalom"
    }, headers=auth_headers)
    poszt_id = resp.json()["id"]
    response = client.get(f"/posztok/{poszt_id}")
    assert response.status_code == 200
    assert response.json()["cim"] == "Keresett"

def test_poszt_nem_letezik(client):
    response = client.get("/posztok/9999")
    assert response.status_code == 404

def test_poszt_modositas(client, auth_headers):
    resp = client.post("/posztok", json={
        "cim": "Régi cím", "tartalom": "Régi tartalom"
    }, headers=auth_headers)
    poszt_id = resp.json()["id"]
    response = client.put(f"/posztok/{poszt_id}", json={
        "cim": "Új cím"
    }, headers=auth_headers)
    assert response.status_code == 200
    assert response.json()["cim"] == "Új cím"

def test_poszt_torles(client, auth_headers):
    resp = client.post("/posztok", json={
        "cim": "Törlendő", "tartalom": "Tartalom"
    }, headers=auth_headers)
    poszt_id = resp.json()["id"]
    response = client.delete(f"/posztok/{poszt_id}", headers=auth_headers)
    assert response.status_code == 200
    assert client.get(f"/posztok/{poszt_id}").status_code == 404

def test_mas_posztjat_nem_torolheti(client, auth_headers, create_user):
    resp = client.post("/posztok", json={
        "cim": "Eredeti", "tartalom": "Tartalom"
    }, headers=auth_headers)
    poszt_id = resp.json()["id"]
    token2 = create_user(nev="Más", email="mas@test.com")
    response = client.delete(f"/posztok/{poszt_id}", headers={
        "Authorization": f"Bearer {token2}"
    })
    assert response.status_code == 403

def test_auth_nelkul_nem_hozhat_letre(client):
    response = client.post("/posztok", json={
        "cim": "Próba", "tartalom": "Tartalom"
    })
    assert response.status_code == 401
```

---

## 143–144. óra: Docker, CI és véglegesítés

### Tesztek futtatása lokálisan

```bash
pytest tests/ -v --cov=app
```

### Docker Compose tesztelés

```bash
docker compose up --build -d
curl http://localhost:8000/health
docker compose down
```

### README.md készítése

```markdown
# Blog API

Backend API FastAPI keretrendszerrel.

## Végpontok

| Módszer | Útvonal | Leírás | Auth |
|---------|---------|--------|------|
| POST | /auth/regisztracio | Regisztráció | ❌ |
| POST | /auth/login | Bejelentkezés | ❌ |
| GET | /posztok | Posztok listázása | ❌ |
| POST | /posztok | Új poszt | ✅ |
| GET | /posztok/{id} | Egy poszt | ❌ |
| PUT | /posztok/{id} | Módosítás | ✅ (saját) |
| DELETE | /posztok/{id} | Törlés | ✅ (saját) |

## Telepítés

\```bash
docker compose up --build
\```

## Tesztek

\```bash
pytest tests/ -v
\```
```

### Végső ellenőrzőlista

- [ ] Minden végpont működik (Swagger UI)
- [ ] Legalább 15 teszt fut sikeresen
- [ ] Docker Compose elindul hibátlanul
- [ ] GitHub Actions CI zöld
- [ ] README.md tartalmazza a végpont leírásokat
- [ ] .env.example fájl létezik
- [ ] Nincs jelszó vagy titkos kulcs a kódban

---

## Gyakorlat

1. Írj legalább 15 tesztet (auth + CRUD + jogosultság)
2. Ellenőrizd a lefedettséget (coverage >80%)
3. Teszteld Docker Compose-zal
4. Készítsd el a README.md-t
5. Ellenőrizd a GitHub Actions eredményt
6. Commitold és pushold a végleges projektet
