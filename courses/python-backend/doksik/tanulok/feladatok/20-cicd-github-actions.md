# Feladatok – 20. hét: CI/CD és GitHub Actions

> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz
> A megoldásokat commitold és pushold a GitHub repódba.

---

### 20.1 – Alap CI workflow ⭐
Hozd létre a `.github/workflows/ci.yml` fájlt: checkout → setup-python 3.11 → pip install → pytest. Push-old és ellenőrizd a GitHub Actions fülön.

### 20.2 – Lint hozzáadás ⭐⭐
Adj hozzá `flake8` lint lépést a workflowhoz. Javítsd ki az esetleges lint hibákat az `app/` mappában.

### 20.3 – Coverage ⭐⭐
Add hozzá a `pytest-cov`-ot a workflowhoz: `pytest --cov=app --cov-report=term-missing`. A coverage eredménye jelenjen meg a CI logban.

### 20.4 – Több job ⭐⭐
Készíts két job-ot: `lint` és `test`. A `test` job `needs: lint` – csak akkor fut, ha a lint sikeres.

### 20.5 – Badge és README ⭐⭐⭐
Adj CI status badge-et a `README.md`-hoz. A badge mutassa a workflow aktuális állapotát (passing/failing). Készíts teljes README-t a projekt leírásával, telepítési útmutatóval és végpont táblázattal.
