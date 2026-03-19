# Backend FastAPI szintfelmérő (A variáns: Todo API)

**Időtartam:** 240 perc
**Összpontszám:** 60 pont

---

## 1. feladat – Pydantic sémák és utility függvények (10 pont)

Készítsd el a `schemas.py` és `utils.py` fájlokat a Todo API-hoz.

### 1.1 Pydantic sémák (`schemas.py`) (6 pont)

Hozd létre az alábbi Pydantic modelleket:

**`TodoCreate`:**
- `cim`: kötelező string, legalább 3 karakter
- `leiras`: opcionális string, alapértelmezett `None`
- `prioritas`: int, 1–5 közötti érték (1 = alacsony, 5 = sürgős), alapértelmezett 3
- `hatarido`: opcionális string (`"2026-06-15"` formátum), alapértelmezett `None`

**`TodoRead`:**
- Minden mező, ami a `TodoCreate`-ben van, plusz:
- `id`: int
- `kesz`: bool, alapértelmezett `False`
- `letrehozva`: string

**`TodoUpdate`:**
- `cim`: opcionális string
- `leiras`: opcionális string
- `prioritas`: opcionális int (1–5)
- `hatarido`: opcionális string
- `kesz`: opcionális bool

**`FelhasznaloCreate`:**
- `felhasznalonev`: kötelező string, legalább 3 karakter
- `jelszo`: kötelező string, legalább 6 karakter

**`Token`:**
- `access_token`: string
- `token_type`: string, alapértelmezett `"bearer"`

### 1.2 Utility függvények (`utils.py`) (4 pont)

Írj segédfüggvényeket:

1. **`prioritas_szoveg(prioritas: int) -> str`** – Visszaadja a prioritás szöveges nevét:
   - 1 → `"alacsony"`, 2 → `"normál"`, 3 → `"közepes"`, 4 → `"magas"`, 5 → `"sürgős"`
   - Érvénytelen érték esetén: `"ismeretlen"`

2. **`hatarido_lejart(hatarido: str) -> bool`** – Visszaadja, hogy a határidő lejárt-e (a mai dátumhoz képest). Formátum: `"2026-06-15"`.

3. **`szuro_prioritas(todok: list[dict], min_prioritas: int) -> list[dict]`** – Visszaadja azokat a todo-kat, amelyek prioritása ≥ `min_prioritas`.

4. **`statisztika(todok: list[dict]) -> dict`** – Visszaad egy szótárt: `{"osszes": int, "kesz": int, "hatra_van": int}`

---

## 2. feladat – SQLAlchemy adatbázis és CRUD API (20 pont)

### 2.1 Adatbázis beállítás (6 pont)

**`database.py`** – Adatbázis konfiguráció:
- SQLite adatbázis (`sqlite:///./todok.db`)
- `engine`, `SessionLocal`, `Base` definiálása
- `get_db()` dependency függvény (yield + close minta)

**`models.py`** – SQLAlchemy modellek:

**`TodoModel`** tábla (`todos`):
- `id`: Integer, primary key, auto increment
- `cim`: String, kötelező
- `leiras`: String, opcionális
- `prioritas`: Integer, alapértelmezett 3
- `hatarido`: String, opcionális
- `kesz`: Boolean, alapértelmezett False
- `letrehozva`: String, alapértelmezett az aktuális dátum

**`FelhasznaloModel`** tábla (`felhasznalok`):
- `id`: Integer, primary key, auto increment
- `felhasznalonev`: String, unique, kötelező
- `jelszo_hash`: String, kötelező

### 2.2 CRUD végpontok (`main.py`) (14 pont)

Készíts egy FastAPI alkalmazást a Todo-k kezeléséhez. Az adatokat SQLAlchemy-n keresztül SQLite adatbázisban tárold.

1. **`GET /`** – Visszaadja: `{"message": "Todo API"}`. Státusz: `200`

2. **`GET /todos`** – Visszaadja az összes todo-t. Támogasd az opcionális query paramétereket:
   - `?kesz=true` → csak a kész todo-k
   - `?min_prioritas=3` → csak a megadott vagy magasabb prioritásúak

3. **`GET /todos/{todo_id}`** – Visszaadja az adott ID-jű todo-t. Ha nem létezik: `404` + `{"detail": "Todo nem található"}`

4. **`POST /todos`** – 🔒 **Védett végpont** – Új todo létrehozása. A `kesz` legyen `False`, a `letrehozva` az aktuális dátum. Státusz: `201`

5. **`PUT /todos/{todo_id}`** – Todo módosítása. Csak a megadott mezőket frissítsd (`exclude_unset`). Ha nem létezik: `404`

6. **`DELETE /todos/{todo_id}`** – 🔒 **Védett végpont** – Todo törlése. Ha nem létezik: `404`. Státusz: `200` + `{"message": "Todo törölve"}`

7. **`GET /todos/statisztika`** – Visszaad egy statisztikát: `{"osszes", "kesz", "hatra_van"}` (figyelem: a `/{todo_id}` elé kell kerüljön a routerben!)

### Adatfájl betöltése:

Az alkalmazás indulásakor olvasd be a `todok.txt` fájlt, és töltsd be az adatbázisba (de csak ha üres a tábla). A fájl formátuma:

```
cím;leírás;prioritás;határidő;kész
```

---

## 3. feladat – Authentikáció (10 pont)

Készíts egyszerű JWT alapú authentikációt az `auth.py` fájlban.

### Végpontok:

1. **`POST /auth/regisztracio`** – Új felhasználó regisztrálása. A jelszót **hash-elve** tárold (`passlib` + `bcrypt`). Ha a felhasználónév foglalt: `400` + `{"detail": "Felhasználónév foglalt"}`. Státusz: `201`

2. **`POST /auth/login`** – Bejelentkezés felhasználónévvel és jelszóval. Helyes adatok esetén JWT tokent ad vissza. Hibás adatok: `401` + `{"detail": "Hibás bejelentkezési adatok"}`

3. **`get_current_user` dependency** – Token ellenőrzés `OAuth2PasswordBearer`-rel. Ha nincs token vagy érvénytelen: `401`.

### A `POST /todos` és `DELETE /todos/{id}` végpontokat védd meg ezzel a dependency-vel!

**Segítség:**
- Használd a `passlib[bcrypt]` csomagot jelszó hash-eléshez
- Használd a `python-jose[cryptography]` csomagot JWT token generáláshoz
- A titkos kulcsot hardcódolhatod vizsgán: `SECRET_KEY = "vizsga2026"`
- Használd az `APIRouter`-t és `app.include_router()`-t a `main.py`-ban

---

## 4. feladat – Adatfeldolgozás (10 pont)

Készíts egy `feldolgozas.py` modult az alábbi függvényekkel (a `todok.txt` fájl alapján):

1. **`beolvasas(fajlnev: str) -> list[dict]`** – Beolvassa a fájlt, és szótárak listájaként adja vissza. A prioritást `int`-re, a `kész` mezőt `bool`-ra alakítsd.

2. **`osszes_darab(todok: list[dict]) -> int`** – Visszaadja a todo-k számát.

3. **`kesz_arany(todok: list[dict]) -> float`** – Visszaadja a kész todo-k arányát százalékban (pl. `42.5`), 1 tizedesre kerekítve.

4. **`legmagasabb_prioritas(todok: list[dict]) -> list[dict]`** – Visszaadja az 5-ös (sürgős) prioritású todo-kat.

5. **`kategoriak_szerint(todok: list[dict]) -> dict`** – Visszaad egy szótárt, ahol a kulcs a prioritás (int), az érték a darabszám.

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

Írj pytest teszteket a `test_todos.py` fájlba (`TestClient` használatával):

1. **`test_root`** – A `GET /` végpont 200-as státuszt ad
2. **`test_create_todo_unauthorized`** – Token nélkül a `POST /todos` 401-et ad
3. **`test_register`** – A `POST /auth/regisztracio` 201-es státuszt ad
4. **`test_login`** – A `POST /auth/login` tokent ad vissza (`access_token` kulcs)
5. **`test_create_todo_with_auth`** – Regisztráció → login → token-nel `POST /todos` 201-et ad
6. **`test_get_todos`** – A `GET /todos` 200-as státuszt ad és lista
7. **`test_get_todo_not_found`** – A `GET /todos/9999` 404-et ad
8. **`test_delete_todo_unauthorized`** – Token nélkül a `DELETE` 401-et ad

---

## 📚 Segédanyagok

- [Kurzus tananyagok és leckék](../../doksik/tanulok/README.md)
- [FastAPI dokumentáció](https://fastapi.tiangolo.com/)
- [SQLAlchemy dokumentáció](https://docs.sqlalchemy.org/en/20/)
- [Pydantic dokumentáció](https://docs.pydantic.dev/latest/)

## Beadás

1. Commitold és pushold a megoldásod a GitHub Classroom repóba
2. Ellenőrizd az Actions fülön, hogy a tesztek sikeresen lefutnak
3. **Fájlok:** `schemas.py`, `utils.py`, `database.py`, `models.py`, `auth.py`, `main.py`, `feldolgozas.py`, `test_todos.py`, `Dockerfile`, `requirements.txt`
