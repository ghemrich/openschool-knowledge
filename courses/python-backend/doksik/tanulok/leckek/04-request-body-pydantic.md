# Lecke 04 – Request body és Pydantic

> **Dokumentáció:** [Pydantic](https://docs.pydantic.dev/) · [FastAPI Request Body](https://fastapi.tiangolo.com/tutorial/body/) · [FastAPI Body Fields](https://fastapi.tiangolo.com/tutorial/body-fields/)

---

## 25–26. óra: Pydantic modellek

A **Pydantic** automatikus adatvalidálást biztosít. A modellek `BaseModel`-ből öröklődnek:

```python
from pydantic import BaseModel, Field
from typing import Optional

class TermekLetrehozas(BaseModel):
    nev: str = Field(min_length=1, max_length=100, description="Termék neve")
    ar: float = Field(gt=0, description="Termék ára (Ft)")
    leiras: Optional[str] = Field(default=None, max_length=500)
    keszleten: bool = Field(default=True)
```

### Validáció

A Pydantic automatikusan ellenőrzi:
- Típusok egyezését (str, int, float, bool)
- Megszorításokat (min_length, gt, le, stb.)
- Kötelező vs. opcionális mezőket

```python
# ✅ Érvényes
{"nev": "Laptop", "ar": 299990.0}

# ❌ Hibás (ar negatív)
{"nev": "Laptop", "ar": -100}
# → 422 Unprocessable Entity
```

### Beágyazott modellek

```python
class Cim(BaseModel):
    varos: str
    utca: str
    iranyitoszam: str

class Felhasznalo(BaseModel):
    nev: str
    email: str
    cim: Cim
```

---

## 27–28. óra: POST végpont request body-val

```python
from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()

class TermekLetrehozas(BaseModel):
    nev: str = Field(min_length=1, max_length=100)
    ar: float = Field(gt=0)
    leiras: Optional[str] = None

# Memóriában tárolt adatok (később adatbázissal váltjuk ki)
termekek = []
kovetkezo_id = 1

@app.post("/termekek/", status_code=201)
def termek_letrehozas(termek: TermekLetrehozas):
    global kovetkezo_id
    uj_termek = {
        "id": kovetkezo_id,
        "nev": termek.nev,
        "ar": termek.ar,
        "leiras": termek.leiras
    }
    termekek.append(uj_termek)
    kovetkezo_id += 1
    return uj_termek
```

A Swagger UI-ban a „Try it out" gombbal tudsz JSON request body-t küldeni.

---

## 29–30. óra: PUT és DELETE végpontok

```python
from fastapi import HTTPException

@app.get("/termekek/")
def termekek_listazasa():
    return termekek

@app.get("/termekek/{termek_id}")
def termek_lekerese(termek_id: int):
    for termek in termekek:
        if termek["id"] == termek_id:
            return termek
    raise HTTPException(status_code=404, detail="Termék nem található")

@app.put("/termekek/{termek_id}")
def termek_modositasa(termek_id: int, frissites: TermekLetrehozas):
    for termek in termekek:
        if termek["id"] == termek_id:
            termek["nev"] = frissites.nev
            termek["ar"] = frissites.ar
            termek["leiras"] = frissites.leiras
            return termek
    raise HTTPException(status_code=404, detail="Termék nem található")

@app.delete("/termekek/{termek_id}", status_code=204)
def termek_torlese(termek_id: int):
    for i, termek in enumerate(termekek):
        if termek["id"] == termek_id:
            termekek.pop(i)
            return
    raise HTTPException(status_code=404, detail="Termék nem található")
```

---

## Gyakorlat

1. Készíts teljes CRUD API-t „Feladatok" (todo) témában
   - Pydantic modell: `cim`, `leiras` (opcionális), `kesz` (bool, alapértelmezett: False)
   - POST, GET (lista + egyedi), PUT, DELETE végpontok
   - Memóriában tárolt lista
2. Teszteld a Swagger UI-ban
3. Commitold és pushold
