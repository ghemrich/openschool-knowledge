# 10. hét – Authentikáció és JWT

> **Beadás:** commitold és pushold a megoldásaidat ebbe a repóba!
> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz

---

Ezen a héten megtanulod, hogyan védd le az API végpontjaidat felhasználói hitelesítéssel (authentikáció). JWT (JSON Web Token) tokenek segítségével a felhasználók biztonságosan igazolhatják a személyazonosságukat.

---

## 10.1 – Jelszó hash ⭐
Készíts egy `auth.py` fájlt, benne `hash_jelszo(jelszo: str)` és `jelszo_ellenorzes(jelszo: str, hash: str)` függvényekkel. Használd a `passlib` csomagot `bcrypt` algoritmussal. A `main.py`-ból teszteld, hogy a hash-elés és ellenőrzés működik.

> 💡 Telepítsd: `pip install passlib[bcrypt]`

## 10.2 – Regisztráció ⭐⭐
Készíts `Felhasznalo` modellt (id, nev, email, jelszo_hash). Hozz létre egy `POST /auth/regisztracio` végpontot, ami:
- Fogadja a felhasználó nevét, emailjét és jelszavát
- Hash-eli a jelszót a 10.1-es `hash_jelszo()` függvénnyel
- Elmenti az adatbázisba
- Ha az email már létezik, `400 Bad Request` választ ad

## 10.3 – JWT Login ⭐⭐
Egészítsd ki az `auth.py`-t egy `create_access_token(data: dict)` függvénnyel. Készíts `POST /auth/login` végpontot, ami email + jelszó alapján ellenőrzi a felhasználót, és sikeres belépés esetén visszaad egy JWT tokent.

> 💡 Telepítsd: `pip install python-jose[cryptography]`

## 10.4 – Védett végpont ⭐⭐
Készíts egy `get_current_user` dependency-t (FastAPI `Depends`), ami a kérés fejlécéből kiszedi a JWT tokent, dekódolja, és visszaadja a felhasználó adatait. Hozz létre egy `GET /auth/profil` végpontot, ami a bejelentkezett felhasználó adatait adja vissza. Token nélkül `401 Unauthorized` választ adj.

## 10.5 – Jogosultság ⭐⭐⭐
A `POST /konyvek` és `DELETE /konyvek/{id}` végpontok csak bejelentkezett felhasználóknak legyenek elérhetők. Használd a `get_current_user` dependency-t a végpontok paramétereként. Teszteld a Swagger UI 🔒 gombbal (Authorize).

---

## Dokumentáció

- [FastAPI Security](https://fastapi.tiangolo.com/tutorial/security/)
- [python-jose](https://github.com/mpdavis/python-jose)
- [passlib](https://passlib.readthedocs.io/)

## 📚 Kapcsolódó anyagok

Az ehhez a héthez tartozó elméleti anyagot és további gyakorlófeladatokat itt találod:

- 📖 [Lecke: Autentikáció és JWT](https://github.com/ghemrich/openschool-knowledge/blob/master/courses/python-backend/leckek/10-auth-jwt.md)

## Beadás

1. `auth.py`, `dependencies.py` legyen a repóban
2. Commitolj értelmes üzenetekkel
3. `git push` – ez a beadás!
