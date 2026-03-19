# Kiegészítő gyakorlatok – 20. hét: CI/CD és GitHub Actions

> Ezek a feladatok a heti házi feladat melletti **extra gyakorlást** szolgálják.
> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz

---

### 20.1 – Matrix stratégia ⭐
Bővítsd a CI workflow-t matrix-szal: futtasd a teszteket Python 3.10, 3.11 és 3.12 verziókkal. Ellenőrizd, hogy mindhárom verzióval sikeresen fut.

### 20.2 – Cache használata ⭐⭐
Adj `actions/cache` lépést a pip függőségek cache-eléséhez. Hasonlítsd össze a workflow futási idejét cache-sel és anélkül.

### 20.3 – PR ellenőrzés ⭐⭐
Készíts külön workflow-t ami csak pull request-eknél fut:
- Lint (flake8 vagy ruff)
- Típusellenőrzés (mypy)
- Tesztek
- Megjegyzés a PR-hoz a coverage eredménnyel

### 20.4 – Docker image build ⭐⭐
Adj Docker build lépést a CI-hoz: `docker build -t app:${{ github.sha }} .`. Ellenőrizd, hogy az image sikeresen épül. Ha a `main` branch-re merge-ölöd, push-old a GitHub Container Registry-be.

### 20.5 – Környezet-függő deploy ⭐⭐⭐
Készíts multi-stage workflow-t:
1. `test` job: lint + tesztek
2. `build` job: Docker image build (needs: test)
3. `deploy-staging` job: (szimulált) staging deploy (needs: build, only on `develop` branch)
4. `deploy-prod` job: (szimulált) production deploy (needs: build, only on `main` branch, manual approval)

A deploy jobok "szimulációja" elegendő: `echo "Deploying to staging..."` + environment változók kiírása.
