# Feladatok – 3. hét: Útvonalak és paraméterek

> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz
> A megoldásokat commitold és pushold a GitHub repódba.

---

### 3.1 – Path paraméterek ⭐
Készíts végpontot: `GET /koszontes/{nev}` amely visszaadja: `{"uzenet": "Helló, {nev}!"}`.

### 3.2 – Típusos path paraméter ⭐
Készíts végpontot: `GET /szorzas/{a}/{b}` ahol `a` és `b` integer. Adja vissza a szorzatukat. Teszteld mi történik, ha szöveget adsz meg.

### 3.3 – Query paraméterek ⭐⭐
Készíts végpontot: `GET /kereso` amely `q` (kötelező string) és `limit` (opcionális int, alapértelmezett 10) query paramétereket fogad. Adja vissza: `{"kereses": q, "limit": limit}`.

### 3.4 – Enum paraméter ⭐⭐
Hozz létre egy `Szin` Enum-ot (piros, zold, kek). Készíts végpontot `GET /szin/{szin}` amely visszaadja a szín nevét és hex kódját.

### 3.5 – Lapozás ⭐⭐
Hozz létre egy listát 50 elemmel (pl. `["elem_0", "elem_1", ...]`). Készíts `GET /elemek` végpontot `skip` és `limit` query paraméterekkel. Validáld: `skip >= 0`, `limit` 1 és 50 között.

### 3.6 – Kombinált paraméterek ⭐⭐⭐
Készíts egy `GET /termekek/{kategoria}` végpontot, ahol:
- `kategoria` path paraméter (Enum: elektronika, ruha, elelmiszer)
- `min_ar` és `max_ar` opcionális query paraméterek (int, >= 0)
- `rendezes` opcionális query paraméter (Enum: ar_novekvo, ar_csökkeno, nev)

Adja vissza a szűrési feltételeket JSON-ként.
