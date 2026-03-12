# GitHub Classroom – Mentori útmutató a házi feladatokhoz

Ez a dokumentum lépésről lépésre elmagyarázza, hogyan kell a GitHub Classroom rendszert használni a heti házi feladatok kiosztásához és értékeléséhez. A Backend FastAPI kurzusban az autograding **pytest** alapú.

---

## 1. Előkészületek (egyszer kell megcsinálni)

### 1.1 GitHub Organization létrehozása

1. Lépj be a [github.com](https://github.com) oldalra a saját GitHub fiókoddal
2. Kattints a jobb felső sarokban a **+** gombra → **New organization**
3. Válaszd a **Free** tervet
4. Adj nevet (pl. `openschool-backend-2026`)
5. Add meg az email címedet, majd kattints a **Create** gombra

### 1.2 GitHub Classroom létrehozása

1. Nyisd meg: [classroom.github.com](https://classroom.github.com)
2. Kattints: **New Classroom**
3. Válaszd ki az imént létrehozott Organization-t
4. Adj nevet a Classroom-nak (pl. „Backend FastAPI – 2026”)
5. Készen is van!

### 1.3 Tanulók meghívása

1. A Classroom oldalán kattints a **Students** fülre
2. Itt két lehetőséged van:
   - **Meghívó link** küldése (a tanulók magukat adják hozzá)
   - **Névsor feltöltése** (CSV fájl, hogy a tanulók nevüket kiválaszthassák)
3. **Ajánlás:** Töltsd fel a névjegyzéket, hogy a résztvevők a saját azonosítójukat válasszák ki az első assignment elfogadásakor — így a GitHub felhasználónevük össze lesz rendelve a névjegyzékbeli nevükkel

---

## 2. Template repok feltöltése GitHubra

A `github-classroom/` mappában 25+ kész template repo van, hetente egy (+ vizsga variánsok). Mindegyiket külön GitHub repóként kell feltölteni az Organization-be.

### Lépések (minden hétre ismételd):

```bash
# Példa a 0. hétre:
cd github-classroom/het00-git-github-linux

git init
git add .
git commit -m "template"
git branch -M main
git remote add origin https://github.com/ORGANIZATION_NEVE/het00-git-github-linux.git
git push -u origin main
```

> **FONTOS:** A repot a GitHub weboldalon is létre kell hozni az Organization alatt, mielőtt pusholsz!

### Gyors módszer (mind a 25 repo):

1. A GitHub weboldalon, az Organization alatt hozd létre a repokat:
   - `het00-git-github-linux`
   - `het01-python-venv`
   - `het02-fastapi-bevezetes`
   - `het03-uvonalak-parameterek`
   - `het04-request-body-pydantic`
   - `het05-response-hibak`
   - `het06-dependency-injection`
   - `het07-docker-postgresql`
   - `het08-sqlalchemy-orm`
   - `het09-crud-muveletek`
   - `het10-auth-jwt`
   - `het11-middleware-cors`
   - `het12-felev-osszefoglalas`
   - `het13-pytest-alapok`
   - `het14-fastapi-teszteles`
   - `het15-db-mock-teszteles`
   - `het16-halado-teszteles`
   - `het17-fajlkezeles-kepfeltoltes`
   - `het18-background-websocket`
   - `het19-docker-compose-eles`
   - `het20-cicd-github-actions`
   - `het21-projekt-tervezes`
   - `het22-projekt-fejlesztes-1`
   - `het23-projekt-fejlesztes-2`
   - `het24-vizsga`

2. Mindegyik repot **Template repository**-nak kell jelölni:
   - Repo → **Settings** → **General** → ✅ **Template repository** jelölőnégyzet

3. Pushold fel a tartalmat a `github-classroom/` mappából

---

## 3. Heti házi feladat kiosztása

Minden héten egy új **Assignment**-et kell létrehozni. Ezt kell tenned:

### 3.1 Assignment létrehozása

1. Nyisd meg a Classroom-ot: [classroom.github.com](https://classroom.github.com)
2. Kattints: **New Assignment**
3. Töltsd ki:

| Mező | Érték | Példa |
|------|-------|-------|
| **Title** | A hét neve | `Het 04 - Request body es Pydantic` |
| **Deadline** | A következő óra dátuma + időpont | `2026-03-16 08:00` |
| **Individual or Group** | **Individual** | - |
| **Repository visibility** | **Private** | (ne másolhassák egymástól) |
| **Template repository** | Az adott heti template | `het04-request-body-pydantic` |

4. Kattints: **Create Assignment**
5. Megkapod a **meghívó linket** (pl. `https://classroom.github.com/a/AbCdEf`)

### 3.2 Link kiosztása

- Küldd el a meghívó linket a tanulóknak (Teams, email, Kréta üzenet, stb.)
- A tanuló rákattint → elfogadja → automatikusan létrejön a saját privát repoja
  (pl. `het04-request-body-pydantic-kissanna`)

---

## 4. Automatikus tesztelés (Autograding – pytest)

### 4.1 Hogyan működik?

A Backend FastAPI kurzusban az autograding **pytest** alapú (nem shell teszt):

1. A tanuló pushol → a GitHub Actions automatikusan lefuttatja a `pytest` teszteket
2. A Classroom felületén megjelenik az eredmény
3. A tanuló is látja a saját eredményét a repojában (Actions fül → zöld ✅ vagy piros ❌)

### 4.2 A tesztek felépítése

A pytest tesztek a `tests/` mappában vannak:

```
het13-pytest-alapok/
├── README.md
├── requirements.txt
├── tests/
│   └── test_utils.py        ← pytest tesztek
└── .github/
    └── workflows/
        └── classroom.yml    ← GitHub Actions workflow
```

### 4.3 GitHub Actions workflow (classroom.yml)

Minden template repo tartalmaz egy `.github/workflows/classroom.yml` fájlt:

```yaml
name: Autograding
on: [push]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
      - name: Run tests
        run: pytest tests/ -v
```

### 4.4 A requirements.txt tartalma

A tesztekhez szükséges minimális `requirements.txt`:

```
fastapi
uvicorn
httpx
pytest
sqlalchemy
pydantic
```

> **Megjegyzés:** A GitHub Actions-ben nincs PostgreSQL — ezért a tesztek **SQLite in-memory** adatbázist használnak (`dependency_overrides` mechanizmussal).

### 4.5 Mock adatbázis a GitHub Classroom tesztekhez

A kulcselem a `conftest.py`, amely az SQLite in-memory DB-t állítja be:

```python
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.main import app
from app.database import Base, get_db

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(autouse=True)
def setup_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

@pytest.fixture
def db():
    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()

@pytest.fixture
def client(db):
    def override_get_db():
        try:
            yield db
        finally:
            pass
    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as c:
        yield c
    app.dependency_overrides.clear()
```

> A mentornak érdemes ezt a mintát a **15. héten** részletesen elmagyarázni a tanulóknak.

---

## 5. Házi feladatok ellenőrzése

### 5.1 Áttekintés a Classroom-ban

1. Nyisd meg az Assignment-et a Classroom-ban
2. Látod az összes tanuló státuszát:
   - ✅ Elfogadta a feladatot
   - 🔄 Commitolt (utolsó commit időpontja)
   - 📊 Teszt eredmény (zöld/piros)
   - A repojára kattintva megnézheted a kódot

### 5.2 Kód megtekintése

- Kattints egy tanuló repojára → a GitHub oldalon megnyílik
- A **Commits** fülön látod, mikor és mit commitolt
- Az **Actions** fülön látod a pytest eredményeit
- A fájlokra kattintva megnézheted a kódot

### 5.3 Gyors ellenőrzés – klónozás

Ha a gépen is le akarod tölteni az összes megoldást:

```bash
# GitHub Classroom Assistant alkalmazás használata (ajánlott):
# https://classroom.github.com/assistant

# VAGY manuálisan, egyenként:
git clone https://github.com/ORGANIZATION/het09-crud-muveletek-kissanna.git
```

---

## 6. Heti teendők összefoglalása

Minden héten ezeket kell megtenned:

| # | Teendő | Mikor |
|---|--------|-------|
| 1 | Hozd létre az Assignment-et a Classroom-ban | Az óra előtt |
| 2 | Oszd ki a meghívó linket a tanulóknak | Az órán |
| 3 | A deadline után nézd meg a beadásokat | A következő óra előtt |
| 4 | Adj visszajelzést (GitHub komment vagy szóban) | A következő órán |

---

## 7. Template repok tartalma

| Mappa | Tartalom | pytest tesztek |
|-------|----------|---------------|
| `het00-git-github-linux/` | README.md | – |
| `het01-python-venv/` | README.md | – |
| `het02-fastapi-bevezetes/` | README.md | – |
| `het03-uvonalak-parameterek/` | README.md | – |
| `het04-request-body-pydantic/` | README.md | – |
| `het05-response-hibak/` | README.md | – |
| `het06-dependency-injection/` | README.md | – |
| `het07-docker-postgresql/` | README.md | – |
| `het08-sqlalchemy-orm/` | README.md | – |
| `het09-crud-muveletek/` | README.md | – |
| `het10-auth-jwt/` | README.md | – |
| `het11-middleware-cors/` | README.md | – |
| `het12-felev-osszefoglalas/` | README.md | – |
| `het13-pytest-alapok/` | README.md, requirements.txt | `tests/test_utils.py` (18 teszt) |
| `het14-fastapi-teszteles/` | README.md, requirements.txt | `tests/test_api.py` (8 teszt) |
| `het15-db-mock-teszteles/` | README.md, requirements.txt, `tests/conftest_minta.py` | `tests/test_termekek.py` (10 teszt) |
| `het16-halado-teszteles/` | README.md | – |
| `het17-fajlkezeles-kepfeltoltes/` | README.md | – |
| `het18-background-websocket/` | README.md | – |
| `het19-docker-compose-eles/` | README.md | – |
| `het20-cicd-github-actions/` | README.md | – |
| `het21-projekt-tervezes/` | README.md | – |
| `het22-projekt-fejlesztes-1/` | README.md | – |
| `het23-projekt-fejlesztes-2/` | README.md | – |
| `het24-vizsga/` | README.md | – |

> A 13–15. heti template repók tartalmaznak pytest tesztfájlokat. A korábbi hetek (0–12) nem tartalmaznak automatikus teszteket, mert a tanulók ekkor még nem ismerik a pytest-et. A 16. héttől a tanulók maguk írják a teszteket.

---

## 8. Értékelési javaslat a házi feladatokhoz

| Szempont | Leírás |
|----------|--------|
| **Beadta-e?** | Van-e commit a deadline előtt? |
| **Működik-e?** | A kód lefut hiba nélkül? Pytest tesztek PASS? |
| **Helyes-e?** | A végpontok megfelelnek a feladat leírásnak? |
| **Git használat** | Értelmes commit üzenetek, rendszeres commitolás? |
| **Kódminőség** | Strukturált, olvasható kód? Pydantic sémák helyesek? |

### Egyszerű értékelési skála:

| Szint | Feltétel |
|-------|----------|
| Kiváló | Minden feladat kész, helyes, szép kód, tesztek zöldek |
| Haladó | A ⭐ és ⭐⭐ feladatok készen vannak és helyesek |
| Megfelelő | A ⭐ feladatok készen vannak és helyesek |
| Kezdő | Legalább 2 feladat beadva, de hibás |
| Nem teljesített | Nem adott be semmit, vagy nem commitolt |

---

## 9. Gyakori problémák és megoldásaik

Részletes hibaelhárítási táblázat és megoldások:

- [Hibaelhárítás és GYIK — GitHub Classroom](../../../../guides/hibaelharitas.md#github-classroom)
- [Hibaelhárítás és GYIK — Git és GitHub](../../../../guides/hibaelharitas.md#git-és-github)
- [GitHub Classroom — Tanuló útmutató](../../../../guides/github-classroom-tanulo-utmutato.md) (tanulóknak továbbítható)

---

## 10. Tippek

- **Első alkalommal** (0. hét): szánj rá időt, hogy mindenki beállítsa a Git-et és a GitHub fiókot. Ezt akár előzetesen kiadhatod önálló feladatnak.
- **Névsor feltöltése** a Classroom-ba: így a tanulók nevéhez rendelheted a GitHub felhasználónevüket
- **Docker telepítés** (7. hét): készíts lépésről lépésre útmutatót, mert ez a leggyakoribb technikai akadály
- **pytest bevezetése** (13. hét): innentől az autograding pytest-tel történik — készítsd fel a tanulókat, hogy a tesztfájlokat NE módosítsák
- **Vizsga előtt** (23. hét): tartass próbavizsgát GitHub Classroom-ban a `het12-felev-osszefoglalas` template-tel
