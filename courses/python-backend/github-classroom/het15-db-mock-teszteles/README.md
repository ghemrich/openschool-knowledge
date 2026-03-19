# 15. hét – Adatbázis mock-olás teszteléshez

> **Határidő:** a következő óra előtt
> **Beadás:** commitold és pushold a megoldásaidat ebbe a repóba!
> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz

---

Ezen a héten megtanulod, hogyan tesztelj adatbázist használó kódot úgy, hogy a tesztek ne függjenek valós adatbázistól. A mock-olás segítségével gyors és megbízható teszteket írhatsz.

---

## Feladat

Készíts egy **Termék API**-t adatbázissal, amelyhez a tesztek SQLite mock DB-t használnak.

### Struktúra:
```
app/
├── __init__.py
├── main.py
├── database.py       # engine, SessionLocal, Base, get_db
├── models.py         # Termek modell
├── schemas.py        # TermekCreate, TermekResponse
├── crud.py           # CRUD függvények
└── routers/
    ├── __init__.py
    └── termekek.py   # Router
tests/
└── conftest.py       # SQLite mock DB + fixtures (te írod!)
requirements.txt
```

### Termek modell:
- `id` (Integer, PK)
- `nev` (String, nem null)
- `ar` (Integer, > 0)
- `leiras` (String, opcionális)

### Végpontok:
- `GET /` → `{"message": "Termék API"}` ⭐
- `GET /termekek` → listázás ⭐
- `POST /termekek` → létrehozás (201) ⭐⭐
- `GET /termekek/{id}` → egy termék (404) ⭐⭐
- `DELETE /termekek/{id}` → törlés (404 ha nincs) ⭐⭐⭐

### Mock DB beállítás (`tests/conftest.py`):
Te készíted el! Használd a `dependency_overrides[get_db]` mintát SQLite-tal.

---

## Automatikus tesztelés

A push után rejtett tesztek futnak a te `conftest.py`-od `client` fixture-jével (GitHub Classroom Autograding). Helyi teszteléshez használd a `conftest_minta.py`-t kiindulásként:
```bash
cp conftest_minta.py tests/conftest.py
pip install -r requirements.txt
pytest tests/ -v
```

## Dokumentáció

- [FastAPI Testing Database](https://fastapi.tiangolo.com/advanced/testing-database/)
- [SQLAlchemy SQLite](https://docs.sqlalchemy.org/en/20/dialects/sqlite.html)

## 📚 Kapcsolódó anyagok

Az ehhez a héthez tartozó elméleti anyagot és további gyakorlófeladatokat itt találod:

- 📖 [Lecke: DB mock teszt](../../doksik/tanulok/leckek/15-db-mock-teszteles.md)
- 📝 [Gyakorlófeladatok: DB mock teszt](../../doksik/tanulok/feladatok/15-db-mock-teszteles.md)

## Beadás

1. `app/` csomag + `tests/conftest.py` legyen a repóban
2. A push után a rejtett tesztek automatikusan futnak a te `conftest.py`-oddal
3. Commitolj értelmes üzenetekkel
4. `git push` – ez a beadás!
