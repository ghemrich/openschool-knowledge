# Projekt Labor — Tanterv

## Áttekintés

| Tulajdonság | Érték |
|-------------|-------|
| Előfeltétel | Backend FastAPI kurzus |
| Modulok száma | 7 |
| Tech stack | FastAPI, PostgreSQL, Docker Compose, Astro, nginx, GitHub Actions |
| Végeredmény | Működő, éles környezetben futó, open source oktatási platform |
| Platform repó | `openschool-platform` (külön repó) |

## Célok

1. Egy valódi webalkalmazás felépítése az ötlettől az éles üzemig
2. Projekt struktúra és fejlesztési munkafolyamatok elsajátítása
3. DevOps alapok: Docker Compose, CI/CD, VPS deploy, SSL
4. OAuth és JWT alapú autentikáció implementálása
5. Külső API integráció (GitHub API)
6. Frontend fejlesztés statikus oldal generátorral (Astro)
7. Open source projekt indítása és közösségépítés

## Tanulási útvonal

```
Backend 13 kurzus (előfeltétel)
        │
        ▼
┌─────────────────────────────────────────────────────────┐
│  Modul 1: Projekt indítás                               │
│  Docker Compose + FastAPI + PostgreSQL + CI + Alembic    │
│  Eredmény: futó, tesztelhető projekt                    │
└─────────────────────┬───────────────────────────────────┘
                      │
        ┌─────────────┴─────────────┐
        ▼                           ▼
┌───────────────────┐   ┌───────────────────────┐
│  Modul 2          │   │  Modul 5              │
│  Felhasználó-     │   │  Frontend (Astro)     │
│  kezelés (OAuth)  │   │                       │
└────────┬──────────┘   └───────────┬───────────┘
         │                          │
         ▼                          │
┌───────────────────┐               │
│  Modul 3          │               │
│  Kurzusok és      │               │
│  haladás          │               │
└────────┬──────────┘               │
         │                          │
         ▼                          │
┌───────────────────┐               │
│  Modul 4          │               │
│  Tanúsítvány      │               │
└────────┬──────────┘               │
         │                          │
         └──────────┬───────────────┘
                    ▼
┌─────────────────────────────────────────────────────────┐
│  Modul 6: Éles üzem                                     │
│  nginx, SSL, GitHub Actions CD, VPS deploy               │
│  Eredmény: a platform fut a domain-en                    │
└─────────────────────┬───────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────┐
│  Modul 7: Open source és közösség                       │
│  CONTRIBUTING.md, issue/PR templates, közösségi modellek │
│  Eredmény: a projekt kész kontribútorok fogadására      │
└─────────────────────────────────────────────────────────┘
```

> **Megjegyzés:** A Modul 5 (Frontend) párhuzamosan is építhető a Modul 2–4-gyel. A backend és a frontend egymástól függetlenül fejleszthető, amíg az API szerződés (endpoint-ok) tiszta.

## Platform architektúra

```
openschool.hu
     │
     ▼
┌─────────┐
│  nginx  │ ← SSL (Cloudflare), reverse proxy
└────┬────┘
     │
     ├── /api/*  ──→  FastAPI backend (Docker)
     │                    │
     │                    ├── PostgreSQL (Docker)
     │                    └── GitHub API
     │
     └── /*      ──→  Astro frontend (static files)
```

## Verifikációs tesztek

Minden modulhoz tartozik egy **verifikációs tesztcsomag**, ami kívülről ellenőrzi a modul végeredményét.

| Típus | Ki írja? | Hol van? | Cél |
|-------|----------|----------|-----|
| Saját tesztek | A tanuló (a modul feladataként) | `backend/tests/` | Tanulás, TDD gyakorlat |
| Verifikációs tesztek | A kurzusanyag adja | `tesztek/modul-XX/` | Végeredmény ellenőrzése |

**Használat:**

```bash
# Az openschool repóból másold a teszteket a platform repóba
cp -r courses/projekt-labor/tesztek/ /path/to/openschool-platform/tesztek/

# Futtasd az adott modul tesztjeit
cd openschool-platform
pytest tesztek/modul-01/ -v
```

Minden teszt hibaüzenete elmondja, mi hiányzik és mit kell csinálni. A verifikációs tesztek nem helyettesítik a saját teszteket — kiegészítik.

→ Részletes útmutató: [../../tesztek/README.md](../../tesztek/README.md)

## Modulok részletesen

### Modul 1 — Projekt indítás

A platform alapjainak felépítése. A modul végére egy üres, de teljesen konfigurált projekt áll rendelkezésre: fut Docker Compose-ban, van benne adatbázis, tesztek futnak, és minden push-ra lefut a CI.

**Témák:**
- Repó létrehozása, mappastruktúra megtervezése
- Docker Compose: FastAPI + PostgreSQL + nginx
- Alembic migrációs keretrendszer beállítása
- pytest + TestClient + SQLite in-memory teszt konfig
- GitHub Actions CI pipeline (lint + teszt minden push-ra)
- Fejlesztői dokumentáció (README, .env.example, Makefile)
- Pre-commit hooks (ruff)

**Eredmény:** `docker compose up` → fut a backend, elérhető a health check endpoint, a tesztek zöldek, a CI pipeline zöld.

---

### Modul 2 — Felhasználókezelés

GitHub OAuth alapú autentikáció, JWT session kezelés, és szerepkör-rendszer.

**Témák:**
- GitHub OAuth 2.0 flow megértése és implementálása
- User modell + Alembic migráció
- JWT token pár (access + refresh)
- Login/logout/me API endpoint-ok
- Szerepkörök: tanuló, mentor, admin
- Auth middleware (Depends)
- Tesztek: mock OAuth, védett endpoint-ok

**Eredmény:** A felhasználó tud GitHub-bal belépni, és a rendszer tudja, ki ő és milyen szerepköre van.

---

### Modul 3 — Kurzusok és haladás

Kurzusmodellek, beiratkozás, és automatikus haladáskövetés a GitHub API-n keresztül.

**Témák:**
- Course, Module, Exercise adatmodellek
- Kurzus CRUD (admin) és beiratkozás API
- GitHub API integráció: workflow run-ok lekérdezése
- Progress tracking logic: melyik exercise repóban van zöld pipeline
- Dashboard endpoint-ok: összesített haladás
- Background task vagy scheduled job: periodikus GitHub API polling
- Rate limiting kezelése (GitHub API korlátok)

**Eredmény:** A beiratkozott felhasználó látja, hány feladatot teljesített, és a rendszer automatikusan frissíti a GitHub repók állapota alapján.

---

### Modul 4 — Tanúsítvány rendszer

Automatikus tanúsítvány generálás kurzus befejezésekor, verifikálható URL-lel.

**Témák:**
- Completion logika: mikor tekinthető befejezettnek egy kurzus
- Certificate adatmodell (egyedi ID, felhasználó, kurzus, dátum)
- PDF generálás (fpdf2)
- QR kód generálás a verifikációs URL-lel
- Publikus verification endpoint: `/verify/{cert_id}`
- Tanúsítvány sablon tervezés

**Eredmény:** A kurzust befejező felhasználó automatikusan kap egy PDF tanúsítványt, amit bárki ellenőrizhet a verifikációs URL-en.

---

### Modul 5 — Frontend

Astro-val épített statikus weboldal, amely megjeleníti a kurzusokat és a felhasználói dashboardot.

**Témák:**
- Astro projekt setup és struktúra
- Markdown → HTML rendering (kurzus tartalmak az OpenSchool repóból)
- Landing page: mi az OpenSchool, hogyan működik, kurzuslista
- GitHub OAuth login gomb és session kezelés (API hívások)
- Dashboard oldal: haladás, befejezett kurzusok, tanúsítványok
- Reszponzív design
- Build és Docker integráció

**Eredmény:** Az openschool.hu-n megjelenik a teljes weboldal: kurzusok böngészése, belépés, haladás követése.

---

### Modul 6 — Éles üzem

A platform kihelyezése a VPS-re, domain beállítás, HTTPS, és automatikus deploy.

**Témák:**
- nginx konfiguráció: reverse proxy (API + static files)
- SSL beállítás Cloudflare-rel
- Docker Compose production konfig (.env, restart policy, volumes)
- GitHub Actions CD: push to main → SSH → docker compose pull + up
- Staging vs production környezet elkülönítése
- Health check endpoint és alap monitoring
- PostgreSQL backup stratégia (cron + pg_dump)
- Logok kezelése

**Eredmény:** A platform él a domain-en, HTTPS-sel, és minden main-re push-olt kód automatikusan kitelepül.

---

### Modul 7 — Open source és közösség

A projekt előkészítése arra, hogy mások is hozzájáruljanak.

**Témák:**
- LICENSE kiválasztása (MIT / Apache 2.0)
- CONTRIBUTING.md: hogyan nyiss issue-t, hogyan küldj PR-t
- Issue template-ek (bug report, feature request)
- PR template (mit változtat, hogyan teszteld)
- Branch stratégia: main + feature branches, kötelező PR review
- Közösségi szerepkörök: tanuló → kontribútor → mentor → maintainer
- GitHub Discussions vagy Discord integráció
- First-timer friendly issue-k címkézése (`good first issue`)

**Eredmény:** A repó készen áll arra, hogy Backend 13 végzősök (vagy bárki más) hozzájáruljanak. A munkafolyamat dokumentált, az első PR-ek írásához van útmutató.
