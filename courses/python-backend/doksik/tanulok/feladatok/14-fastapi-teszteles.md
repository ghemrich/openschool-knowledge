# Feladatok – 14. hét: FastAPI tesztelés

> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz
> A megoldásokat commitold és pushold a GitHub repódba.

---

### 14.1 – TestClient ⭐
Készíts tesztet a `GET /` végpontra TestClient-tel. Ellenőrizd a status kódot és a JSON tartalmat.

### 14.2 – GET tesztek ⭐⭐
Írj teszteket a listázó és az egyedi lekérő végpontokra. Teszteld a 200-as és 404-es válaszokat is.

### 14.3 – POST teszt ⭐⭐
Írj tesztet a `POST` végpontra: küldj JSON adatot, ellenőrizd a 201-es kódot és a visszaadott adatokat.

### 14.4 – Auth tesztek ⭐⭐
Írj teszteket:
- Regisztráció sikeres (201)
- Dupla email (400)
- Login sikeres (200 + access_token)
- Login rossz jelszóval (401)

### 14.5 – Védett végpont tesztek ⭐⭐⭐
Írj teszteket:
- Védett végpont token nélkül (401)
- Védett végpont érvényes tokennel (200)
- Profil végpont visszaadja a helyes email-t

Használj `auth_headers` fixture-t a conftest.py-ban.
