# 📘 Lecke 04 – Request body és Pydantic

> 📚 Dokumentáció:
> https://docs.pydantic.dev/
> https://fastapi.tiangolo.com/tutorial/body/
> https://fastapi.tiangolo.com/tutorial/body-fields/

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

### 🧠 Részletes Magyarázat

- **`BaseModel`** – A Pydantic alaposztálya. Minden osztály, ami ebből öröklődik, automatikusan kap adatvalidálást, típuskonverziót és JSON szerializálást. Lényegében egy „okos adatcsomag", ami ellenőrzi saját magát.
- **`Field()`** – Mezőszintű validációs szabályok és metaadatok megadására szolgál. A fontosabb paraméterek:

| Paraméter | Jelentés | Példa |
|-----------|----------|-------|
| `min_length` | Szöveg minimális hossza | `Field(min_length=1)` |
| `max_length` | Szöveg maximális hossza | `Field(max_length=100)` |
| `gt` | Nagyobb mint (greater than) | `Field(gt=0)` → nem lehet 0 |
| `ge` | Nagyobb vagy egyenlő | `Field(ge=0)` → lehet 0 |
| `lt` / `le` | Kisebb / kisebb-egyenlő | `Field(lt=100)` |
| `default` | Alapértelmezett érték | `Field(default=None)` |
| `description` | Swagger UI leírás | `Field(description="Ár Ft-ban")` |

- **`Optional[str]`** – Azt jelenti, hogy a mező értéke `str` vagy `None` lehet. Ha van `default=None`, akkor **nem kötelező** megadni.
- **Kötelező vs. opcionális mező** – Ha nincs alapértelmezés, a mező kötelező. Ha van (`default=...` vagy `Optional` + `None`), opcionális.

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

### 🧠 Részletes Magyarázat

- **`422 Unprocessable Entity`** – Ez a HTTP státuszkód azt jelenti: „Megértettem a kérésed formátumát (érvényes JSON), de az adatok tartalmilag hibásak." A FastAPI + Pydantic páros automatikusan ezt a kódot adja vissza, ha a validáció sikertelen.
- **Automatikus hibaüzenet** – A Pydantic részletes JSON-t ad vissza a hiba okáról, pl. melyik mező hibás és miért. Nem kell kézzel írni a hibakezelést, a rendszer magától megoldja.

### Beágyazott modellek

```python
class Cim(BaseModel):
    varos: str
    utca: str
    iranyitoszam: str

class Felhasznalo(BaseModel):
    nev: str
    email: str
    cim: Cim  # Beágyazott modell
```

### 🧠 Részletes Magyarázat

- **Beágyazott modell (nested model)** – Egy Pydantic modell mezője lehet egy másik Pydantic modell. Ilyenkor a JSON-ban is beágyazott objektumot kell küldeni:
```json
{
  "nev": "Kiss Béla",
  "email": "bela@example.com",
  "cim": {
    "varos": "Budapest",
    "utca": "Fő utca 1",
    "iranyitoszam": "1011"
  }
}
```
- **Láncos validáció** – A `Felhasznalo` modell validálásakor a `Cim` modell is automatikusan validálódik. Ha az `iranyitoszam` hiányzik, a teljes kérés 422-vel elutasítódik.

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

### 🧠 Részletes Magyarázat

- **Request body** – A HTTP kérés „törzse", ami JSON formátumú adatot tartalmaz. POST és PUT kéréseknél a kliens így küldi el az új/módosított adatokat. FastAPI automatikusan felismeri, hogy ha egy függvény paramétere Pydantic modell típusú, az a request body-ból jön.
- **`status_code=201`** – A `201 Created` státuszkód jelzi, hogy sikeresen létrejött egy új erőforrás a szerveren. POST végpontoknál ez az ajánlott válaszkód (nem 200).
- **`global kovetkezo_id`** – A Python globális változót a függvényen belül módosítani csak a `global` kulcsszóval lehet. Ez egy egyszerű ID-generátor, ami minden új elemnél eggyel nő. Adatbázissal később automatikus lesz (auto-increment).
- **`termek.nev`** – A Pydantic modell mezőit pont-operátorral érjük el (nem szögletes zárójellel, mint egy dict-et). A modell validálja az adatot, majd Python objektumként használható.
- **In-memory tárolás** – A `termekek = []` lista a szerver memóriájában él. Ha a szerver újraindul, minden adat elveszik. Ez csak fejlesztési célokra jó, éles alkalmazásban adatbázist használunk.

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

### 🧠 Részletes Magyarázat

Ez a kód egy teljes **CRUD** (Create, Read, Update, Delete) API-t valósít meg:

| Művelet | HTTP metódus | Végpont | Státuszkód |
|---------|-------------|---------|------------|
| Listázás | `GET` | `/termekek/` | 200 |
| Lekérés | `GET` | `/termekek/{id}` | 200 / 404 |
| Létrehozás | `POST` | `/termekek/` | 201 |
| Módosítás | `PUT` | `/termekek/{id}` | 200 / 404 |
| Törlés | `DELETE` | `/termekek/{id}` | 204 / 404 |

- **`HTTPException`** – FastAPI beépített hibaosztálya. A `raise HTTPException(status_code=404, ...)` azonnal megszakítja a függvény futását és JSON hibaüzenetet küld a kliensnek: `{"detail": "Termék nem található"}`.
- **`raise` vs. `return`** – A `return` normális választ küld, a `raise` hibát dob. A `raise HTTPException` kifejezetten HTTP hibát jelent, ami a megfelelő státuszkóddal tér vissza.
- **PUT logika** – A `termek_modositasa` függvény két paramétert kap: `termek_id` az URL-ből (path paraméter), `frissites` a request body-ból (Pydantic modell). A FastAPI automatikusan felismeri, melyik honnan jön.
- **`enumerate(termekek)`** – A DELETE-nél az indexre is szükségünk van (a `pop(i)` miatt), ezért `enumerate`-et használunk, ami `(index, elem)` párokat ad.
- **`status_code=204`** – A `204 No Content` státuszkódot DELETE-nél használjuk. Azt jelenti: „Sikeres volt a művelet, de nincs visszaküldendő adat." Ilyenkor a `return` üres (nincs adat a válaszban).

---

## Gyakorlat

1. Készíts teljes CRUD API-t „Feladatok" (todo) témában
   - Pydantic modell: `cim`, `leiras` (opcionális), `kesz` (bool, alapértelmezett: False)
   - POST, GET (lista + egyedi), PUT, DELETE végpontok
   - Memóriában tárolt lista
2. Teszteld a Swagger UI-ban
3. Commitold és pushold
