# Feladatok – 2. hét: FastAPI bevezetés

> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz
> A megoldásokat commitold és pushold a GitHub repódba.

---

### 2.1 – Első API ⭐
Hozz létre egy FastAPI alkalmazást, amely a `GET /` végponton egy JSON üdvözlő üzenetet ad vissza: `{"message": "Helló, világ!"}`.

### 2.2 – Több végpont ⭐
Bővítsd az alkalmazást a következő végpontokkal:
- `GET /info` → `{"nev": "Az én API-m", "verzio": "1.0"}`
- `GET /datum` → `{"datum": "2024-01-15"}` (az aktuális dátumot)

### 2.3 – Swagger dokumentáció ⭐⭐
Add hozzá az alkalmazáshoz a `title`, `description` és `version` paramétereket. Nyisd meg a `/docs` oldalt, készíts képernyőképet a Swagger UI-ról.

### 2.4 – Gyümölcsök API ⭐⭐
Hozz létre egy egyszerű Gyümölcs API-t:
- `GET /gyumolcsok` → visszaadja a gyümölcsök listáját (lista a memóriában)
- `GET /gyumolcsok/{index}` → visszaadja az adott indexű gyümölcsöt

### 2.5 – HTTP metódusok ⭐⭐⭐
Készíts egy API-t ami kezeli az összes fő HTTP metódust egy `uzenet` erőforráson:
- `GET /uzenetek` → listázás
- `POST /uzenetek` → hozzáadás (sima string body)
- `DELETE /uzenetek` → összes törlése

Teszteld az összes végpontot a Swagger UI-ban.
