# 20. hét – CI/CD és GitHub Actions

> **Beadás:** commitold és pushold a megoldásaidat ebbe a repóba!
> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz

---

Ezen a héten megismerkedsz a CI/CD (Continuous Integration / Continuous Deployment) fogalmával és a GitHub Actions eszközzel. Automatizált pipeline-t építesz, ami minden push után lefuttatja a teszteket és ellenőrzi a kódodat.

---

## Feladat

Készíts CI/CD pipeline-t a projektedhez.

### 20.1 – Alap CI ⭐
Készíts `.github/workflows/ci.yml`-t: checkout → setup-python → pip install → pytest.

### 20.2 – Lint ⭐⭐
Adj hozzá flake8 lint lépést a workflowhoz. Javítsd ki a hibákat.

### 20.3 – Coverage ⭐⭐
Adj hozzá `pytest --cov=app` lépést a CI-hoz.

### 20.4 – Multi-job ⭐⭐⭐
Készíts két job-ot: `lint` (flake8) és `test` (pytest). A `test` job `needs: lint`.

### 20.5 – Badge ⭐⭐⭐
Adj CI status badge-et a README.md-hoz.

---

## Dokumentáció

- [GitHub Actions](https://docs.github.com/en/actions)
- [actions/setup-python](https://github.com/actions/setup-python)

## 📚 Kapcsolódó anyagok

Az ehhez a héthez tartozó elméleti anyagot és további gyakorlófeladatokat itt találod:

- 📖 [Lecke: CI/CD és GitHub Actions](https://github.com/ghemrich/openschool-knowledge/blob/master/courses/python-backend/leckek/20-cicd-github-actions.md)

## Beadás

1. `.github/workflows/ci.yml` + `README.md` legyen a repóban
2. A CI zöld legyen
3. Commitolj értelmes üzenetekkel
4. `git push` – ez a beadás!
