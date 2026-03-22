# 19. hét – Docker Compose éles környezet

> **Beadás:** commitold és pushold a megoldásaidat ebbe a repóba!
> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz

---

Ezen a héten megtanulod a Docker Compose használatát éles környezetben. Több szolgáltatást (API, adatbázis, Nginx) futtatsz egyszerre, és konfigúrálod a production környezetet.

---

## Feladat

Készíts production-ready Docker konfigurációt a Termék API-hoz.

### 19.1 – Dockerfile ⭐
Készíts `Dockerfile`-t és `.dockerignore`-t. Az image python:3.11-slim alapú legyen.

### 19.2 – Docker Compose ⭐⭐
Készíts `docker-compose.yml`-t `api` és `db` szolgáltatásokkal. Named volume, healthcheck, depends_on.

### 19.3 – Health endpoint ⭐⭐
`GET /health` → `{"status": "healthy", "database": "connected"}` vagy 503.

### 19.4 – Entrypoint ⭐⭐⭐
Készíts `entrypoint.sh`-t: alembic migrate → uvicorn start. Teszteld: `docker compose down -v` → `docker compose up --build` → minden működik.

---

## Dokumentáció

- [Docker Compose](https://docs.docker.com/compose/)
- [Dockerfile](https://docs.docker.com/engine/reference/builder/)

## 📚 Kapcsolódó anyagok

Az ehhez a héthez tartozó elméleti anyagot és további gyakorlófeladatokat itt találod:

- 📖 [Lecke: Docker Compose éles környezet](https://github.com/ghemrich/openschool-knowledge/blob/master/courses/python-backend/leckek/19-docker-compose-eles.md)

## Beadás

1. `Dockerfile`, `docker-compose.yml`, `.dockerignore` legyen a repóban
2. Commitolj értelmes üzenetekkel
3. `git push` – ez a beadás!
