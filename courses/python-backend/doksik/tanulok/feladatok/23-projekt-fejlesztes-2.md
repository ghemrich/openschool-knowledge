# Feladatok – 23. hét: Projekt fejlesztés II.

> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz
> A megoldásokat commitold és pushold a GitHub repódba.

---

### 23.1 – conftest.py ⭐⭐
Készíts teljes `tests/conftest.py`-t: SQLite mock DB, setup_db, client, auth_headers, create_user factory fixture.

### 23.2 – Auth tesztek ⭐⭐
Írj legalább 5 auth tesztet: regisztráció, dupla email, login, rossz jelszó, profil lekérés.

### 23.3 – CRUD tesztek ⭐⭐
Írj legalább 8 CRUD tesztet: create, list, get, update, delete, not_found, jogosultság, validáció.

### 23.4 – CI pipeline ⭐⭐
Készítsd el a `.github/workflows/ci.yml`-t lint + test jobokkal. Push-old és ellenőrizd, hogy zöld.

### 23.5 – README és véglegesítés ⭐⭐⭐
Készíts teljes `README.md`-t: projekt leírás, végpont táblázat, telepítési útmutató, tesztelési parancsok. Ellenőrizd a végső ellenőrzőlistát:
- [ ] Minden végpont működik
- [ ] Min. 15 teszt zöld
- [ ] Docker Compose elindul
- [ ] CI zöld
- [ ] README kész
