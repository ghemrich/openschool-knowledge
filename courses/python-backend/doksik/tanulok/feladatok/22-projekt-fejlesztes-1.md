# Feladatok – 22. hét: Projekt fejlesztés I.

> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz
> A megoldásokat commitold és pushold a GitHub repódba.

---

### 22.1 – Modellek ⭐⭐
Hozd létre az összes SQLAlchemy modellt `relationship()`-ekkel. Futtasd az Alembic migrációkat.

### 22.2 – Sémák ⭐⭐
Készítsd el a Pydantic sémákat: minden modellhez Create, Update (opcionális mezők), Response.

### 22.3 – CRUD modul ⭐⭐
Készítsd el a `crud/` modul összes függvényét: list, get_by_id, create, update, delete.

### 22.4 – Routerek ⭐⭐
Készítsd el a routereket: minden CRUD végpont működjön. Teszteld a Swagger UI-ban.

### 22.5 – Auth integráció ⭐⭐⭐
Adj hozzá auth-ot: regisztráció, login, JWT. A create/update/delete végpontok legyenek védettek. A felhasználó csak a saját elemeit módosíthassa/törölhesse. Commitold minden lépés után!
