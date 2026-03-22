# 📘 Lecke 24 – Vizsga

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

### 🧠 Részletes Magyarázat

| Elem | Leírás |
|------|--------|
| **Pydantic sémák** | Minden entitáshoz legalább 3 séma kell: `Create` (létrehozás – kötelező mezők), `Read/Response` (válasz – tartalmazza az `id`-t és időbélyegeket), `Update` (módosítás – opcionális mezők) |
| **Auth sémák** | `FelhasznaloCreate` (nev, email, jelszo) és `Token` (access_token, token_type) – ezek a regisztráció és bejelentkezés be/kimeneti formátumai |
| **Utility függvények** | Segédfüggvények, amelyek a kódot tisztábbá teszik – pl. dátumformázás, szövegvalidáció, adatkonverzió, statisztika számítás |

Tipp: a sémákat a **21. lecke tervei** alapján készítsd el – az ER diagramból közvetlenül látszanak a mezők és típusok.

### 2. feladat – SQLAlchemy adatbázis és CRUD API (20 pont)

- SQLAlchemy modell a megadott mezőkkel + Felhasználó modell (6 pont)
- SQLite adatbázis (`database.py`: engine, SessionLocal, Base, get_db) (6 pont)
- CRUD végpontok: GET all (query paraméterekkel), GET by id, POST (védett), PUT, DELETE (védett), statisztika (14 pont)
- Adatfájl betöltése (txt → DB) az induláskor

### 🧠 Részletes Magyarázat

| Részfeladat | Kapcsolódó lecke | Kulcsfogalmak |
|-------------|-----------------|---------------|
| **SQLAlchemy modell** | 8–9. lecke | `Column`, `ForeignKey`, `relationship`, típusok (`Integer`, `String`, `Text`, `DateTime`) |
| **database.py** | 8. lecke | `create_engine("sqlite:///./app.db")`, `SessionLocal`, `Base = declarative_base()`, `get_db` generator |
| **GET all + query** | 5. lecke | `skip`, `limit` paraméterek, opcionális szűrés (`Query(None)`) |
| **POST (védett)** | 10. lecke | `Depends(get_current_user)` – csak bejelentkezett felhasználó hozhat létre |
| **DELETE (védett)** | 10. lecke + 22. lecke | Token + tulajdonos-ellenőrzés (`szerzo_id == user.id`) |
| **Statisztika** | Egyedi végpont | `func.count()`, `func.avg()` – aggregáló lekérdezések |
| **Adatfájl betöltés** | 10. lecke (fájlkezelés) | A `txt` fájl sorait beolvasod, feldolgozod, és `db.add_all()` + `db.commit()` segítségével az adatbázisba töltöd |

Ez a **legnagyobb pontszámú feladat** (20 pont) – a teljes CRUD + adatbázis réteg, amit a félév során tanultunk. A `database.py` fájl szinte sablon: ha a 8. lecke kódját ismered, gyorsan összerakható.

### 3. feladat – JWT autentikáció (10 pont)

- `POST /auth/regisztracio` – jelszó hash-elés (`passlib` + `bcrypt`) (3 pont)
- `POST /auth/login` – JWT token generálás (`python-jose`) (3 pont)
- `get_current_user` dependency – token ellenőrzés, védett végpontok (4 pont)

### 🧠 Részletes Magyarázat

| Komponens | Csomag | Funkció |
|-----------|--------|---------|
| **Jelszó hash-elés** | `passlib[bcrypt]` | `CryptContext(schemes=["bcrypt"])` → `pwd_context.hash(jelszo)` és `pwd_context.verify(jelszo, hash)` |
| **JWT token generálás** | `python-jose[cryptography]` | `jwt.encode({"sub": email, "exp": lejarat}, SECRET_KEY, algorithm="HS256")` |
| **Token ellenőrzés** | `python-jose` + FastAPI | `jwt.decode(token, SECRET_KEY, algorithms=["HS256"])` → kinyeri az email-t → lekérdezi a felhasználót az adatbázisból |
| **OAuth2 séma** | FastAPI beépített | `OAuth2PasswordBearer(tokenUrl="/auth/login")` – a Swagger UI automatikusan kezeli a bejelentkezést |

A **10. lecke** anyaga alapján építhető fel. A legfontosabb: a `SECRET_KEY` **környezeti változóból** jöjjön (`.env` fájl), soha ne legyen beégetve a kódba. A `get_current_user` dependency a `Depends()` rendszeren keresztül automatikusan védi a végpontokat.

### 4. feladat – Adatfeldolgozás (10 pont)

- `feldolgozas.py`: 5 függvény az adatfájl feldolgozására
- Beolvasás, darabszám, statisztikák, szűrés, csoportosítás

### 🧠 Részletes Magyarázat

| Függvény típusa | Példa | Python eszköz |
|----------------|-------|---------------|
| **Beolvasás** | Fájl sorait listába olvasni | `open("adat.txt", encoding="utf-8")` + `.readlines()` vagy `csv.reader()` |
| **Darabszám** | Összesen hány elem van | `len(lista)` |
| **Statisztikák** | Átlag, min, max | `sum(ertekek) / len(ertekek)`, `min()`, `max()` |
| **Szűrés** | Feltétel alapján kiválogatás | List comprehension: `[x for x in lista if x.kor > 18]` |
| **Csoportosítás** | Kategória szerint rendezés | `defaultdict(list)` vagy egyszerű dict |

Ez a feladat a **Python alapok** kurzus anyagát kéri számon – fájlkezelés, listák, szótárak, list comprehension. Az 5 függvény egymásra építhető: először beolvasás, aztán a beolvasott adaton dolgoznak a többi függvények.

### 5. feladat – Docker és tesztelés (10 pont)

- `Dockerfile` (python:3.11-slim, uvicorn, port 8000) (2,5 pont)
- `requirements.txt` a szükséges csomagokkal (2,5 pont)
- pytest tesztek `TestClient`-tel (min. 8 teszt) (5 pont)

### 🧠 Részletes Magyarázat

| Elem | Tartalom | Lecke |
|------|----------|-------|
| **Dockerfile** | `FROM python:3.11-slim` → `COPY requirements.txt .` → `RUN pip install` → `COPY . .` → `CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]` | 7. és 19. lecke |
| **requirements.txt** | `fastapi`, `uvicorn`, `sqlalchemy`, `python-jose[cryptography]`, `passlib[bcrypt]`, `pytest`, `httpx` | Minden lecke alapján |
| **pytest tesztek** | Minimum 8 teszt: regisztráció, login, CRUD műveletek, jogosultság-ellenőrzés | 13–16. és 23. lecke |

A Dockerfile **rétegelt másolást** használ: először a `requirements.txt`-t másoljuk és telepítjük, aztán a kódot – így az újraépítés gyorsabb, mert a függőségek rétege cache-elhető. A tesztekhez a **15. lecke** conftest.py mintáját használd (SQLite + dependency override).

---

## Értékelés

| Szint | Pontszám |
|-------|----------|
| Kiváló | 54–60 |
| Haladó | 43–53 |
| Megfelelő | 31–42 |
| Kezdő | 19–30 |
| Nem teljesített | 0–18 |

### 🧠 Részletes Magyarázat

- **Kiváló (54–60):** Minden feladat elkészült, a kód tiszta, a tesztek átmennek, a Docker működik.
- **Haladó (43–53):** A legtöbb feladat kész, kisebb hiányosságok (pl. nem minden teszt, vagy a Docker nem tökéletes).
- **Megfelelő (31–42):** Az alapvető CRUD és auth működik, de hiányozhatnak tesztek, Docker, vagy egyes végpontok.
- **Kezdő (19–30):** Részleges megoldás – néhány végpont vagy séma elkészült, de a rendszer nem működik egyben.
- **Nem teljesített (0–18):** Minimális vagy nem beadott munka.

A legfontosabb: **a működő, tesztelt kód több pontot ér**, mint a sok de hibás. Inkább kevesebb végpont tökéletesen, mint az összes félig.

---

## Beadás

1. Pushold a kész projektet a GitHub Classroom repóba
2. Ellenőrizd az Actions fülön, hogy a tesztek sikeresen lefutnak
3. **Fájlok:** `schemas.py`, `utils.py`, `database.py`, `models.py`, `auth.py`, `main.py`, `feldolgozas.py`, `test_*.py`, `Dockerfile`, `requirements.txt`

### 🧠 Részletes Magyarázat

| Lépés | Leírás |
|-------|--------|
| **`git add .`** | Az összes módosított fájlt hozzáadja a staging area-hoz |
| **`git commit -m "vizsga megoldás"`** | Véglegesíti a változtatásokat helyi üzenettel |
| **`git push`** | Feltölti a GitHub Classroom repóba – a push után automatikusan futnak a tesztek |
| **Actions fül** | A GitHub repó „Actions" fülén zöld pipa = minden teszt átment, piros X = hiba van |

A **fájlstruktúra** fontos: a tesztek a `tests/` mappába kerüljenek (`test_` előtaggal), az alkalmazás kód az `app/` mappába. A `Dockerfile` és `requirements.txt` a projekt gyökerében legyen. Ha az automatikus tesztek nem futnak le, ellenőrizd, hogy a fájlok a megfelelő helyen vannak-e.

---

## Felkészülési tippek

- Ismételd át a leckéket, különösen a kód példákat
- Gyakorold a teljes projekt felépítést a nulláról (ez a legfontosabb)
- Próbáld megoldani a próbavizsga feladatot (12. lecke) időre
- Készíts saját "sablon projektet" amit gyorsan tudsz módosítani
- Ellenőrizd, hogy a Docker és pytest beállítások működnek

### 🧠 Részletes Magyarázat

| Tipp | Részletek |
|------|-----------|
| **Leckék átismétlése** | Különösen a 8. (SQLAlchemy), 10. (JWT), 13–15. (tesztelés), 19. (Docker) leckék kód példái |
| **Nulláról építés** | Gyakorold: üres mappa → `venv` → `pip install` → `database.py` → modell → séma → CRUD → router → `main.py` – minél gyorsabban |
| **Próbavizsga (12. lecke)** | A félév összefoglalás ugyanezt a folyamatot gyakoroltatja – ha azt 240 perc alatt megoldod, a vizsgán is boldogulsz |
| **Sablon projekt** | Készíts egy működő mini projektet (1 modell + auth + teszt + Docker), amit gyorsan át tudsz alakítani bármilyen témára |
| **Docker + pytest** | A leggyakoribb buktató: a `Dockerfile` nem jó, vagy a `conftest.py` hiányzik – ezeket **előre** teszteld le |
