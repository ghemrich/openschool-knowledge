# Feladatok – 11. hét: Middleware és CORS

> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz
> A megoldásokat commitold és pushold a GitHub repódba.

---

### 11.1 – Naplózó middleware ⭐
Készíts middleware-t, amely kiírja a konzolra: `[METHOD] /utvonal - STATUS (0.123s)`. Teszteld néhány kéréssel.

### 11.2 – CORS beállítás ⭐⭐
Konfiguráld a CORS-t, hogy a `http://localhost:3000` és `http://localhost:5173` eredetek engedélyezettek legyenek. Teszteld: mi történik, ha egy nem engedélyezett eredetről próbálsz kérést küldeni?

### 11.3 – Request ID middleware ⭐⭐
Készíts middleware-t, amely egyedi `X-Request-ID` headert ad minden válaszhoz (uuid4). Ellenőrizd a böngésző DevTools Network fülén.

### 11.4 – Lifespan ⭐⭐
Használd a `@asynccontextmanager` és `lifespan` mintát az alkalmazás indulási és leállási eseményeinek kezelésére. Írasd ki: "API elindult" és "API leállt".

### 11.5 – Rate limiting ⭐⭐⭐
Készíts egyszerű rate limiting middleware-t: egy dictionary-ban tárold az IP címeket és a kérések számát. Ha egy IP 60 másodperc alatt 100-nál több kérést küld, adj vissza 429-es hibát.
