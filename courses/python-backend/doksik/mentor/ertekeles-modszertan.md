# Értékelési módszertan – Backend FastAPI

## 1. Értékelési filozófia

### Alapelvek

- **Formatív értékelés elsőbbsége:** A félév során a cél a tanulás támogatása, nem a szűrés. A heti házi feladatok visszajelzésként szolgálnak, nem büntetésként.
- **Fokozatos nehezítés:** A heti feladatok komplexitása nő (egyszerű API → CRUD + DB → auth + teszt), a vizsga az összesített tudást méri (60 pont).
- **Automatizált + emberi értékelés:** A GitHub Classroom pytest-tel ad objektív alappontszámot, de a mentori kód-átnézés (code review) is része az értékelésnek.
- **Növekedési szemlélet (growth mindset):** A résztvevők eltérő háttérrel érkeznek — az előrehaladás fontosabb, mint az abszolút szint.
- **Gyakorlatorientáltság:** A backend fejlesztés kézműves szakma — a vizsga is gyakorlati (kódot kell írni, nem elméleti kérdésekre válaszolni).

### Mit mérünk?

| Szint | Leírás | Példa |
|-------|--------|-------|
| **Működik** | Az API indítható, a végpontok reagálnak | pytest: PASS |
| **Helyes** | A kód a specifikáció szerint működik | Státuszkódok, válaszformátum egyezik |
| **Strukturált** | Pydantic sémák, CRUD réteg, routerek szétválasztva | Code review: van-e rétegezés |
| **Tesztelt** | Automatizált pytest tesztek megvannak és zöldek | pytest + coverage |
| **Önálló** | Nem másolt, a tanuló el tudja magyarázni | Szóbeli kérdés vagy Git history |

---

## 2. Értékelési összetevők

### Összesített értékelés

| Összetevő | Súly | Mérés módja |
|-----------|------|-------------|
| Heti házi feladatok (het00–het23) | 20% | GitHub Classroom pytest + mentori átnézés |
| Órai munka és aktivitás | 15% | Mentori megfigyelés |
| Próbavizsga (het12) | 15% | GitHub Classroom pytest + code review |
| Szintfelmérő vizsga (het24) | 50% | GitHub Classroom pytest + code review |

### Szinthatárok (szintfelmérő vizsga: 60 pont)

| Pontszám | Százalék | Szint |
|----------|----------|-------|
| 54–60 | 90–100% | Kiváló |
| 43–53 | 72–89% | Haladó |
| 31–42 | 52–71% | Megfelelő |
| 19–30 | 32–51% | Kezdő |
| 0–18 | 0–31% | Nem teljesített |

---

## 3. Automatizált értékelés (pytest + GitHub Classroom)

### Hogyan működik?

1. A tanuló pushol a GitHub repójába
2. A GitHub Actions workflow automatikusan lefut
3. A `pytest` tesztek ellenőrzik a kódot
4. Az eredmény megjelenik a GitHub Actions-ben (és a Classroom felületen)

### A tesztek jellemzői

**A Backend FastAPI kurzusban a tesztek pytest-tel futnak:**

```python
# Példa: test_api.py
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200

def test_create_item():
    response = client.post("/items/", json={"nev": "Teszt", "ar": 100})
    assert response.status_code == 201
    assert response.json()["nev"] == "Teszt"

def test_create_item_invalid():
    response = client.post("/items/", json={"nev": ""})
    assert response.status_code == 422
```

### Mock adatbázis a tesztekben

A GitHub Classroom-ban **nincs PostgreSQL** — ezért a tesztek SQLite in-memory adatbázist használnak:

```python
# conftest.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base, get_db
from app.main import app

engine = create_engine("sqlite:///./test.db", connect_args={"check_same_thread": False})
TestSession = sessionmaker(bind=engine)

@pytest.fixture(autouse=True)
def setup_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

@pytest.fixture
def client():
    def override():
        db = TestSession()
        try:
            yield db
        finally:
            db.close()
    app.dependency_overrides[get_db] = override
    with TestClient(app) as c:
        yield c
    app.dependency_overrides.clear()
```

### Automatizált pontszámok értelmezése

| pytest eredmény | Értelmezés |
|----------------|------------|
| Minden teszt PASS | A kód megfelel a specifikációnak |
| 70%+ PASS | Az alap funkcionalitás megvan, néhány részlet hiányzik |
| 30–69% PASS | Próbálkozott, de a megvalósítás hiányos |
| 0–29% PASS | Nem készült el, vagy alapvető hibák vannak |

### Fontos: a pytest nem elég

A pytest **szükséges, de nem elégséges** feltétele a jó eredménynek:
- Egy tanuló másolhatott (→ Git history ellenőrzés)
- A kód működik, de olvashatatlan (→ code review)
- A kód túl egyszerű megoldást használ (→ struktúra ellenőrzés)
- A tanuló nem érti a saját kódját (→ szóbeli kérdés)

---

## 4. Mentori kód-átnézés (Code Review)

### Mikor szükséges?

- **Heti házi feladatok:** Szúrópróbaszerűen (heti 3-5 tanuló repóját)
- **Próbavizsga:** Minden tanuló kódját
- **Szintfelmérő vizsga:** Minden tanuló kódját részletesen

### Code review szempontok

**Ellenőrzőlista (vizsga):**

```
□ schemas.py – Pydantic sémák helyesek? Van Create/Read szétválasztás?
□ models.py  – SQLAlchemy modellek megfelelőek? Oszloptípusok jók?
□ crud.py    – CRUD függvények paraméteressel dolgoznak?
                Nem használ globális változókat?
                Session-t kap paraméterként?
□ routers/   – Végpontok helyesen implementálva?
                Megfelelő státuszkódok? HTTPException használata?
□ tests/     – Van-e teszt? A mock DB jól van beállítva?
                Pozitív és negatív tesztek is vannak?
□ Kódminőség – Értelmes változónevek? (nem a, b, x, y)
                Nincs felesleges kód? Nincs kikommentált szemét?
□ Git history – Legalább 5 commit? Értelmes commit üzenetek?
                Az időbélyegek a vizsga idejére esnek?
□ Biztonság  – Nincs plain text jelszó? .env nincs commitolva?
                Jelszó hash-elés bcrypt-tel?
```

### Pontmódosítás code review alapján

| Eset | Módosítás |
|------|----------|
| pytest PASS + jó kódminőség | Teljes pontszám |
| pytest PASS + gyenge kódminőség | –10% a részfeladaton |
| pytest FAIL + jó megközelítés, apró hiba | +1–2 pont részpontként |
| pytest PASS + gyanús Git history (1 commit, copy-paste) | Szóbeli ellenőrzés szükséges |

---

## 5. Git history elemzés

A Git history a leghatékonyabb eszköz a másolás kiszűrésére és a munkafolyamat megértésére.

### Ellenőrizendő

```bash
# Commitok száma és időzítése
git log --oneline --format="%h %ai %s"

# Ki írta a kódot?
git log --format="%an <%ae>" | sort -u

# Mikor történtek a commitok?
git log --format="%ai" | head -20

# Soronkénti szerzőség
git blame app/routers/items.py
```

### Piros zászlók

- **1 commit az egész vizsgára** → valószínű másolás
- **Commitok a vizsga időablakán kívül** → otthoni előkészítés (megengedett-e?)
- **Más felhasználónév a commitban** → másolás másik tanulótól
- **Hatalmas commit diff** → nem fokozatosan dolgozott
- **Tökéletesen egyforma kód két tanulónál** → összehasonlítás szükséges

---

## 6. Szóbeli ellenőrzés

### Mikor alkalmazzuk?

- Gyanús Git history esetén
- Kiemelkedően jó vagy gyenge pytest eredménynél az elvárthoz képest
- A tanuló kérésére (javítási lehetőség)

### Kérdések szintenként

**Alapszint:**
- Mi a különbség a GET és POST kérés között?
- Mi az a Pydantic modell, és mire jó?
- Hogyan indítod el a FastAPI szervert?
- Mi az a `venv` és miért használjuk?

**Középszint:**
- Magyarázd el, mit csinál a `get_db()` dependency!
- Miért használunk `dependency_overrides`-t a tesztekben?
- Mi történik, ha egy Pydantic modell validációja sikertelen?
- Hogyan működik a JWT authentikáció?

**Haladó szint:**
- Mi a különbség a Pydantic schema és az SQLAlchemy model között?
- Hogyan oldottad meg a teszt izolációt (hogy a tesztek ne befolyásolják egymást)?
- Miért SQLite-ot használunk a tesztekben PostgreSQL helyett?
- Hogyan lenne érdemes a kódot refaktorálni, ha egy új entitást kellene hozzáadni?

### Szóbeli értékelés hatása

| Eredmény | Hatás az értékelésre |
|----------|----------------------|
| A tanuló magabiztosan elmagyarázza a kódját | Megerősíti a pytest eredményt |
| A tanuló részben érti, de vannak hiányosságok | A pytest eredményt max 1 szinttel csökkenti |
| A tanuló nem tudja elmagyarázni a saját kódját | A feladatra 0 pont (másolásgyanú) |

---

## 7. Házi feladatok értékelése

### Heti házi feladatok (het00–het23)

- **Automatikus (13. héttől):** pytest eredmény (azonnal látható a tanulónak)
- **Manuális (0–12. hét):** Mentori kód-átnézés (nincs autograding ezeken a heteken)
- **Határidő:** A következő óra előtt 1 nappal
- **Késés:** Heti 1 nap késés megengedett, utána 50% levonás
- **Minimumkövetelmény:** A félév végéig legalább 16 házi feladat beadva (a 24-ből)

### Összesítés

A 24 heti házi feladat összesített értékelése:

| Teljesítmény | Házi feladat szint |
|-------------|--------------------|
| 80–100% beadva és helyes | Kiváló |
| 60–79% beadva és helyes | Haladó |
| 40–59% beadva és helyes | Megfelelő |
| 20–39% beadva és helyes | Kezdő |
| 0–19% beadva | Nem teljesített |

---

## 8. Vizsgavariánsok kezelése

### 4 variáns rendszer

| Variáns | Téma | Fő entitások | Fő különbség |
|---------|------|--------------|-------------|
| A (todo-api) | Teendők kezelése | Todo, Kategória | Prioritás, határidő, státusz szűrés |
| B (blog-api) | Blog platform | Blogpost, Szerző | Címke szűrés, publikálás dátum |
| C (webshop-api) | Webáruház | Termék, Kategória | Ár szűrés, készlet kezelés |
| D (recept-api) | Recept kezelő | Recept, Hozzávaló | Kalória, elkészítési idő szűrés |

### Kiosztási javaslat

- **2 csoport:** A+B vagy C+D variáns
- **4 csoport:** Minden variáns más sorrendben (A, B, C, D)
- **Véletlenszerű:** GitHub Classroom-ban 4 assignment, a tanulók random kapják

A variánsok **azonos nehézségűek** — mindegyik azonos struktúrájú (5 feladat: 10+20+10+10+10 pont), és a pytest tesztek pontról pontra megfelelnek egymásnak.

### Vizsga felépítése (minden variáns)

| Feladat | Pont | Tartalom |
|---------|------|----------|
| 1. feladat | 10 pont | Pydantic sémák + utility/validációs függvények |
| 2. feladat | 20 pont | SQLAlchemy DB + CRUD API végpontok (SQLite, query paraméterek, adatfájl) |
| 3. feladat | 10 pont | JWT autentikáció (regisztráció, login, védett végpontok) |
| 4. feladat | 10 pont | Adatfeldolgozás fájlból (feldolgozas.py, 5 függvény) |
| 5. feladat | 10 pont | Docker (Dockerfile, requirements.txt) + pytest tesztek (8 teszt) |
| **Összesen** | **60 pont** | |

---

## 9. Különleges esetek

### Hiányzó tanuló a vizsgán
- Pótvizsga: másik variánssal (C vagy D, ha az órákon A és B volt)
- Határidő: 1 héten belül

### Technikai probléma a vizsgán
- A tanuló jelezze azonnal
- A mentor ellenőrizze a Git history-t (volt-e push?)
- Szükség esetén a helyi fájlok manuális begyűjtése (USB)
- Ha Docker/PostgreSQL nem elérhető: a vizsga memóriában (listával/szótárral) is megoldható — ne büntessük ezért

### Plágiumgyanú
1. Git history összehasonlítás két tanulónál (`git log`, `git blame`)
2. Kód hasonlóság vizsgálat (változónevek, struktúra, kommentek, import sorrend)
3. Szóbeli ellenőrzés mindkét tanulóval
4. Ha bizonyított: mindkét tanuló 0 pontot kap a feladatra

### Kimagasló teljesítmény
- 54+/60 pont + kiváló kódminőség + minden teszt zöld: dicséret, mentor szerep lehetőség
- A tanuló segíthet a gyengébb társainak (pair programming)

---

## 10. Összefoglalás

```
Értékelési piramis:

    ┌──────────────┐
    │  SZÓBELI (?)  │  ← csak gyanú esetén
    ├──────────────┤
    │  CODE REVIEW  │  ← mentori átnézés
    ├──────────────┤
    │  GIT HISTORY  │  ← munkafolyamat ellenőrzés
    ├──────────────┤
    │   PYTEST      │  ← objektív alappontszám
    └──────────────┘
```

**A pytest az alap, nem a plafon.** A számítógép megmondja, hogy működik-e a kód — a mentor dönti el, hogy a tanuló érti-e és önállóan készítette-e.
