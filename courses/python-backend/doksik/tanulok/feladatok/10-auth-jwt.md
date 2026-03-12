# Feladatok – 10. hét: Authentikáció és JWT

> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz
> A megoldásokat commitold és pushold a GitHub repódba.

---

### 10.1 – Jelszó hash-elés ⭐
Készíts `auth.py` modult `hash_jelszo()` és `jelszo_ellenorzes()` függvényekkel (passlib + bcrypt). Teszteld: hash-eld a "titok123" jelszót, majd ellenőrizd helyes és helytelen jelszóval.

### 10.2 – Regisztráció ⭐⭐
Készíts `Felhasznalo` modellt (id, nev, email, jelszo_hash) és `POST /auth/regisztracio` végpontot. Az email legyen unique – dupla regisztrációnál 400-at adjon.

### 10.3 – JWT token ⭐⭐
Egészítsd ki az `auth.py`-t `token_letrehozas()` és `token_dekodolas()` függvényekkel. Készíts `POST /auth/login` végpontot, amely sikeres belépés után JWT tokent ad vissza.

### 10.4 – Védett végpont ⭐⭐
Készíts `get_current_user` dependency-t, amely a `Bearer` tokenből kinyeri a felhasználót. Készíts `GET /auth/profil` védett végpontot.

### 10.5 – Jogosultság ⭐⭐⭐
Módosítsd a `POST /konyvek` és `DELETE /konyvek/{id}` végpontokat, hogy csak bejelentkezett felhasználók férjenek hozzá. Token nélkül 401-et adjanak. Teszteld a Swagger UI-ban a 🔒 gombbal.
