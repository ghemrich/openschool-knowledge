# 📘 Lecke 05 – Response modellek és hibakezelés

> 📚 Dokumentáció:
> https://fastapi.tiangolo.com/tutorial/response-model/
> https://fastapi.tiangolo.com/tutorial/handling-errors/

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

### 🧠 Részletes Magyarázat

- **`response_model=TermekValasz`** – A dekorátor paramétere meghatározza, hogy a válasz milyen formátumú legyen. A FastAPI a visszaadott adatot átszűri ezen a modellen: csak azok a mezők jelennek meg a válaszban, amelyek a `TermekValasz`-ban definiálva vannak. Ha extra mezők vannak (pl. jelszó), azok automatikusan kiesnek.
- **`model_dump()`** – A Pydantic v2 metódusa, ami a modellt Python dict-té alakítja. Korábban (v1) `.dict()` volt a neve. Ez visszaadja a mező-érték párokat: `{"nev": "Laptop", "ar": 299990.0, "leiras": None}`.
- **`**termek.model_dump()`** – A `**` (double star / unpack) operátor „kicsomagolja" a dict tartalmát. Így az `{"id": 1, **termek.model_dump()}` egyenértékű ezzel: `{"id": 1, "nev": "Laptop", "ar": 299990.0, "leiras": None}`.
- **Miért két modell?** – A `TermekLetrehozas` azt írja le, mit **küld** a kliens (nincs benne `id`, mert azt a szerver generálja). A `TermekValasz` azt írja le, mit **kap vissza** a kliens (benne van az `id`). Ez a szétválasztás az API tervezés legjobb gyakorlata.

### Különböző sémák – biztonsági szűrés

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

### 🧠 Részletes Magyarázat

- **Séma szétválasztás (Input vs. Output)** – A `FelhasznaloLetrehozas` tartalmazza a jelszót (mert a regisztráláskor szükség van rá), de a `FelhasznaloValasz` nem (mert soha nem szabad visszaküldeni). A `response_model` biztosítja, hogy még ha a belső dict-ben benne is van a jelszó, a válaszban nem jelenik meg.
- **Általános minta:**

| Séma típus | Elnevezés | Tartalom |
|-----------|-----------|----------|
| Input (POST) | `XxxCreate` / `XxxLetrehozas` | Amit a kliens küld (jelszó, adatok) |
| Input (PUT) | `XxxUpdate` / `XxxModositas` | Amit a kliens módosíthat |
| Output | `XxxResponse` / `XxxValasz` | Amit a kliens visszakap (id, de jelszó nélkül) |

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

### 🧠 Részletes Magyarázat

- **`status` modul** – A `fastapi.status` (valójában `starlette.status`) modul konstansokat tartalmaz a HTTP státuszkódokhoz. A `status.HTTP_201_CREATED` ugyanaz, mint a `201`, de olvashatóbb és „önleíró" – a kódból egyértelmű, mit jelent.
- **Gyakori státuszkódok és mikor használjuk őket:**

| Kód | Konstans | Jelentés | Mikor |
|-----|----------|----------|-------|
| 200 | `HTTP_200_OK` | Sikeres | GET, PUT alapértelmezett |
| 201 | `HTTP_201_CREATED` | Létrehozva | POST után |
| 204 | `HTTP_204_NO_CONTENT` | Tartalom nélkül | DELETE után |
| 400 | `HTTP_400_BAD_REQUEST` | Hibás kérés | Üzleti logika hiba |
| 404 | `HTTP_404_NOT_FOUND` | Nem található | Nincs ilyen erőforrás |
| 422 | `HTTP_422_UNPROCESSABLE_ENTITY` | Feldolgozhatatlan | Validációs hiba |

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

### 🧠 Részletes Magyarázat

- **`HTTPException`** – FastAPI beépített kivételosztálya. Amikor `raise`-zel dobjuk, a FastAPI automatikusan JSON választ ad a megadott státuszkóddal. A kliens ezt kapja:
```json
{
  "detail": "Elem nem található"
}
```
- **`raise` és a futás megszakítása** – A `raise HTTPException(...)` után a függvény nem fut tovább. Nem kell `else` ágat írni, mert ha a `raise` végrehajtódik, a `return item` sor sosem érhető el. Ez tisztább kódot eredményez, mint az `if-else` szerkezet.
- **`if not item`** – Ha az `item` értéke `None` (nem találtunk ilyet), a `not None` igaz, tehát belépünk az `if` blokkba és hibát dobunk.

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

### 🧠 Részletes Magyarázat

- **Egyedi exception osztály** – A `NemTalalhatoHiba(Exception)` egy saját hibaosztály, ami a Python beépített `Exception`-ből öröklődik. Azért hozzuk létre, mert testre szabott hibakezelést akarunk (pl. más JSON formátum, naplózás, stb.).
- **`@app.exception_handler()`** – Ez a dekorátor regisztrál egy függvényt, ami minden alkalommal lefut, amikor a megadott típusú kivétel keletkezik. A FastAPI elkapja a `NemTalalhatoHiba`-t, és meghívja a kezelő függvényt ahelyett, hogy 500-as hibát adna.
- **`JSONResponse`** – Alacsony szintű válaszobjektum, amivel teljes mértékben kontroláljuk a válasz tartalmát és státuszkódját. A `content` paraméter automatikusan JSON-ná alakul.
- **`async def`** – Aszinkron függvény. A FastAPI kezelői lehetnek `async` vagy szinkron (`def`) is. Az exception handlerek ajánlottan `async`, de a gyakorlatban mindkettő működik.
- **Mikor használjunk egyedi hibakezelőt?** – Ha az alkalmazás egészében egységes hibaformátumot akarunk (pl. `{"hiba": "...", "kod": "..."}` az alap `{"detail": "..."}` helyett), vagy ha naplózni akarjuk a hibákat.

---

## 35–36. óra: Validációs hibák testreszabása

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

### 🧠 Részletes Magyarázat

- **`RequestValidationError`** – Ez a FastAPI beépített kivétele, ami akkor keletkezik, ha a Pydantic validáció sikertelen (pl. hiányzó mező, rossz típus, szabálysértés). Alapértelmezetten a FastAPI egy részletes, de nem mindig olvasható hibaüzenetet ad.
- **`exc.errors()`** – Visszaadja a validációs hibák listáját. Minden hiba tartalmazza: melyik mező (`loc`), milyen hiba (`type`), és mi az üzenet (`msg`). Például:
```json
[
  {
    "loc": ["body", "ar"],
    "msg": "Input should be greater than 0",
    "type": "greater_than"
  }
]
```
- **Testreszabás célja** – Az alapértelmezett hibaformátum angolul van és túl technikai lehet az API fogyasztói számára. Egy egyedi kezelővel átformázhatjuk, lefordíthatjuk magyarra, vagy egyszerűsíthetjük a választ.

---

## Gyakorlat

1. Bővítsd a feladatkezelő (todo) API-t:
   - Készíts külön sémákat: `TodoCreate`, `TodoUpdate`, `TodoResponse`
   - Adj `response_model`-t minden végponthoz
   - Kezeld a 404 hibát, ha nem létezik a feladat
   - Kezeld a 400 hibát, ha üres a cím
2. Teszteld a hibás kéréseket is a Swagger UI-ban
3. Commitold és pushold
