# Kiegészítő gyakorlatok – 11. hét: Middleware és CORS

> Ezek a feladatok a heti házi feladat melletti **extra gyakorlást** szolgálják.
> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz

---

### 11.1 – Feldolgozási idő header ⭐
Készíts middleware-t, amely `X-Process-Time` headerben visszaadja a kérés feldolgozási idejét milliszekundumban. Ellenőrizd a DevTools Network fülén.

### 11.2 – CORS teszt böngészőből ⭐⭐
Készíts egy egyszerű HTML oldalt a `static/` mappában, ami `fetch()`-csel kérést küld az API-nak. Teszteld:
1. CORS nélkül – mi a hibaüzenet a konzolban?
2. Engedélyezd a CORS-t és teszteld újra
3. Próbálj kérést küldeni nem engedélyezett eredetről

### 11.3 – Kérés naplózás fájlba ⭐⭐
Készíts middleware-t, ami minden kérést naplóz egy `access.log` fájlba:
```
2024-01-15 14:30:00 | GET /api/items | 200 | 0.045s | 192.168.1.1
```
Használd a Python `logging` modult `RotatingFileHandler`-rel.

### 11.4 – Maintenance mode ⭐⭐
Készíts middleware-t, ami a `MAINTENANCE_MODE=true` környezeti változó esetén minden kérésre 503-at ad vissza: `{"detail": "Karbantartás folyamatban, próbáld később."}`. Kivétel: a `GET /health` végpont mindig elérhető.

### 11.5 – Security headers ⭐⭐⭐
Készíts middleware-t, ami biztonsági headereket ad minden válaszhoz:
- `X-Content-Type-Options: nosniff`
- `X-Frame-Options: DENY`
- `Strict-Transport-Security: max-age=31536000`
- `Content-Security-Policy: default-src 'self'`

Készíts `GET /headers-check` végpontot, ami ellenőrzi és kiírja a válasz headereket.
