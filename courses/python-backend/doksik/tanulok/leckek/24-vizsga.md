# Lecke 24 – Vizsga

---

## A vizsgáról

- **Időtartam:** 240 perc
- **Összpontszám:** 60 pont
- **Eszközök:** Saját gép, VS Code, dokumentáció (internet), Docker
- **Nem használható:** AI eszközök, más személy segítsége, korábbi megoldások másolása

---

## Vizsga felépítése

### 1. feladat – Pydantic sémák és utility függvények (10 pont)

Készítsd el a `schemas.py` és `utils.py` fájlokat:
- Pydantic sémák (Create, Read, Update + auth sémák: FelhasznaloCreate, Token) (6 pont)
- 4 utility/validációs segédfüggvény (4 pont)

### 2. feladat – SQLAlchemy adatbázis és CRUD API (20 pont)

- SQLAlchemy modell a megadott mezőkkel + Felhasználó modell (6 pont)
- SQLite adatbázis (`database.py`: engine, SessionLocal, Base, get_db) (6 pont)
- CRUD végpontok: GET all (query paraméterekkel), GET by id, POST (védett), PUT, DELETE (védett), statisztika (14 pont)
- Adatfájl betöltése (txt → DB) az induláskor

### 3. feladat – JWT autentikáció (10 pont)

- `POST /auth/regisztracio` – jelszó hash-elés (`passlib` + `bcrypt`) (3 pont)
- `POST /auth/login` – JWT token generálás (`python-jose`) (3 pont)
- `get_current_user` dependency – token ellenőrzés, védett végpontok (4 pont)

### 4. feladat – Adatfeldolgozás (10 pont)

- `feldolgozas.py`: 5 függvény az adatfájl feldolgozására
- Beolvasás, darabszám, statisztikák, szűrés, csoportosítás

### 5. feladat – Docker és tesztelés (10 pont)

- `Dockerfile` (python:3.11-slim, uvicorn, port 8000) (2,5 pont)
- `requirements.txt` a szükséges csomagokkal (2,5 pont)
- pytest tesztek `TestClient`-tel (min. 8 teszt) (5 pont)

---

## Értékelés

| Szint | Pontszám |
|-------|----------|
| Kiváló | 54–60 |
| Haladó | 43–53 |
| Megfelelő | 31–42 |
| Kezdő | 19–30 |
| Nem teljesített | 0–18 |

---

## Beadás

1. Pushold a kész projektet a GitHub Classroom repóba
2. Ellenőrizd az Actions fülön, hogy a tesztek sikeresen lefutnak
3. **Fájlok:** `schemas.py`, `utils.py`, `database.py`, `models.py`, `auth.py`, `main.py`, `feldolgozas.py`, `test_*.py`, `Dockerfile`, `requirements.txt`

---

## Felkészülési tippek

- Ismételd át a leckéket, különösen a kód példákat
- Gyakorold a teljes projekt felépítést a nulláról (ez a legfontosabb)
- Próbáld megoldani a próbavizsga feladatot (12. lecke) időre
- Készíts saját "sablon projektet" amit gyorsan tudsz módosítani
- Ellenőrizd, hogy a Docker és pytest beállítások működnek
