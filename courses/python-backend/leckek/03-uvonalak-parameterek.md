# 📘 Lecke 03 – Útvonalak és paraméterek

> 📚 Dokumentáció:  
> https://fastapi.tiangolo.com/tutorial/path-params/ ·  
> https://fastapi.tiangolo.com/tutorial/query-params/

---

# 19–20. óra: Path paraméterek

A path paraméter az URL **útvonalában** van, kapcsos zárójelek között:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id, "nev": f"Termék #{item_id}"}
```

Hívás: `GET /items/42` → `{"item_id": 42, "nev": "Termék #42"}`

### 🧠 Részletes Magyarázat

**Path paraméter** – Az URL egy dinamikus része. A `{item_id}` az útvonalban megfelel a függvény `item_id` paraméterének.

```
URL:      /items/42
            ↓
Minta:    /items/{item_id}
            ↓
Függvény: def get_item(item_id: int)
            ↓
item_id = 42
```

A FastAPI automatikusan:
1. Kiszedi az URL-ből az értéket
2. Konvertálja a megadott típusba (`int`)
3. Átadja a függvénynek paraméterként

---

## 🔒 Típusmegkötés

A típus automatikusan ellenőrzésre kerül:

```python
@app.get("/users/{user_id}")
def get_user(user_id: int):    # Csak egész szám!
    return {"user_id": user_id}
```

`GET /users/abc` → `422 Unprocessable Entity`

### 🧠 Részletes Magyarázat

Ha a type hint `int`, a FastAPI automatikusan:
- ✅ `/users/42` → Elfogadja, `user_id = 42`
- ✅ `/users/1` → Elfogadja
- ❌ `/users/abc` → Elutasítja: 422-es hibával, részletes hibaüzenettel

Ez az **automatikus validáció** – nem kell kézzel ellenőrizni! A FastAPI a type hint-ek alapján csinálja.

---

## 📋 Enum típusú paraméterek

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

### 🧠 Részletes Magyarázat

**Enum** – Felsorolás típus. Előre meghatározott értékek közül választhat a kliens. Ha más értéket küld, 422-es hibát kap.

```python
class Kategoria(str, Enum):  # str + Enum = szöveges felsorolás
    akcio = "akció"           # A "akcio" a kulcs, "akció" az érték
    drama = "dráma"
```

- `GET /filmek/akcio` → ✅ `{"kategoria": "akció"}`
- `GET /filmek/horror` → ❌ 422 hiba (nincs ilyen enum érték)

A Swagger UI-ban legördülő menüként jelenik meg – a kliens csak érvényes értéket tud választani!

---

# 21–22. óra: Query paraméterek

A query paraméterek az URL-ben a `?` után jönnek:

```python
from typing import Optional

@app.get("/items/")
def list_items(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}
```

Hívás: `GET /items/?skip=5&limit=20`

### 🧠 Részletes Magyarázat

**Query paraméter** – Az URL `?` jele utáni kulcs=érték párok. Több paramétert `&`-vel választunk el.

```
URL: /items/?skip=5&limit=20
              ↓         ↓
Függvény: list_items(skip: int = 0, limit: int = 10)
              ↓         ↓
          skip = 5, limit = 20
```

**Path vs Query:**
| | Path | Query |
|-|------|-------|
| Hol? | URL-ben: `/items/42` | URL után: `/items/?limit=10` |
| Mire? | Erőforrás azonosítás | Szűrés, lapozás, rendezés |
| Kötelező? | Mindig kötelező | Lehet opcionális |

**Alapértelmezett érték** – A `skip: int = 0` azt jelenti: ha a kliens nem adja meg, az alapérték 0. `GET /items/` → `skip=0, limit=10`.

---

## ❓ Opcionális paraméterek

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

### 🧠 Részletes Magyarázat

**Optional[str]** – A paraméter lehet `str` vagy `None`. Az `= None` alapértték jelzi, hogy opcionális.

```python
GET /kereso/                        → q=None, kategoria=None
GET /kereso/?q=python               → q="python", kategoria=None
GET /kereso/?q=python&kategoria=it  → q="python", kategoria="it"
```

---

## ✅ Validáció Query-vel

```python
from fastapi import Query

@app.get("/kereso/")
def kereses(
    q: str = Query(min_length=3, max_length=50, description="Keresőkifejezés"),
    limit: int = Query(default=10, ge=1, le=100, description="Max találatok")
):
    return {"q": q, "limit": limit}
```

### 🧠 Részletes Magyarázat

**Query()** – Részletes validációs szabályokat adhatunk meg:

| Paraméter | Jelentés | Példa |
|-----------|----------|-------|
| `min_length` | Minimum szöveghossz | `min_length=3` |
| `max_length` | Maximum szöveghossz | `max_length=50` |
| `ge` | Greater or equal (≥) | `ge=1` (min. 1) |
| `le` | Less or equal (≤) | `le=100` (max. 100) |
| `description` | Swagger-ben megjelenő leírás | |

Ha a kliens érvénytelen adatot küld, automatikusan 422-es hibát kap részletes hibaüzenettel.

---

# 23–24. óra: Path + Query kombinálása

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

### 🧠 Részletes Magyarázat

Egy végpont tartalmazhat **path ÉS query** paramétereket egyszerre. A FastAPI automatikusan megkülönbözteti:
- Ha a paraméter neve szerepel az URL-mintában (`{kategoria_id}`) → **path paraméter**
- Ha nem szerepel → **query paraméter**

```python
@app.get("/kategoriak/{kategoria_id}/termekek/")
def termekek_kategoriaban(
    kategoria_id: int,     # Path: az URL-ben van
    rendez: str = "nev",   # Query: nincs az URL-mintában
    novekvo: bool = True,  # Query
    limit: int = ...       # Query
):
```

---

## ✏️ Gyakorlat

1. Készíts egy „Terméklistázó" API-t:
   - `GET /termekek/` – összes termék (skip, limit query paraméterekkel)
   - `GET /termekek/{termek_id}` – egy termék az ID alapján
   - `GET /kategoriak/{kategoria}/termekek/` – termékek kategória szerint
2. Teszteld a Swagger UI-ban
3. Commitold és pushold
