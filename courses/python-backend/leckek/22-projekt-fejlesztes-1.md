# 📘 Lecke 22 – Projekt fejlesztés I.

> 📚 **Dokumentáció:**
> https://docs.sqlalchemy.org/en/20/orm/relationships.html
> https://fastapi.tiangolo.com/tutorial/bigger-applications/

---

## 133–134. óra: Modellek és migrációk

### Modellek közötti kapcsolatok

```python
# app/models/felhasznalo.py
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base

class Felhasznalo(Base):
    __tablename__ = "felhasznalok"
    id = Column(Integer, primary_key=True, index=True)
    nev = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False, index=True)
    jelszo_hash = Column(String, nullable=False)
    letrehozva = Column(DateTime, server_default=func.now())

    posztok = relationship("Poszt", back_populates="szerzo")
    kommentek = relationship("Komment", back_populates="szerzo")
```

### 🧠 Részletes Magyarázat

| Elem | Leírás |
|------|--------|
| **`__tablename__`** | Az adatbázis tábla neve – a Python osztálynévtől függetlenül megadhatjuk |
| **`primary_key=True`** | Ez a mező lesz az elsődleges kulcs, egyedi azonosító minden sorhoz |
| **`index=True`** | Indexet hoz létre a mezőre – gyorsabb keresés email alapján |
| **`unique=True`** | Nem enged két azonos értéket – egy email csak egyszer szerepelhet |
| **`nullable=False`** | A mező kötelező, nem lehet `NULL` |
| **`server_default=func.now()`** | Az adatbázis szerver automatikusan beállítja a jelenlegi időt létrehozáskor |
| **`relationship("Poszt", back_populates="szerzo")`** | Kétirányú kapcsolat: a felhasználóból elérhetők a posztjai, a posztból az szerzője |

A **`relationship`** nem hoz létre oszlopot az adatbázisban – ez egy ORM szintű kényelmi funkció. A tényleges kapcsolatot a **`ForeignKey`** valósítja meg a másik modellben.

```python
# app/models/poszt.py
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base

class Poszt(Base):
    __tablename__ = "posztok"
    id = Column(Integer, primary_key=True, index=True)
    cim = Column(String(200), nullable=False)
    tartalom = Column(Text, nullable=False)
    szerzo_id = Column(Integer, ForeignKey("felhasznalok.id"), nullable=False)
    letrehozva = Column(DateTime, server_default=func.now())
    modositva = Column(DateTime, onupdate=func.now())

    szerzo = relationship("Felhasznalo", back_populates="posztok")
    kommentek = relationship("Komment", back_populates="poszt", cascade="all, delete-orphan")
```

### 🧠 Részletes Magyarázat

| Elem | Leírás |
|------|--------|
| **`String(200)`** | Maximum 200 karakter hosszú szöveges mező (cím korlátozás) |
| **`Text`** | Korlátlan hosszúságú szöveges mező – hosszabb tartalmakhoz |
| **`ForeignKey("felhasznalok.id")`** | Idegen kulcs – összeköti a posztot a szerzővel a `felhasznalok` tábla `id` mezőjén keresztül |
| **`onupdate=func.now()`** | Automatikusan frissíti a mezőt, amikor a sort módosítjuk |
| **`cascade="all, delete-orphan"`** | Ha egy posztot törlünk, az összes hozzá tartozó komment is törlődik automatikusan |
| **`back_populates`** | A kétirányú kapcsolat másik oldala – `poszt.szerzo` és `felhasznalo.posztok` kölcsönösen hivatkoznak egymásra |

A **cascade** nagyon fontos az adatintegritás szempontjából: a **`"all, delete-orphan"`** azt jelenti, hogy a szülő (poszt) minden műveletét továbbítja a gyerekekre (kommentek), és ha egy komment „árva" marad (nincs posztja), törlődik.

### Migrációk

```bash
alembic revision --autogenerate -m "felhasznalok es posztok tabla"
alembic upgrade head
```

### 🧠 Részletes Magyarázat

- **`alembic revision --autogenerate`** – Az Alembic összehasonlítja a Python modelleket az adatbázis jelenlegi állapotával, és automatikusan generál egy migrációs szkriptet a különbségekből.
- **`-m "felhasznalok es posztok tabla"`** – A migráció üzenete (leírása), ami a fájlnévben is megjelenik.
- **`alembic upgrade head`** – Végrehajtja az összes még nem alkalmazott migrációt, frissítve az adatbázist a legújabb állapotra.

A migrációk előnye, hogy **verziókezelhetők** (Git-ben tárolhatók) és **visszafordíthatók** (`alembic downgrade`). Így a csapat minden tagja azonos adatbázis-struktúrával dolgozik.

---

## 135–136. óra: CRUD és sémák

### Pydantic sémák

```python
# app/schemas/poszt.py
from pydantic import BaseModel, Field
from datetime import datetime

class PosztBase(BaseModel):
    cim: str = Field(min_length=1, max_length=200)
    tartalom: str = Field(min_length=1)

class PosztCreate(PosztBase):
    pass

class PosztUpdate(BaseModel):
    cim: str | None = Field(None, min_length=1, max_length=200)
    tartalom: str | None = Field(None, min_length=1)

class PosztResponse(PosztBase):
    id: int
    szerzo_id: int
    letrehozva: datetime
    modositva: datetime | None = None

    class Config:
        from_attributes = True
```

### 🧠 Részletes Magyarázat

| Séma | Szerep |
|------|--------|
| **`PosztBase`** | Közös alap – a `cim` és `tartalom` mezőket definiálja validációval |
| **`PosztCreate`** | Létrehozáshoz használt séma – örökli a `PosztBase` mezőit, de nem ad hozzá újakat (a `szerzo_id`-t a szerver tölti ki) |
| **`PosztUpdate`** | Módosításhoz – minden mező opcionális (`None` alapértelmezéssel), így részleges frissítés is lehetséges |
| **`PosztResponse`** | Válasz séma – tartalmazza az `id`-t, `szerzo_id`-t és az időbélyegeket is |

A **`Field(min_length=1, max_length=200)`** biztosítja, hogy a cím nem lehet üres és nem lehet 200 karakternél hosszabb. A **`from_attributes = True`** (korábban `orm_mode`) lehetővé teszi, hogy a Pydantic közvetlenül az SQLAlchemy objektumból olvassa ki az adatokat.

Az **öröklési hierarchia** (`PosztBase` → `PosztCreate`, `PosztResponse`) csökkenti a kódduplikációt: a közös mezőket csak egyszer definiáljuk.

### CRUD műveletek

```python
# app/crud/poszt.py
from sqlalchemy.orm import Session
from app.models.poszt import Poszt
from app.schemas.poszt import PosztCreate, PosztUpdate

def get_posztok(db: Session, skip: int = 0, limit: int = 20):
    return db.query(Poszt).offset(skip).limit(limit).all()

def get_poszt(db: Session, poszt_id: int):
    return db.query(Poszt).filter(Poszt.id == poszt_id).first()

def create_poszt(db: Session, poszt: PosztCreate, szerzo_id: int):
    db_poszt = Poszt(**poszt.model_dump(), szerzo_id=szerzo_id)
    db.add(db_poszt)
    db.commit()
    db.refresh(db_poszt)
    return db_poszt

def update_poszt(db: Session, db_poszt: Poszt, poszt: PosztUpdate):
    for key, value in poszt.model_dump(exclude_unset=True).items():
        setattr(db_poszt, key, value)
    db.commit()
    db.refresh(db_poszt)
    return db_poszt

def delete_poszt(db: Session, db_poszt: Poszt):
    db.delete(db_poszt)
    db.commit()
```

### 🧠 Részletes Magyarázat

| Függvény | Művelet | Kulcs részlet |
|----------|---------|---------------|
| **`get_posztok`** | Listázás | Az **`offset`** és **`limit`** lapozást valósít meg – kihagyja az első `skip` elemet és legfeljebb `limit` darabot ad vissza |
| **`get_poszt`** | Egy elem lekérése | A **`.first()`** az első találatot adja vissza, vagy `None`-t ha nincs |
| **`create_poszt`** | Létrehozás | A **`model_dump()`** a Pydantic objektumot szótárrá alakítja, a `**` kicsomagolja kulcsszó-argumentumokként |
| **`update_poszt`** | Módosítás | Az **`exclude_unset=True`** csak a ténylegesen megadott mezőket adja vissza – így a `None` és a „nem küldött" megkülönböztethető |
| **`delete_poszt`** | Törlés | A **`db.delete()`** jelöli törlésre, a **`db.commit()`** véglegesíti |

A **`db.refresh(db_poszt)`** újratölti az objektumot az adatbázisból – így az automatikusan generált mezők (pl. `id`, `letrehozva`) is megjelennek a válaszban. A **`setattr(db_poszt, key, value)`** dinamikusan állítja be az attribútumokat – ez rugalmasabb, mint minden mezőt kézzel felsorolni.

---

## 137–138. óra: Routerek és jogosultságok

### Router

```python
# app/routers/posztok.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.dependencies import get_current_user
from app.crud import poszt as crud_poszt
from app.schemas.poszt import PosztCreate, PosztUpdate, PosztResponse

router = APIRouter(prefix="/posztok", tags=["Posztok"])

@router.get("/", response_model=list[PosztResponse])
def lista(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    return crud_poszt.get_posztok(db, skip, limit)

@router.get("/{poszt_id}", response_model=PosztResponse)
def egy_poszt(poszt_id: int, db: Session = Depends(get_db)):
    poszt = crud_poszt.get_poszt(db, poszt_id)
    if not poszt:
        raise HTTPException(404, "Poszt nem található")
    return poszt

@router.post("/", response_model=PosztResponse, status_code=201)
def letrehozas(
    poszt: PosztCreate,
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    return crud_poszt.create_poszt(db, poszt, user.id)

@router.put("/{poszt_id}", response_model=PosztResponse)
def modositas(
    poszt_id: int,
    poszt: PosztUpdate,
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    db_poszt = crud_poszt.get_poszt(db, poszt_id)
    if not db_poszt:
        raise HTTPException(404, "Poszt nem található")
    if db_poszt.szerzo_id != user.id:
        raise HTTPException(403, "Csak a saját posztod módosíthatod")
    return crud_poszt.update_poszt(db, db_poszt, poszt)

@router.delete("/{poszt_id}", status_code=200)
def torles(
    poszt_id: int,
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    db_poszt = crud_poszt.get_poszt(db, poszt_id)
    if not db_poszt:
        raise HTTPException(404, "Poszt nem található")
    if db_poszt.szerzo_id != user.id:
        raise HTTPException(403, "Csak a saját posztod törölheted")
    crud_poszt.delete_poszt(db, db_poszt)
    return {"message": "Poszt törölve"}
```

### 🧠 Részletes Magyarázat

| Elem | Leírás |
|------|--------|
| **`APIRouter(prefix="/posztok", tags=["Posztok"])`** | Külön router modul – a `prefix` minden útvonal elé teszi a `/posztok`-ot, a `tags` csoportosítja a Swagger UI-ban |
| **`response_model=list[PosztResponse]`** | A FastAPI automatikusan a megadott séma szerint szűri és validálja a választ |
| **`Depends(get_db)`** | Dependency injection – minden kéréshez új adatbázis munkamenetet (session) biztosít |
| **`Depends(get_current_user)`** | A token alapján azonosítja a bejelentkezett felhasználót – ha nincs/rossz a token, 401-et dob |
| **`status_code=201`** | A POST sikeres válaszkódja – „Created" |

A **jogosultság-ellenőrzés** (authorization) két szinten működik:
1. **Autentikáció** – a `get_current_user` dependency ellenőrzi, hogy a felhasználó be van-e jelentkezve (érvényes JWT token)
2. **Tulajdonos-ellenőrzés** – a `db_poszt.szerzo_id != user.id` biztosítja, hogy csak a saját tartalmát módosíthatja/törölheti

Ez a **CRUD + Router + Schema** minta a FastAPI projektek standard felépítése: a felelősségek szétválasztása (separation of concerns) könnyebben karbantarthatóvá és tesztelhetővé teszi a kódot.

---

## Gyakorlat

1. Hozd létre a modellek közötti kapcsolatokat (relationship)
2. Készítsd el az összes sémát (Create, Update, Response)
3. Írd meg a CRUD függvényeket
4. Készítsd el a routereket jogosultság-ellenőrzéssel
5. Futtasd az Alembic migrációkat
6. Teszteld a Swagger UI-ban
7. Commitold és pushold
