# Verifikációs tesztek

A Projekt Labor minden moduljához tartozik egy verifikációs tesztcsomag. Ezek a tesztek **nem azonosak** a modulok során írt saját tesztekkel — céljuk, hogy **kívülről** ellenőrizzék a modul végeredményét.

## Két típusú teszt

| Típus | Ki írja? | Hol van? | Mikor fut? |
|-------|----------|----------|------------|
| **Saját tesztek** | Te, a modul feladataként | `openschool-platform/backend/tests/` | Fejlesztés közben, CI-ban |
| **Verifikációs tesztek** | A kurzusanyag adja | `openschool-platform/tesztek/` | Modul befejezésekor |

A **saját tesztek** a tanulási folyamat részei — a modul leírás alapján te írod meg őket. A **verifikációs tesztek** olyanok, mint egy vizsgafeladat: mi adjuk, te futtatod a saját kódod ellen.

## Használat

### 1. Másold a teszteket a platform repóba

```bash
# Az openschool repóból másold a tesztek/ mappát az openschool-platform repóba
cp -r courses/projekt-labor/tesztek/ /path/to/openschool-platform/tesztek/
```

### 2. Telepítsd a függőségeket

```bash
cd openschool-platform
pip install pytest pyyaml
pip install -r backend/requirements.txt
```

### 3. Futtasd egy adott modul tesztjeit

```bash
# Modul 1 tesztjei
pytest tesztek/modul-01/ -v

# Modul 2 tesztjei
pytest tesztek/modul-02/ -v

# Összes modul (ha meg akarod nézni az összképet)
pytest tesztek/ -v
```

### 4. Értelmezd az eredményt

```
tesztek/modul-01/test_health.py::test_health_endpoint_exists PASSED
tesztek/modul-01/test_health.py::test_health_endpoint_returns_ok PASSED
tesztek/modul-01/test_docker.py::test_docker_compose_exists PASSED
tesztek/modul-01/test_docker.py::test_backend_dockerfile_exists FAILED
```

- **PASSED** — a szükséges dolog implementálva van
- **FAILED** — hiányzik vagy hibás valami, a hibaüzenet elmondja, mit kell csinálni

Minden hibaüzenet tartalmaz egy rövid magyarázatot: mi hiányzik, mit hozz létre, és hol.

## Modul tesztek áttekintés

| Modul | Tesztfájlok | Mit ellenőriz |
|-------|------------|---------------|
| 1 — Projekt indítás | `test_health.py`, `test_docker.py`, `test_alembic.py` | Health endpoint, Docker konfig, Alembic, CI, projekt struktúra |
| 2 — Felhasználókezelés | `test_auth_flow.py`, `test_protected.py`, `test_roles.py` | Auth endpoint-ok, JWT, védett útvonalak, szerepkörök |
| 3 — Kurzusok és haladás | `test_courses.py`, `test_progress.py` | Modellek, CRUD, beiratkozás, GitHub API service, dashboard |
| 4 — Tanúsítvány | `test_completion.py`, `test_verify.py` | Completion logika, Certificate modell, verifikáció, PDF/QR service |
| 5 — Frontend | `test_pages.py` | Astro projekt struktúra, oldalak, Dockerfile, komponensek |
| 6 — Éles üzem | `test_prod.py` | Production compose, nginx, CD workflow, backup, biztonság |
| 7 — Open source | `test_community.py` | LICENSE, CONTRIBUTING.md, issue/PR template-ek, README |

## CI integráció

Opcionálisan a verifikációs tesztek is futtathatók a CI-ban:

```yaml
# .github/workflows/ci.yml — kiegészítés
- name: Run verification tests
  run: pytest tesztek/ -v --tb=short
```

## Tippek

- **Modulonként futtasd** a teszteket, ne egyszerre az összeset — a későbbi modulok tesztjei addig failelni fognak, amíg nem dolgozol odáig
- Ha egy teszt FAILED, olvasd el a hibaüzenetet — pontosan megmondja, mit kell csinálni
- A verifikációs tesztek nem helyettesítik a saját tesztjeidet — a saját tesztek részletesebbek, ezek csak a végeredményt ellenőrzik
- A tesztek az `openschool-platform` repó gyökeréből keresik a fájlokat — a `tesztek/` mappa legyen a repó gyökerében
