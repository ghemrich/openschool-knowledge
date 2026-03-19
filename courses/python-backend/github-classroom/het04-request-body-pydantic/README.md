# 4. hét – Request body és Pydantic

> **Határidő:** a következő óra előtt
> **Beadás:** commitold és pushold a megoldásaidat ebbe a repóba!
> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz

---

Ezen a héten megtanulod, hogyan fogadj és validálj bejövő adatokat a Pydantic modellek segítségével. A Pydantic automatikusan ellenőrzi az adatokat, és érthető hibaüzeneteket ad, ha valami nem stimmel.

---

## 4.1 – Pydantic modell ⭐
Készíts `Termek` Pydantic modellt (`models.py`): `nev` (str), `ar` (int), `leiras` (str). Készíts `POST /termekek` végpontot (`main.py`).

## 4.2 – Validáció ⭐
Add hozzá Field validációt: `nev` min 1 karakter, `ar` > 0, `leiras` max 500 karakter. Teszteld hibás adatokkal.

## 4.3 – In-memory CRUD ⭐⭐
Készíts teljes CRUD API-t in-memory listával:
- `GET /termekek` – listázás
- `POST /termekek` – létrehozás (id-t a szerver generálja)
- `GET /termekek/{id}` – egy termék (404 ha nincs)
- `PUT /termekek/{id}` – módosítás
- `DELETE /termekek/{id}` – törlés

## 4.4 – Beágyazott modell ⭐⭐
Készíts `Rendeles` modellt: `vevo_nev` (str), `cim` (Cim modell: varos, utca, irszam), `tetelek` (list[Tetel]: nev, db, ar). Készíts `POST /rendelesek` végpontot.

## 4.5 – Partial update ⭐⭐⭐
Készíts `TermekUpdate` modellt ahol minden mező opcionális. A `PUT /termekek/{id}` csak a megadott mezőket módosítsa.

---

## Dokumentáció

- [Request Body](https://fastapi.tiangolo.com/tutorial/body/)
- [Pydantic Field](https://fastapi.tiangolo.com/tutorial/body-fields/)
- [Nested Models](https://fastapi.tiangolo.com/tutorial/body-nested-models/)

## 📚 Kapcsolódó anyagok

Az ehhez a héthez tartozó elméleti anyagot és további gyakorlófeladatokat itt találod:

- 📖 [Lecke: Request body és Pydantic](../../doksik/tanulok/leckek/04-request-body-pydantic.md)
- 📝 [Gyakorlófeladatok: Request body és Pydantic](../../doksik/tanulok/feladatok/04-request-body-pydantic.md)

## Beadás

1. `main.py` + `models.py` legyen a repóban
2. Commitolj értelmes üzenetekkel
3. `git push` – ez a beadás!
