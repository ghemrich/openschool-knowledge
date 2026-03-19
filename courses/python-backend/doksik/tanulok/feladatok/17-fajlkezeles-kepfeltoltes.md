# Kiegészítő gyakorlatok – 17. hét: Fájlkezelés és képfeltöltés

> Ezek a feladatok a heti házi feladat melletti **extra gyakorlást** szolgálják.
> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz

---

### 17.1 – CSV import ⭐
Készíts `POST /import/csv` végpontot, ami CSV fájlt fogad. Olvasd be a csv modullal, és add vissza a sorok számát és az oszlopneveket: `{"sorok": 42, "oszlopok": ["nev", "email", "kor"]}`.

### 17.2 – Fájl letöltés ⭐⭐
Készíts `GET /export/{formatum}` végpontot (formátum: csv, json). A végpont az adatbázis tartalmát exportálja és `FileResponse`-ként vagy `StreamingResponse`-ként adja vissza a megfelelő Content-Type-pal.

### 17.3 – Több fájl feltöltése ⭐⭐
Készíts `POST /feltoltes/tobb` végpontot, ami egyszerre több fájlt fogad (`files: list[UploadFile]`). Ellenőrizd mindegyik méretét és típusát. Add vissza a sikeres és sikertelen feltöltések listáját.

### 17.4 – Kép átméretezés ⭐⭐
Készíts `POST /feltoltes/kep` végpontot, ami:
1. Fogadja a képet (JPEG/PNG)
2. Pillow-val átméretezi 800x600-ra (thumbnail)
3. Mindkét verziót menti: `uploads/original/` és `uploads/thumb/`
4. Visszaadja mindkét URL-t

### 17.5 – Fájl feltöltés tesztelése ⭐⭐⭐
Írj pytest teszteket a feltöltéshez:
- Sikeres kép feltöltés (bytes tartalommal)
- Túl nagy fájl → 400
- Nem engedélyezett típus (.exe) → 400
- Üres fájl → 400

Használd a TestClient `files=` paraméterét: `client.post("/feltoltes", files={"file": ("test.jpg", content, "image/jpeg")})`.
