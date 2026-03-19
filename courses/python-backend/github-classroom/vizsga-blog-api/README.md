# Backend FastAPI szintfelmérő (B variáns: Blog API)

**Időtartam:** 240 perc
**Összpontszám:** 60 pont

---

## 1. feladat – Pydantic sémák és utility függvények (10 pont)

Készítsd el a `schemas.py` és `utils.py` fájlokat a Blog API-hoz.

### 1.1 Pydantic sémák (`schemas.py`) (6 pont)

Hozd létre az alábbi Pydantic modelleket:

**`PostCreate`:**
- `cim`: kötelező string, legalább 5 karakter
- `tartalom`: kötelező string, legalább 10 karakter
- `szerzo`: kötelező string, legalább 3 karakter
- `cimke`: opcionális string, alapértelmezett `None`

**`PostRead`:**
- Minden mező, ami a `PostCreate`-ben van, plusz:
- `id`: int
- `publikalva`: bool, alapértelmezett `False`
- `letrehozva`: string

**`PostUpdate`:**
- `cim`: opcionális string
- `tartalom`: opcionális string
- `cimke`: opcionális string
- `publikalva`: opcionális bool

**`FelhasznaloCreate`:**
- `felhasznalonev`: kötelező string, legalább 3 karakter
- `jelszo`: kötelező string, legalább 6 karakter

**`Token`:**
- `access_token`: string
- `token_type`: string, alapértelmezett `"bearer"`

### 1.2 Utility függvények (`utils.py`) (4 pont)

Írj segédfüggvényeket:

1. **`szavak_szama(tartalom: str) -> int`** – Visszaadja a szövegben lévő szavak számát.

2. **`rovid_kivonat(tartalom: str, max_hossz: int = 100) -> str`** – Visszaadja a tartalom első `max_hossz` karakterét. Ha a szöveg hosszabb, `"..."` kerüljön a végére.

3. **`szuro_cimke(posztok: list[dict], cimke: str) -> list[dict]`** – Visszaadja azokat a posztokat, amelyeknek a címkéje megegyezik a megadottal.

4. **`statisztika(posztok: list[dict]) -> dict`** – Visszaad egy szótárt: `{"osszes": int, "publikus": int, "piszkozat": int}`

---

## 2. feladat – SQLAlchemy adatbázis és CRUD API (20 pont)

### 2.1 Adatbázis beállítás (6 pont)

**`database.py`** – Adatbázis konfiguráció:
- SQLite adatbázis (`sqlite:///./blog.db`)
- `engine`, `SessionLocal`, `Base` definiálása
- `get_db()` dependency függvény (yield + close minta)

**`models.py`** – SQLAlchemy modellek:

**`PostModel`** tábla (`posts`):
- `id`: Integer, primary key, auto increment
- `cim`: String, kötelező
- `tartalom`: String, kötelező
- `szerzo`: String, kötelező
- `cimke`: String, opcionális
- `publikalva`: Boolean, alapértelmezett False
- `letrehozva`: String, alapértelmezett az aktuális dátum

**`FelhasznaloModel`** tábla (`felhasznalok`):
- `id`: Integer, primary key, auto increment
- `felhasznalonev`: String, unique, kötelező
- `jelszo_hash`: String, kötelező

### 2.2 CRUD végpontok (`main.py`) (14 pont)

Készíts egy FastAPI alkalmazást a blogposztok kezeléséhez. Az adatokat SQLAlchemy-n keresztül SQLite adatbázisban tárold.

1. **`GET /`** – Visszaadja: `{"message": "Blog API"}`. Státusz: `200`

2. **`GET /posts`** – Visszaadja az összes posztot. Támogasd az opcionális query paramétereket:
   - `?publikalva=true` → csak a publikus posztok
   - `?cimke=tech` → csak az adott címkéjű posztok

3. **`GET /posts/{post_id}`** – Visszaadja az adott ID-jű posztot. Ha nem létezik: `404` + `{"detail": "Poszt nem található"}`

4. **`POST /posts`** – 🔒 **Védett végpont** – Új poszt létrehozása. A `publikalva` legyen `False`, a `letrehozva` az aktuális dátum. Státusz: `201`

5. **`PUT /posts/{post_id}`** – Poszt módosítása. Csak a megadott mezőket frissítsd (`exclude_unset`). Ha nem létezik: `404`

6. **`DELETE /posts/{post_id}`** – 🔒 **Védett végpont** – Poszt törlése. Ha nem létezik: `404`. Státusz: `200` + `{"message": "Poszt törölve"}`

7. **`GET /posts/statisztika`** – Visszaad egy statisztikát: `{"osszes", "publikus", "piszkozat"}` (figyelem: a `/{post_id}` elé kell kerüljön a routerben!)

### Adatfájl betöltése:

Az alkalmazás indulásakor olvasd be a `posztok.txt` fájlt, és töltsd be az adatbázisba (de csak ha üres a tábla). A fájl formátuma:

```
cím;tartalom;szerző;címke;publikálva
```

---

## 3. feladat – Authentikáció (10 pont)

Készíts egyszerű JWT alapú authentikációt az `auth.py` fájlban.

### Végpontok:

1. **`POST /auth/regisztracio`** – Új felhasználó regisztrálása. A jelszót **hash-elve** tárold (`passlib` + `bcrypt`). Ha a felhasználónév foglalt: `400` + `{"detail": "Felhasználónév foglalt"}`. Státusz: `201`

2. **`POST /auth/login`** – Bejelentkezés felhasználónévvel és jelszóval. Helyes adatok esetén JWT tokent ad vissza. Hibás adatok: `401` + `{"detail": "Hibás bejelentkezési adatok"}`

3. **`get_current_user` dependency** – Token ellenőrzés `OAuth2PasswordBearer`-rel. Ha nincs token vagy érvénytelen: `401`.

### A `POST /posts` és `DELETE /posts/{id}` végpontokat védd meg ezzel a dependency-vel!

**Segítség:**
- Használd a `passlib[bcrypt]` csomagot jelszó hash-eléshez
- Használd a `python-jose[cryptography]` csomagot JWT token generáláshoz
- A titkos kulcsot hardcódolhatod vizsgán: `SECRET_KEY = "vizsga2026"`
- Használd az `APIRouter`-t és `app.include_router()`-t a `main.py`-ban

---

## 4. feladat – Adatfeldolgozás (10 pont)

Készíts egy `feldolgozas.py` modult az alábbi függvényekkel (a `posztok.txt` fájl alapján):

1. **`beolvasas(fajlnev: str) -> list[dict]`** – Beolvassa a fájlt, és szótárak listájaként adja vissza. A `publikalva` mezőt `bool`-ra alakítsd.

2. **`osszes_darab(posztok: list[dict]) -> int`** – Visszaadja a posztok számát.

3. **`publikus_arany(posztok: list[dict]) -> float`** – Visszaadja a publikus posztok arányát százalékban, 1 tizedesre kerekítve.

4. **`leghosszabb_poszt(posztok: list[dict]) -> dict`** – Visszaadja a leghosszabb tartalmú posztot.

5. **`cimkek_szerint(posztok: list[dict]) -> dict`** – Visszaad egy szótárt, ahol a kulcs a címke, az érték a darabszám.

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

Írj pytest teszteket a `test_blog.py` fájlba (`TestClient` használatával):

1. **`test_root`** – A `GET /` végpont 200-as státuszt ad
2. **`test_create_post_unauthorized`** – Token nélkül a `POST /posts` 401-et ad
3. **`test_register`** – A `POST /auth/regisztracio` 201-es státuszt ad
4. **`test_login`** – A `POST /auth/login` tokent ad vissza (`access_token` kulcs)
5. **`test_create_post_with_auth`** – Regisztráció → login → token-nel `POST /posts` 201-et ad
6. **`test_get_posts`** – A `GET /posts` 200-as státuszt ad és lista
7. **`test_get_post_not_found`** – A `GET /posts/9999` 404-et ad
8. **`test_delete_post_unauthorized`** – Token nélkül a `DELETE` 401-et ad

---

## 📚 Segédanyagok

- [Kurzus tananyagok és leckék](../../doksik/tanulok/README.md)
- [FastAPI dokumentáció](https://fastapi.tiangolo.com/)
- [SQLAlchemy dokumentáció](https://docs.sqlalchemy.org/en/20/)
- [Pydantic dokumentáció](https://docs.pydantic.dev/latest/)

## Beadás

1. Commitold és pushold a megoldásod a GitHub Classroom repóba
2. Ellenőrizd az Actions fülön, hogy a tesztek sikeresen lefutnak
3. **Fájlok:** `schemas.py`, `utils.py`, `database.py`, `models.py`, `auth.py`, `main.py`, `feldolgozas.py`, `test_blog.py`, `Dockerfile`, `requirements.txt`
