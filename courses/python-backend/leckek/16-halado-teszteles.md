# 📘 Lecke 16 – Haladó tesztelési minták

> 📚 Dokumentáció:
> https://docs.pytest.org/en/stable/how-to/parametrize.html
> https://docs.pytest.org/en/stable/how-to/mark.html
> https://coverage.readthedocs.io/

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

### 🧠 Részletes Magyarázat

- **Parametrizált API teszt** – Ugyanaz a végpont, de 4 különböző bemenettel tesztelve. Egyetlen tesztfüggvénnyel 4 esetet fedünk le: 1 helyes és 3 hibás.
- **`422 Unprocessable Entity`** – A FastAPI/Pydantic automatikusan visszaadja ezt a státuszkódot, ha a bemeneti adat nem felel meg a sémának (üres string, negatív szám stb.). Nem kell kézzel validálni, ha a Pydantic modellben `Field(min_length=1)` vagy `Field(gt=0)` van.
- **Miért 4 adat?** – Az érvényes eset bizonyítja, hogy a végpont működik. A 3 hibás eset bizonyítja, hogy a validáció működik: üres név, negatív ár, nulla ár. Ezek a leggyakoribb boundary (határ) értékek.

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

### 🧠 Részletes Magyarázat

A negatív tesztek a **biztonsági** és **üzleti szabályok** betartását ellenőrzik:

| Teszt | Mit ellenőriz | Miért fontos |
|-------|--------------|-------------|
| `test_login_rossz_jelszo` | Rossz jelszóval nem lehet belépni | Alap biztonsági követelmény |
| `test_login_nem_letezo_user` | Nem létező email-lel nem lehet belépni | Nem szabad különböző hibaüzenetet adni! (401, nem 404) |
| `test_dupla_regisztracio` | Ugyanaz az email nem regisztrálható kétszer | Adatbázis integritás |
| `test_update_mas_itemet` | Más felhasználó erőforrását nem lehet módosítani | **Broken Access Control** – OWASP Top 1 |

- **401 vs 404 login-nál** – Ha a szerver „Nincs ilyen email" és „Rossz jelszó" különböző üzenetet adna, a támadó megtudhatná, mely email-ek regisztráltak. Mindkét esetben egységes 401-et adunk.
- **403 Forbidden** – A `test_update_mas_itemet` a jogosultsági logikát teszteli: bejelentkezett felhasználó sem módosíthatja más adatát.

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

### 🧠 Részletes Magyarázat

- **Fájlonkénti szervezés** – Minden fájl egy logikai területet fed le. Amikor `test_auth.py` elbukik, tudod, hogy az autentikációval van gond. Ha minden teszt egyetlen fájlban lenne, nehéz lenne megtalálni a problémát.
- **Elnevezési konvenció** – `test_<terület>.py` formátum. A `conftest.py` speciális: a pytest automatikusan betölti.
- **Skálázhatóság** – Kis projektnél 3-5 fájl elég. Nagyobbnál almappákat is használhatunk: `tests/api/`, `tests/models/`, stb.

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

### 🧠 Részletes Magyarázat

- **`@pytest.mark.<marker>`** – Egyedi címkét ad a tesztnek. A marker az `pytest.ini`-ben regisztrálandó (különben warning-ot kapsz).
- **`pytest -m auth`** – Csak az `auth` címkéjű teszteket futtatja. Fejlesztés közben hasznos, ha csak egy területen dolgozol.
- **`pytest -m "not slow"`** – A lassú teszteket kihagyja. A CI-ban mindent futtatsz, de helyi fejlesztésnél a gyors tesztek elegendők.
- **Beépített markerek** – `@pytest.mark.skip`, `@pytest.mark.xfail` (tudjuk, hogy bukni fog – pl. ismert bug), `@pytest.mark.skipif(condition)`.

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

### 🧠 Részletes Magyarázat

- **Coverage (lefedettség)** – Megmutatja, a kód hány százalékát futtatják a tesztek. 97% azt jelenti, hogy a 63 kódsorból 61-et legalább egy teszt érint.
- **`--cov=app`** – Csak az `app/` mappa lefedettségét méri (a `tests/` könyvtárat nem).
- **`--cov-report=html`** – HTML riportot generál a `htmlcov/` mappába. Böngészőben megnyitva soronként zölden/pirossal jelöli, mi futott és mi nem.
- **Stmts** (Statements) – Futtatható kódsorok száma. **Miss** – Nem futtatott sorok. **Cover** – Lefedettség százalék.
- **Cél** – 80% felett jó, 90% felett kiváló. A 100% nem mindig szükséges (pl. error handler, amit nehéz triggerelni).

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

### 🧠 Részletes Magyarázat

- **Független** – Minden teszt önmagában is futtatható, bármilyen sorrendben. A `setup_db` autouse fixture gondoskodik az izoláltságról.
- **Ismételhető** – Ne használj `random`-ot a tesztben (hacsak nem fix seed-del). Ne függj a rendszeridőtől.
- **Érthetően elnevezett** – A teszt neve legyen **mondat**: `test_create_item_without_auth_returns_401`. Bukásnál a név azonnal mondja, mi romlott el.
- **Egy dolgot tesztel** – Ha egy teszt 10 dolgot ellenőriz és elbukik, nem tudod, melyik a hibás. Egy teszt = egy viselkedés.

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

### 🧠 Részletes Magyarázat

- **Arrange** – Előkészítés: létrehozzuk az adatokat, amikre szükség lesz. Itt egy item-et hozunk létre, aminek az `id`-jét a következő lépésben használjuk.
- **Act** – A tesztelendő művelet: egyetlen API hívás. Ez az, amit tesztelni akarunk.
- **Assert** – Ellenőrzés: a válasz az-e, amit vártunk. A státuszkód ÉS a tartalom is fontos.
- **Miért 3 lépés?** – Olvashatóság. Bárki ránéz a tesztre és érti: mit állítunk be, mit csinálunk, mit várunk.

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

### 🧠 Részletes Magyarázat

- **Factory fixture** – Egy fixture, ami nem adatot ad vissza, hanem egy **függvényt**. A teszten belül tetszőleges paraméterekkel hívhatjuk: `create_user("Anna", "anna@test.com")`, `create_user("Béla", "bela@test.com")`.
- **Miért jobb, mint az `auth_headers`?** – Az `auth_headers` mindig ugyanazt az egy felhasználót hozza létre. A factory fixture tetszőleges számú, különböző felhasználót tud létrehozni – hasznos jogosultsági teszteknél.
- **Default paraméter** – A `jelszo="jelszo123"` alapértelmezett érték. Ha nem adjuk meg, minden user ugyanazt a jelszót kapja. Teszt rövidítés.

---

## Gyakorlat

1. Írj legalább 3 parametrizált tesztet
2. Írj negatív teszteket (rossz jelszó, dupla regisztráció, jogosultsági hiba)
3. Szervezd a teszteket logikus fájlokba
4. Futtasd a teszteket coverage riporttal
5. Commitold és pushold
