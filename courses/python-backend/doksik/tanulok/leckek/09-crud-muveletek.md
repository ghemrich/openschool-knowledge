# Lecke 09 – CRUD műveletek adatbázissal

> **Dokumentáció:** [FastAPI SQL Databases](https://fastapi.tiangolo.com/tutorial/sql-databases/) · [SQLAlchemy Query](https://docs.sqlalchemy.org/en/20/orm/queryguide/)

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

Ezt `Depends(get_db)` formában használjuk a végpontokban:

```python
@app.get("/items/")
def list_items(db: Session = Depends(get_db)):
    items = db.query(Termek).all()
    return items
```

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

---

## Gyakorlat

1. Készítsd el a `crud.py`, `schemas.py` és `routers/items.py` fájlokat
2. Kötsd össze a végpontokat az adatbázissal
3. Teszteld a Swagger UI-ban: hozz létre, módosíts, kérdezz le és törölj termékeket
4. Ellenőrizd psql-ben, hogy az adatok bekerültek
5. Commitold és pushold
