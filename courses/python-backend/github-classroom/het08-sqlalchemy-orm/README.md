# 8. hét – SQLAlchemy ORM

> **Beadás:** commitold és pushold a megoldásaidat ebbe a repóba!
> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz

---

Ezen a héten megismerkedsz az SQLAlchemy ORM-mel, amivel Python objektumok segítségével kezelheted az adatbázist SQL lekérdezések írása nélkül. Beállítod az adatbázis-kapcsolatot és létrehozod az első modelleidet.

---

## 8.1 – Database modul ⭐
Készíts `database.py`-t: engine (PostgreSQL URL-lel), SessionLocal, Base, `get_db`. A URL jöjjön `.env`-ből.

## 8.2 – Első modell ⭐
Készíts `models.py`-t egy `Konyv` modellel: id, cim (String), szerzo (String), oldalszam (Integer), kiadas_ev (Integer).

## 8.3 – Alembic ⭐⭐
Inicializáld az Alembic-et (`alembic init alembic`). Konfiguráld a `env.py`-t. Generálj és futtasd az első migrációt.

## 8.4 – Modell módosítás ⭐⭐
Adj `ar` (Integer) és `elerheto` (Boolean, default True) mezőket a modellhez. Generálj és futtasd az új migrációt.

## 8.5 – Relationship ⭐⭐⭐
Készíts `Szerzo` modellt (id, nev, szuletes_ev). Módosítsd a `Konyv`-et: `szerzo_id` ForeignKey. Adj hozzá `relationship()`-et mindkét modellhez. Migráció + tesztelés.

---

## Dokumentáció

- [SQLAlchemy ORM](https://docs.sqlalchemy.org/en/20/orm/quickstart.html)
- [Alembic Tutorial](https://alembic.sqlalchemy.org/en/latest/tutorial.html)
- [FastAPI SQL Databases](https://fastapi.tiangolo.com/tutorial/sql-databases/)

## 📚 Kapcsolódó anyagok

Az ehhez a héthez tartozó elméleti anyagot és további gyakorlófeladatokat itt találod:

- 📖 [Lecke: SQLAlchemy ORM](https://github.com/ghemrich/openschool-knowledge/blob/master/courses/python-backend/leckek/08-sqlalchemy-orm.md)

## Beadás

1. `database.py`, `models.py`, `alembic/` legyen a repóban
2. `.env` NE legyen benne, `.env.example` igen
3. Commitolj értelmes üzenetekkel
4. `git push` – ez a beadás!
