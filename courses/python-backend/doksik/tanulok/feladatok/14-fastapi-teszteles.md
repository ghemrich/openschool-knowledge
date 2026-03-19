# Kiegészítő gyakorlatok – 14. hét: FastAPI tesztelés

> Ezek a feladatok a heti házi feladat melletti **extra gyakorlást** szolgálják.
> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz

---

### 14.1 – Health check teszt ⭐
Készíts tesztet a `GET /health` végpontra. Ellenőrizd: status kód 200, válasz tartalmazza a `"status": "ok"` mezőt, és a Content-Type `application/json`.

### 14.2 – Validációs tesztek ⭐⭐
Írj teszteket, amelyek ellenőrzik a Pydantic validációt:
- Hiányzó kötelező mező → 422
- Rossz típus (string szám helyett) → 422
- Túl rövid név → 422
- `detail` mező tartalmazza a hiba okát

### 14.3 – CRUD integrációs tesztek ⭐⭐
Írj integrációs tesztsorozatot, ami végigmegy egy teljes életcikluson:
1. Létrehozás (POST) → 201, visszakapott id
2. Lekérés (GET /{id}) → 200, helyes adatok
3. Módosítás (PUT /{id}) → 200, frissített adatok
4. Listázás (GET) → 200, tartalmazza az elemet
5. Törlés (DELETE /{id}) → 200
6. Lekérés törlés után (GET /{id}) → 404

### 14.4 – Fixture-ök újrahasznosítása ⭐⭐
Készíts a `conftest.py`-ban:
- `client` fixture (TestClient)
- `minta_elem` fixture (létrehoz egy elemet és visszaadja az adatokat)
- `tobb_elem` fixture (létrehoz 5 elemet)

Használd őket a tesztekben, hogy ne ismételd a létrehozási kódot.

### 14.5 – Edge case tesztelés ⭐⭐⭐
Írj teszteket speciális esetekre:
- Nagyon hosszú név (1000+ karakter)
- Speciális karakterek a szöveges mezőkben (ékezetek, emoji)
- Nem létező ID (0, -1, 99999)
- Üres body küldése POST-nál
- Duplikált létrehozás (ha releváns)

Dokumentáld kommentben, mit vársz minden teszttől.
