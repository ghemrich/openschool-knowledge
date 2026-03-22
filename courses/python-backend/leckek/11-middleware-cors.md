# 📘 Lecke 11 – Middleware és CORS

> 📚 Dokumentáció:
> https://fastapi.tiangolo.com/tutorial/middleware/
> https://fastapi.tiangolo.com/tutorial/cors/
> https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS

---

## 67–68. óra: Middleware fogalma

### Mi a middleware?

A middleware egy "köztes réteg", amely **minden kérés előtt és/vagy után** lefut. Gondolj rá úgy, mint egy kapuőrre:

```
Kérés → [Middleware] → Útvonal (endpoint) → [Middleware] → Válasz
```

### 🧠 Részletes Magyarázat

- **Middleware** – Olyan kód, ami a kérés és a végpont között helyezkedik el. Minden HTTP kérésnél lefut, még mielőtt a végpont elérné. Utána is lefuthat, mielőtt a válasz visszamegy a klienshez.
- **Tipikus felhasználás:**
  - Naplózás (melyik végpontot hívták, mennyi ideig tartott)
  - Authentikáció ellenőrzés
  - Request ID hozzáadása
  - Hibakezelés
  - Válasz fejlécek hozzáadása
- **Különbség a dependency-vel:** A dependency végpontonként működik (amit `Depends()`-zel adunk meg). A middleware **minden** végpontra hat, globálisan.

### Egyedi middleware készítése

```python
# app/middleware.py
import time
from fastapi import Request

async def log_middleware(request: Request, call_next):
    start = time.time()
    response = await call_next(request)
    duration = time.time() - start
    print(f"{request.method} {request.url.path} - {response.status_code} ({duration:.3f}s)")
    return response
```

### 🧠 Részletes Magyarázat

- **`request: Request`** – A bejövő HTTP kérés objektuma. Tartalmazza a metódust (`GET`, `POST`), az URL-t, a fejléceket, a body-t, stb.
- **`call_next`** – A „következő lépés" a feldolgozási láncban. Meghívja a végpont függvényt (vagy a következő middleware-t), és visszaadja a választ. Ez a pont, ahol a tényleges munka történik.
- **`await call_next(request)`** – Az `await` az aszinkron hívás: megvárja, amíg a végpont lefut, és visszakapjuk a `response` objektumot.
- **Végrehajtási sorrend:**
  1. `start = time.time()` → **kérés előtt** (stopperóra indul)
  2. `response = await call_next(request)` → végpont lefut
  3. `duration = time.time() - start` → **válasz után** (stopperóra megáll)
  4. `print(...)` → naplózás
  5. `return response` → válasz továbbítása a kliensnek

### Middleware regisztrálása

```python
# app/main.py
from fastapi import FastAPI
from app.middleware import log_middleware

app = FastAPI()

@app.middleware("http")
async def add_logging(request, call_next):
    return await log_middleware(request, call_next)
```

### 🧠 Részletes Magyarázat

- **`@app.middleware("http")`** – Dekorátor, ami HTTP middleware-t regisztrál. A `"http"` paraméter a middleware típusa (jelenleg ez az egyetlen támogatott). Minden HTTP kérésnél lefut.
- **Sorrend:** Ha több middleware van, az **utoljára** regisztrált fut **elsőnek** (LIFO – Last In, First Out). Gondolj rá úgy, mint hagymarétegek: kívülről befelé haladunk.

### Gyakorlati middleware-ek

**Request ID middleware** – egyedi azonosító minden kéréshez:

```python
import uuid

@app.middleware("http")
async def add_request_id(request: Request, call_next):
    request_id = str(uuid.uuid4())
    response = await call_next(request)
    response.headers["X-Request-ID"] = request_id
    return response
```

### 🧠 Részletes Magyarázat

- **`uuid.uuid4()`** – Véletlenszerű, universally unique identifier (UUID). Gyakorlatilag lehetetlen, hogy két kérés ugyanazt az ID-t kapja. Formátum: `"550e8400-e29b-41d4-a716-446655440000"`.
- **`X-Request-ID`** – Egyedi fejléc a válaszban. Az `X-` előtag egyedi (nem szabványos) fejlécet jelöl. Hibakeresésnél hasznos: a kliens megkapja az ID-t, és a szerver naplóban is megjelenik → gyorsan megtaláljuk a problémás kérést.
- **`response.headers[...] = ...`** – A válasz fejléceihez adunk hozzá egy értéket. A middleware a válasz visszaküldése **előtt** módosíthatja a fejléceket.

---

## 69–70. óra: CORS

### Mi a CORS probléma?

A böngésző biztonsági okokból blokkolja a kéréseket, ha a frontend (pl. `http://localhost:3000`) más domainről kér adatot, mint az API (pl. `http://localhost:8000`).

### 🧠 Részletes Magyarázat

- **Same-Origin Policy** – A böngésző biztonsági szabálya: egy weboldalról csak az **azonos** origin-re (protokoll + domain + port) lehet kéréseket küldeni. Pl. a `http://localhost:3000` nem kérhet adatot a `http://localhost:8000`-ről (más port = más origin!).
- **CORS (Cross-Origin Resource Sharing)** – Egy mechanizmus, ami **lazítja** a Same-Origin szabályt. A szerver a válasz fejléceiben jelzi, hogy melyik origin-ekről fogad kéréseket. Ha a kliens origin-je szerepel a listán, a böngésző engedi a kérést.
- **Preflight request** – Bonyolultabb kéréseknél (POST JSON-nal, egyedi fejlécekkel) a böngésző először egy `OPTIONS` kérést küld, hogy lekérdezze: „Szabad-e ezt a kérést küldeni?" Ha a szerver megfelelő CORS fejlécekkel válaszol, csak akkor küldi a tényleges kérést.
- **Fontos:** Ez **csak böngészőkben** van! A Swagger UI, curl, Postman nem érintett – ők közvetlenül küldik a kéréseket.

### CORS beállítása FastAPI-ban

```python
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### 🧠 Részletes Magyarázat

- **`CORSMiddleware`** – FastAPI (Starlette) beépített middleware-e CORS kezelésre.
- **`allow_origins=origins`** – Azok a frontend URL-ek, ahonnan fogadunk kéréseket. A `http://localhost:3000` a React alapértelmezett portja, a `http://localhost:5173` a Vite-é.

| Paraméter | Jelentés | Ajánlás |
|-----------|----------|---------|
| `allow_origins` | Engedélyezett frontend URL-ek | Konkrét lista élesben |
| `allow_credentials` | Cookie-k/tokenek küldése | `True` ha auth kell |
| `allow_methods` | Engedélyezett HTTP metódusok | `["*"]` vagy konkrét lista |
| `allow_headers` | Engedélyezett kérés fejlécek | `["*"]` vagy konkrét lista |

### Miért nem `allow_origins=["*"]` éles környezetben?

Ha mindent engedélyezünk, bármelyik weboldal küldhet kérést az API-nkra. Élesben **mindig** konkrét domaineket adj meg, különösen ha `allow_credentials=True`.

### 🧠 Részletes Magyarázat

- **`["*"]` veszélye** – Ha `allow_origins=["*"]`, egy rosszindulatú weboldal (pl. `evil-site.com`) is küldhet kéréseket az API-nkra a felhasználó nevében. Ha `allow_credentials=True` is be van kapcsolva, a támadó hozzáférhet a felhasználó adataihoz.
- **Ajánlott megoldás élesben** – A `.env` fájlból olvasni az engedélyezett origin-eket:
```python
# .env
ALLOWED_ORIGINS=https://myapp.com,https://admin.myapp.com
```

---

## 71–72. óra: Haladó middleware minták

### Hibakezelő middleware

```python
from fastapi.responses import JSONResponse

@app.middleware("http")
async def error_handler(request: Request, call_next):
    try:
        response = await call_next(request)
        return response
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"detail": "Belső szerverhiba"}
        )
```

### 🧠 Részletes Magyarázat

- **Globális hibakezelő** – Ez a middleware elkapja a nem kezelt kivételeket, és egységes JSON választ ad vissza. Anélkül a szerver egy csúnya HTML hibaoldalt vagy stack trace-t adna, ami biztonsági kockázat (felfedi a belső struktúrát).
- **`except Exception as e`** – Minden kivételt elkap. Élesben érdemes naplózni a hibát (pl. `logging.error(str(e))`), majd a felhasználónak „Belső szerverhiba" üzenetet adni – a pontos hibaüzenet nem kerülhet a válaszba.

### Startup és shutdown események

```python
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Induláskor
    print("Alkalmazás elindult")
    yield
    # Leálláskor
    print("Alkalmazás leállt")

app = FastAPI(lifespan=lifespan)
```

### 🧠 Részletes Magyarázat

- **`lifespan`** – Az alkalmazás „életciklus" kezelője. A `yield` előtti rész az alkalmazás **indulásakor** fut (pl. adatbázis kapcsolat inicializálása, cache töltése), a `yield` utáni rész a **leállásakor** (pl. kapcsolatok bezárása, erőforrások felszabadítása).
- **`@asynccontextmanager`** – A Python dekorátora, ami `yield`-es generátor függvényből kontextuskezelőt csinál. A FastAPI lifespan ezt az interfészt várja.
- **Régi módszer (deprecated):** Korábban `@app.on_event("startup")` és `@app.on_event("shutdown")` volt, de ez elavult. A `lifespan` az új, ajánlott megoldás.

### Teljes main.py összefoglalás

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from app.routers import items, auth
from app.config import settings

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("API elindult")
    yield
    print("API leállt")

app = FastAPI(title=settings.app_name, lifespan=lifespan)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routerek
app.include_router(auth.router)
app.include_router(items.router)

@app.get("/")
def root():
    return {"message": "API fut"}
```

### 🧠 Részletes Magyarázat

Ez a `main.py` összefogja az alkalmazás minden elemét. A felépítés sorrendje:

1. **Importok** – Könyvtárak és saját modulok
2. **Lifespan** – Indulási/leállási logika
3. **App létrehozás** – `FastAPI()` a konfigurációval
4. **Middleware-ek** – CORS és egyéb middleware-ek
5. **Routerek** – `include_router()` hívások
6. **Gyökér végpont** – Health check (`GET /`)

- **`settings.allowed_origins`** – A CORS origin-ek a `.env` fájlból jönnek, nem a kódba vannak beégetve. Ez lehetővé teszi, hogy fejlesztésnél `localhost`-ot, élesben a tényleges domaint használjuk.
- **Health check (`GET /`)** – Egyszerű végpont, ami jelzi, hogy az API fut. Monitoring eszközök és load balancerek használják az alkalmazás állapotának ellenőrzésére.

---

## Gyakorlat

1. Adj hozzá naplózó middleware-t, amely kiírja a kérés módját, útvonalát és a válaszidőt
2. Konfigurálj CORS-t, hogy a `http://localhost:3000` frontend hozzáférjen
3. Hozz létre egy Request ID middleware-t
4. Használd a `lifespan` kontextuskezelőt indulási üzenethez
5. Commitold és pushold
