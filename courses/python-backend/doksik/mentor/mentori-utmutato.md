# Mentori útmutató – Backend FastAPI

## Kurzus felépítése

A kurzus 25 hétre van bontva (0–24. hét, heti 6 óra = 3 × 2 óra), és fokozatosan építi fel a vizsgához szükséges tudást. A vizsga beadása **GitHub Classroom**-on keresztül történik, automatikus pytest értékeléssel.

**Kapcsolódó dokumentumok:**
- Tanterv: [`doksik/tanterv/tanterv.md`](../tanterv/tanterv.md)
- Tanuló leckék: [`doksik/tanulok/leckek/`](../tanulok/leckek/)
- Tanuló feladatok: [`doksik/tanulok/feladatok/`](../tanulok/feladatok/)
- GitHub Classroom útmutató: [`github-classroom-utmutato.md`](github-classroom-utmutato.md)
- Értékelési módszertan: [`ertekeles-modszertan.md`](ertekeles-modszertan.md)

---

## Heti ütemterv és javaslatok

### 0. hét: Git, GitHub, parancssor alapok
- **Cél:** A tanulók beállítják a fejlesztői környezetet, ismétlik a Git-et, és megismerik a GitHub Classroom workflow-t
- **Tipp:** Előre készíts egy GitHub Classroom szervezetet és egy próba-feladatot. Egyes résztvevők régebben tanulták a Git-et — számíts arra, hogy ismétlésre szükség lesz. **Windowsos tanulóknál** a Git Bash telepítését és a Docker Desktop beállítását külön segítsd.
- **Beállítás:** Lásd [`github-classroom-utmutato.md`](github-classroom-utmutato.md)
- **Házi feladat:** Próba repo: klónozás, branch létrehozása, merge, push

### 1. hét: Python ismétlés, virtuális környezet
- **Cél:** A tanulók kényelmesen írjanak Python programokat és értsék a `venv` jelentőségét
- **Tipp:** A virtuális környezet koncepció sok tanulónak új — dedikálj rá egy teljes órapárt. Mutasd meg, mi történik `venv` nélkül, ha két projekt különböző verziójú csomagokat igényel.
- **Házi feladat:** Python gyakorló feladatok, `venv` készítése, `requirements.txt` generálása

### 2. hét: FastAPI bevezetés
- **Cél:** Az első működő REST API elkészítése
- **Tipp:** A Swagger UI (`/docs`) nagy motiváló erő — az óra elején mutasd meg az elkészült eredményt, utána építsétek fel lépésről lépésre.
- **Házi feladat:** Hello API: 3-4 végpont, Swagger UI-ban tesztelés

### 3. hét: Útvonalak és paraméterek
- **Cél:** Path és query paraméterek, validáció
- **Tipp:** A `Path()` és `Query()` validátorok mindig lenyűgözik a tanulókat — élőben mutasd meg, hogyan reagál a Swagger hibás bemenetre.
- **Házi feladat:** Terméklistázó API path és query paraméterekkel

### 4. hét: Request body és Pydantic
- **Cél:** POST/PUT/DELETE végpontok, Pydantic validáció
- **Tipp:** Ez kulcsfontosságú hét. A Pydantic modellek végigkísérik a kurzust — itt kell alaposan megtanulniuk.
- **Házi feladat:** Teljes CRUD API memóriában (lista/szótár)

### 5. hét: Response modellek és hibakezelés
- **Cél:** `response_model`, `HTTPException`, státuszkódok
- **Tipp:** A különböző create/read sémákat érdemes egy konkrét példán (pl. User) megmutatni — miért nem akarjuk, hogy a jelszó visszajöjjön a válaszban.
- **Házi feladat:** Robusztus API hibakezeléssel, különböző response modellekkel

### 6. hét: Dependency Injection és projektstruktúra
- **Cél:** `Depends()`, `APIRouter`, `BaseSettings`, projekt szervezés
- **Tipp:** A DI koncepció absztrakt — konkrét példákkal mutasd meg (pl. pagination, API key ellenőrzés). Az `APIRouter` bevezetése a jó alkalom a projekt átstrukturálására.
- **Házi feladat:** Strukturált API projekt `app/` mappával, routerekkel

### 7. hét: Docker és PostgreSQL
- **Cél:** Docker alapok, PostgreSQL konténer, Docker Compose
- **Tipp:** **Telepítés/beállítás — szánj rá időt!** A Docker telepítése kihívás lehet (Linuxon felhasználó hozzáadása a `docker` csoporthoz, Windowson Docker Desktop + WSL2 beállítás). Készíts egy lépésről lépésre telepítési segédletet mindkét rendszerre. A `docker compose up -d` utáni `psql` csatlakozás az első „varázslat” — mutasd élőben.
- **Házi feladat:** Docker Compose: FastAPI + PostgreSQL, `psql` csatlakozás

### 8. hét: SQLAlchemy ORM
- **Cél:** ORM fogalma, modellek, Alembic migrációk
- **Tipp:** Az ORM fogalom nagy ugrás — érdemes először a „Python objektum = adatbázis sor" analógiával indítani. Az Alembic migrációknál kézzel is mutasd meg, mi történik a háttérben (generált SQL).
- **Házi feladat:** Felhasználó tábla: modell, migráció, psql ellenőrzés

### 9. hét: CRUD műveletek adatbázissal
- **Cél:** `get_db()` dependency, CRUD függvények, router integráció
- **Tipp:** Ez a hét köti össze az eddigi tudást (FastAPI + SQLAlchemy + Pydantic). Érdemes egy komplett példát (pl. Termék entitás) elejétől a végéig felépíteni az órán.
- **Házi feladat:** Teljes CRUD API PostgreSQL-lel

### 10. hét: Authentikáció és JWT
- **Cél:** Jelszó hash-elés, JWT tokenek, védett végpontok
- **Tipp:** A biztonsági fogalmak (hash vs. titkosítás, token vs. session) elméleti háttere fontos — de ne húzd el túlságosan. A `bcrypt` és `python-jose` library-k használata a lényeg. **Figyelem:** soha ne tároljunk plain text jelszavakat a kódpéldákban sem!
- **Házi feladat:** Regisztráció + login + védett profil végpont

### 11. hét: Middleware, CORS, biztonság
- **Cél:** Middleware-ek, CORS beállítás, biztonsági bevált gyakorlatok
- **Tipp:** A CORS-t érdemes élőben demonstrálni: egy egyszerű HTML oldal `fetch()`-csel, ami CORS hiba nélkül/hibával hívja az API-t.
- **Házi feladat:** Logging middleware + CORS beállítás hozzáadása

### 12. hét: Félév összefoglalás, próbavizsga
- **Cél:** Próbavizsga vizsgakörülmények között
- **Tipp:** A próbavizsga **vizsgakörülmények között** zajlik — GitHub Classroom-on keresztül, 120 perc, 60 pont. A próba utáni megbeszélés legalább annyira fontos, mint maga a próba. Tipikus hibákat érdemes közösen elemezni. A próbavizsga GitHub Classroom repója: `het12-felev-osszefoglalas`
- **Házi feladat:** A próbavizsga hiányosságainak pótlása

### 13. hét: Tesztelés alapok, pytest
- **Cél:** `pytest` alapok, fixture-ök, parametrizálás
- **Tipp:** A tanulók eddig nem írtak automatikus teszteket — az `assert` egyszerűségével érdemes kezdeni. A fixture fogalma először nehéz lehet — használj analógiát (pl. egy konyha előkészítése főzés előtt).
- **Házi feladat:** Python utility függvények tesztelése (pytest)

### 14. hét: FastAPI tesztelés TestClient-tel
- **Cél:** `TestClient` használata, GET/POST/auth tesztelés
- **Tipp:** A TestClient a `requests` library-hez hasonlóan működik — ha ismerik, könnyebb az áttérés. Mutasd meg, hogyan futnak ugyanazok a tesztek, amiket eddig Swagger-ben manuálisan csináltak.
- **Házi feladat:** CRUD végpontok tesztjei TestClient-tel

### 15. hét: Adatbázis mockolás tesztekhez
- **Cél:** SQLite in-memory mock DB, `dependency_overrides`, conftest.py
- **Tipp:** **Ez a kurzus egyik legfontosabb hete.** A GitHub Classroom CI-ban nincs PostgreSQL — ezért az SQLite in-memory megoldás elengedhetetlen. A `dependency_overrides[get_db]` minta egyszerű, de precízen kell bemutatni. A conftest.py fájlt érdemes közösen megírni.
- **Házi feladat:** Teljes API tesztelése mock DB-vel

### 16. hét: Haladó tesztelés
- **Cél:** Parametrizálás, negatív tesztek, coverage, factory fixture-ök
- **Tipp:** A `pytest --cov` kimenete motiváló — a tanulók versenyezhetnek a coverage százalékban. A negatív tesztek (404, 422, 401) legalább annyira fontosak, mint a pozitívak.
- **Házi feladat:** Coverage javítás, negatív tesztek írása

### 17. hét: Fájlkezelés és feltöltés
- **Cél:** `UploadFile`, `StaticFiles`, képfeltöltés, CSV feldolgozás
- **Tipp:** A fájlfeltöltés tesztelése `io.BytesIO`-val történik — ezt élőben mutasd meg. A méret- és típusellenőrzés biztonsági szempontból fontos.
- **Házi feladat:** Kép feltöltés API végpont + teszt

### 18. hét: Background Tasks és WebSocket
- **Cél:** `BackgroundTasks`, WebSocket echo/broadcast
- **Tipp:** Az email küldés szimuláció (fájlba írás) jó bevezetés — ne használj valódi SMTP-t az órán. A WebSocket tesztelése a böngésző konzolból is megmutatható.
- **Házi feladat:** Háttérfeladat + egyszerű WebSocket endpoint

### 19. hét: Docker Compose haladó, éles üzem
- **Cél:** Production Dockerfile, multi-stage build, `docker-compose.yml` bővítés, health check, `entrypoint.sh`
- **Tipp:** A multi-stage build koncepciója fontos — mutasd meg az image méret különbséget. Az `entrypoint.sh` (alembic upgrade + uvicorn start) tipikus production minta.
- **Házi feladat:** Production-ready Docker setup készítése

### 20. hét: CI/CD és GitHub Actions
- **Cél:** CI/CD fogalmak, GitHub Actions workflow, lint, coverage
- **Tipp:** A `.github/workflows/ci.yml` fájlt közösen írjátok meg. Mutasd meg, hogyan futnak le a tesztek automatikusan push után.
- **Házi feladat:** CI workflow hozzáadása a projekthez

### 21. hét: Projekt tervezés
- **Cél:** API tervezés, adatmodell, endpoint terv, projekt váz
- **Tipp:** 4 téma közül választhatnak (Todo, Blog, Webshop, Recept API). Érdemes mindenkit arra bátorítani, hogy a vizsgaformátumhoz hasonló komplexitásút válasszon. Az adatmodell diagramot papíron is érdemes megrajzolni a tervezési fázisban.
- **Házi feladat:** Projekt váz: mappastruktúra, modellek, alap végpontok

### 22–23. hét: Projekt fejlesztés
- **Cél:** Teljes API implementáció, tesztek, Docker, dokumentáció
- **Tipp:** Ezek a hetek mentori jellegűek — a tanulók önállóan dolgoznak, a mentor segít. Érdemes napi stand-up-ot tartani (mit csináltál, mi a következő, mi blokkol). A tesztek írása ne maradjon a végére — párhuzamosan haladjon a fejlesztéssel.
- **Házi feladat:** Projekt elkészítése, README megírása

### 24. hét: Vizsga
- **Cél:** Szintfelmérő vizsga, 240 perc, 60 pont
- **Tipp:** A vizsga GitHub Classroom-on keresztül zajlik, automatikus pytest értékeléssel. A tanulók SQLite adatbázist használnak (a vizsgán nincs PostgreSQL elérés). A vizsga 5 feladatból áll: sémák+utility, SQLAlchemy CRUD, JWT auth, adatfeldolgozás, Docker+tesztelés.

---

## Vizsgavariánsok

Négy vizsga variáns áll rendelkezésre:

| | A – todo-api | B – blog-api | C – webshop-api | D – recept-api |
|---|---|---|---|---|
| **Feladatlap** | `vizsgak/todo-api/feladat/vizsga.md` | `vizsgak/blog-api/feladat/vizsga.md` | `vizsgak/webshop-api/feladat/vizsga.md` | `vizsgak/recept-api/feladat/vizsga.md` |
| **Értékelés** | `vizsgak/todo-api/feladat/ertekeles.md` | `vizsgak/blog-api/feladat/ertekeles.md` | `vizsgak/webshop-api/feladat/ertekeles.md` | `vizsgak/recept-api/feladat/ertekeles.md` |
| **Forrásfájlok** | `vizsgak/todo-api/forras/` | `vizsgak/blog-api/forras/` | `vizsgak/webshop-api/forras/` | `vizsgak/recept-api/forras/` |
| **Megoldás** | `vizsgak/todo-api/megoldas/` | `vizsgak/blog-api/megoldas/` | `vizsgak/webshop-api/megoldas/` | `vizsgak/recept-api/megoldas/` |

**Különbségek:**
- 1. feladat: Pydantic sémák + utility függvények (todo / blogpost / termék / recept adatokra)
- 2. feladat: SQLAlchemy DB + CRUD API végpontok (todo-k / posztok / termékek / receptek kezelése)
- 3. feladat: JWT autentikáció (regisztráció, login, védett végpontok)
- 4. feladat: Adatfeldolgozás fájlból (feldolgozas.py, 5 függvény)
- 5. feladat: Docker + pytest tesztek (Dockerfile, requirements.txt, 8 teszt)

> **Részletes értékelési módszertan:** lásd [`ertekeles-modszertan.md`](ertekeles-modszertan.md)

---

## Értékelés

Részletes értékelési rendszer, szinthatárok, code review szempontok és szóbeli kérdések: lásd [`ertekeles-modszertan.md`](ertekeles-modszertan.md).

Vizsga és házi feladat kezelése GitHub Classroom-ban: lásd [`github-classroom-utmutato.md`](github-classroom-utmutato.md).

---

## Gyakori tanulói problémák és megoldásuk

A kurzus-specifikus hibák és megoldásaik részletes listáját lásd a központi hibaelhárítási útmutatóban:

- [Hibaelhárítás és GYIK — Backend FastAPI kurzus](../../../../guides/hibaelharitas.md#backend-fastapi-kurzus)
- [Hibaelhárítás és GYIK — Docker](../../../../guides/hibaelharitas.md#docker)
- [Hibaelhárítás és GYIK — Git és GitHub](../../../../guides/hibaelharitas.md#git-és-github)
- [Hibaelhárítás és GYIK — GitHub Classroom](../../../../guides/hibaelharitas.md#github-classroom)

---

## Különbségek a Python Alapok kurzushoz képest

| Szempont | Python Alapok | Backend FastAPI |
|----------|-------------|-------------|
| Időtartam | 13 hét, heti 2 óra | 25 hét, heti 6 óra |
| Nyelv | Python (script) | Python + FastAPI (web API) |
| Adatbázis | Fájlkezelés (txt) | PostgreSQL (Docker) |
| Tesztelés | Shell tesztek (autograding) | pytest (automatikus) |
| Beadás | Shell + Python tesztek | pytest tesztek a GitHub Classroom-ban |
| Vizsga | 40 pont, 90 perc | 60 pont, 240 perc |
| Célcsoport | Kezdők | Haladók (Python előismerettel) |

---

## Ajánlott mentori workflow

### Óra előtt
1. Olvasd át a heti lecke anyagot
2. Készítsd el a GitHub Classroom Assignment-et (ha házi feladat van)
3. Teszteld lokálisan a feladatokat és a megoldásokat

### Óra közben
1. Rövid elméleti bevezető (max 15 perc órapáronként)
2. Élő kód írás (live coding) — a tanulók együtt kódolnak
3. Gyakorlás: a feladatsor 1-2 feladata az órán
4. Kérdések megbeszélése

### Óra után
1. Oszd ki a házi feladat GitHub Classroom linkjét
2. Ellenőrizd a korábbi heti beadásokat
3. Adj visszajelzést (GitHub comment vagy szóban)
