# Kiegészítő gyakorlatok – 6. hét: Dependency Injection, Router, Config

> Ezek a feladatok a heti házi feladat melletti **extra gyakorlást** szolgálják.
> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz

---

### 6.1 – Nyelvi dependency ⭐
Készíts `get_language` dependency-t, amely az `Accept-Language` headerből kinyeri a nyelvet (alapértelmezett: `hu`). Használd 2 végpontban, hogy a válaszüzenetek a megfelelő nyelven szóljanak.

### 6.2 – Router tags és prefix ⭐⭐
Készíts 3 routert külön fájlokban: `routers/auth.py`, `routers/konyvek.py`, `routers/statisztikak.py`. Mindegyiknek legyen saját prefix-e és tag-je. A `/docs`-ban 3 külön szekció jelenjen meg.

### 6.3 – BaseSettings + .env ⭐⭐
Készíts `Settings` osztályt a következő konfigurációkkal:
- `database_url`, `secret_key`, `debug` (bool), `allowed_origins` (list[str])
- Használj `@lru_cache` mintát a `get_settings()` függvényben
- Készíts `.env.example` fájlt minden változóval
- Készíts `GET /config` végpontot, ami kilistázza a nem titkos beállításokat

### 6.4 – Class-based dependency ⭐⭐
Készíts `RateLimiter` osztályt, amit dependency-ként használhatsz:
```python
class RateLimiter:
    def __init__(self, max_requests: int, window_sec: int):
        ...
    def __call__(self, request: Request):
        ...
```
Használd különböző limitekkel: `Depends(RateLimiter(10, 60))` és `Depends(RateLimiter(100, 60))`.

### 6.5 – Plugin rendszer ⭐⭐⭐
Készíts moduláris alkalmazást, ahol minden "plugin" egy külön Python csomag:
```
app/
├── main.py
├── config.py
└── plugins/
    ├── __init__.py
    ├── users/       (router + dependency-k)
    └── products/    (router + dependency-k)
```
A `main.py` automatikusan regisztrálja az összes plugin routerjét. Minden plugin tartalmaz egy `router` változót és egy `setup()` függvényt.
