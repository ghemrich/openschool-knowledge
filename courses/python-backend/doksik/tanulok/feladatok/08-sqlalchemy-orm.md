# Kiegészítő gyakorlatok – 8. hét: SQLAlchemy ORM

> Ezek a feladatok a heti házi feladat melletti **extra gyakorlást** szolgálják.
> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz

---

### 8.1 – Filmadatbázis modell ⭐
Hozz létre `Film` SQLAlchemy modellt: id, cim, rendezo, ev, ertekeles (Float), mufaj. Konfiguráld a `database.py`-t és hozd létre a táblát.

### 8.2 – Alsó-felső korláttal ⭐⭐
Adj a `Film` modellhez `CheckConstraint`-eket:
- `ertekeles` 0.0 és 10.0 között
- `ev` 1888 és 2100 között

Próbálj érvénytelen adatot beszúrni és figyeld a hibát.

### 8.3 – Több táblás migráció ⭐⭐
Hozz létre két új modellt egyszerre: `Mufaj` (id, nev) és `Szinesz` (id, nev, szuletesi_ev). Generálj egyetlen Alembic migrációt, ami mindkét táblát létrehozza.

### 8.4 – Many-to-Many ⭐⭐⭐
Készíts many-to-many kapcsolatot `Film` és `Szinesz` között (asszociációs tábla: `film_szinesz`). Használj `relationship()` + `secondary` paramétert. Generáld a migrációt és teszteld.

### 8.5 – Alembic downgrade ⭐⭐⭐
Gyakorold az Alembic műveleteket:
1. Futtasd az `alembic history`-t
2. Végezz `downgrade -1` műveletet
3. Ellenőrizd, hogy a tábla eltűnt
4. Futtasd újra az `upgrade head`-et
5. Hozz létre "data migration"-t: egy migráció, ami kezdőadatokat szúr be
