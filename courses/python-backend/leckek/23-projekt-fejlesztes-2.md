# 📘 Lecke 23 – Projekt fejlesztés II.

> 📚 **Dokumentáció:**
> https://docs.pytest.org/en/stable/how-to/fixtures.html
> https://fastapi.tiangolo.com/tutorial/testing/

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

### 🧠 Részletes Magyarázat

| Elem | Leírás |
|------|--------|
| **`sqlite:///./test.db`** | Teszt adatbázis – külön fájl a teszteléshez, nem az éles adatbázist használjuk |
| **`check_same_thread: False`** | SQLite alapértelmezetten egyetlen szálat enged – a TestClient másik szálról is hozzáfér, ezt kell engedélyezni |
| **`dependency_overrides[get_db]`** | A FastAPI dependency injection felülírása – a tesztekben a teszt DB-t kapják a végpontok az éles helyett |
| **`autouse=True`** | A `setup_db` fixture automatikusan lefut minden tesztfüggvény előtt és után, anélkül hogy paraméterként meg kellene adni |
| **`create_all` / `drop_all`** | Minden teszt előtt létrehozza a táblákat, utána törli – így minden teszt tiszta, üres adatbázissal indul |
| **`auth_headers`** | Tesztben regisztrál + bejelentkezik, majd visszaadja a kész Authorization fejlécet – bármelyik teszt használhatja |
| **`create_user` (factory fixture)** | Egy függvényt ad vissza, amit a tesztben többször is meghívhatunk különböző paraméterekkel – így több felhasználót hozhatunk létre |

A **fixture-ök hierarchiája**: a `client` fixture-re épít az `auth_headers` és `create_user` is. A pytest automatikusan feloldja a függőségeket: ha `auth_headers(client)` kér egy `client`-et, a pytest először létrehozza azt.

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

### 🧠 Részletes Magyarázat

| Teszt | Mit ellenőriz |
|-------|---------------|
| **`test_regisztracio`** | Sikeres regisztráció – 201-es válasz, az email visszatér, de a jelszó NEM szerepel a válaszban (biztonsági ellenőrzés) |
| **`test_dupla_email`** | Duplikált email elutasítása – az első regisztráció sikerül, a második 400-as hibát kap |
| **`test_login`** | Sikeres bejelentkezés – 200-as válasz és `access_token` mező a válaszban |
| **`test_rossz_jelszo`** | Hibás jelszóval nem lehet bejelentkezni – 401 Unauthorized |

Fontos különbség: a **regisztrációnál** `json=` a paraméter (JSON body), míg a **bejelentkezésnél** `data=` (form data) – ez azért van, mert az OAuth2 szabvány form-adatot vár a token végpontnál. Az **`assert "jelszo" not in response.json()`** biztonsági teszt: soha nem szabad a jelszót (még hash-elve sem) visszaadni az API válaszban.

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

### 🧠 Részletes Magyarázat

| Teszt | Kategória | Mit ellenőriz |
|-------|-----------|---------------|
| **`test_poszt_letrehozas`** | CRUD – Create | Bejelentkezett felhasználó létrehozhat posztot (201) |
| **`test_poszt_lista`** | CRUD – Read | 3 poszt létrehozása után a lista végpont mind a 3-at visszaadja |
| **`test_poszt_lekeres`** | CRUD – Read | Egy konkrét poszt lekérhető az ID-ja alapján |
| **`test_poszt_nem_letezik`** | Negatív | Nem létező ID esetén 404-es hiba |
| **`test_poszt_modositas`** | CRUD – Update | Részleges módosítás – csak a címet változtatjuk, a tartalom megmarad |
| **`test_poszt_torles`** | CRUD – Delete | Törlés után az elem már nem elérhető (404) |
| **`test_mas_posztjat_nem_torolheti`** | Jogosultság | Más felhasználó nem törölheti a posztot – 403 Forbidden |
| **`test_auth_nelkul_nem_hozhat_letre`** | Biztonság | Token nélkül nem lehet posztot létrehozni – 401 Unauthorized |

A tesztek az **AAA mintát** követik (Arrange–Act–Assert):
1. **Arrange** – adatok előkészítése (poszt létrehozása, felhasználó regisztrálása)
2. **Act** – a tesztelendő művelet végrehajtása (GET, POST, PUT, DELETE kérés)
3. **Assert** – az eredmény ellenőrzése (státuszkód, válasz tartalom)

A **`test_mas_posztjat_nem_torolheti`** a `create_user` factory fixture-t használja egy második felhasználó létrehozásához – ez mutatja, hogy a jogosultság-ellenőrzés valóban működik.

---

## 143–144. óra: Docker, CI és véglegesítés

### Tesztek futtatása lokálisan

```bash
pytest tests/ -v --cov=app
```

### 🧠 Részletes Magyarázat

- **`pytest tests/`** – A `tests/` mappában lévő összes tesztfájlt futtatja.
- **`-v`** (verbose) – Részletes kimenet: minden tesztfüggvény nevét és eredményét kiírja (PASSED/FAILED).
- **`--cov=app`** – Kód lefedettségi riportot készít az `app/` mappára – megmutatja, hogy a kód hány százalékát futtatják a tesztek.

### Docker Compose tesztelés

```bash
docker compose up --build -d
curl http://localhost:8000/health
docker compose down
```

### 🧠 Részletes Magyarázat

- **`docker compose up --build -d`** – Újraépíti az image-eket (`--build`) és háttérben indítja a konténereket (`-d` = detached).
- **`curl http://localhost:8000/health`** – Ellenőrzi, hogy az API válaszol-e – a `/health` végpont egy egyszerű állapotjelező.
- **`docker compose down`** – Leállítja és eltávolítja a konténereket, hálózatokat – takarítás a tesztelés után.

Ez a három parancs a **füstpróba** (smoke test): a lehető legegyszerűbb módon ellenőrizzük, hogy a rendszer elindul és válaszol.

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

### 🧠 Részletes Magyarázat

A **README.md** a projekt „névjegye" – ez az első dolog, amit bárki lát a GitHub repóban. Tartalmazza:

| Szekció | Célja |
|---------|-------|
| **Végpontok táblázat** | Gyors áttekintés minden API útvonalról és jogosultságról |
| **Auth oszlop** | ✅ = token szükséges, ❌ = nyilvános, (saját) = csak a tulajdonos |
| **Telepítés** | Egyetlen parancs az induláshoz – Docker Compose mindent kezel |
| **Tesztek** | Hogyan futtathatók a tesztek lokálisan |

Egy jó README segíti a **mentort** a projekt áttekintésében és a **fejlesztőt** a későbbi visszatérésben.

### Végső ellenőrzőlista

- [ ] Minden végpont működik (Swagger UI)
- [ ] Legalább 15 teszt fut sikeresen
- [ ] Docker Compose elindul hibátlanul
- [ ] GitHub Actions CI zöld
- [ ] README.md tartalmazza a végpont leírásokat
- [ ] .env.example fájl létezik
- [ ] Nincs jelszó vagy titkos kulcs a kódban

### 🧠 Részletes Magyarázat

| Ellenőrzési pont | Miért fontos |
|------------------|-------------|
| **Swagger UI** | Interaktív tesztelés – ha ott működik, az API jól van konfigurálva |
| **15+ teszt** | Megfelelő teszt lefedettség – auth + CRUD + jogosultság + negatív esetek |
| **Docker Compose** | Az alkalmazás bármilyen gépen futtatható konténerben |
| **GitHub Actions CI** | Automatikus tesztelés minden push-ra – a „zöld pipa" jelzi, hogy minden rendben |
| **`.env.example`** | Minta a szükséges környezeti változókhoz – a `.env` fájl NEM kerül Git-be (`.gitignore`-ban van), de az `.env.example` igen |
| **Nincs titkos kulcs** | Biztonsági ellenőrzés – a JWT secret, DB jelszó stb. soha nem kerülhet a forráskódba |

---

## Gyakorlat

1. Írj legalább 15 tesztet (auth + CRUD + jogosultság)
2. Ellenőrizd a lefedettséget (coverage >80%)
3. Teszteld Docker Compose-zal
4. Készítsd el a README.md-t
5. Ellenőrizd a GitHub Actions eredményt
6. Commitold és pushold a végleges projektet
