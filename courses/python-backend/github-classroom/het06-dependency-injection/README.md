# 6. hét – Dependency Injection, Router, Config

> **Határidő:** a következő óra előtt
> **Beadás:** commitold és pushold a megoldásaidat ebbe a repóba!
> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz

---

Ezen a héten megismerkedsz a Dependency Injection mintával, az APIRouter-rel és a konfigurációkezeléssel. Ezek segítségével a kódodat modulokra bonthatod és könnyebben karbantarthatóvá teheted.

---

## 6.1 – Dependency ⭐
Készíts `common_params(skip, limit)` dependency-t. Használd `Depends()`-szel két végpontban.

## 6.2 – APIRouter ⭐⭐
Szervezd ki a termék végpontokat `routers/termekek.py`-ba `APIRouter`-rel. Regisztráld a `main.py`-ban `include_router`-rel.

## 6.3 – Config ⭐⭐
Készíts `config.py`-t `BaseSettings` osztállyal (`app_name`, `debug`). Hozd létre az `.env` és `.env.example` fájlokat. Használd a configot a `main.py`-ban.

## 6.4 – Projekt struktúra ⭐⭐
Szervezd a kódot `app/` csomagba:
```
app/
├── __init__.py
├── main.py
├── config.py
├── dependencies.py
└── routers/
    ├── __init__.py
    └── termekek.py
```

## 6.5 – API Key védelem ⭐⭐⭐
Készíts `get_api_key` dependency-t, amely ellenőrzi az `X-API-Key` headert. Ha nem egyezik a config-ban tárolt kulccsal, 401-et dob. Védj vele egy végpontot.

---

## Dokumentáció

- [Dependencies](https://fastapi.tiangolo.com/tutorial/dependencies/)
- [Bigger Applications](https://fastapi.tiangolo.com/tutorial/bigger-applications/)
- [Settings](https://fastapi.tiangolo.com/advanced/settings/)

## 📚 Kapcsolódó anyagok

Az ehhez a héthez tartozó elméleti anyagot és további gyakorlófeladatokat itt találod:

- 📖 [Lecke: Dependency Injection](../../doksik/tanulok/leckek/06-dependency-injection.md)
- 📝 [Gyakorlófeladatok: Dependency Injection](../../doksik/tanulok/feladatok/06-dependency-injection.md)

## Beadás

1. Az `app/` csomag struktúra legyen a repóban
2. `.env.example` legyen benne (`.env` ne!)
3. Commitolj értelmes üzenetekkel
4. `git push` – ez a beadás!
