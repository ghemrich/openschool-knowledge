# Feladatok – 5. hét: Response modellek és hibakezelés

> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz
> A megoldásokat commitold és pushold a GitHub repódba.

---

### 5.1 – Response model ⭐
A `Termek` modellbed adj hozzá egy `titkos_kod` mezőt, amit NEM szabad visszaadni. Készíts külön `TermekResponse` modellt `response_model`-ként, ami nem tartalmazza a `titkos_kod`-ot.

### 5.2 – Status kódok ⭐
Állíts be helyes HTTP status kódokat:
- `POST` → 201 Created
- `DELETE` → 200 OK (vagy 204 No Content)
- `GET` nem létező elem → 404

### 5.3 – HTTPException ⭐⭐
Készíts egy `GET /felhasznalok/{id}` végpontot, amely:
- 404 hibát dob, ha az id nem létezik, `detail`: "Felhasználó nem található"
- 403 hibát dob, ha az id 0 (admin), `detail`: "Hozzáférés megtagadva"

### 5.4 – Egyedi kivételkezelő ⭐⭐
Hozz létre egy saját `NemTalalhatoError` kivétel osztályt. Regisztrálj hozzá kivételkezelőt az `app`-ban, ami 404-et ad vissza egyedi JSON formátumban: `{"hiba": true, "uzenet": "..."}`.

### 5.5 – Hibakezelés tesztelés ⭐⭐⭐
Készíts egy API-t amely legalább 5 különböző hibakódot tud visszaadni (400, 401, 403, 404, 422). Mindegyikhez írj tesztet a Swagger UI-ban, és dokumentáld a hibakódokat a `responses` paraméterrel.
