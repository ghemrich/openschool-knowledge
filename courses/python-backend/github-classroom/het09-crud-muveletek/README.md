# 9. hét – CRUD műveletek adatbázissal

> **Határidő:** a következő óra előtt
> **Beadás:** commitold és pushold a megoldásaidat ebbe a repóba!
> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz

---

Ezen a héten megvalósítod a CRUD (Create, Read, Update, Delete) műveleteket adatbázissal. Ezek a legalapvetőbb adatkezelési műveletek, amik szinte minden webes alkalmazásban megtalálhatók.

---

## 9.1 – Sémák ⭐
Készíts `schemas.py`-t: `KonyvBase`, `KonyvCreate(KonyvBase)`, `KonyvResponse(KonyvBase)` (id-vel, `from_attributes = True`).

## 9.2 – CRUD modul ⭐⭐
Készíts `crud.py`-t: `get_konyvek(db, skip, limit)`, `get_konyv(db, id)`, `create_konyv(db, konyv)`, `update_konyv(db, id, konyv)`, `delete_konyv(db, id)`.

## 9.3 – Router ⭐⭐
Készíts `routers/konyvek.py`-t teljes CRUD-dal:
- `GET /konyvek` – listázás (skip, limit)
- `GET /konyvek/{id}` – egy könyv (404)
- `POST /konyvek` – létrehozás (201)
- `PUT /konyvek/{id}` – módosítás
- `DELETE /konyvek/{id}` – törlés

## 9.4 – Keresés ⭐⭐
Adj `kereses` query paramétert a `GET /konyvek` végponthoz. Szűrjön cím és szerző alapján (`ilike`).

## 9.5 – Teljes API ⭐⭐⭐
Integráld a teljes alkalmazást: `main.py` → router → crud → database. Indítsd Docker Compose-zal és teszteld a Swagger UI-ban. Minden CRUD művelet működjön.

---

## Dokumentáció

- [FastAPI SQL Databases](https://fastapi.tiangolo.com/tutorial/sql-databases/)
- [Pydantic Model Config](https://docs.pydantic.dev/latest/concepts/config/)
- [SQLAlchemy Query](https://docs.sqlalchemy.org/en/20/orm/queryguide/)

## 📚 Kapcsolódó anyagok

Az ehhez a héthez tartozó elméleti anyagot és további gyakorlófeladatokat itt találod:

- 📖 [Lecke: CRUD műveletek](../../doksik/tanulok/leckek/09-crud-muveletek.md)
- 📝 [Gyakorlófeladatok: CRUD műveletek](../../doksik/tanulok/feladatok/09-crud-muveletek.md)

## Beadás

1. `schemas.py`, `crud.py`, `routers/` legyen a repóban
2. Commitolj értelmes üzenetekkel
3. `git push` – ez a beadás!
