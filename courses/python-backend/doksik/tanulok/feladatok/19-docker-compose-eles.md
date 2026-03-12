# Feladatok – 19. hét: Docker Compose éles környezet

> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz
> A megoldásokat commitold és pushold a GitHub repódba.

---

### 19.1 – Production Dockerfile ⭐
Készíts optimalizált `Dockerfile`-t `.dockerignore`-ral. Ne kerüljön bele: `venv/`, `tests/`, `__pycache__/`, `.env`, `.git`.

### 19.2 – Docker Compose ⭐⭐
Készíts `docker-compose.yml`-t `api` és `db` szolgáltatásokkal. Használj named volume-ot a PostgreSQL adatoknak. Az API `depends_on` healthcheck-kel várja a DB-t.

### 19.3 – Health endpoint ⭐⭐
Készíts `GET /health` végpontot, amely ellenőrzi a DB kapcsolatot (`SELECT 1`). Adj vissza `{"status": "healthy"}` vagy 503-at.

### 19.4 – Alembic Docker-ben ⭐⭐
Készíts `entrypoint.sh`-t, amely először futtatja az `alembic upgrade head`-et, majd indítja az uvicorn-t. Vagy készíts különálló `migrate` szolgáltatást a compose-ban.

### 19.5 – Teljes deploy teszt ⭐⭐⭐
Állj meg teljesen, töröld az összes adatot (`docker compose down -v`), puis indítsd újra (`docker compose up --build`). Teszteld: regisztrálj, lépj be, hozz létre elemeket, állítsd le és indítsd újra – az adatok megmaradnak.
