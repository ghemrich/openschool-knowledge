# Backend FastAPI szintfelmérő (D variáns: Recept API)

**Időtartam:** 240 perc
**Összpontszám:** 60 pont

---

## 1. feladat – Pydantic sémák és utility függvények (10 pont)

Készítsd el a `schemas.py` és `utils.py` fájlokat a Recept API-hoz.

### 1.1 Pydantic sémák (`schemas.py`) (6 pont)

Hozd létre az alábbi Pydantic modelleket:

**`ReceptCreate`:**
- `nev`: kötelező string, legalább 3 karakter
- `leiras`: opcionális string, alapértelmezett `None`
- `kategoria`: kötelező string, legalább 2 karakter (pl. `"leves"`, `"főétel"`, `"desszert"`)
- `elkeszitesi_ido`: int, legalább 1 (percben)
- `kaloria`: int, legalább 0, alapértelmezett 0

**`ReceptRead`:**
- Minden mező, ami a `ReceptCreate`-ben van, plusz:
- `id`: int
- `kedvenc`: bool, alapértelmezett `False`
- `letrehozva`: string

**`ReceptUpdate`:**
- `nev`: opcionális string
- `leiras`: opcionális string
- `kategoria`: opcionális string
- `elkeszitesi_ido`: opcionális int (legalább 1)
- `kaloria`: opcionális int (legalább 0)
- `kedvenc`: opcionális bool

**`FelhasznaloCreate`:**
- `felhasznalonev`: kötelező string, legalább 3 karakter
- `jelszo`: kötelező string, legalább 6 karakter

**`Token`:**
- `access_token`: string
- `token_type`: string, alapértelmezett `"bearer"`

### 1.2 Utility függvények (`utils.py`) (4 pont)

Írj segédfüggvényeket:

1. **`ido_formatum(perc: int) -> str`** – A percet formázza: `"1 óra 30 perc"`. Ha kevesebb mint 60 perc: `"45 perc"`. Ha pontosan 60: `"1 óra"`.

2. **`kaloria_kategoria(kaloria: int) -> str`** – Kategorizálja a kalóriát: 0–200 → `"könnyű"`, 201–500 → `"közepes"`, 501+ → `"kalóriadús"`.

3. **`szuro_kategoria(receptek: list[dict], kategoria: str) -> list[dict]`** – Visszaadja az adott kategóriájú recepteket.

4. **`statisztika(receptek: list[dict]) -> dict`** – Visszaad egy szótárt: `{"osszes": int, "kedvenc": int, "atlag_ido": float, "atlag_kaloria": float}`

---

## 2. feladat – SQLAlchemy adatbázis és CRUD API (20 pont)

### 2.1 Adatbázis beállítás (6 pont)

**`database.py`** – Adatbázis konfiguráció:
- SQLite adatbázis (`sqlite:///./receptek.db`)
- `engine`, `SessionLocal`, `Base` definiálása
- `get_db()` dependency függvény (yield + close minta)

**`models.py`** – SQLAlchemy modellek:

**`ReceptModel`** tábla (`receptek`):
- `id`: Integer, primary key, auto increment
- `nev`: String, kötelező
- `leiras`: String, opcionális
- `kategoria`: String, kötelező
- `elkeszitesi_ido`: Integer, kötelező
- `kaloria`: Integer, alapértelmezett 0
- `kedvenc`: Boolean, alapértelmezett False
- `letrehozva`: String, alapértelmezett az aktuális dátum

**`FelhasznaloModel`** tábla (`felhasznalok`):
- `id`: Integer, primary key, auto increment
- `felhasznalonev`: String, unique, kötelező
- `jelszo_hash`: String, kötelező

### 2.2 CRUD végpontok (`main.py`) (14 pont)

Készíts egy FastAPI alkalmazást a receptek kezeléséhez. Az adatokat SQLAlchemy-n keresztül SQLite adatbázisban tárold.

1. **`GET /`** – Visszaadja: `{"message": "Recept API"}`. Státusz: `200`

2. **`GET /receptek`** – Visszaadja az összes receptet. Támogasd az opcionális query paramétereket:
   - `?kategoria=leves` → csak az adott kategóriájú receptek
   - `?max_ido=30` → csak a megadott időnél rövidebb elkészítésű receptek

3. **`GET /receptek/{recept_id}`** – Visszaadja az adott ID-jű receptet. Ha nem létezik: `404` + `{"detail": "Recept nem található"}`

4. **`POST /receptek`** – 🔒 **Védett végpont** – Új recept létrehozása. A `kedvenc` legyen `False`, a `letrehozva` az aktuális dátum. Státusz: `201`

5. **`PUT /receptek/{recept_id}`** – Recept módosítása. Csak a megadott mezőket frissítsd (`exclude_unset`). Ha nem létezik: `404`

6. **`DELETE /receptek/{recept_id}`** – 🔒 **Védett végpont** – Recept törlése. Ha nem létezik: `404`. Státusz: `200` + `{"message": "Recept törölve"}`

7. **`GET /receptek/statisztika`** – Visszaad egy statisztikát: `{"osszes", "kedvenc", "atlag_ido", "atlag_kaloria"}` (figyelem: a `/{recept_id}` elé kell kerüljön a routerben!)

### Adatfájl betöltése:

Az alkalmazás indulásakor olvasd be a `receptek.txt` fájlt, és töltsd be az adatbázisba (de csak ha üres a tábla). A fájl formátuma:

```
név;leírás;kategória;elkészítési_idő;kalória;kedvenc
```

---

## 3. feladat – Authentikáció (10 pont)

Készíts egyszerű JWT alapú authentikációt az `auth.py` fájlban.

### Végpontok:

1. **`POST /auth/regisztracio`** – Új felhasználó regisztrálása. A jelszót **hash-elve** tárold (`passlib` + `bcrypt`). Ha a felhasználónév foglalt: `400` + `{"detail": "Felhasználónév foglalt"}`. Státusz: `201`

2. **`POST /auth/login`** – Bejelentkezés felhasználónévvel és jelszóval. Helyes adatok esetén JWT tokent ad vissza. Hibás adatok: `401` + `{"detail": "Hibás bejelentkezési adatok"}`

3. **`get_current_user` dependency** – Token ellenőrzés `OAuth2PasswordBearer`-rel. Ha nincs token vagy érvénytelen: `401`.

### A `POST /receptek` és `DELETE /receptek/{id}` végpontokat védd meg ezzel a dependency-vel!

**Segítség:**
- Használd a `passlib[bcrypt]` csomagot jelszó hash-eléshez
- Használd a `python-jose[cryptography]` csomagot JWT token generáláshoz
- A titkos kulcsot hardcódolhatod vizsgán: `SECRET_KEY = "vizsga2026"`
- Használd az `APIRouter`-t és `app.include_router()`-t a `main.py`-ban

---

## 4. feladat – Adatfeldolgozás (10 pont)

Készíts egy `feldolgozas.py` modult az alábbi függvényekkel (a `receptek.txt` fájl alapján):

1. **`beolvasas(fajlnev: str) -> list[dict]`** – Beolvassa a fájlt, és szótárak listájaként adja vissza. Az elkészítési időt és kalóriát `int`-re, a `kedvenc` mezőt `bool`-ra alakítsd.

2. **`osszes_darab(receptek: list[dict]) -> int`** – Visszaadja a receptek számát.

3. **`atlag_kaloria(receptek: list[dict]) -> float`** – Visszaadja az átlagos kalóriát, 1 tizedesre kerekítve.

4. **`leggyorsabb(receptek: list[dict]) -> dict`** – Visszaadja a legrövidebb elkészítési idejű receptet.

5. **`kategoriak_szerint(receptek: list[dict]) -> dict`** – Visszaad egy szótárt, ahol a kulcs a kategória, az érték a darabszám.

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

Írj pytest teszteket a `test_receptek.py` fájlba (`TestClient` használatával):

1. **`test_root`** – A `GET /` végpont 200-as státuszt ad
2. **`test_create_recept_unauthorized`** – Token nélkül a `POST /receptek` 401-et ad
3. **`test_register`** – A `POST /auth/regisztracio` 201-es státuszt ad
4. **`test_login`** – A `POST /auth/login` tokent ad vissza (`access_token` kulcs)
5. **`test_create_recept_with_auth`** – Regisztráció → login → token-nel `POST /receptek` 201-et ad
6. **`test_get_receptek`** – A `GET /receptek` 200-as státuszt ad és lista
7. **`test_get_recept_not_found`** – A `GET /receptek/9999` 404-et ad
8. **`test_delete_recept_unauthorized`** – Token nélkül a `DELETE` 401-et ad

---

## 📚 Segédanyagok

- [Kurzus tananyagok és leckék](../../doksik/tanulok/README.md)
- [FastAPI dokumentáció](https://fastapi.tiangolo.com/)
- [SQLAlchemy dokumentáció](https://docs.sqlalchemy.org/en/20/)
- [Pydantic dokumentáció](https://docs.pydantic.dev/latest/)

## Beadás

1. Commitold és pushold a megoldásod a GitHub Classroom repóba
2. Ellenőrizd az Actions fülön, hogy a tesztek sikeresen lefutnak
3. **Fájlok:** `schemas.py`, `utils.py`, `database.py`, `models.py`, `auth.py`, `main.py`, `feldolgozas.py`, `test_receptek.py`, `Dockerfile`, `requirements.txt`
