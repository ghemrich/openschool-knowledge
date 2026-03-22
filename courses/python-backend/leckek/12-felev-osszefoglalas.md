# 📘 Lecke 12 – Félév összefoglalás és próbavizsga

> 📚 Dokumentáció:
> Lásd az előző leckék hivatkozásait

---

## 73–74. óra: Félév áttekintés

### Eddig tanultak összefoglalása

| Hét | Téma | Kulcs fogalmak |
|-----|------|----------------|
| 0 | Git, GitHub, parancssor | CLI, git branch, GitHub Classroom |
| 1 | Python, venv | venv, pip, requirements.txt |
| 2 | FastAPI bevezetés | REST, HTTP methods, Swagger UI |
| 3 | Útvonalak, paraméterek | Path params, Query params |
| 4 | Request body, Pydantic | BaseModel, Field, validation |
| 5 | Response, hibakezelés | response_model, HTTPException |
| 6 | DI, Router, Config | Depends(), APIRouter, BaseSettings |
| 7 | Docker, PostgreSQL | Dockerfile, docker-compose, SQL |
| 8 | SQLAlchemy ORM | Models, engine, Alembic |
| 9 | CRUD műveletek | crud.py, schemas, get_db |
| 10 | Auth, JWT | bcrypt, JWT, OAuth2 |
| 11 | Middleware, CORS | Middleware, CORS, lifespan |

### 🧠 Részletes Magyarázat

Az első 12 hét lefedi egy modern backend alkalmazás **teljes alapját**. Az összefüggések:

```
FastAPI app (2. hét)
  ├── Végpontok: Path + Query paraméterek (3. hét)
  ├── Request body: Pydantic validáció (4. hét)
  ├── Response: Sémák, hibakezelés (5. hét)
  ├── Struktúra: Router, DI, Config (6. hét)
  ├── Adatbázis: Docker + PostgreSQL (7. hét)
  │     └── ORM: SQLAlchemy + Alembic (8. hét)
  │           └── CRUD: crud.py (9. hét)
  ├── Auth: JWT + bcrypt (10. hét)
  └── Middleware: CORS, naplózás (11. hét)
```

Minden hétnek az előzőre épül. A 2. félév (13–24. hét) a **tesztelést**, **haladó funkciók**at és a **vizsgaprojekt**et fedi le.

### Teljes projekt struktúra

```
backend-projekt/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI app, middleware, routerek
│   ├── config.py             # BaseSettings, .env
│   ├── database.py           # engine, SessionLocal, Base, get_db
│   ├── auth.py               # hash, JWT
│   ├── dependencies.py       # get_current_user
│   ├── models.py             # SQLAlchemy modellek
│   ├── schemas.py            # Pydantic sémák
│   └── routers/
│       ├── __init__.py
│       ├── auth.py
│       └── items.py
├── alembic/                  # Migrációk
│   └── versions/
├── alembic.ini
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── .env
└── .env.example
```

### 🧠 Részletes Magyarázat

A fájlok közötti **adatfolyam** egy tipikus kérésnél:

```
HTTP kérés
  → main.py (middleware: CORS, naplózás)
    → routers/items.py (végpont, Pydantic validáció)
      → dependencies.py (get_current_user → auth.py + database.py)
        → crud.py (adatbázis műveletek)
          → models.py (SQLAlchemy) → PostgreSQL
        ← schemas.py (response_model szűrés)
      ← JSON válasz
```

| Réteg | Fájl(ok) | Felelősség |
|-------|----------|-----------|
| **HTTP** | main.py, middleware | Kérés fogadás, CORS, naplózás |
| **Routing** | routers/*.py | URL → függvény hozzárendelés |
| **Validáció** | schemas.py | Input/output adatellenőrzés |
| **Auth** | auth.py, dependencies.py | Azonosítás, jogosultság |
| **Üzleti logika** | crud.py | CRUD műveletek |
| **Adatbázis** | models.py, database.py | ORM, session, migráció |
| **Konfiguráció** | config.py, .env | Környezeti beállítások |

---

## 75–76. óra: Teljes API építés (gyakorlás)

### Feladat: Jegyzet API

Építs egy teljes **Jegyzet API**-t a nulláról 2 óra alatt:

**Adatmodell:**
```python
class Jegyzet(Base):
    __tablename__ = "jegyzetek"
    id = Column(Integer, primary_key=True, index=True)
    cim = Column(String, nullable=False)
    tartalom = Column(String, nullable=False)
    szerzo_id = Column(Integer, ForeignKey("felhasznalok.id"))
    letrehozva = Column(DateTime, default=func.now())
```

### 🧠 Részletes Magyarázat

- **`ForeignKey("felhasznalok.id")`** – Idegen kulcs: a `szerzo_id` mező a `felhasznalok` tábla `id` oszlopára hivatkozik. Ez kapcsolatot teremt a két tábla között (egy felhasználónak sok jegyzete lehet). Az adatbázis szinten biztosítja, hogy csak létező felhasználó ID-t lehet beírni.
- **Kapcsolatok (relations)** – A `ForeignKey` az adatbázis szintű kapcsolat. Ha az ORM-ben is szeretnénk navigálni (`jegyzet.szerzo.nev`), használjuk az SQLAlchemy `relationship()`-et is:
```python
from sqlalchemy.orm import relationship
# A Jegyzet modellben:
szerzo = relationship("Felhasznalo", back_populates="jegyzetek")
# A Felhasznalo modellben:
jegyzetek = relationship("Jegyzet", back_populates="szerzo")
```

**Végpontok:**
- `POST /auth/regisztracio` – regisztráció
- `POST /auth/login` – bejelentkezés
- `GET /jegyzetek` – összes jegyzet listázás
- `POST /jegyzetek` – új jegyzet (védett)
- `GET /jegyzetek/{id}` – egy jegyzet
- `PUT /jegyzetek/{id}` – módosítás (csak saját, védett)
- `DELETE /jegyzetek/{id}` – törlés (csak saját, védett)

### 🧠 Részletes Magyarázat

A „csak saját" logika a végpontban:
```python
@router.put("/jegyzetek/{id}")
def modositas(id: int, adat: JegyzetFrissites, 
              current_user = Depends(get_current_user),
              db: Session = Depends(get_db)):
    jegyzet = crud.get_jegyzet(db, id)
    if not jegyzet:
        raise HTTPException(404, "Nem található")
    if jegyzet.szerzo_id != current_user.id:
        raise HTTPException(403, "Nincs jogosultságod")
    return crud.update_jegyzet(db, id, adat)
```

- **403 vs. 404** – A `403 Forbidden` jelzi: „Tudom ki vagy, de nem teheted." A `404 Not Found` jelzi: „Nincs ilyen." Biztonsági szempontból néha szándékosan 404-et adunk 403 helyett, hogy ne áruljuk el, létezik-e az erőforrás.

---

## 77–78. óra: Próbavizsga

### Próbavizsga feladat (60 pont, 120 perc)

Ez a próbavizsga az első félév anyagát (1–11. hét) fedi le. A valódi vizsga (24. hét) 240 perc és 5 feladatból áll — a próbavizsga az első 3 feladattípust (API, DB, Auth) gyakoroltatja.

### 🧠 Részletes Magyarázat

**Vizsgastratégia:**
1. **Olvasd el az összes feladatot** (5 perc) – ne kezdj el kódolni, amíg nem érted az összképet
2. **Projekt létrehozása** (10 perc) – `venv`, `pip install`, `alembic init`, projekt struktúra
3. **Adatmodell + migráció** (15 perc) – `models.py`, `alembic revision --autogenerate`, `alembic upgrade head`
4. **Sémák** (10 perc) – `schemas.py` (Create, Update, Response)
5. **CRUD + végpontok** (40 perc) – `crud.py`, `routers/*.py`
6. **Auth** (30 perc) – regisztráció, login, védett végpontok
7. **Tesztelés** (10 perc) – Swagger UI-ban végigpróbálni mindent

#### 1. feladat – Alap végpontok (15 pont)

Készíts egy FastAPI alkalmazást könyv-nyilvántartásra:
- `GET /` – üdvözlő üzenet (3 pont)
- `GET /konyvek` – összes könyv listázása (4 pont)
- `GET /konyvek/{id}` – egy könyv lekérése, 404 ha nem létezik (4 pont)
- `POST /konyvek` – új könyv hozzáadása (4 pont)

#### 2. feladat – Adatbázis integráció (20 pont)

- SQLAlchemy modell: Konyv (id, cim, szerzo, ev, ar) (5 pont)
- Pydantic sémák (Create, Update, Response) (5 pont)
- CRUD műveletek (crud.py) (5 pont)
- Alembic migráció (5 pont)

#### 3. feladat – Auth és védett végpontok (25 pont)

- Felhasznalo modell és regisztráció (5 pont)
- JWT login (5 pont)
- `POST /konyvek` csak bejelentkezett felhasználóknak (5 pont)
- `PUT /konyvek/{id}` és `DELETE /konyvek/{id}` védett (5 pont)
- Helyes hibakódok (401, 403, 404) (5 pont)

### 🧠 Részletes Magyarázat

**Pontozás és gyakori hibák:**

| Hiba | Elveszíthető pont | Megelőzés |
|------|-------------------|-----------|
| Nincs `response_model` | 1-2 pont/végpont | Mindig add meg |
| Rossz státuszkód (200 POST helyett 201) | 1 pont/végpont | POST=201, DELETE=204 |
| Jelszó a válaszban | 3-5 pont | Külön Input/Output séma |
| `alembic upgrade head` elmarad | 5 pont | Migráció futtatása! |
| Nincs 404 kezelés | 2-3 pont/végpont | `if not item: raise HTTPException` |

---

## Gyakorlat

1. Ismételd át az eddigi leckéket – nézd végig a kód példákat
2. Oldd meg a Jegyzet API feladatot önállóan
3. Próbáld meg a próbavizsga feladatot 120 perc alatt
4. Commitold és pushold mindkét projektet
