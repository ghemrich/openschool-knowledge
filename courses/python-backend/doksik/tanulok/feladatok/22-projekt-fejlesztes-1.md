# Kiegészítő gyakorlatok – 22. hét: Projekt fejlesztés I.

> Ezek a feladatok a heti házi feladat melletti **extra gyakorlást** szolgálják.
> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz

---

### 22.1 – Git workflow ⭐⭐
Használj feature branch-eket a fejlesztéshez:
- `feature/models` – SQLAlchemy modellek
- `feature/schemas` – Pydantic sémák
- `feature/crud` – CRUD műveletek

Mindegyiket merge-öld a `main`-be külön-külön. A `git log --oneline --graph` mutasson szép történetet.

### 22.2 – Seed adatok ⭐⭐
Készíts `scripts/seed.py` scriptet, ami legalább 20 minta adattal tölti fel az adatbázist (felhasználók, elemek, kapcsolatok). Legyen futtatható külső scriptkent: `python -m scripts.seed`.

### 22.3 – Logging ⭐⭐
Adj be Python `logging`-ot az alkalmazásba:
- CRUD műveleteknknél: `logger.info("Könyv létrehozva: %s", konyv.cim)`
- Hibáknál: `logger.error("Nem található: %s", id)`
- Auth-nál: `logger.warning("Sikertelen login: %s", email)`

Konfiguráld a log szintet környezeti változóval (`LOG_LEVEL=DEBUG`).

### 22.4 – Swagger testreszabás ⭐⭐
Testreszabd a Swagger dokumentlációt:
- `title`, `description`, `version`
- Végpont leírások (`summary` és `description`)
- Response példák (`responses` paraméterrel)
- Tag-ek csoportosítása

### 22.5 – Code review checklist ⭐⭐⭐
Nézd át a teljes kódot az alábbi checklist szerint:
- [ ] Minden végpont helyes status kódot ad vissza
- [ ] Minden végpont használ response_model-t
- [ ] Nincs hardcoded érték (titkok a config-ból jönnek)
- [ ] Minden CRUD függvény kezeli a "nem található" esetet
- [ ] Az auth dependency minden védett végponton rajta van
- [ ] A .env.example tartalmazza az összes szükséges változót

Dokumentáld a talált problémákat és javítsd ki őket.
