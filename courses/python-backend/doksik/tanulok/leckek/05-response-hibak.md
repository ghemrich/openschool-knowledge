# Lecke 05 – Response modellek és hibakezelés

> **Dokumentáció:** [FastAPI Response Model](https://fastapi.tiangolo.com/tutorial/response-model/) · [FastAPI Handling Errors](https://fastapi.tiangolo.com/tutorial/handling-errors/)

---

## 31–32. óra: Response modellek

Eddig a végpontjaink bármilyen adatot visszaadhattak. A `response_model` paraméterrel **meghatározzuk**, mit kapjon a kliens:

```python
from pydantic import BaseModel
from typing import Optional

class TermekLetrehozas(BaseModel):
    nev: str
    ar: float
    leiras: Optional[str] = None

class TermekValasz(BaseModel):
    id: int
    nev: str
    ar: float
    leiras: Optional[str] = None

@app.post("/termekek/", response_model=TermekValasz, status_code=201)
def termek_letrehozas(termek: TermekLetrehozas):
    uj_termek = {"id": 1, **termek.model_dump()}
    return uj_termek
```

### Miért jó ez?

- A válasz **garantáltan** a megadott formátumú lesz
- A Swagger UI dokumentáció pontosabb
- Kiszűri a felesleges mezőket (pl. jelszó hash)

### Különböző sémák

```python
class FelhasznaloLetrehozas(BaseModel):
    nev: str
    email: str
    jelszo: str

class FelhasznaloValasz(BaseModel):
    id: int
    nev: str
    email: str
    # A jelszo NEM szerepel a válaszban!
```

---

## 33–34. óra: Státuszkódok és hibakezelés

### Státuszkódok beállítása

```python
from fastapi import FastAPI, HTTPException, status

app = FastAPI()

@app.post("/items/", status_code=status.HTTP_201_CREATED)
def create_item(item: ItemCreate):
    return item

@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int):
    return
```

### HTTPException

```python
from fastapi import HTTPException

@app.get("/items/{item_id}")
def get_item(item_id: int):
    item = kereso_fuggveny(item_id)
    if not item:
        raise HTTPException(
            status_code=404,
            detail="Elem nem található"
        )
    return item
```

### Egyedi hibakezelő

```python
from fastapi import Request
from fastapi.responses import JSONResponse

class NemTalalhatoHiba(Exception):
    def __init__(self, uzenet: str):
        self.uzenet = uzenet

@app.exception_handler(NemTalalhatoHiba)
async def nem_talalhato_handler(request: Request, exc: NemTalalhatoHiba):
    return JSONResponse(
        status_code=404,
        content={"hiba": exc.uzenet}
    )
```

---

## 35–36. óra: Validációs hibák

A Pydantic automatikusan visszaad `422` kódot, ha a bemeneti adat hibás. Ezt testreszabhatjuk:

```python
from fastapi.exceptions import RequestValidationError

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={
            "hiba": "Érvénytelen adatok",
            "reszletek": exc.errors()
        }
    )
```

---

## Gyakorlat

1. Bővítsd a feladatkezelő (todo) API-t:
   - Készíts külön sémákat: `TodoCreate`, `TodoUpdate`, `TodoResponse`
   - Adj `response_model`-t minden végponthoz
   - Kezeld a 404 hibát, ha nem létezik a feladat
   - Kezeld a 400 hibát, ha üres a cím
2. Teszteld a hibás kéréseket is a Swagger UI-ban
3. Commitold és pushold
