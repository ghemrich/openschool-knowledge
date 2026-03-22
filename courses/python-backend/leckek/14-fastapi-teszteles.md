# 📘 Lecke 14 – FastAPI tesztelés

> 📚 Dokumentáció:
> https://fastapi.tiangolo.com/tutorial/testing/
> https://www.python-httpx.org/
> https://www.starlette.io/testclient/

---

## 85–86. óra: TestClient alapok

### API tesztelés

Az API végpontokat a `TestClient` segítségével teszteljük – ez HTTP kéréseket szimulál a szerver elindítása nélkül:

```bash
pip install httpx   # a TestClient ezt használja
```

### 🧠 Részletes Magyarázat

- **`TestClient`** – A FastAPI (Starlette) beépített tesztkliense. HTTP kéréseket küld az alkalmazásnak anélkül, hogy tényleges hálózati szerver futna. Minden a memóriában történik → gyors és megbízható.
- **`httpx`** – Modern Python HTTP kliens könyvtár (a `requests` utódja). A `TestClient` ezt használja a háttérben, ezért kell telepíteni.
- **Szerver nélkül** – Nem kell `uvicorn`-t indítani a tesztekhez. A `TestClient` közvetlenül meghívja a FastAPI alkalmazást, mintha HTTP kérés érkezett volna.

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

### 🧠 Részletes Magyarázat

- **`TestClient(app)`** – Az `app` az `app/main.py`-ban létrehozott `FastAPI()` objektum. A `TestClient` ehhez küld kéréseket.
- **`client.get("/")`** – GET kérést szimulál a `/` végpontra. Visszaad egy `Response` objektumot, aminek ellenőrizhetjük a `status_code`-ját és a tartalmát.
- **`response.json()`** – A válasz body-t JSON-ként (Python dict-ként) adja vissza. Közvetlenül össze tudjuk hasonlítani egy dict-tel.
- **Tipikus teszt minta** – Minden API tesztben ez a 3 lépés: (1) kérés küldése, (2) státuszkód ellenőrzése, (3) válasz tartalom ellenőrzése.

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

### 🧠 Részletes Magyarázat

- **`isinstance(response.json(), list)`** – Ellenőrzi, hogy a válasz egy lista (nem dict, nem string). A listázó végpontoknál ez az alap elvárás.
- **Query paraméterek tesztelése** – A `client.get("/items?skip=0&limit=5")` az URL-ben küldi a paramétert. Egy másik lehetőség: `client.get("/items", params={"skip": 0, "limit": 5})`.
- **`len(data) <= 5`** – A `limit=5` esetén legfeljebb 5 elemünk lehet. `<=` mert ha kevesebb elem van az adatbázisban, kevesebbet kapunk.

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

### 🧠 Részletes Magyarázat

- **`client.post("/items", json=uj_item)`** – POST kérés JSON body-val. A `json=` paraméter automatikusan beállítja a `Content-Type: application/json` fejlécet és szerializálja a dict-et.
- **`assert "id" in data`** – Ellenőrzi, hogy a válasz tartalmazza az `id` mezőt. Az `id`-t a szerver generálja, ezért nem tudjuk az exact értéket, de a jelenlétét igen.
- **`status_code == 201`** – POST-nál 201-et várunk (Created), nem 200-at. Ha 200-at kapunk, az is „sikeres", de nem a helyes REST konvenció.

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

### 🧠 Részletes Magyarázat

- **`json=` vs. `data=`** – Fontos különbség!
  - `json={...}` → `Content-Type: application/json` – a regisztrációnál Pydantic modellt várunk, ami JSON-ból jön
  - `data={...}` → `Content-Type: application/x-www-form-urlencoded` – a login az `OAuth2PasswordRequestForm`-ot használja, ami form adatot vár
- **Sorrend fontos** – A `test_login` feltételezi, hogy a `test_regisztracio` már lefutott. A tesztek sorrendjétől való függés bizonytalan! A megoldás: fixture-ökbe szervezni (lásd a következő órát).
- **`"access_token" in response.json()`** – Nem a token értékét ellenőrizzük (az minden alkalommal más), hanem a kulcs jelenlétét. A token értéket a védett végpontnál fogjuk felhasználni.

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

### 🧠 Részletes Magyarázat

- **Negatív teszt** – A `test_vedett_vegpont_token_nelkul` teszt azt ellenőrzi, hogy token nélkül **nem** lehet hozzáférni a végponthoz. Ez legalább annyira fontos, mint a pozitív teszt! Ha ez átmegy 200-zal, az biztonsági rést jelent.
- **`headers={"Authorization": f"Bearer {token}"}`** – A TestClient-ben a `headers` paraméterrel küldünk egyedi fejlécet. Az `Authorization` fejléc a `Bearer ` prefixszel tartalmazza a JWT tokent.
- **`get_token()` segédfüggvény** – Regisztrál egy felhasználót, bejelentkezik, és visszaadja a tokent. Ezt fixture-ként kellene megírni (lásd conftest.py), de segédfüggvényként is működik.

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

### 🧠 Részletes Magyarázat

- **`client` fixture** – A `TestClient(app)` létrehozása fixture-ben történik, nem globális szinten. Így minden teszt friss klienst kap (bár a `TestClient` állapotmentes, szokás fixture-be tenni a tesztelhetőség miatt).
- **`auth_headers` fixture** – Előkészít egy bejelentkezett felhasználót és visszaadja az auth fejlécet dict-ként. Bármelyik tesztben használható paraméterként.
- **Fixture láncolás** – Az `auth_headers` fixture a `client` fixture-t használja paraméterként. A pytest automatikusan feloldja a függőséget: először a `client`-et hozza létre, majd átadja az `auth_headers`-nek.

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

### 🧠 Részletes Magyarázat

- **`client, auth_headers`** – A tesztfüggvény két fixture-t is kérhet egyszerre. A pytest mindkettőt automatikusan létrehozza és átadja.
- **Authentikáció nélkül** – A második teszt szándékosan nem kér `auth_headers`-t. Így token nélkül hívja a végpontot, és 401-et vár. Ez biztosítja, hogy a végpont valóban védett.
- **Fontos minta:** Minden védett végpontra írj **két** tesztet: (1) tokennel → 2xx, (2) token nélkül → 401.

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
