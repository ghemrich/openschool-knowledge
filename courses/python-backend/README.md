# Backend (FastAPI) kurzus – 13. évfolyam

25 hetes backend fejlesztés kurzus FastAPI keretrendszerrel, felnőttek és középiskolai diákok számára, GitHub Classroom integrációval és automatizált értékeléssel.

## Mappaszerkezet

| Mappa | Tartalom |
|-------|----------|
| [`doksik/`](doksik/) | Összes dokumentáció (diákok, tanár, tanterv) |
| [`vizsgak/`](vizsgak/) | Vizsgavariánsok (feladatlapok, értékelések, megoldások, forrásfájlok) |
| [`github-classroom/`](github-classroom/) | GitHub Classroom template repók (heti házi + vizsgák) |

## Gyors navigáció

- **Diákoknak:** [Leckék](doksik/diakok/leckek/) · [Feladatok](doksik/diakok/feladatok/)
- **Tanárnak:** [Tanári útmutató](doksik/tanar/tanari-utmutato.md) · [GitHub Classroom útmutató](doksik/tanar/github-classroom-utmutato.md) · [Értékelési módszertan](doksik/tanar/ertekeles-modszertan.md)
- **Tanterv:** [25 hetes tanterv](doksik/tanterv/tanterv.md)
- **Vizsgák:** [4 variáns](vizsgak/) (todo-api, blog-api, webshop-api, recept-api)

## Összefoglaló

- **Időtartam:** 25 hét (0–24), heti 6 óra
- **Nyelv:** Python 3.10+, FastAPI keretrendszer
- **Adatbázis:** PostgreSQL 16 (Docker), SQLAlchemy ORM, Alembic
- **Tesztelés:** pytest + TestClient, SQLite in-memory mock DB
- **Vizsga:** 60 pont, 240 perc, 5 feladat (10 + 20 + 10 + 10 + 10 pont)
- **Beadás:** GitHub Classroom (automatikus értékelés)
- **Variánsok:** 4 db (A – todo-api, B – blog-api, C – webshop-api, D – recept-api)
