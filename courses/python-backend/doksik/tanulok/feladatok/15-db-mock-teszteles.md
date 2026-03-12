# Feladatok – 15. hét: Adatbázis mock-olás

> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz
> A megoldásokat commitold és pushold a GitHub repódba.

---

### 15.1 – Mock DB beállítás ⭐
Állítsd be a `tests/conftest.py`-t SQLite in-memory adatbázissal. Használd a `dependency_overrides[get_db]` mintát. Ellenőrizd, hogy a tesztek futnak.

### 15.2 – setup_db fixture ⭐⭐
Készíts `autouse=True` fixture-t, amely minden teszt előtt létrehozza és utána törli a táblákat. Ellenőrizd, hogy a tesztek egymástól függetlenek.

### 15.3 – CRUD tesztek mock DB-vel ⭐⭐
Írj tesztet minden CRUD műveletre: create, list, get_by_id, update, delete. Mindegyik a mock DB-t használja.

### 15.4 – Auth + DB tesztek ⭐⭐
Írj teszteket:
- Regisztráció mock DB-vel
- Login mock DB-vel
- Védett végpont létrehozás + lekérés

### 15.5 – CI integráció ⭐⭐⭐
Hozd létre a `.github/workflows/test.yml` fájlt. A workflow: checkout → setup-python → pip install → pytest. Push-old és ellenőrizd a GitHub Actions eredményt. A taszk sikeres, ha a CI zöld.
