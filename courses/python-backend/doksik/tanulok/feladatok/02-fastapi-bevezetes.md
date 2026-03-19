# Kiegészítő gyakorlatok – 2. hét: FastAPI bevezetés

> Ezek a feladatok a heti házi feladat melletti **extra gyakorlást** szolgálják.
> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz

---

### 2.1 – Egészségjelző API ⭐
Készíts egy FastAPI alkalmazást két végponttal:
- `GET /health` → `{"status": "ok", "uptime": "..."}`
- `GET /verzio` → `{"api_verzio": "0.1.0", "python_verzio": "3.11.x"}` (a valós Python verziót használd `sys.version`-nel)

### 2.2 – Szótár API ⭐
Készíts egy egyszerű szótár API-t, amely in-memory szótárból dolgozik:
- `GET /szavak` → visszaadja az összes szót és jelentését
- `GET /szavak/{szo}` → visszaadja egy konkrét szó jelentését

Tárolj legalább 5 magyar–angol szópárt.

### 2.3 – Időjárás szimulátor ⭐⭐
Készíts API-t, amely városonként "szimulál" időjárást (in-memory dict):
- `GET /idojaras` → az összes város aktuális időjárása
- `GET /idojaras/{varos}` → egy város időjárása (hőmérséklet, szél, leírás)
- `POST /idojaras/{varos}` → új város hozzáadása

### 2.4 – Többnyelvű API ⭐⭐
Készíts API-t, ahol a `GET /` végpont `lang` query paraméter alapján más nyelven köszön:
- `lang=hu` → "Üdvözöllek!"
- `lang=en` → "Welcome!"
- `lang=de` → "Willkommen!"
- más érték → 400-as hiba

Használj dictionary-t a fordításokhoz.

### 2.5 – Idézet API ⭐⭐⭐
Készíts REST API-t idézetekhez (in-memory lista):
- `GET /idezetek` → összes idézet (id-val)
- `GET /idezetek/random` → véletlenszerű idézet
- `POST /idezetek` → új idézet hozzáadása (szerző, szöveg)
- `DELETE /idezetek/{id}` → törlés
- `GET /idezetek/szerzok` → egyedi szerzők listája

Tárolj legalább 10 idézetet különböző szerzőktől.
