# Modul 5 — Frontend

## Cél

Astro-val épített statikus weboldal, amely megjeleníti a kurzusokat, kezeli a bejelentkezést, és mutatja a haladást. A modul végére:

- Landing page: mi az OpenSchool, kurzuslista
- GitHub OAuth belépés a frontendről
- Dashboard: haladás, tanúsítványok
- Reszponzív, mobilon is használható design

> **Megjegyzés:** Ez a modul párhuzamosan is építhető a Modul 2–4-gyel, amíg az API endpoint-ok meg vannak határozva.

## 5.1 Astro projekt setup

[Astro](https://astro.build/) egy statikus oldal generátor, ami gyors, könnyű, és jól kezeli a markdown tartalmakat.

```bash
npm create astro@latest frontend
cd frontend
npm install
```

**Mappastruktúra:**
```
frontend/
├── astro.config.mjs
├── package.json
├── Dockerfile
├── public/
│   └── favicon.svg
├── src/
│   ├── layouts/
│   │   └── Layout.astro
│   ├── pages/
│   │   ├── index.astro          # Landing page
│   │   ├── courses/
│   │   │   ├── index.astro      # Kurzuslista
│   │   │   └── [slug].astro     # Kurzus részletek
│   │   ├── dashboard.astro      # Haladás
│   │   ├── login.astro          # Belépés
│   │   └── verify/
│   │       └── [id].astro       # Tanúsítvány verifikáció
│   ├── components/
│   │   ├── Header.astro
│   │   ├── Footer.astro
│   │   ├── CourseCard.astro
│   │   └── ProgressBar.astro
│   └── styles/
│       └── global.css
```

**Feladat:**
- Hozd létre az Astro projektet a `frontend/` mappában
- Állítsd be az alap layout-ot (fejléc, lábléc, navigáció)
- Adj hozzá egy Dockerfile-t az Astro buildhez

## 5.2 Landing page

Az openschool.hu főoldala. Tartalma:

1. **Hero szekció:** rövid bemutatkozás — mi az OpenSchool, kinek szól
2. **Hogyan működik:** 3 lépés (beiratkozás → feladatok → tanúsítvány)
3. **Kurzuslista:** elérhető kurzusok kártya nézetben
4. **CTA:** "Kezdd el ingyen" gomb → belépés / kurzuslista

**Feladat:**
- Implementáld az `index.astro` oldalt
- A kurzuslistát az API-ból töltsd be (`/api/courses`)
- A dizájn legyen letisztult, professzionális

## 5.3 Kurzus oldalak

**Kurzuslista (`/courses`):**
- Kártya nézet: kurzus neve, rövid leírás, modul szám
- Szűrés/keresés opcionális

**Kurzus részletek (`/courses/{slug}`):**
- Kurzus leírás
- Modulok és feladatok listája (fa struktúra)
- Ha a felhasználó beiratkozott: haladás jelölők
- "Beiratkozás" gomb (ha nincs beiratkozva)

**Feladat:**
- Implementáld mindkét oldalt
- A kurzus tartalom (leírás, modulok) az API-ból jön
- A beiratkozás gomb hívja a `POST /api/courses/{id}/enroll` endpoint-ot

## 5.4 Autentikáció

A frontend az API-n keresztül kezeli a belépést:

1. Felhasználó kattint a "Belépés GitHub-bal" gombra
2. Frontend átirányít → `GET /api/auth/login` → GitHub OAuth
3. GitHub visszairányít → `/api/auth/callback` → JWT generálás
4. Backend visszairányítja a frontendre a token-nel
5. Frontend elmenti az access token-t (localStorage vagy memória)

**Session kezelés:**
- Az access token-t minden API hívás `Authorization: Bearer` fejlécében küldd
- Ha lejárt → hívd a `/api/auth/refresh` endpoint-ot
- Ha a refresh is lejárt → irányítsd át a login oldalra

**Feladat:**
- Implementáld a login flow-t a frontenden
- Hozz létre egy `api.js` utility-t az API hívásokhoz (fetch wrapper + token kezelés)
- A navigációban jelenjen meg a felhasználó neve + avatar (bejelentkezve) vagy "Belépés" gomb

## 5.5 Dashboard

A bejelentkezett felhasználó saját oldala:

**Tartalom:**
- Beiratkozott kurzusok listája
- Kurzusonként: progress bar (pl. "8/12 feladat — 67%")
- Befejezett kurzusok tanúsítvány letöltés gombbal
- Ha egy kurzus kész és nincs tanúsítvány → "Tanúsítvány igénylése" gomb

**API hívások:**
- `GET /api/me/dashboard` → kurzusok + haladás
- `GET /api/me/certificates` → tanúsítványok
- `POST /api/me/courses/{id}/certificate` → tanúsítvány igénylése
- `GET /api/me/certificates/{cert_id}/pdf` → PDF letöltése

**Feladat:**
- Implementáld a dashboard oldalt
- A progress bar vizuálisan jelezze a haladást
- A tanúsítvány igénylés gomb csak akkor legyen aktív, ha a kurzus kész

## 5.6 Tanúsítvány verifikáció

Publikus oldal: `/verify/{cert_id}`

- Bárki megnyithatja (nem kell belépés)
- Ha érvényes: megjelenik a név, kurzus, dátum, tanúsítvány ID
- Ha nem érvényes: "Érvénytelen tanúsítvány"

**API hívás:** `GET /api/verify/{cert_id}`

**Feladat:**
- Implementáld a verifikációs oldalt
- Letisztult, egyszerű design — ez egy "hivatalos" oldal

## 5.7 Reszponzív design

A weboldal legyen használható:
- Desktop (1200px+)
- Tablet (768px – 1199px)
- Mobil (320px – 767px)

**Feladat:**
- Használj CSS media query-ket vagy modern CSS-t (container queries, flex/grid)
- A navigáció mobilon hamburger menü legyen
- Teszteld a három méretben

## 5.8 Docker integráció

Az Astro build eredménye statikus fájlok — nginx-szel szolgáljuk ki.

```dockerfile
# frontend/Dockerfile
FROM node:20-alpine AS build
WORKDIR /app
COPY package*.json .
RUN npm ci
COPY . .
RUN npm run build

FROM nginx:alpine
COPY --from=build /app/dist /usr/share/nginx/html
```

**Feladat:**
- Írd meg a frontend Dockerfile-t (multi-stage build)
- Add hozzá a `docker-compose.yml`-hez:
  ```yaml
  frontend:
    build: ./frontend
    # nginx szolgálja ki a statikus fájlokat
  ```
- Frissítsd az nginx konfigot, hogy az API és a frontend is elérhető legyen

## Háttéranyag

Ezeket nem kell elejétől végig elolvasni — használd referenciaként, amikor az adott témánál tartasz.

| Téma | Link | Miért hasznos |
|------|------|---------------|
| Astro dokumentáció | [docs.astro.build](https://docs.astro.build/) | Astro alapok, oldalak, komponensek, layout-ok |
| Astro + API integráció | [docs.astro.build/en/guides/data-fetching](https://docs.astro.build/en/guides/data-fetching/) | Adatlekérés backend API-ból |
| Static Site Generation | [docs.astro.build/en/guides/content-collections](https://docs.astro.build/en/guides/content-collections/) | Statikus oldal generálás és tartalom kezelés |
| CSS Flexbox/Grid | [css-tricks.com/snippets/css/a-guide-to-flexbox](https://css-tricks.com/snippets/css/a-guide-to-flexbox/) | Reszponzív layout-ok alapjai |
| Fetch API | [developer.mozilla.org/en-US/docs/Web/API/Fetch_API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API) | Frontend → Backend API hívások |
| Docker multi-stage build | [docs.docker.com/build/building/multi-stage](https://docs.docker.com/build/building/multi-stage/) | Astro build + nginx egy Dockerfile-ban |

## Verifikációs tesztek

A modul végén futtasd a verifikációs teszteket:

```bash
cd openschool-platform
pytest tesztek/modul-05/ -v
```

**Mit ellenőriznek a tesztek:**

| Tesztfájl | Ellenőrzések |
|-----------|---------------|
| `test_pages.py` | `frontend/` mappa létezik; `package.json` tartalmazza az Astro-t; `astro.config.mjs` létezik; `src/pages/` és landing page létezik; layout és components mappák; frontend Dockerfile létezik |

> **Megjegyzés:** A frontend verifikációs tesztek a **struktúrát** ellenőrzik (fájlok létezése, konfiguráció), nem a vizuális megjelenést. A részponzív design és a felhasználói élmény manuális tesztelést igényel.

## Ellenőrzőlista

- [ ] Astro projekt fut: `npm run dev` → localhost elérhető
- [ ] Landing page: bemutatkozás + kurzuslista
- [ ] GitHub OAuth belépés működik a frontendről
- [ ] Dashboard: haladás, tanúsítványok
- [ ] Kurzus oldalak: modulok, feladatok, beiratkozás
- [ ] Tanúsítvány verifikációs oldal
- [ ] Reszponzív design: desktop, tablet, mobil
- [ ] Docker build: Astro → statikus fájlok → nginx
- [ ] `pytest tesztek/modul-05/ -v` → minden zöld (verifikációs tesztek)
