# Feladatok – 12. hét: Félév összefoglalás és próbavizsga

> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz
> A megoldásokat commitold és pushold a GitHub repódba.

---

### 12.1 – Ismétlés: REST API ⭐
Készíts egy új "leltár" API-t a nulláról (10 perc). Végpontok: `GET /`, `GET /eszkozok`, `POST /eszkozok`. Pydantic modell: `Eszkoz(nev, kategoria, ertek)`.

### 12.2 – Ismétlés: Adatbázis ⭐⭐
Adj adatbázist az előző feladathoz: SQLAlchemy modell, `get_db`, CRUD funkciók, Alembic migráció. (20 perc)

### 12.3 – Ismétlés: Auth ⭐⭐
Adj hozzá auth-ot: regisztráció, login, JWT, védett `POST /eszkozok` végpont. (20 perc)

### 12.4 – Próbavizsga ⭐⭐⭐
Oldd meg a 12. lecke próbavizsga feladatát 120 perc alatt. Építs teljes Könyv API-t auth-tal és adatbázissal. Mérj időt!

### 12.5 – Docker teljes projekt ⭐⭐⭐
A próbavizsga megoldásodhoz készíts `docker-compose.yml`-t (API + DB) és `Dockerfile`-t. Indítsd el és teszteld, hogy minden működik.
