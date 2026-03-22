# 📘 Lecke 09 – CRUD műveletek adatbázissal

> 📚 Dokumentáció:
> https://fastapi.tiangolo.com/tutorial/sql-databases/
> https://docs.sqlalchemy.org/en/20/orm/queryguide/

---

## 55–56. óra: Adatbázis session kezelés

### get_db dependency

```python
# app/database.py
from fastapi import Depends
from sqlalchemy.orm import Session

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

### 🧠 Részletes Magyarázat

- **`Session`** – Az SQLAlchemy munkamenet-objektuma. Ezen keresztül kommunikálunk az adatbázissal: lekérdezés, beszúrás, módosítás, törlés. Egy session egy „tranzakciót" képvisel – vagy minden sikerül, vagy semmi (atomikus).
- **`yield db`** – A FastAPI Depends rendszere generátor-alapú: a `yield` előtt a session létrejön, a végpont megkapja és használja, majd a `yield` után (a `finally` blokkban) bezáródik. Ez biztosítja, hogy soha ne maradjon nyitott kapcsolat.
- **Egy kérés = egy session** – Minden HTTP kéréshez külön session jön létre és záródik be. Ez az ajánlott minta, mert elkerüli az állapotkezelési problémákat.

Ezt `Depends(get_db)` formában használjuk a végpontokban:

```python
@app.get("/items/")
def list_items(db: Session = Depends(get_db)):
    items = db.query(Termek).all()
    return items
```

### 🧠 Részletes Magyarázat

- **`db: Session = Depends(get_db)`** – A FastAPI dependency injection rendszere: a `db` paramétert automatikusan a `get_db()` függvényből kapja, típusa `Session`. A típus jelölés az IDE-nek segít (autocomplete, típusellenőrzés).
- **`db.query(Termek)`** – Egy lekérdezés-objektumot hoz létre a `termekek` táblára. Ez még nem futtat SQL-t! Csak egy „lekérdezés-tervet" épít.
- **`.all()`** – Végrehajtja a lekérdezést és listában adja vissza az összes sort. Egyéb módszerek: `.first()` (első sor vagy `None`), `.one()` (pontosan egy sor, hiba ha több/kevesebb).

---

## 57–58. óra: CRUD függvények

Hozz létre egy `app/crud.py` modult a CRUD műveletekhez:

```python
# app/crud.py
from sqlalchemy.orm import Session
from app import models, schemas

def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Termek).offset(skip).limit(limit).all()

def get_item(db: Session, item_id: int):
    return db.query(models.Termek).filter(models.Termek.id == item_id).first()

def create_item(db: Session, item: schemas.TermekLetrehozas):
    db_item = models.Termek(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def update_item(db: Session, item_id: int, item: schemas.TermekFrissites):
    db_item = db.query(models.Termek).filter(models.Termek.id == item_id).first()
    if not db_item:
        return None
    for key, value in item.model_dump(exclude_unset=True).items():
        setattr(db_item, key, value)
    db.commit()
    db.refresh(db_item)
    return db_item

def delete_item(db: Session, item_id: int):
    db_item = db.query(models.Termek).filter(models.Termek.id == item_id).first()
    if not db_item:
        return False
    db.delete(db_item)
    db.commit()
    return True
```

### 🧠 Részletes Magyarázat

Ez a fájl a **CRUD logikát** különíti el a végpontoktól. Előnyei: (1) a végpontok tisztábbak, (2) a CRUD függvények tesztelhetők a FastAPI nélkül is, (3) egy helyen van az összes adatbázis művelet.

**Create (létrehozás) – `create_item`:**
```
item.model_dump()  →  {"nev": "Laptop", "ar": 299990}
models.Termek(**...)  →  Termek(nev="Laptop", ar=299990)
db.add(db_item)  →  Session-be kerül (még nincs az adatbázisban!)
db.commit()  →  INSERT SQL fut, adat beíródik
db.refresh(db_item)  →  Az adatbázisból visszaolvassa (id, letrehozva kitöltődik)
```

**Read (olvasás) – `get_items` és `get_item`:**
- **`.offset(skip).limit(limit)`** – Lapozás (pagination). Az `offset` kihagyja az első N sort, a `limit` legfeljebb N sort ad vissza. Példa: `skip=20, limit=10` → a 21-30. sorok.
- **`.filter(models.Termek.id == item_id)`** – SQL WHERE feltétel. Az `==` itt nem Python összehasonlítás, hanem az SQLAlchemy operátor-túlterhelése, ami `WHERE id = :id` SQL-t generál.
- **`.first()`** – Az első találatot adja vissza, vagy `None`-t ha nincs. Nem dob hibát, mint a `.one()`.

**Update (módosítás) – `update_item`:**
- **`model_dump(exclude_unset=True)`** – Csak azokat a mezőket adja vissza, amelyeket a kliens **ténylegesen megadott**. Ha csak az `ar`-t küldik, a `nev` nem jelenik meg a dict-ben → nem íródik felül.
- **`setattr(db_item, key, value)`** – Dinamikusan beállítja az objektum attribútumát. A `setattr(db_item, "ar", 199990)` egyenértékű a `db_item.ar = 199990`-vel, de ciklusban használható.

**Delete (törlés) – `delete_item`:**
- **`db.delete(db_item)`** – A session-ből törlésre jelöli az objektumot. A `db.commit()` hívás futtatja a tényleges `DELETE FROM` SQL-t.

### Sémák (Pydantic)

```python
# app/schemas.py
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class TermekLetrehozas(BaseModel):
    nev: str = Field(min_length=1, max_length=100)
    ar: float = Field(gt=0)
    leiras: Optional[str] = None

class TermekFrissites(BaseModel):
    nev: Optional[str] = Field(default=None, min_length=1, max_length=100)
    ar: Optional[float] = Field(default=None, gt=0)
    leiras: Optional[str] = None

class TermekValasz(BaseModel):
    id: int
    nev: str
    ar: float
    leiras: Optional[str] = None
    aktiv: bool
    letrehozva: datetime

    class Config:
        from_attributes = True
```

### 🧠 Részletes Magyarázat

Három különböző séma, három különböző feladatra:

| Séma | Felhasználás | Speciális |
|------|-------------|----------|
| `TermekLetrehozas` | POST kérés body | Minden mező kötelező (kivéve leiras) |
| `TermekFrissites` | PUT kérés body | Minden mező opcionális (részleges frissítés) |
| `TermekValasz` | Válasz (output) | Tartalmazza az `id`-t, `aktiv`-ot, `letrehozva`-t |

- **`class Config: from_attributes = True`** – Ez mondja meg a Pydantic-nak, hogy az SQLAlchemy objektumokat is el tudja fogadni (nem csak dict-eket). Enélkül a `return db_item` hibát dobna, mert a Pydantic nem tudná kiolvasni a `Termek` ORM objektum attribútumait. (Pydantic v1-ben ez `orm_mode = True` volt.)
- **`TermekFrissites`** – Minden mező opcionális (`Optional`), mert PUT-nál nem kötelező mindent megadni. Az `exclude_unset=True` a `crud.py`-ban gondoskodik róla, hogy csak a megadott mezők frissüljenek.

---

## 59–60. óra: CRUD összekötése végpontokkal

```python
# app/routers/items.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app import crud, schemas

router = APIRouter(prefix="/termekek", tags=["Termékek"])

@router.get("/", response_model=List[schemas.TermekValasz])
def termekek_listazasa(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_items(db, skip=skip, limit=limit)

@router.get("/{termek_id}", response_model=schemas.TermekValasz)
def termek_lekerese(termek_id: int, db: Session = Depends(get_db)):
    db_item = crud.get_item(db, item_id=termek_id)
    if not db_item:
        raise HTTPException(status_code=404, detail="Termék nem található")
    return db_item

@router.post("/", response_model=schemas.TermekValasz, status_code=status.HTTP_201_CREATED)
def termek_letrehozasa(item: schemas.TermekLetrehozas, db: Session = Depends(get_db)):
    return crud.create_item(db=db, item=item)

@router.put("/{termek_id}", response_model=schemas.TermekValasz)
def termek_modositasa(termek_id: int, item: schemas.TermekFrissites, db: Session = Depends(get_db)):
    db_item = crud.update_item(db, item_id=termek_id, item=item)
    if not db_item:
        raise HTTPException(status_code=404, detail="Termék nem található")
    return db_item

@router.delete("/{termek_id}", status_code=status.HTTP_204_NO_CONTENT)
def termek_torlese(termek_id: int, db: Session = Depends(get_db)):
    success = crud.delete_item(db, item_id=termek_id)
    if not success:
        raise HTTPException(status_code=404, detail="Termék nem található")
```

### 🧠 Részletes Magyarázat

Ez a fájl összekötí a CRUD logikát a HTTP végpontokkal. A végpontok felelőssége:
1. **Input fogadás** – Path paraméterek, query paraméterek, request body (Pydantic séma)
2. **CRUD meghívás** – A `crud` modul függvényeinek hívása
3. **Hibakezelés** – Ha a CRUD `None`-t / `False`-t ad, 404 hiba
4. **Output formázás** – A `response_model` biztosítja a válasz formátumot

- **`List[schemas.TermekValasz]`** – A válasz egy lista, ahol minden elem `TermekValasz` típusú. A FastAPI a Swagger UI-ban is ezt mutatja.
- **Tiszta rétegek** – A végpont NEM tartalmaz SQL logikát (az a `crud.py`-ban van), és NEM tartalmaz validációt (az a `schemas.py`-ban van). Ez a **Separation of Concerns** elv: minden rétegnek egy feladata van.
- **Adatfolyam egy POST kérésnél:**
```
Kliens → JSON body → schemas.TermekLetrehozas (validáció)
  → crud.create_item() → models.Termek (ORM) → SQL INSERT
  → db.refresh() → schemas.TermekValasz (response_model) → JSON válasz
```

---

## Gyakorlat

1. Készítsd el a `crud.py`, `schemas.py` és `routers/items.py` fájlokat
2. Kötsd össze a végpontokat az adatbázissal
3. Teszteld a Swagger UI-ban: hozz létre, módosíts, kérdezz le és törölj termékeket
4. Ellenőrizd psql-ben, hogy az adatok bekerültek
5. Commitold és pushold
