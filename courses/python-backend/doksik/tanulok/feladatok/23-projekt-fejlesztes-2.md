# Kiegészítő gyakorlatok – 23. hét: Projekt fejlesztés II.

> Ezek a feladatok a heti házi feladat melletti **extra gyakorlást** szolgálják.
> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz

---

### 23.1 – Negatív tesztgyűjtemény ⭐⭐
Készíts külön `tests/test_negativ.py` fájlt legalább 10 negatív teszttel:
- Érvénytelen token formátum
- Lejárt token
- Nem létező erőforrás
- Jogosultság megsértése (más user adata)
- Üres és null értékek
- Túl hosszú mezőértékek

### 23.2 – Integrációs teszt sorozat ⭐⭐
Írj "forgatkönyv" alapú tesztet, ami végigmegy egy valós használati eseten:
```python
def test_teljes_vasarlasi_folyamat(client, db):
    # 1. Regisztráció
    # 2. Login
    # 3. Termék böngészés
    # 4. Rendelés leadva
    # 5. Rendelés státusz ellenőrzés
```

### 23.3 – Teljesítmény mérés ⭐⭐
Készíts egyszerű benchmark scriptet:
```python
import httpx, time
start = time.time()
for i in range(100):
    httpx.get("http://localhost:8000/items")
print(f"100 kérés: {time.time() - start:.2f}s")
```
Mérd a legtöbbet használt végpontokat. Van-e szűk keresztmetszet?

### 23.4 – Error handling audit ⭐⭐
Nézd végig az összes végpontot és ellenőrizd:
- Minden hiba eset kezelve van? (404, 401, 403, 422)
- A hibaüzenetek szép formátumúak és informatvak?
- Nincs stack trace a válaszban?

Dokumentáld a hiányosságokat és javítsd ki őket.

### 23.5 – Demo készítés ⭐⭐⭐
Készítsd el a projekt "demo" leírását `docs/DEMO.md`-ben:
1. Hogyan indítható el a projekt (`docker compose up`)
2. Lépésről lépésre bemutató (curl parancsokkal):
   - Regisztráció, login, token mentés
   - CRUD műveletek a tokennal
   - Hibakezelés bemutatása
3. Hogyan futtathatók a tesztek
