# 📘 Lecke 20 – CI/CD és GitHub Actions

> 📚 Dokumentáció:
> https://docs.github.com/en/actions
> https://github.com/actions/checkout
> https://github.com/actions/setup-python

---

## 121–122. óra: CI/CD fogalma

### Mi a CI/CD?

| Rövidítés | Jelentés | Mit csinál? |
|-----------|----------|-------------|
| **CI** | Continuous Integration | Automatikus tesztelés minden push-nál |
| **CD** | Continuous Deployment | Automatikus telepítés sikeres tesztek után |

### 🧠 Részletes Magyarázat

- **CI (Continuous Integration)** – Minden `git push` után automatikusan lefutnak a tesztek. Ha egy fejlesztő hibás kódot push-ol, a CI azonnal jelzi (piros X a commiton). Így a hiba nem jut tovább.
- **CD (Continuous Deployment/Delivery)** – A sikeres teszteket követően az alkalmazás automatikusan települ az éles szerverre. Delivery = kézzel kell jóváhagyni, Deployment = teljesen automatikus.
- **Miért fontos?** – Emberi ellenőrzés helyett automatizálás. Nincs „elfelejtett teszt futtatás", nincs „működik a gépemen" probléma.

### GitHub Actions alapok

A GitHub Actions a `.github/workflows/` mappában lévő YAML fájlokkal konfigurálható:

```
.github/
└── workflows/
    └── ci.yml
```

### Alap CI workflow

```yaml
# .github/workflows/ci.yml
name: CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Kód letöltése
        uses: actions/checkout@v4

      - name: Python beállítása
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Függőségek telepítése
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Tesztek futtatása
        run: pytest tests/ -v
```

### 🧠 Részletes Magyarázat

A YAML fájl felépítése:

| Elem | Jelentés |
|------|----------|
| `name: CI` | A workflow neve (a GitHub UI-ban jelenik meg) |
| `on: push/pull_request` | Mikor fut: push-ra és PR-ra a `main` ágon |
| `jobs:` | A futtatandó feladatok |
| `runs-on: ubuntu-latest` | Linux virtuális gép (a GitHub biztosítja ingyen) |
| `steps:` | Lépések sorrendben |
| `uses: actions/checkout@v4` | Beépített action: a repó kódját letölti a runner-re |
| `uses: actions/setup-python@v5` | Beépített action: Python-t telepít |
| `run:` | Shell parancsot futtat |

- **`on: push + pull_request`** – A CI dupla védelmet ad: (1) PR-nál a merge előtt ellenőriz, (2) push-nál a merge után is.
- **`|` a `run:` után** – Többsoros shell parancs. Minden sor egy új parancs.

---

## 123–124. óra: Haladó workflow

### Környezeti változók és secrets

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    env:
      SECRET_KEY: teszt-titkos-kulcs
      DATABASE_URL: sqlite:///./test.db

    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - run: pip install -r requirements.txt
      - run: pytest tests/ -v --tb=short
```

### 🧠 Részletes Magyarázat

- **`env:` a job szintjén** – Környezeti változók, amiket minden step lát. A `SECRET_KEY` és `DATABASE_URL` a CI-ban teszt értékeket kapnak (nem az éles titkokat!).
- **`sqlite:///./test.db`** – A CI-ban SQLite-ot használunk (nincs PostgreSQL szolgáltatás). A mock DB stratégia (15. lecke) ezt teszi lehetővé.
- **GitHub Secrets** – Éles titkok (pl. deploy kulcs) a repository Settings → Secrets alatt tárolhatók. YAML-ben: `${{ secrets.SECRET_NAME }}`. Ezek a logban **soha** nem jelennek meg.

### Lint ellenőrzés hozzáadása

```yaml
      - name: Kód formázás ellenőrzés
        run: |
          pip install flake8
          flake8 app/ --max-line-length=120 --exclude=__pycache__
```

### 🧠 Részletes Magyarázat

- **`flake8`** – Python linter: a kód stílusát és alapvető hibákat ellenőrzi (nem használt importok, túl hosszú sorok, szintaktikai hibák). Nem futtatja a kódot, csak olvassa.
- **`--max-line-length=120`** – A Python alapértelmezett sorhosszkorlátja 79 karakter (PEP 8). A 120 egy gyakori enyhítés modern monitorokra.
- **`--exclude=__pycache__`** – A cache fájlokat kihagyja az ellenőrzésből.

### Coverage riport

```yaml
      - name: Tesztek coverage-dzsel
        run: |
          pip install pytest-cov
          pytest tests/ -v --cov=app --cov-report=term-missing
```

### 🧠 Részletes Magyarázat

- **`--cov-report=term-missing`** – A terminálban mutatja a lefedettséget + a nem érintett sorok számát. Pl.: `app/auth.py  18  2  89%  Missing: 42, 58` → a 42. és 58. sort nem futtatta teszt.
- **CI-ban miért hasznos?** – A PR review-nál a fejlesztő és a reviewer azonnal látja, ha a kód nem tesztelt. Kiegészíthető: `--cov-fail-under=80` → ha a lefedettség 80% alá esik, a CI elbukik.

### Teljes CI workflow

```yaml
name: CI Pipeline

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - run: pip install flake8
      - run: flake8 app/ --max-line-length=120

  test:
    runs-on: ubuntu-latest
    needs: lint
    env:
      SECRET_KEY: ci-teszt-kulcs
      DATABASE_URL: sqlite:///./test.db
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - run: pip install -r requirements.txt
      - run: pytest tests/ -v --cov=app --cov-report=term-missing
```

### 🧠 Részletes Magyarázat

- **Két job: `lint` → `test`** – A `needs: lint` azt jelenti, hogy a `test` job **csak a `lint` sikeres befejezése után** indul. Ha a lint hibát talál, a tesztek meg sem futnak (gyorsabb visszajelzés).
- **Párhuzamosítás** – Ha nincs `needs:`, a jobok **párhuzamosan** futnak. Ez gyorsabb, de a lint + test minta logikusabb: ha a kód formailag rossz, nincs értelme tesztelni.
- **Külön environment** – Minden job saját runner-t (virtuális gépet) kap. A `lint` job-nak nem kell a `requirements.txt`, csak a `flake8`.

---

## 125–126. óra: GitHub Classroom autograding

### Hogyan működik a GitHub Classroom?

1. A mentor létrehozza a feladatot (assignment) és template repót
2. A tanuló elfogadja → saját fork jön létre
3. A tanuló kódol és push-ol
4. A GitHub Actions futtatja a **pytest**-et automatikusan
5. A mentor látja az eredményt

### 🧠 Részletes Magyarázat

- **Template repó** – A mentor előre megírja a teszteket (`tests/` mappa) és a workflow fájlt. A tanuló feladata: megírni az `app/` kódot, ami átmegy a teszteken.
- **Automatikus értékelés** – A GitHub Actions minden push-nál futtatja a teszteket. A mentor nem kell, hogy kézzel futtassa – a zöld/piros pipa mutatja az eredményt.
- **Átláthatóság** – A mentor a GitHub Classroom felületen összesítve látja: ki adta be, kinek mennyi tesztje fut.

### Autograding workflow

```yaml
# .github/workflows/classroom.yml
name: Autograding

on:
  push:
    branches: [main]

jobs:
  grade:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - run: pip install -r requirements.txt
      - name: Tesztek
        run: pytest tests/ -v
        env:
          SECRET_KEY: classroom-teszt-kulcs
```

### 🧠 Részletes Magyarázat

- **`on: push: branches: [main]`** – Csak a `main` ágra push-oláskor fut. A feature branch-ek nem triggerelnek (a tanulónál nem is szokás feature branch).
- **`SECRET_KEY: classroom-teszt-kulcs`** – Teszt érték. Az éles `SECRET_KEY` nincs a CI-ban – a tesztek mock DB-t használnak, ami nem igényel valódi titkot.
- **Munkamenet:** Tanuló kódol → `git push` → GitHub Actions fut → pipa (zöld = sikeres, piros = hibás).

### Badge hozzáadása a README-hez

```markdown
![CI](https://github.com/FELHASZNALO/REPO/actions/workflows/ci.yml/badge.svg)
```

### 🧠 Részletes Magyarázat

- **Badge** – Kis kép a README-ben, ami mutatja a CI állapotát (passing/failing). A `FELHASZNALO/REPO` részt a saját repódra kell cserélni. A kép automatikusan frissül minden CI futás után.

---

## Gyakorlat

1. Hozd létre a `.github/workflows/ci.yml` fájlt
2. Konfigurálj lint + test pipeline-t
3. Push-old és ellenőrizd a GitHub Actions fülön az eredményt
4. Add hozzá a coverage riportot
5. Hozd létre az autograding workflow-t
6. Commitold és pushold
