# Lecke 16 – Haladó tesztelési minták

> **Dokumentáció:** [pytest parametrize](https://docs.pytest.org/en/stable/how-to/parametrize.html) · [pytest markers](https://docs.pytest.org/en/stable/how-to/mark.html) · [coverage](https://coverage.readthedocs.io/)

---

## 97–98. óra: Parametrizált és negatív tesztek

### Parametrizált API tesztek

```python
import pytest

@pytest.mark.parametrize("nev, ar, status", [
    ("Laptop", 350000, 201),        # érvényes
    ("", 100, 422),                  # üres név → validációs hiba
    ("Telefon", -500, 422),          # negatív ár → validációs hiba
    ("Tablet", 0, 422),              # nulla ár → validációs hiba
])
def test_create_item_validacio(client, auth_headers, nev, ar, status):
    response = client.post("/items", json={
        "nev": nev,
        "ar": ar
    }, headers=auth_headers)
    assert response.status_code == status
```

### Negatív tesztek

A jó teszt suite nemcsak a **helyes** viselkedést ellenőrzi, hanem a **hibás** bemenetekre adott válaszokat is:

```python
def test_login_rossz_jelszo(client):
    client.post("/auth/regisztracio", json={
        "nev": "User", "email": "user@test.com", "jelszo": "helyes"
    })
    response = client.post("/auth/login", data={
        "username": "user@test.com",
        "password": "rossz_jelszo"
    })
    assert response.status_code == 401

def test_login_nem_letezo_user(client):
    response = client.post("/auth/login", data={
        "username": "nincs@test.com",
        "password": "mindegy"
    })
    assert response.status_code == 401

def test_dupla_regisztracio(client):
    adat = {"nev": "User", "email": "dupla@test.com", "jelszo": "jelszo123"}
    client.post("/auth/regisztracio", json=adat)
    response = client.post("/auth/regisztracio", json=adat)
    assert response.status_code == 400

def test_update_mas_itemet(client, auth_headers):
    """Más felhasználó itemjét nem lehet módosítani."""
    # Első user itemje
    resp = client.post("/items", json={"nev": "Item1", "ar": 100}, headers=auth_headers)
    item_id = resp.json()["id"]

    # Második user regisztrál és bejelentkezik
    client.post("/auth/regisztracio", json={
        "nev": "User2", "email": "user2@test.com", "jelszo": "jelszo123"
    })
    login_resp = client.post("/auth/login", data={
        "username": "user2@test.com", "password": "jelszo123"
    })
    headers2 = {"Authorization": f"Bearer {login_resp.json()['access_token']}"}

    # Próbálja módosítani
    response = client.put(f"/items/{item_id}", json={
        "nev": "Hacked", "ar": 0
    }, headers=headers2)
    assert response.status_code == 403
```

---

## 99–100. óra: Teszt szervezés és lefedettség

### Tesztek szervezése fájlokba

```
tests/
├── conftest.py           # közös fixture-ök
├── test_root.py           # GET / teszt
├── test_auth.py           # regisztráció, login, profil
├── test_items_crud.py     # CRUD műveletek
├── test_items_auth.py     # jogosultsági tesztek
└── test_validation.py     # bemeneti validáció
```

### Tesztek címkézése (markers)

```python
# pytest.ini
# [pytest]
# markers =
#     slow: lassú tesztek
#     auth: autentikációs tesztek

@pytest.mark.auth
def test_login(client):
    ...

@pytest.mark.slow
def test_nagy_adathalmaz(client, auth_headers):
    for i in range(100):
        client.post("/items", json={"nev": f"Item {i}", "ar": i}, headers=auth_headers)
    response = client.get("/items")
    assert len(response.json()) == 100
```

```bash
pytest -m auth           # csak auth tesztek
pytest -m "not slow"     # lassú tesztek kihagyása
```

### Kód lefedettség (coverage)

```bash
pip install pytest-cov
pytest --cov=app tests/ -v
pytest --cov=app --cov-report=html tests/   # HTML riport
```

```
---------- coverage: ... ----------
Name                    Stmts   Miss  Cover
-------------------------------------------
app/__init__.py             0      0   100%
app/auth.py                18      2    89%
app/crud.py                25      0   100%
app/main.py                12      0   100%
app/models.py               8      0   100%
-------------------------------------------
TOTAL                      63      2    97%
```

---

## 101–102. óra: Tesztelési best practices

### Jó teszt jellemzői

| Tulajdonság | Leírás |
|-------------|--------|
| **Független** | Nem függ más tesztek állapotától |
| **Ismételhető** | Mindig ugyanazt az eredményt adja |
| **Gyors** | Másodpercek alatt lefut |
| **Érthetően elnevezett** | `test_create_item_without_auth_returns_401` |
| **Egy dolgot tesztel** | Egy assert csoport per teszt |

### AAA minta (Arrange, Act, Assert)

```python
def test_item_modositas(client, auth_headers):
    # Arrange – előkészítés
    resp = client.post("/items", json={"nev": "Régi", "ar": 100}, headers=auth_headers)
    item_id = resp.json()["id"]

    # Act – végrehajtás
    response = client.put(f"/items/{item_id}", json={
        "nev": "Új", "ar": 200
    }, headers=auth_headers)

    # Assert – ellenőrzés
    assert response.status_code == 200
    assert response.json()["nev"] == "Új"
    assert response.json()["ar"] == 200
```

### Tipp: Factory fixture

```python
@pytest.fixture
def create_user(client):
    """Factory fixture: bármennyi usert létrehozhatunk."""
    def _create(nev, email, jelszo="jelszo123"):
        return client.post("/auth/regisztracio", json={
            "nev": nev, "email": email, "jelszo": jelszo
        })
    return _create
```

---

## Gyakorlat

1. Írj legalább 3 parametrizált tesztet
2. Írj negatív teszteket (rossz jelszó, dupla regisztráció, jogosultsági hiba)
3. Szervezd a teszteket logikus fájlokba
4. Futtasd a teszteket coverage riporttal
5. Commitold és pushold
