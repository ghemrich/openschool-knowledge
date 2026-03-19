# Kiegészítő gyakorlatok – 7. hét: Docker és PostgreSQL

> Ezek a feladatok a heti házi feladat melletti **extra gyakorlást** szolgálják.
> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz

---

### 7.1 – Docker parancsok ⭐
Gyakorold a Docker CLI-t:
- Listázd a futó konténereket (`docker ps`)
- Listázd az összes image-et (`docker images`)
- Indíts egy Alpine konténert interaktív módban (`docker run -it alpine sh`)
- Nézd meg egy konténer logjait (`docker logs`)
- Töröld a használatlan erőforrásokat (`docker system prune`)

### 7.2 – Multi-stage Dockerfile ⭐⭐
Készíts multi-stage Dockerfile-t:
- 1. stage: `builder` – telepíti a függőségeket
- 2. stage: `runtime` – csak a szükséges fájlokat másolja át

Hasonlítsd össze a két image méretét (egyétlen stage vs multi-stage).

### 7.3 – SQL összekapcsolás ⭐⭐
Hozz létre két táblát PostgreSQL-ben: `szerzok` (id, nev) és `konyvek` (id, cim, szerzo_id). Szúrj be adatokat és írj lekérdezéseket:
- JOIN: szerzők és könyveik
- GROUP BY: hány könyve van minden szerzőnek
- ORDER BY + LIMIT: legutóbbi 5 könyv

### 7.4 – Docker volume mentés ⭐⭐
Hozz létre named volume-ot, töltsd fel adatokkal a PostgreSQL-ben. Állítsd le a konténert, majd indítsd újra. Ellenőrizd, hogy az adatok megmaradtak. Próbáld ki a `docker volume inspect` parancsot.

### 7.5 – Docker network ⭐⭐⭐
Készíts két konténert kézzel (Docker Compose nélkül):
1. PostgreSQL konténer egyéni hálózaton
2. Python konténer ugyanazon a hálózaton, ami `psycopg2`-vel csatlakozik a DB-hez

Használd: `docker network create`, `docker run --network`, és a konténer nevét mint hostname-t.
