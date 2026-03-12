# Feladatok – 6. hét: Dependency Injection, Router, Config

> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz
> A megoldásokat commitold és pushold a GitHub repódba.

---

### 6.1 – Egyszerű dependency ⭐
Készíts egy `common_params` függvényt ami `skip` és `limit` query paramétereket fogad, és használd `Depends()`-szel két különböző végpontban.

### 6.2 – APIRouter ⭐⭐
Szervezd szét a végpontokat: `routers/termekek.py` és `routers/felhasznalok.py`. Használj `APIRouter(prefix=..., tags=[...])` mindkettőhöz. Regisztráld őket a `main.py`-ban.

### 6.3 – Konfiguráció ⭐⭐
Hozz létre `config.py`-t `BaseSettings` osztállyal. Kezeld a következő beállításokat: `app_name`, `debug`, `api_prefix`. Készíts `.env` és `.env.example` fájlokat.

### 6.4 – Dependency chaining ⭐⭐
Készíts két egymásra épülő dependency-t: `get_settings()` → `get_api_key(settings)`. A `get_api_key` ellenőrzi, hogy a kérés `X-API-Key` headerje megegyezik-e a beállított kulccsal. Ha nem, 401-et dob.

### 6.5 – Teljes projekt struktúra ⭐⭐⭐
Készítsd el a teljes projekt struktúrát:
```
app/
├── __init__.py
├── main.py
├── config.py
├── dependencies.py
└── routers/
    ├── __init__.py
    ├── termekek.py
    └── felhasznalok.py
```
Az `app/main.py` csak az app-ot hozza létre és regisztrálja a routereket. A végpontok a `routers/` mappában legyenek. Commitold és pushold.
