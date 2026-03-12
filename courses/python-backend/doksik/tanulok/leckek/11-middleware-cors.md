# Lecke 11 – Middleware és CORS

> **Dokumentáció:** [FastAPI Middleware](https://fastapi.tiangolo.com/tutorial/middleware/) · [CORS](https://fastapi.tiangolo.com/tutorial/cors/) · [MDN CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)

---

## 67–68. óra: Middleware fogalma

### Mi a middleware?

A middleware egy "köztes réteg", amely **minden kérés előtt és/vagy után** lefut. Gondolj rá úgy, mint egy kapuőrre:

```
Kérés → [Middleware] → Útvonal (endpoint) → [Middleware] → Válasz
```

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

---

## 69–70. óra: CORS

### Mi a CORS probléma?

A böngésző biztonsági okokból blokkolja a kéréseket, ha a frontend (pl. `http://localhost:3000`) más domainről kér adatot, mint az API (pl. `http://localhost:8000`).

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

### Miért nem `allow_origins=["*"]` éles környezetben?

Ha mindent engedélyezünk, bármelyik weboldal küldhet kérést az API-nkra. Élesben **mindig** konkrét domaineket adj meg, különösen ha `allow_credentials=True`.

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

---

## Gyakorlat

1. Adj hozzá naplózó middleware-t, amely kiírja a kérés módját, útvonalát és a válaszidőt
2. Konfigurálj CORS-t, hogy a `http://localhost:3000` frontend hozzáférjen
3. Hozz létre egy Request ID middleware-t
4. Használd a `lifespan` kontextuskezelőt indulási üzenethez
5. Commitold és pushold
