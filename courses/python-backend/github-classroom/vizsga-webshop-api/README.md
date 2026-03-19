# Backend FastAPI szintfelmérő (C variáns: Webshop API)

**Időtartam:** 240 perc
**Összpontszám:** 60 pont

---

## 1. feladat – Pydantic sémák és utility függvények (10 pont)

Készítsd el a `schemas.py` és `utils.py` fájlokat a Webshop API-hoz.

### 1.1 Pydantic sémák (`schemas.py`) (6 pont)

Hozd létre az alábbi Pydantic modelleket:

**`TermekCreate`:**
- `nev`: kötelező string, legalább 3 karakter
- `leiras`: opcionális string, alapértelmezett `None`
- `ar`: int, legalább 1 (Ft)
- `kategoria`: kötelező string, legalább 2 karakter
- `keszlet`: int, legalább 0, alapértelmezett 0

**`TermekRead`:**
- Minden mező, ami a `TermekCreate`-ben van, plusz:
- `id`: int
- `aktiv`: bool, alapértelmezett `True`
- `letrehozva`: string

**`TermekUpdate`:**
- `nev`: opcionális string
- `leiras`: opcionális string
- `ar`: opcionális int (legalább 1)
- `kategoria`: opcionális string
- `keszlet`: opcionális int (legalább 0)
- `aktiv`: opcionális bool

**`FelhasznaloCreate`:**
- `felhasznalonev`: kötelező string, legalább 3 karakter
- `jelszo`: kötelező string, legalább 6 karakter

**`Token`:**
- `access_token`: string
- `token_type`: string, alapértelmezett `"bearer"`

### 1.2 Utility függvények (`utils.py`) (4 pont)

Írj segédfüggvényeket:

1. **`ar_formatum(ar: int) -> str`** – Visszaadja a formázott árat: `"1 500 Ft"` (ezres elválasztóval és Ft végződéssel).

2. **`keszleten_van(termek: dict) -> bool`** – Visszaadja, hogy a termék készleten van-e (`keszlet > 0`).

3. **`szuro_kategoria(termekek: list[dict], kategoria: str) -> list[dict]`** – Visszaadja az adott kategóriájú termékeket.

4. **`statisztika(termekek: list[dict]) -> dict`** – Visszaad egy szótárt: `{"osszes": int, "keszleten": int, "kifogyott": int, "atlag_ar": float}`

---

## 2. feladat – SQLAlchemy adatbázis és CRUD API (20 pont)

### 2.1 Adatbázis beállítás (6 pont)

**`database.py`** – Adatbázis konfiguráció:
- SQLite adatbázis (`sqlite:///./webshop.db`)
- `engine`, `SessionLocal`, `Base` definiálása
- `get_db()` dependency függvény (yield + close minta)

**`models.py`** – SQLAlchemy modellek:

**`TermekModel`** tábla (`termekek`):
- `id`: Integer, primary key, auto increment
- `nev`: String, kötelező
- `leiras`: String, opcionális
- `ar`: Integer, kötelező
- `kategoria`: String, kötelező
- `keszlet`: Integer, alapértelmezett 0
- `aktiv`: Boolean, alapértelmezett True
- `letrehozva`: String, alapértelmezett az aktuális dátum

**`FelhasznaloModel`** tábla (`felhasznalok`):
- `id`: Integer, primary key, auto increment
- `felhasznalonev`: String, unique, kötelező
- `jelszo_hash`: String, kötelező

### 2.2 CRUD végpontok (`main.py`) (14 pont)

Készíts egy FastAPI alkalmazást a termékek kezeléséhez. Az adatokat SQLAlchemy-n keresztül SQLite adatbázisban tárold.

1. **`GET /`** – Visszaadja: `{"message": "Webshop API"}`. Státusz: `200`

2. **`GET /termekek`** – Visszaadja az összes terméket. Támogasd az opcionális query paramétereket:
   - `?kategoria=elektronika` → csak az adott kategóriájú termékek
   - `?min_ar=1000` → csak a megadott ár feletti termékek
   - `?max_ar=5000` → csak a megadott ár alatti termékek

3. **`GET /termekek/{termek_id}`** – Visszaadja az adott ID-jű terméket. Ha nem létezik: `404` + `{"detail": "Termék nem található"}`

4. **`POST /termekek`** – 🔒 **Védett végpont** – Új termék létrehozása. Az `aktiv` legyen `True`, a `letrehozva` az aktuális dátum. Státusz: `201`

5. **`PUT /termekek/{termek_id}`** – Termék módosítása. Csak a megadott mezőket frissítsd (`exclude_unset`). Ha nem létezik: `404`

6. **`DELETE /termekek/{termek_id}`** – 🔒 **Védett végpont** – Termék törlése. Ha nem létezik: `404`. Státusz: `200` + `{"message": "Termék törölve"}`

7. **`GET /termekek/statisztika`** – Visszaad egy statisztikát: `{"osszes", "keszleten", "kifogyott", "atlag_ar"}` (figyelem: a `/{termek_id}` elé kell kerüljön a routerben!)

### Adatfájl betöltése:

Az alkalmazás indulásakor olvasd be a `termekek.txt` fájlt, és töltsd be az adatbázisba (de csak ha üres a tábla). A fájl formátuma:

```
név;leírás;ár;kategória;készlet;aktív
```

---

## 3. feladat – Authentikáció (10 pont)

Készíts egyszerű JWT alapú authentikációt az `auth.py` fájlban.

### Végpontok:

1. **`POST /auth/regisztracio`** – Új felhasználó regisztrálása. A jelszót **hash-elve** tárold (`passlib` + `bcrypt`). Ha a felhasználónév foglalt: `400` + `{"detail": "Felhasználónév foglalt"}`. Státusz: `201`

2. **`POST /auth/login`** – Bejelentkezés felhasználónévvel és jelszóval. Helyes adatok esetén JWT tokent ad vissza. Hibás adatok: `401` + `{"detail": "Hibás bejelentkezési adatok"}`

3. **`get_current_user` dependency** – Token ellenőrzés `OAuth2PasswordBearer`-rel. Ha nincs token vagy érvénytelen: `401`.

### A `POST /termekek` és `DELETE /termekek/{id}` végpontokat védd meg ezzel a dependency-vel!

**Segítség:**
- Használd a `passlib[bcrypt]` csomagot jelszó hash-eléshez
- Használd a `python-jose[cryptography]` csomagot JWT token generáláshoz
- A titkos kulcsot hardcódolhatod vizsgán: `SECRET_KEY = "vizsga2026"`
- Használd az `APIRouter`-t és `app.include_router()`-t a `main.py`-ban

---

## 4. feladat – Adatfeldolgozás (10 pont)

Készíts egy `feldolgozas.py` modult az alábbi függvényekkel (a `termekek.txt` fájl alapján):

1. **`beolvasas(fajlnev: str) -> list[dict]`** – Beolvassa a fájlt, és szótárak listájaként adja vissza. Az árat és készletet `int`-re, az `aktiv` mezőt `bool`-ra alakítsd.

2. **`osszes_darab(termekek: list[dict]) -> int`** – Visszaadja a termékek számát.

3. **`atlag_ar(termekek: list[dict]) -> float`** – Visszaadja az átlagárat, 1 tizedesre kerekítve.

4. **`legdragabb(termekek: list[dict]) -> dict`** – Visszaadja a legdrágább terméket.

5. **`kategoriak_szerint(termekek: list[dict]) -> dict`** – Visszaad egy szótárt, ahol a kulcs a kategória, az érték a darabszám.

---

## 5. feladat – Docker és tesztelés (10 pont)

### 5.1 Docker (5 pont)

Készíts `Dockerfile`-t az alkalmazáshoz:
- `python:3.11-slim` base image
- Munkadirektória: `/app`
- `requirements.txt` másolása és telepítése (`pip install`)
- Az összes fájl bemásolása
- Az alkalmazás a `8000`-es porton fusson (`uvicorn main:app`)

Készíts `requirements.txt` fájlt a szükséges csomagokkal.

### 5.2 Tesztelés (5 pont)

Írj pytest teszteket a `test_webshop.py` fájlba (`TestClient` használatával):

1. **`test_root`** – A `GET /` végpont 200-as státuszt ad
2. **`test_create_termek_unauthorized`** – Token nélkül a `POST /termekek` 401-et ad
3. **`test_register`** – A `POST /auth/regisztracio` 201-es státuszt ad
4. **`test_login`** – A `POST /auth/login` tokent ad vissza (`access_token` kulcs)
5. **`test_create_termek_with_auth`** – Regisztráció → login → token-nel `POST /termekek` 201-et ad
6. **`test_get_termekek`** – A `GET /termekek` 200-as státuszt ad és lista
7. **`test_get_termek_not_found`** – A `GET /termekek/9999` 404-et ad
8. **`test_delete_termek_unauthorized`** – Token nélkül a `DELETE` 401-et ad

---

## 📚 Segédanyagok

- [Kurzus tananyagok és leckék](../../doksik/tanulok/README.md)
- [FastAPI dokumentáció](https://fastapi.tiangolo.com/)
- [SQLAlchemy dokumentáció](https://docs.sqlalchemy.org/en/20/)
- [Pydantic dokumentáció](https://docs.pydantic.dev/latest/)

## Beadás

1. Commitold és pushold a megoldásod a GitHub Classroom repóba
2. Ellenőrizd az Actions fülön, hogy a tesztek sikeresen lefutnak
3. **Fájlok:** `schemas.py`, `utils.py`, `database.py`, `models.py`, `auth.py`, `main.py`, `feldolgozas.py`, `test_webshop.py`, `Dockerfile`, `requirements.txt`
