# Feladatok – 8. hét: SQLAlchemy ORM

> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz
> A megoldásokat commitold és pushold a GitHub repódba.

---

### 8.1 – Első modell ⭐
Hozz létre egy `Konyv` SQLAlchemy modellt (id, cim, szerzo, oldalszam, kiadas_ev). Konfiguráld a `database.py`-t (engine, SessionLocal, Base).

### 8.2 – Alembic beállítás ⭐⭐
Inicializáld az Alembic-et a projektben. Generáld le az első migrációt a `Konyv` modellhez. Futtasd a migrációt Docker-ben futó PostgreSQL-en.

### 8.3 – Modell módosítás ⭐⭐
Adj hozzá egy `ar` (Integer) és egy `elerheto` (Boolean, default True) mezőt a `Konyv` modellhez. Generálj új Alembic migrációt, és futtasd le.

### 8.4 – Több modell ⭐⭐
Hozz létre egy `Szerzo` modellt (id, nev, szuletes_ev) és módosítsd a `Konyv` modellt, hogy `szerzo_id` ForeignKey-jel hivatkozzon rá. Generáld és futtasd a migrációt.

### 8.5 – Relationship ⭐⭐⭐
Adj hozzá `relationship()` kapcsolatot a `Szerzo` és `Konyv` modellekhez (`back_populates`). Teszteld Python shell-ben, hogy a `szerzo.konyvek` listája elérhető.
