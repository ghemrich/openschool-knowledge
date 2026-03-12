# Feladatok – 9. hét: CRUD műveletek

> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz
> A megoldásokat commitold és pushold a GitHub repódba.

---

### 9.1 – get_db dependency ⭐
Hozd létre a `get_db` generátor függvényt `yield`-del. Használd `Depends(get_db)`-ként egy végpontban, amely kiírja, hogy "DB kapcsolat OK".

### 9.2 – CRUD modul ⭐⭐
Készíts `crud.py` modult a `Konyv` modellhez a következő függvényekkel: `get_konyvek(db, skip, limit)`, `get_konyv(db, id)`, `create_konyv(db, konyv)`, `delete_konyv(db, id)`.

### 9.3 – Pydantic sémák ⭐⭐
Hozz létre `schemas.py`-t a következő sémákkal: `KonyvBase`, `KonyvCreate(KonyvBase)`, `KonyvResponse(KonyvBase)` (id-vel, `from_attributes = True`). Használd a routerben `response_model`-ként.

### 9.4 – Teljes CRUD router ⭐⭐
Készíts teljes CRUD routert: `GET /konyvek`, `GET /konyvek/{id}`, `POST /konyvek`, `PUT /konyvek/{id}`, `DELETE /konyvek/{id}`. Minden végpont a `crud.py` függvényeit használja.

### 9.5 – Keresés és szűrés ⭐⭐⭐
Adj hozzá keresési lehetőséget: `GET /konyvek?kereses=python` – a cím vagy szerző alapján szűr. Használj SQLAlchemy `filter()` és `ilike()` metódusokat.
