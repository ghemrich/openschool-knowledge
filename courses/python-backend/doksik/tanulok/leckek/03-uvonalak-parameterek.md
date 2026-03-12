# Lecke 03 – Útvonalak és paraméterek

> **Dokumentáció:** [FastAPI Path Parameters](https://fastapi.tiangolo.com/tutorial/path-params/) · [Query Parameters](https://fastapi.tiangolo.com/tutorial/query-params/)

---

## 19–20. óra: Path paraméterek

A path paraméter az URL **útvonalában** van, kapcsos zárójelek között:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id, "nev": f"Termék #{item_id}"}
```

Hívás: `GET /items/42` → `{"item_id": 42, "nev": "Termék #42"}`

### Típusmegkötés

A típus automatikusan ellenőrzésre kerül:

```python
@app.get("/users/{user_id}")
def get_user(user_id: int):    # Csak egész szám!
    return {"user_id": user_id}
```

`GET /users/abc` → `422 Unprocessable Entity`

### Enum típusú paraméterek

```python
from enum import Enum

class Kategoria(str, Enum):
    akcio = "akció"
    drama = "dráma"
    vigjatek = "vígjáték"

@app.get("/filmek/{kategoria}")
def filmek_kategoria(kategoria: Kategoria):
    return {"kategoria": kategoria.value}
```

---

## 21–22. óra: Query paraméterek

A query paraméterek az URL-ben a `?` után jönnek:

```python
from typing import Optional

@app.get("/items/")
def list_items(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}
```

Hívás: `GET /items/?skip=5&limit=20`

### Opcionális paraméterek

```python
@app.get("/kereso/")
def kereses(q: Optional[str] = None, kategoria: Optional[str] = None):
    results = {"items": []}
    if q:
        results["q"] = q
    if kategoria:
        results["kategoria"] = kategoria
    return results
```

### Validáció Query-vel

```python
from fastapi import Query

@app.get("/kereso/")
def kereses(
    q: str = Query(min_length=3, max_length=50, description="Keresőkifejezés"),
    limit: int = Query(default=10, ge=1, le=100, description="Max találatok")
):
    return {"q": q, "limit": limit}
```

---

## 23–24. óra: Path + Query kombinálása

```python
@app.get("/kategoriak/{kategoria_id}/termekek/")
def termekek_kategoriaban(
    kategoria_id: int,
    rendez: str = "nev",
    novekvo: bool = True,
    limit: int = Query(default=10, ge=1, le=100)
):
    return {
        "kategoria_id": kategoria_id,
        "rendez": rendez,
        "novekvo": novekvo,
        "limit": limit
    }
```

Hívás: `GET /kategoriak/3/termekek/?rendez=ar&novekvo=false&limit=5`

---

## Gyakorlat

1. Készíts egy „Terméklistázó" API-t:
   - `GET /termekek/` – összes termék (skip, limit query paraméterekkel)
   - `GET /termekek/{termek_id}` – egy termék az ID alapján
   - `GET /kategoriak/{kategoria}/termekek/` – termékek kategória szerint
2. Teszteld a Swagger UI-ban
3. Commitold és pushold
