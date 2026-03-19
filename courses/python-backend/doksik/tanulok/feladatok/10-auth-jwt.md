# Kiegészítő gyakorlatok – 10. hét: Authentikáció és JWT

> Ezek a feladatok a heti házi feladat melletti **extra gyakorlást** szolgálják.
> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz

---

### 10.1 – Token vizsgálat ⭐
Készíts `GET /auth/token-info` végpontot, ami a Bearer tokenből dekodolt adatokat adja vissza: `{"sub": "...", "exp": "...", "remaining_sec": 1234}`. Token nélkül adj 401-et.

### 10.2 – Jelszó erősség ⭐⭐
Készíts `jelszo_eros(jelszo: str) -> bool` függvényt, ami ellenőrzi:
- Min. 8 karakter
- Tartalmaz nagybetűt, kisbetűt, számot, speciális karaktert

A regisztráció utasítsa el a gyenge jelszót 400-as hibával és részletes üzenettel: melyik feltétel nem teljesül.

### 10.3 – Refresh token ⭐⭐
Valósítsd meg a refresh token mintát:
- Login-nál két tokent adj vissza: `access_token` (15 perc) és `refresh_token` (7 nap)
- Készíts `POST /auth/refresh` végpontot, ami új access tokent ad a refresh token alapján

### 10.4 – Jelszó váltás ⭐⭐
Készíts `PUT /auth/jelszo-valtas` végpontot:
- Kötelező mezők: `regi_jelszo`, `uj_jelszo`, `uj_jelszo_ujra`
- Ellenőrizd a régi jelszót, az új jelszó erősségét, és hogy a két új jelszó egyezik
- Védett végpont (JWT szükséges)

### 10.5 – Role-based access ⭐⭐⭐
Valósíts meg szerepkör-alapú jogosultságkezelést:
- Adj `role` mezőt a `Felhasznalo` modellhez (Enum: user, admin)
- Készíts `require_role(role)` dependency factory-t
- `DELETE /felhasznalok/{id}` – csak admin
- `GET /admin/statisztikak` – csak admin
- Sima userek 403-at kapnak
