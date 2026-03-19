# Kiegészítő gyakorlatok – 19. hét: Docker Compose éles környezet

> Ezek a feladatok a heti házi feladat melletti **extra gyakorlást** szolgálják.
> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz

---

### 19.1 – .dockerignore ⭐
Készíts optimális `.dockerignore` fájlt. Építsd meg az image-et előtte és utána, és hasonlítsd össze a méreteket. Miként befolyásolja a build context méretét?

### 19.2 – Docker Compose profiles ⭐⭐
Készíts `docker-compose.yml`-t profile-okkal:
- alapból: `api` + `db`
- `--profile dev`: + pgAdmin
- `--profile monitoring`: + Prometheus + Grafana (image-ek, portok, config nélkül elegendő)

Teszteld: `docker compose up`, `docker compose --profile dev up`.

### 19.3 – Healthcheck ⭐⭐
Adj healthcheck-et mindkét szolgáltatáshoz:
- DB: `pg_isready -U postgres`
- API: `curl -f http://localhost:8000/health`

A `docker compose ps`-ben lásd a `(healthy)` státuszt. Az API `depends_on` használjon `condition: service_healthy`-t.

### 19.4 – Környezeti változók kezelése ⭐⭐
Készíts két környezetet:
- `docker-compose.yml` + `docker-compose.override.yml` (dev: debug=true, hot reload)
- `docker-compose.yml` + `docker-compose.prod.yml` (prod: workers=4, no debug)

Teszteld: `docker compose up` (dev) vs `docker compose -f docker-compose.yml -f docker-compose.prod.yml up`.

### 19.5 – Backup és restore ⭐⭐⭐
Készíts shell scripteket:
- `backup.sh`: `pg_dump` a konténerből időbélyeges fájlnévvel
- `restore.sh`: `psql < dump.sql` a konténerbe

Teszteld: hozz létre adatokat, készíts backupot, töröld a volume-ot, állítsd vissza a backupból.
