# Lecke 08 – SQLAlchemy ORM

> **Dokumentáció:** [SQLAlchemy](https://docs.sqlalchemy.org/) · [FastAPI SQL Databases](https://fastapi.tiangolo.com/tutorial/sql-databases/) · [Alembic](https://alembic.sqlalchemy.org/)

---

## 49–50. óra: SQLAlchemy bevezetés

### Mi az ORM?

Az **ORM** (Object-Relational Mapping) lehetővé teszi, hogy Python osztályokkal dolgozzunk adatbázis táblák helyett. Nem kell SQL-t írnunk – az ORM lefordítja a Python kódot SQL-re.

```
Python osztály  ←→  Adatbázis tábla
Python objektum ←→  Tábla sor
Attribútum      ←→  Oszlop
```

### Telepítés

```bash
pip install sqlalchemy psycopg2-binary
pip freeze > requirements.txt
```

### Adatbázis kapcsolat

```python
# app/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://kurzus:jelszo123@localhost:5432/backenddb"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
```

### Dependency: get_db

```python
# app/database.py (folytatás)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

---

## 51–52. óra: Modellek definiálása

```python
# app/models.py
from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime
from sqlalchemy.sql import func
from app.database import Base

class Termek(Base):
    __tablename__ = "termekek"

    id = Column(Integer, primary_key=True, index=True)
    nev = Column(String(100), nullable=False)
    ar = Column(Float, nullable=False)
    leiras = Column(String(500), nullable=True)
    aktiv = Column(Boolean, default=True)
    letrehozva = Column(DateTime(timezone=True), server_default=func.now())
```

### Oszloptípusok

| SQLAlchemy | Python | SQL |
|------------|--------|-----|
| `Integer` | `int` | `INTEGER` |
| `String(n)` | `str` | `VARCHAR(n)` |
| `Float` | `float` | `FLOAT` |
| `Boolean` | `bool` | `BOOLEAN` |
| `DateTime` | `datetime` | `TIMESTAMP` |
| `Text` | `str` | `TEXT` |

---

## 53–54. óra: Alembic migrációk

Az **Alembic** kezeli az adatbázis séma változásait (migrációk).

### Beállítás

```bash
pip install alembic
alembic init alembic
```

Szerkeszd az `alembic/env.py` fájlt:

```python
# alembic/env.py (a target_metadata sor módosítása)
from app.database import Base
from app.models import Termek  # Importáld az összes modellt!

target_metadata = Base.metadata
```

Szerkeszd az `alembic.ini` fájlt:

```ini
sqlalchemy.url = postgresql://kurzus:jelszo123@localhost:5432/backenddb
```

### Migráció létrehozása és futtatása

```bash
# Migráció generálása
alembic revision --autogenerate -m "termekek tabla letrehozasa"

# Migráció futtatása
alembic upgrade head

# Aktuális állapot
alembic current

# Visszaállítás
alembic downgrade -1
```

---

## Gyakorlat

1. Hozd létre az `app/database.py` és `app/models.py` fájlokat
2. Definiálj egy `Felhasznalo` modellt (id, nev, email, jelszo_hash, aktiv, letrehozva)
3. Állítsd be az Alembic-et
4. Futtasd a migrációt
5. Ellenőrizd psql-ben, hogy létrejött a tábla
6. Commitold és pushold
