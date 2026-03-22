# 📘 Lecke 08 – SQLAlchemy ORM

> 📚 Dokumentáció:
> https://docs.sqlalchemy.org/
> https://fastapi.tiangolo.com/tutorial/sql-databases/
> https://alembic.sqlalchemy.org/

---

## 49–50. óra: SQLAlchemy bevezetés

### Mi az ORM?

Az **ORM** (Object-Relational Mapping) lehetővé teszi, hogy Python osztályokkal dolgozzunk adatbázis táblák helyett. Nem kell SQL-t írnunk – az ORM lefordítja a Python kódot SQL-re.

```
Python osztály  ←→  Adatbázis tábla
Python objektum ←→  Tábla sor
Attribútum      ←→  Oszlop
```

### 🧠 Részletes Magyarázat

- **ORM (Object-Relational Mapping)** – Egy „fordító" réteg az alkalmazás és az adatbázis között. Ahelyett, hogy SQL szöveget írnánk, Python objektumokkal dolgozunk, és az ORM generálja a megfelelő SQL-t a háttérben.
- **Miért jó?** – (1) Nem kell SQL-t írnunk kézzel, (2) Python kód típusbiztos és IDE-támogatott, (3) adatbázis-függetlenség: ha PostgreSQL-ről SQLite-ra váltunk, a Python kód nem változik.
- **SQLAlchemy** – A legelterjedtebb Python ORM. Két használati módja van: Core (alacsony szintű SQL-szerű) és ORM (magas szintű, osztály-alapú). Mi az ORM módot használjuk.

### Telepítés

```bash
pip install sqlalchemy psycopg2-binary
pip freeze > requirements.txt
```

### 🧠 Részletes Magyarázat

- **`sqlalchemy`** – Maga az ORM könyvtár.
- **`psycopg2-binary`** – PostgreSQL driver Pythonhoz. Az SQLAlchemy ezt használja a háttérben a PostgreSQL-lel való kommunikációhoz. A `-binary` változat előre lefordítva érkezik, nem kell C fordító a telepítéshez.
- **`pip freeze > requirements.txt`** – Az összes telepített csomag verziószámát elmenti. Így más fejlesztő (vagy a Docker konténer) pontosan ugyanazokkal a verziókkal tudja telepíteni a függőségeket.

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

### 🧠 Részletes Magyarázat

- **`create_engine(DATABASE_URL)`** – Létrehoza az adatbázis „motort", ami kezeli a kapcsolatokat. A `DATABASE_URL` formátuma: `driver://user:password@host:port/database`. Az engine közvetlenül nem SQL-t futtat, hanem egy connection pool-t kezel (újrahasználja a kapcsolatokat, így gyorsabb).
- **`sessionmaker(...)`** – Egy „session gyár", ami session objektumokat hoz létre. A session az ORM munkamenete: ezen keresztül kérdezünk le, adunk hozzá, módosítunk és törlünk adatokat.
  - `autocommit=False` – Nem commitol automatikusan, nekünk kell meghívni a `db.commit()`-ot. Ez biztonságosabb, mert hiba esetén visszagörgethetünk.
  - `autoflush=False` – Nem szinkronizálja automatikusan a memóriabeli változásokat az adatbázissal. Mi döntjük el, mikor történjen.
  - `bind=engine` – A session ehhez az engine-hez (adatbázishoz) kapcsolódik.
- **`declarative_base()`** – Az ORM modellek alaposztálya. Minden modellünk ebből öröklődik, és ez tartja nyilván, hogy milyen táblák léteznek.

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

### 🧠 Részletes Magyarázat

- **`get_db()`** – Ez a FastAPI dependency, ami minden kéréshez biztosít egy adatbázis session-t. A `yield` előtti rész a kérés **elején** fut (session létrehozás), a `finally` blokk a kérés **végén** (session bezárás).
- **Miért `yield` és nem `return`?** – A `return` után nem tudnánk bezárni a session-t. A `yield` „szünetelteti" a függvényt: átadja a session-t a végpontnak, megvárja amíg a végpont lefut, majd folytatódik a `finally` blokkal.
- **``finally: db.close()``** – Mindig bezárja a session-t, még ha hiba történt is a végpont futása közben. Ez megakadályozza a „connection leak" problémát (amikor a kapcsolatok nem szabadulnak fel).

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

### 🧠 Részletes Magyarázat

- **`Base`** – A `declarative_base()` által létrehozott alaposztály. Minden modell, ami ebből öröklődik, automatikusan egy adatbázis táblát képvisel.
- **`__tablename__ = "termekek"`** – Meghatározza, hogy a Python osztály melyik adatbázis táblához tartozik. Konvenció: kisbetűs, többes szám.
- **`Column()` paraméterek:**

| Paraméter | Jelentés | Példa |
|-----------|----------|-------|
| Első arg. | Oszlop típusa | `Integer`, `String(100)` |
| `primary_key=True` | Elsődleges kulcs (egyedi azonosító) | `id` |
| `index=True` | Index létrehozása (gyorsabb keresés) | `id` |
| `nullable=False` | Kötelező mező (nem lehet NULL) | `nev` |
| `default=True` | Python-oldali alapértelmezés | `aktiv` |
| `server_default=func.now()` | Adatbázis-oldali alapértelmezés | `letrehozva` |

- **`default` vs. `server_default`** – A `default=True` Python-oldali: az ORM állítja be az értéket INSERT előtt. A `server_default=func.now()` adatbázis-oldali: az SQL szinten a `DEFAULT NOW()` kerül a CREATE TABLE-be. Dátumokhoz a `server_default` jobb, mert az adatbázis időzónáját használja.

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

### 🧠 Részletes Magyarázat

- **Migráció** – Egy adatbázis séma módosítás lépése. Ha hozzáadunk egy új oszlopot, az egy migráció. Ha törlünk egy táblát, az is. A migrációk **verziókezelve** vannak, mint a Git commitok az adatbázis sémához.
- **Miért kell Alembic?** – Ha csak `Base.metadata.create_all()`-t használunk, az csak **új** táblákat tud létrehozni, meglévőket nem módosít. Az Alembic képes: oszlop hozzáadás/törlés, típusváltoztatás, index hozzáadás, stb. – és mindezt visszafordíthatóan.

### Beállítás

```bash
pip install alembic
alembic init alembic
```

### 🧠 Részletes Magyarázat

- **`alembic init alembic`** – Létrehoz egy `alembic/` mappát és egy `alembic.ini` konfigurációs fájlt. Az `alembic/` mappa tartalmazza a migrációs szkripteket és az `env.py` konfigurációt.

Szerkeszd az `alembic/env.py` fájlt:

```python
# alembic/env.py (a target_metadata sor módosítása)
from app.database import Base
from app.models import Termek  # Importáld az összes modellt!

target_metadata = Base.metadata
```

### 🧠 Részletes Magyarázat

- **`target_metadata = Base.metadata`** – Megmondja az Alembic-nek, hogy milyen táblastruktúrát „célozzon". A `Base.metadata` tartalmazza az összes regisztrált modell tábla-leírását.
- **Miért kell importálni a modelleket?** – A `from app.models import Termek` fontos! Ha nem importáljuk, a Python nem tölti be a modellt, a `Base.metadata` üres lesz, és az Alembic nem talál semmit, amiből migrációt generálhatna.

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

### 🧠 Részletes Magyarázat

| Parancs | Mit csinál |
|---------|-----------|
| `revision --autogenerate -m "..."` | Összehasonlítja a modelleket az adatbázissal, és generál egy migrációs szkriptet a különbségekből |
| `upgrade head` | Az összes még nem futtatott migrációt alkalmazza (a legújabbig) |
| `current` | Megmutatja, melyik migrációnál tart az adatbázis |
| `downgrade -1` | Visszagörgeti az utolsó migrációt (hasznos, ha hibáztunk) |

- **`--autogenerate`** – Az Alembic automatikusan detektálja a különbségeket a Python modellek és az adatbázis jelenlegi állapota között. Új tábla? Új oszlop? Változott típus? Mind megjelenik a generált migrációban.
- **Migrációs fájl** – Az `alembic/versions/` mappában jön létre egy Python fájl két függvénnyel: `upgrade()` (alkalmazás) és `downgrade()` (visszafordítás). Mindig érdemes átnézni, mielőtt futtatjuk!

---

## Gyakorlat

1. Hozd létre az `app/database.py` és `app/models.py` fájlokat
2. Definiálj egy `Felhasznalo` modellt (id, nev, email, jelszo_hash, aktiv, letrehozva)
3. Állítsd be az Alembic-et
4. Futtasd a migrációt
5. Ellenőrizd psql-ben, hogy létrejött a tábla
6. Commitold és pushold
