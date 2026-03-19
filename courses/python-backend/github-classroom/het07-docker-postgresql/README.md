# 7. hét – Docker és PostgreSQL

> **Határidő:** a következő óra előtt
> **Beadás:** commitold és pushold a megoldásaidat ebbe a repóba!
> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz

---

Ezen a héten megismerkedsz a Dockerrel és a PostgreSQL adatbázissal. A Docker segítségével izolált környezetben futtathatod az alkalmazásodat, a PostgreSQL pedig egy professzionális, nyílt forráskódú adatbázis.

---

## 7.1 – Dockerfile ⭐
Készíts `Dockerfile`-t a FastAPI alkalmazásodhoz. Építsd meg és futtasd. Add a repóba a `Dockerfile`-t.

## 7.2 – PostgreSQL ⭐
Indíts PostgreSQL konténert. Csatlakozz `psql`-lel. Készíts `sql-parancsok.txt` fájlt a futtatott SQL parancsokkal (CREATE TABLE, INSERT, SELECT).

## 7.3 – SQL gyakorlat ⭐⭐
Készíts `tanulok` táblát (id, nev, email, kor). Szúrj be 5 sort, kérdezd le szűréssel, módosíts és törölj. Mentsd az SQL-t a `feladatok.sql` fájlba.

## 7.4 – Docker Compose ⭐⭐
Készíts `docker-compose.yml`-t egy PostgreSQL szolgáltatással. Named volume a perzisztenciához. Teszteld: leállítás → újraindítás → adatok megmaradtak.

## 7.5 – FastAPI + DB ⭐⭐⭐
Egészítsd ki a `docker-compose.yml`-t: `api` és `db` szolgáltatás. Az API `depends_on` a DB-n. Teszteld, hogy a http://localhost:8000/docs elérhető.

---

## Dokumentáció

- [Docker Get Started](https://docs.docker.com/get-started/)
- [PostgreSQL Docker](https://hub.docker.com/_/postgres)
- [Docker Compose](https://docs.docker.com/compose/)

## 📚 Kapcsolódó anyagok

Az ehhez a héthez tartozó elméleti anyagot és további gyakorlófeladatokat itt találod:

- 📖 [Lecke: Docker és PostgreSQL](../../doksik/tanulok/leckek/07-docker-postgresql.md)
- 📝 [Gyakorlófeladatok: Docker és PostgreSQL](../../doksik/tanulok/feladatok/07-docker-postgresql.md)

## Beadás

1. `Dockerfile`, `docker-compose.yml`, `.sql` fájlok legyenek a repóban
2. Commitolj értelmes üzenetekkel
3. `git push` – ez a beadás!
