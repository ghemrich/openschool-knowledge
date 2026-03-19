# Kiegészítő gyakorlatok – 9. hét: CRUD műveletek

> Ezek a feladatok a heti házi feladat melletti **extra gyakorlást** szolgálják.
> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz

---

### 9.1 – Generáló függvény ⭐
Készíts `seed.py` scriptet, ami generál 20 minta adatot (pl. filmeket vagy termékeket) az adatbázisba. Használd a `get_db` generátort a sessionhöz.

### 9.2 – Szűrés és rendezés ⭐⭐
Bővítsd a listázó végpontot:
- `q` query param: szöveges keresés (cím ILIKE)
- `rendezés` query param (Enum: nev_asc, nev_desc, datum_asc, datum_desc)
- `min_ar` / `max_ar` q paraméterek árszűréshez

Használd a `query.filter()` és `query.order_by()` metódusokat.

### 9.3 – Lapozás metaadatokkal ⭐⭐
Készíts lapozó választ:
```json
{
  "elemek": [...],
  "osszes": 47,
  "oldal": 2,
  "oldalak_szama": 5,
  "meret": 10
}
```
Használd a `db.query().count()` és `.offset().limit()` metódusokat.

### 9.4 – Soft delete ⭐⭐
Ahelyett, hogy törölnéd a rekordot, adj hozzá egy `torolve_mikor: datetime | None` mezőt. A `DELETE` végpont csak beállítja ezt az értéket. A listázó végpont alapértelmezésben nem mutatja a "törölt" elemeket, de `torolt=true` query paraméterrel igen.

### 9.5 – Bulk műveletek ⭐⭐⭐
Készíts bulk végpontokat:
- `POST /elemek/bulk` – több elem létrehozása egyszerre (list[ElemCreate])
- `DELETE /elemek/bulk` – több elem törlése ID lista alapján
- `PATCH /elemek/bulk` – több elem módosítása egyszerre

Használj `db.bulk_save_objects()` vagy tranzakciós kezelést.
