# Kiegészítő gyakorlatok – 15. hét: Adatbázis mock-olás

> Ezek a feladatok a heti házi feladat melletti **extra gyakorlást** szolgálják.
> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz

---

### 15.1 – Két DB konfiguráció ⭐
Készítsd el, hogy a `DATABASE_URL` környezeti változó alapján választ a valós (PostgreSQL) és teszt (SQLite) adatbázis között. A `conftest.py` `TESTING=true`-t állít be, és ez alapján SQLite-ot használ.

### 15.2 – Izolált tesztek ⭐⭐
Készíts `db_session` fixture-t, ami tranzakcióba csomagolja a teszteket:
```python
@pytest.fixture
def db_session():
    connection = engine.connect()
    transaction = connection.begin()
    session = Session(bind=connection)
    yield session
    transaction.rollback()
    connection.close()
```
Ellenőrizd, hogy a tesztek nem hat nak egymásra: az egyik teszt által létrehozott adat NEM látható egy másik tesztben.

### 15.3 – CRUD unit tesztek ⭐⭐
Írj unit teszteket közvetlenül a `crud.py` függvényeire (nem a végpontokon keresztül):
- `test_create_returns_id`
- `test_get_by_id_found`
- `test_get_by_id_not_found_returns_none`
- `test_update_changes_fields`
- `test_delete_removes_record`

### 15.4 – Factory pattern ⭐⭐
Készíts `create_test_user(**kwargs)` és `create_test_item(**kwargs)` factory függvényeket, amelyek alapértelmezett értékeket adnak. Példa:
```python
def create_test_user(db, nev="Teszt", email="teszt@example.com", ...):
    ...
```
Használd 5 tesztben.

### 15.5 – Adatbázis integrációs teszt ⭐⭐⭐
Írj integrációs tesztsorozatot, ami a teljes folyamatot szimulálja mock DB-vel:
1. Regisztráció → 2. Login → 3. Elem létrehozása (token-nel) → 4. Elem listázása → 5. Elem módosítása → 6. Másik user regisztrál → 7. Másik user NEM tudja törölni az elemet (403)

Minden lépés ellenőrzi a várt eredményt.
