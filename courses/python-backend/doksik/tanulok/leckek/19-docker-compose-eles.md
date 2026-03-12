# Lecke 19 – Docker Compose éles környezet

> **Dokumentáció:** [Docker Compose](https://docs.docker.com/compose/) · [Dockerfile reference](https://docs.docker.com/engine/reference/builder/) · [Multi-stage builds](https://docs.docker.com/build/building/multi-stage/)

---

## 115–116. óra: Production Dockerfile

### Fejlesztői vs. éles Dockerfile

Fejlesztéskor: `uvicorn --reload` (forró újratöltés). Élesben: nincs reload, optimalizált image.

### Multi-stage Dockerfile

```dockerfile
# Dockerfile
FROM python:3.11-slim AS base

WORKDIR /app

# Csak a requirements.txt másolása (cache kihasználás)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Alkalmazás másolása
COPY app/ ./app/
COPY alembic/ ./alembic/
COPY alembic.ini .

# Port
EXPOSE 8000

# Indítás
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### .dockerignore

```
__pycache__
*.pyc
.env
.git
.venv
tests/
uploads/
*.md
```

---

## 117–118. óra: Docker Compose teljes alkalmazás

### docker-compose.yml

```yaml
services:
  db:
    image: postgres:16-alpine
    environment:
      POSTGRES_DB: backend_db
      POSTGRES_USER: admin
      POSTGRES_PASSWORD: ${DB_PASSWORD}
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U admin -d backend_db"]
      interval: 5s
      timeout: 5s
      retries: 5

  api:
    build: .
    ports:
      - "8000:8000"
    environment:
      DATABASE_URL: postgresql://admin:${DB_PASSWORD}@db:5432/backend_db
      SECRET_KEY: ${SECRET_KEY}
    depends_on:
      db:
        condition: service_healthy
    volumes:
      - uploads_data:/app/uploads

volumes:
  postgres_data:
  uploads_data:
```

### .env fájl (Docker Compose használja)

```env
DB_PASSWORD=biztonsagos_jelszo_123
SECRET_KEY=nagyon_titkos_kulcs_456
```

### Parancsok

```bash
# Építés és indítás
docker compose up --build

# Háttérben
docker compose up -d --build

# Naplók
docker compose logs -f api
docker compose logs -f db

# Leállítás
docker compose down

# Leállítás + adatok törlése
docker compose down -v
```

---

## 119–120. óra: Migrációk és healthcheck

### Alembic futtatás Docker-ben

```yaml
# docker-compose.yml kiegészítés
  migrate:
    build: .
    command: alembic upgrade head
    environment:
      DATABASE_URL: postgresql://admin:${DB_PASSWORD}@db:5432/backend_db
    depends_on:
      db:
        condition: service_healthy
```

```bash
# Migráció futtatás
docker compose run --rm migrate
```

### Vagy entrypoint scripttel

```bash
#!/bin/bash
# entrypoint.sh
set -e

echo "Migrációk futtatása..."
alembic upgrade head

echo "Szerver indítása..."
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

```dockerfile
COPY entrypoint.sh .
RUN chmod +x entrypoint.sh
CMD ["./entrypoint.sh"]
```

### API healthcheck

```python
@app.get("/health")
def health_check(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        return {"status": "healthy", "database": "connected"}
    except Exception:
        raise HTTPException(503, detail="Database unavailable")
```

```yaml
# docker-compose.yml
  api:
    ...
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      interval: 10s
      timeout: 5s
      retries: 3
```

### Hasznos Docker Compose parancsok

```bash
docker compose ps            # futó konténerek
docker compose exec api bash # shell az API konténerben
docker compose exec db psql -U admin -d backend_db  # psql
docker compose restart api   # újraindítás
docker compose build --no-cache  # cache nélkül újraépítés
```

---

## Gyakorlat

1. Készíts production Dockerfile-t `.dockerignore`-ral
2. Hozd létre a `docker-compose.yml`-t (api + db)
3. Add hozzá a `/health` végpontot az API-hoz
4. Indítsd el a teljes alkalmazást `docker compose up --build`-del
5. Futtasd a migrációkat Docker-ben
6. Commitold és pushold
