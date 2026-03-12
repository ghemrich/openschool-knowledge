# Lecke 20 – CI/CD és GitHub Actions

> **Dokumentáció:** [GitHub Actions](https://docs.github.com/en/actions) · [actions/checkout](https://github.com/actions/checkout) · [actions/setup-python](https://github.com/actions/setup-python)

---

## 121–122. óra: CI/CD fogalma

### Mi a CI/CD?

| Rövidítés | Jelentés | Mit csinál? |
|-----------|----------|-------------|
| **CI** | Continuous Integration | Automatikus tesztelés minden push-nál |
| **CD** | Continuous Deployment | Automatikus telepítés sikeres tesztek után |

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

### Lint ellenőrzés hozzáadása

```yaml
      - name: Kód formázás ellenőrzés
        run: |
          pip install flake8
          flake8 app/ --max-line-length=120 --exclude=__pycache__
```

### Coverage riport

```yaml
      - name: Tesztek coverage-dzsel
        run: |
          pip install pytest-cov
          pytest tests/ -v --cov=app --cov-report=term-missing
```

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

---

## 125–126. óra: GitHub Classroom autograding

### Hogyan működik a GitHub Classroom?

1. A mentor létrehozza a feladatot (assignment) és template repót
2. A tanuló elfogadja → saját fork jön létre
3. A tanuló kódol és push-ol
4. A GitHub Actions futtatja a **pytest**-et automatikusan
5. A mentor látja az eredményt

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

### Badge hozzáadása a README-hez

```markdown
![CI](https://github.com/FELHASZNALO/REPO/actions/workflows/ci.yml/badge.svg)
```

---

## Gyakorlat

1. Hozd létre a `.github/workflows/ci.yml` fájlt
2. Konfigurálj lint + test pipeline-t
3. Push-old és ellenőrizd a GitHub Actions fülön az eredményt
4. Add hozzá a coverage riportot
5. Hozd létre az autograding workflow-t
6. Commitold és pushold
