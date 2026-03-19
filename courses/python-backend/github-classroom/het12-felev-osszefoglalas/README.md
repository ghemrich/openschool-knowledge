# 12. hét – Félév összefoglalás és próbavizsga

> **Határidő:** a következő óra előtt
> **Beadás:** commitold és pushold a megoldásaidat ebbe a repóba!
> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz

---

Ezen a héten összefoglalod az első félév anyagát és egy próbavizsga feladatsoron keresztül gyakorolsz. Ez a tökéletes alkalom, hogy felmérd, mit tudsz már magabiztosan és miben kell még gyakorolnod.

---

## 12.1 – Gyors API ⭐
Építs egy "Leltár" API-t 10 perc alatt: `GET /`, `GET /eszkozok`, `POST /eszkozok`. Pydantic modell: `Eszkoz(nev, kategoria, ertek)`.

## 12.2 – DB integráció ⭐⭐
Adj adatbázist az előző feladathoz 20 perc alatt: SQLAlchemy modell, get_db, CRUD.

## 12.3 – Auth ⭐⭐
Adj auth-ot 20 perc alatt: regisztráció, login, JWT, védett `POST /eszkozok`.

## 12.4 – Próbavizsga ⭐⭐⭐
Oldd meg a [próbavizsga feladatot](probavizsga.md) **120 perc** alatt: Könyv API + DB + Auth. Mérj időt! A megoldásodat a `probavizsga/` mappába tedd.

---

## Dokumentáció

- Lásd az összes korábbi hét dokumentációját

## 📚 Kapcsolódó anyagok

Az ehhez a héthez tartozó elméleti anyagot és további gyakorlófeladatokat itt találod:

- 📖 [Lecke: Félév összefoglalás](../../doksik/tanulok/leckek/12-felev-osszefoglalas.md)
- 📝 [Gyakorlófeladatok: Félév összefoglalás](../../doksik/tanulok/feladatok/12-felev-osszefoglalas.md)
- [Összes heti anyag](../../doksik/tanulok/README.md)

## Beadás

1. `main.py` + `probavizsga/` mappa legyen a repóban
2. Commitolj értelmes üzenetekkel
3. `git push` – ez a beadás!
