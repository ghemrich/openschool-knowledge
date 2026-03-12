# Hibaelhárítás és GYIK

Ez az útmutató összegyűjti a leggyakoribb problémákat és megoldásaikat, kurzusonként csoportosítva.

---

## Tartalomjegyzék

- [Általános problémák](#általános-problémák)
- [Git és GitHub](#git-és-github)
- [GitHub Classroom](#github-classroom)
- [Python Alapok kurzus](#python-alapok-kurzus)
- [Backend FastAPI kurzus](#backend-fastapi-kurzus)
- [Docker](#docker)
- [Discord](#discord)

---

## Általános problémák

| Probléma | Megoldás |
|----------|----------|
| A terminálban „command not found" | A program nincs telepítve, vagy nincs a PATH-ban. Lásd: [Környezet beállítás](kornyezet-beallitas.md) |
| VS Code nem ismeri fel a Python fájlt | Telepítsd a Python kiterjesztést VS Code-ban (`ms-python.python`) |
| A fájl mentve van, de a változás nem látszik | Ellenőrizd, hogy a helyes fájlt szerkeszted-e (nézd meg a fájl nevét és mappáját) |

---

## Git és GitHub

| Probléma | Megoldás |
|----------|----------|
| `fatal: not a git repository` | Nem egy Git repó mappájában vagy. Használd a `cd` parancsot, hogy belépj a repó mappájába. |
| `nothing to commit` | Nem változtattál semmit, vagy már commitoltad a változásokat. Ellenőrizd: `git status` |
| `failed to push` / `rejected` | Valaki módosította a repót. Futtasd: `git pull --rebase` majd `git push` |
| `Permission denied (publickey)` | Az SSH kulcsod nincs beállítva, vagy nem a megfelelő GitHub fiókhoz tartozik. Ellenőrizd: `ssh -T git@github.com` |
| Nem tudom, mit commitoljak | `git add .` → `git commit -m "leíró üzenet"` → `git push` |
| Rossz fájlokat commitoltam | `git reset HEAD~1` visszavonja az utolsó commitot (a fájlok megmaradnak) |

---

## GitHub Classroom

| Probléma | Megoldás |
|----------|----------|
| A Classroom link „404 Not Found" | Nem vagy bejelentkezve GitHubra. Jelentkezz be, majd próbáld újra a linket. |
| „You don't have access" | Nem vagy tagja a GitHub szervezetnek. Kérd a mentorod, hogy hívjon meg. |
| Nem lát semmit a repóban | Valószínűleg nem klónozta le. Használd: `git clone <repó URL>` |
| Commitolt, de nem pusholt | Futtasd: `git push`. Ellenőrizd a GitHub felületen, hogy megjelent-e. |
| A tesztek nem futnak le | Ellenőrizd, hogy a fájljaid a **gyökérmappában** vannak-e (nem egy almappában). |
| Lokálisan működik, Actions-ben nem | A tesztek más környezetben futnak. Ellenőrizd: nem használsz-e abszolút fájlutat? Az `encoding="utf-8"` megvan? |
| Deadline után pusholt | A GitHub mutatja az utolsó commit időpontját. Egyeztesd a mentorral. |
| A kód más gépen nem fut | Valószínűleg abszolút fájlútvonal probléma. Használj relatív útvonalat. |

---

## Python Alapok kurzus

| Probléma | Megoldás |
|----------|----------|
| `SyntaxError` ékezetes változóneveknél | Kerüld az ékezetes változóneveket, használj ASCII neveket (pl. `nev` és ne `név`) |
| `FileNotFoundError` | A `.txt`/`.csv` fájl nem ugyanabban a mappában van, mint a `.py` fájl. Mozgasd egy helyre. |
| `UnicodeDecodeError` | Hiányzik az `encoding="utf-8"` paraméter a `open()` hívásnál: `open("fajl.txt", encoding="utf-8")` |
| `ModuleNotFoundError: fgv` | A `fgv.py` és a főprogram nem ugyanabban a mappában van |
| `TypeError: can't concat str to int` | Elfelejtett típuskonverzió. Használj `int()` a számokhoz vagy `str()` a szövegekhez. |
| `NameError: name 'x' is not defined` | A változó nincs definiálva az adott hatókörben, elírtad a nevét, vagy a függvényen kívül hoztad létre. |
| `IndentationError` | Nem egyenletes a behúzás. Használj **4 szóközt** (ne tabot). VS Code-ban: „Convert Indentation to Spaces" |
| `IndexError: list index out of range` | A lista rövidebb, mint gondoltad. Ellenőrizd a lista hosszát `len()` függvénnyel. |

---

## Backend FastAPI kurzus

| Probléma | Megoldás |
|----------|----------|
| `ModuleNotFoundError: No module named 'fastapi'` | A `venv` nincs aktiválva. Linux: `source venv/bin/activate`, Windows: `venv\Scripts\activate` |
| `uvicorn: command not found` | Telepítsd: `pip install uvicorn` (ellenőrizd, hogy a venv aktív-e) |
| `sqlalchemy.exc.OperationalError: connection refused` | A PostgreSQL konténer nem fut. Indítsd el: `docker compose up -d` |
| `alembic.util.exc.CommandError` | `alembic upgrade head` nem futott le, vagy a `DATABASE_URL` hibás |
| `422 Unprocessable Entity` | A request body nem felel meg a Pydantic sémának. Ellenőrizd a JSON struktúrát és a mezők típusait. |
| `401 Unauthorized` | Hiányzó vagy lejárt JWT token. Jelentkezz be újra, és használd az új tokent. |
| `pydantic.ValidationError` | Érvénytelen adat típus a Pydantic modellben. Ellenőrizd, hogy a megfelelő típusú adatot küldöd. |
| `ImportError: cannot import name 'get_db'` | A `database.py` nincs a megfelelő helyen, vagy rossz az import path |
| `psycopg2` telepítési hiba | Linux: `sudo apt install libpq-dev python3-dev`. Windows: használd a `psycopg2-binary` csomagot. |
| GitHub Classroom tesztek FAIL, de lokálisan PASS | A tesztek SQLite in-memory DB-t használnak. Ellenőrizd a `conftest.py`-t és a `dependency_overrides` beállítást. |

---

## Docker

| Probléma | Megoldás |
|----------|----------|
| `docker: command not found` | A Docker nincs telepítve. Lásd: [Környezet beállítás — Docker](kornyezet-beallitas.md) |
| `permission denied` (Linux) | A felhasználó nincs a `docker` csoportban. Futtasd: `sudo usermod -aG docker $USER`, majd jelentkezz ki és be. |
| `permission denied` (Windows) | A Docker Desktop nem fut, vagy nem rendszergazdaként indítottad. |
| `port is already allocated` | Egy másik program (vagy egy régi konténer) foglalja a portot. Állítsd le: `docker compose down`, vagy változtasd meg a portot. |
| `docker compose up` hibát dob | Ellenőrizd a `docker-compose.yml` szintaxisát. YAML-ben a behúzás számít (szóközökkel, nem tabbal). |
| A konténer elindul, de azonnal leáll | Nézd meg a logokat: `docker compose logs <szolgáltatás_neve>` |
| A PostgreSQL konténer nem indul | Ellenőrizd a környezeti változókat (`.env` fájl): `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_DB` |

---

## Discord

| Probléma | Megoldás |
|----------|----------|
| Nem tudok csatlakozni a szerverhez | Ellenőrizd a meghívó link érvényességét. Ha lejárt, kérj új linket. |
| Nem látom a kurzus csatornáit | Nem kaptad meg a megfelelő szerepkört. Kérd a mentort, hogy adja hozzá. |
| Nem tudok írni a `#közlemények` csatornába | Ez szándékos — oda csak mentorok írhatnak. |
| Túl sok szál, nem találok semmit | Használd a Discord keresőt (Ctrl+F), és szűrj csatornára vagy felhasználóra. |

---

## Általános hibaelhárítási módszer

Ha valami nem működik, kövesd ezt a sorrendet:

1. **Olvasd el a hibaüzenetet** — legtöbbször pontosan megmondja, mi a baj
2. **Ellenőrizd a fájlneveket** — elírtad? Rossz mappában van?
3. **Ellenőrizd a környezetet** — a venv aktív? A Docker fut? A megfelelő mappában vagy?
4. **Keresd meg a hibaüzenetet online** — másold be a hibaüzenetet a keresőbe
5. **Kérdezz a Discord csatornán** — [hogyan kérdezz jól?](kozossegi-utmutato.md)

---

**Kapcsolódó útmutatók:**
- [Környezet beállítás](kornyezet-beallitas.md)
- [Git puskalap](git-puskalap.md)
- [Docker puskalap](docker-puskalap.md)
- [GitHub Classroom — Tanuló útmutató](github-classroom-tanulo-utmutato.md)
