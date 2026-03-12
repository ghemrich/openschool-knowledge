# Feladatok – 7. hét: Docker és PostgreSQL

> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz
> A megoldásokat commitold és pushold a GitHub repódba.

---

### 7.1 – Docker alapok ⭐
Készíts egy `Dockerfile`-t, amely egy egyszerű Python alkalmazást futtat. Építsd meg az image-et és futtasd a konténert. Írd ki a `docker ps` kimenetét.

### 7.2 – PostgreSQL konténer ⭐
Indíts egy PostgreSQL 16 konténert Docker-rel. Csatlakozz hozzá `psql`-lel. Hozz létre egy `teszt` adatbázist és egy `felhasznalok` táblát (id, nev, email).

### 7.3 – SQL gyakorlás ⭐⭐
A PostgreSQL konténerben:
- Szúrj be 5 felhasználót (`INSERT INTO`)
- Kérdezd le az összes felhasználót (`SELECT`)
- Kérdezd le névvel szűrve (`WHERE`)
- Módosíts egy felhasználó emailjét (`UPDATE`)
- Törölj egy felhasználót (`DELETE`)

### 7.4 – Docker Compose ⭐⭐
Készíts `docker-compose.yml` fájlt, amely egy PostgreSQL szolgáltatást tartalmaz named volume-mal. Indítsd el, csatlakozz, és ellenőrizd, hogy a leállítás és újraindítás után az adatok megmaradnak.

### 7.5 – FastAPI + PostgreSQL ⭐⭐⭐
Készíts `docker-compose.yml`-t, amely két szolgáltatást tartalmaz: `api` (FastAPI) és `db` (PostgreSQL). Az API konténer `depends_on` legyen a DB konténeren. Teszteld, hogy az API elindul és elérhető.
