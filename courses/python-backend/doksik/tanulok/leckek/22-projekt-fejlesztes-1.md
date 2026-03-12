# Lecke 22 – Projekt fejlesztés I.

> **Dokumentáció:** [SQLAlchemy Relationships](https://docs.sqlalchemy.org/en/20/orm/relationships.html) · [FastAPI Bigger Applications](https://fastapi.tiangolo.com/tutorial/bigger-applications/)

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

### Migrációk

```bash
alembic revision --autogenerate -m "felhasznalok es posztok tabla"
alembic upgrade head
```

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

---

## Gyakorlat

1. Hozd létre a modellek közötti kapcsolatokat (relationship)
2. Készítsd el az összes sémát (Create, Update, Response)
3. Írd meg a CRUD függvényeket
4. Készítsd el a routereket jogosultság-ellenőrzéssel
5. Futtasd az Alembic migrációkat
6. Teszteld a Swagger UI-ban
7. Commitold és pushold
