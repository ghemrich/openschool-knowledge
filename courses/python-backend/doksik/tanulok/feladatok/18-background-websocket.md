# Kiegészítő gyakorlatok – 18. hét: Background Tasks és WebSocket

> Ezek a feladatok a heti házi feladat melletti **extra gyakorlást** szolgálják.
> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz

---

### 18.1 – Háttér takarítás ⭐
Készíts `DELETE /admin/cleanup` végpontot, ami háttérben törli a 30 napnál régebbi soft-deleted rekordokat. A válasz azonnal megjön: `{"uzenet": "Takarítás elindítva"}`. A háttérfeladat naplózza a törölt elemek számát.

### 18.2 – Értesítés rendszer ⭐⭐
Készíts "webhook szimulátor" háttérfeladatot: amikor egy új elem létrejön (POST), háttérben küldj egy HTTP kérést (httpx) egy konfigurálható URL-re az elem adataival. Ha a kérés sikertelen, naplózd a hibát.

### 18.3 – WebSocket számláló ⭐⭐
Készíts `/ws/szamlalo` WebSocket végpontot. A szerver másodpercenként küld egy számot (1, 2, 3...). A kliens küldheti a "reset" üzenetet, amire a számláló újraindul.

### 18.4 – WebSocket auth ⭐⭐
Készíts `/ws/privat` végpontot, ami a csatlakozáskor token-t vár (query paraméterként: `ws://localhost:8000/ws/privat?token=...`). Érvénytelen tokennél zárd be a kapcsolatot 1008-as kóddal.

### 18.5 – Élő frissítések ⭐⭐⭐
Készíts rendszert, ahol:
1. REST API-n keresztül létrehoznak/módosítanak/törölnek elemeket
2. WebSocket kliensek valós időben kapnak értesítést: `{"esemeny": "letrehozva", "elem": {...}}`
3. `ConnectionManager` kezeli a csatlakozott klienseket
4. Írj tesztet a WebSocket értesítésekre
