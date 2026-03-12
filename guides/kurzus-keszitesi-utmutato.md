# Kurzus készítési útmutató

Ez az útmutató azoknak szól, akik új kurzust, heti feladatot vagy vizsga variánst szeretnének készíteni az OpenSchool rendszerbe.

---

## Mappastruktúra

Minden kurzus a `kurzusok/python/` mappán belül él, és ezt a struktúrát követi:

```
kurzusok/python/<kurzus-neve>/
├── README.md                      # Kurzus áttekintés
├── doksik/
│   ├── README.md
│   ├── tanulok/                    # Tanulók számára elérhető anyagok
│   ├── mentor/                     # Mentor/mentori dokumentáció
│   │   ├── mentori-utmutato.md     # Heti bontású útmutató
│   │   └── ertekeles-modszertan.md # Értékelési módszertan
│   └── tanterv/                   # Tanterv és tematika
├── github-classroom/
│   ├── README.md
│   ├── het00-<tema>/              # Előkészítő hét
│   ├── het01-<tema>/              # 1. hét
│   ├── ...
│   └── vizsga-<tema>/             # Vizsga variánsok
└── vizsgak/
    ├── README.md
    └── <vizsga-nev>/              # Vizsga anyagok
```

---

## Elnevezési konvenciók

| Elem | Formátum | Példa |
|------|----------|-------|
| Kurzus mappa | `kisbetus-kotojeles` | `python-alapok`, `python-backend` |
| Heti feladat | `het{szám:02d}-{téma}` | `het01-alapok`, `het13-pytest-alapok` |
| Feladat fájlok | `feladat{szám}.py` | `feladat1.py`, `feladat5.py` |
| Tesztfájlok | `test_{téma}.py` | `test_health.py`, `test_docker.py` |
| Vizsga variánsok | `vizsga-{téma}` | `vizsga-filmek`, `vizsga-blog-api` |
| Modulok | `modul-{szám:02d}` | `modul-01`, `modul-07` |

> **Fontos:** Mindig kötőjellel válaszd el a szavakat, ne aláhúzással. A számok mindig kétjegyűek (01, 02, ..., 12).

---

## Heti feladat létrehozása

Minden heti feladat egy önálló mappa a `github-classroom/` alatt. A minimális struktúra:

```
het01-alapok/
├── .github/
│   ├── classroom/
│   │   └── autograding.json       # Automatikus tesztek
│   └── workflows/
│       └── classroom.yml          # GitHub Actions konfiguráció
└── README.md                      # Feladat leírás
```

### 1. README.md sablon

```markdown
# X. hét – Téma neve

> **Határidő:** a következő foglalkozás előtt

## Feladatok

### X.1 – Feladat címe ⭐

Leírás, mit kell csinálni.

**Fájlnév:** `feladat1.py`

**Elvárt kimenet:**
```
Helló, Világ!
```

### X.2 – Feladat címe ⭐⭐

Nehezebb feladat leírása.

**Fájlnév:** `feladat2.py`

---

## Beadás

1. `git add .`
2. `git commit -m "X. hét kész"`
3. `git push`

A tesztek automatikusan lefutnak push után. Az eredményt a GitHub repód Actions fülén ellenőrizheted.
```

**Nehézségi jelölések:**
- ⭐ könnyű
- ⭐⭐ közepes
- ⭐⭐⭐ nehéz

### 2. autograding.json sablon

Az automatikus tesztek a `.github/classroom/autograding.json` fájlban vannak definiálva:

```json
{
  "tests": [
    {
      "name": "1.1 – feladat1.py létezik",
      "setup": "",
      "run": "test -f feladat1.py",
      "input": "",
      "output": "",
      "comparison": "included",
      "timeout": 10,
      "points": 1
    },
    {
      "name": "1.1 – feladat1.py kimenet",
      "setup": "",
      "run": "python3 feladat1.py",
      "input": "",
      "output": "Helló, Világ!",
      "comparison": "included",
      "timeout": 10,
      "points": 2
    },
    {
      "name": "1.2 – feladat2.py tartalmaz for ciklust",
      "setup": "",
      "run": "grep -q 'for' feladat2.py",
      "input": "",
      "output": "",
      "comparison": "included",
      "timeout": 10,
      "points": 1
    }
  ]
}
```

**Teszt típusok:**

| Típus | `run` parancs | Mikor használd |
|-------|---------------|----------------|
| Fájl létezik | `test -f feladat1.py` | Ellenőrzés, hogy a fájl be van-e adva |
| Futtatás | `python3 feladat1.py` | A program hiba nélkül lefut |
| Kimenet | `python3 feladat1.py` + `output` mező | A kimenet tartalmazza az elvárt szöveget |
| Kód minta | `grep -q 'for' feladat2.py` | A kódban van-e adott elem (ciklus, import, stb.) |
| Összetett | `test -f f.py && python3 f.py` | Fájl létezik ÉS lefut |

**Pontszámok iránymutatása:**
- Fájl létezik: 1 pont
- Program lefut: 1-2 pont
- Helyes kimenet: 2-4 pont
- Kód minta: 1 pont

### 3. classroom.yml

A GitHub Actions munkafolyamat fájl minden feladatnál ugyanaz:

```yaml
name: GitHub Classroom Workflow

on:
  push:
    branches:
      - main
      - master

jobs:
  build:
    name: Autograding
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: education/autograding@v1
```

> **Figyelem:** Ezt a fájlt nem kell feladatonként módosítani. Ugyanaz a sablon mindenhol.

---

## Vizsga variáns létrehozása

A vizsgák a heti feladatokhoz hasonló struktúrát követnek, de nagyobb terjedelműek:

```
vizsga-filmek/
├── .github/
│   ├── classroom/
│   │   └── autograding.json
│   └── workflows/
│       └── classroom.yml
├── README.md                  # Vizsga feladatsor
└── filmek.csv                 # Adatfájl (ha szükséges)
```

### Vizsga tervezési elvek

1. **4+ variáns** — különböző adathalmazokkal (pl. filmek, könyvek, zenék, sportolók)
2. **Azonos szerkezet** — minden variáns ugyanazt a feladattípust kéri, más adattal
3. **Fokozatos nehézség** — az egyszerűbb feladatok előbb, a nehezebbek hátul
4. **Autograding + kód-átnézés** — az automatikus tesztek ellenőrzik a működést, a mentor a kód minőségét nézi

### Python Alapok vizsga struktúra

| Feladat | Leírás | Pont |
|---------|--------|------|
| 1. Fájl beolvasás | CSV/szöveges fájl feldolgozása | 15 |
| 2. Szűrés | Adatok szűrése feltétel alapján | 20 |
| 3. Statisztika | Összesítés, átlag, maximum, minimum | 20 |
| 4. Függvényekre bontás | Minden logika `fgv.py`-ban, hívás `feladat3.py`-ból | 15 |
| 5. Extra feladat | Bonyolultabb logika (rendezés, top N, stb.) | 10 |

### Backend FastAPI vizsga struktúra

| Feladat | Leírás | Pont |
|---------|--------|------|
| 1. Pydantic sémák | Create/Read modell elkülönítés | 10 |
| 2. SQLAlchemy modellek | Adatbázis definíció | 10 |
| 3. CRUD műveletek | Létrehozás, olvasás, frissítés, törlés | 15 |
| 4. API endpointok | Router implementáció, helyes státuszkódok | 15 |
| 5. Tesztek | Pozitív és negatív esetek, mock adatbázis | 10 |

---

## Mentori dokumentáció

Minden kurzushoz készíts mentori útmutatót a `doksik/mentor/` mappába:

### mentori-utmutato.md tartalma

- **Heti bontás** — mit tanítunk, milyen sorrendben
- **Nehezebb hetek jelölése** — hol kell több idő / több gyakorlat
- **Tipikus hibák** — amiket a tanulók el fognak követni
- **Élő kódolási javaslatok** — mit mutass be a foglalkozáson
- **Vizsga variánsok leírása** — melyik variáns mit tartalmaz

### ertekeles-modszertan.md tartalma

- **Értékelési elvek** — formatív (támogató), nem szűrő jellegű
- **Autograding + kód-átnézés** kombinálása
- **Kód-átnézés ellenőrzőlista** — mit nézzen a mentor
- **Pontmódosítási szabályok** — jó kód + teszt fail / rossz kód + teszt pass
- **Git történet elemzés** — mire figyelj a commitoknál
- **Szóbeli visszakérdezés** — szintenként milyen kérdéseket tegyél fel

---

## Ellenőrzőlista új kurzus/feladat készítésekor

```
□ Mappastruktúra a konvenció szerint?
□ README.md tartalmazza a feladat leírást, nehézséget, fájlneveket?
□ autograding.json tartalmazza az összes tesztet?
□ classroom.yml megvan a .github/workflows/ alatt?
□ A tesztek lokálisan lefutnak? (próbáld ki egy minta megoldással)
□ A pontszámok arányosak a nehézséggel?
□ A vizsga variánsok azonos szerkezetűek?
□ A mentori útmutató frissítve van?
□ A kurzus README.md hivatkozik az új heti feladatra?
```

---

**Kapcsolódó útmutatók:**
- [Mentor útmutató](mentor-utmutato.md)
- [GitHub Classroom — Tanuló útmutató](github-classroom-tanulo-utmutato.md)
- [Git puskalap](git-puskalap.md)
