# Modul 3 — Kurzusok és haladás

## Cél

Az OpenSchool platform magja: kurzusok, feladatok nyilvántartása és automatikus haladáskövetés a GitHub API-n keresztül. A modul végére:

- Kurzus/modul/feladat adatmodellek az adatbázisban
- Beiratkozás API
- A rendszer automatikusan ellenőrzi a GitHub repók CI állapotát
- Dashboard endpoint: összesített haladás

## 3.1 Adatmodellek

```
Course
  ├── Module (sorrend)
  │     └── Exercise (sorrend)
  │           └── feladat repó neve (pl. "het01-alapok")
  │
  └── Enrollment
        ├── user_id
        └── enrolled_at

Progress
  ├── user_id
  ├── exercise_id
  ├── github_repo (pl. "het01-alapok-johndoe")
  ├── status: not_started / in_progress / completed
  └── completed_at
```

**Feladat:**
- Hozd létre a `Course`, `Module`, `Exercise`, `Enrollment`, `Progress` modelleket
- Kapcsolatok:
  - Course → Module (1:N)
  - Module → Exercise (1:N)
  - Course → Enrollment (1:N)
  - User → Enrollment (1:N)
  - User + Exercise → Progress (1:1)
- Generálj Alembic migrációt

## 3.2 Kurzus CRUD (admin)

| Endpoint | Metódus | Jogosultság | Leírás |
|----------|---------|-------------|--------|
| `/api/courses` | GET | nyilvános | Kurzuslista |
| `/api/courses/{id}` | GET | nyilvános | Kurzus részletei (modulok + feladatok) |
| `/api/courses` | POST | admin | Kurzus létrehozása |
| `/api/courses/{id}` | PUT | admin | Kurzus módosítása |
| `/api/courses/{id}/modules` | POST | admin | Modul hozzáadása |
| `/api/courses/{id}/modules/{mid}/exercises` | POST | admin | Feladat hozzáadása |

**Feladat:**
- Implementáld a CRUD endpoint-okat
- Az admin endpoint-ok használják a `require_role(UserRole.admin)` dependency-t
- A GET endpoint-ok nyilvánosak (token nélkül is elérhetők)
- Pydantic schema-k a request/response body-khoz

## 3.3 Beiratkozás

| Endpoint | Metódus | Leírás |
|----------|---------|--------|
| `/api/courses/{id}/enroll` | POST | Beiratkozás (autentikált user) |
| `/api/courses/{id}/unenroll` | POST | Kiiratkozás |
| `/api/me/courses` | GET | Saját kurzusaim |

**Feladat:**
- Implementáld a beiratkozás/kiiratkozás endpoint-okat
- Egy felhasználó egy kurzusra csak egyszer iratkozhat be
- A `/api/me/courses` adja vissza a beiratkozott kurzusokat haladással együtt

## 3.4 GitHub API integráció

Az OpenSchool automatikusan ellenőrzi, hogy a tanuló feladat-repójában fut-e zöld CI pipeline.

**GitHub API endpoint:**
```
GET /repos/{owner}/{repo}/actions/runs
Authorization: Bearer {github_token}
```

**Logika:**
1. A feladat (`Exercise`) tárolja a repó név mintát (pl. `het01-alapok`)
2. A tanuló GitHub Classroom repója: `{repo_prefix}-{github_username}`
3. A rendszer lekérdezi a legutolsó workflow run-t
4. Ha `conclusion == "success"` → a feladat teljesítve

```python
# app/services/github.py
import httpx

async def check_exercise_status(
    owner: str,
    repo_name: str,
    github_token: str
) -> bool:
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"https://api.github.com/repos/{owner}/{repo_name}/actions/runs",
            headers={"Authorization": f"Bearer {github_token}"},
            params={"per_page": 1, "status": "completed"}
        )
        if response.status_code != 200:
            return False
        runs = response.json().get("workflow_runs", [])
        if not runs:
            return False
        return runs[0]["conclusion"] == "success"
```

**Feladat:**
- Implementáld a GitHub API service-t
- Kezeld a hibákat: nem létező repó, nincs workflow, rate limit
- A `github_token`-t a felhasználó OAuth token-jéből vedd (vagy egy szervezeti token-t használj)

## 3.5 Haladáskövetés

Két megközelítés a haladás frissítésére:

**A) On-demand** (egyszerűbb):
- Amikor a felhasználó megnyitja a dashboard-ot, a backend lekérdezi a GitHub API-t
- Hátrány: lassú, API rate limit

**B) Background polling** (skálázhatóbb):
- Periodikus háttérfolyamat ellenőrzi a beiratkozott felhasználók repóit
- A haladást cache-eli az adatbázisban
- A dashboard az adatbázisból olvas

**Ajánlott: B) Background polling**

```python
# app/services/progress.py
from app.models.progress import Progress, ProgressStatus

async def update_progress_for_user(db: Session, user: User):
    enrollments = db.query(Enrollment).filter(
        Enrollment.user_id == user.id
    ).all()
    for enrollment in enrollments:
        exercises = get_exercises_for_course(db, enrollment.course_id)
        for exercise in exercises:
            repo_name = f"{exercise.repo_prefix}-{user.username}"
            is_completed = await check_exercise_status(
                owner="openschool-org",
                repo_name=repo_name,
                github_token=settings.github_org_token
            )
            update_or_create_progress(db, user.id, exercise.id, is_completed)
```

**Feladat:**
- Implementáld a progress service-t
- Használj FastAPI `BackgroundTasks`-ot vagy egy egyszerű periodic task-ot
- Kezeld a GitHub API rate limit-et (max 5000 req/óra, szervezeti token)

## 3.6 Dashboard endpoint-ok

| Endpoint | Metódus | Leírás |
|----------|---------|--------|
| `/api/me/dashboard` | GET | Összesített haladás minden kurzusnál |
| `/api/me/courses/{id}/progress` | GET | Részletes haladás egy kurzuson belül |

**Válasz példa (`/api/me/dashboard`):**
```json
[
  {
    "course_id": 1,
    "course_name": "Python alapok",
    "total_exercises": 12,
    "completed_exercises": 8,
    "progress_percent": 66.7,
    "enrolled_at": "2025-01-15T10:00:00Z"
  }
]
```

**Feladat:**
- Implementáld a dashboard endpoint-okat
- A válasz tartalmazza a százalékos haladást és az utolsó frissítés idejét
- Optimalizáld: ne N+1 query legyen, használj JOIN-okat

## 3.7 Tesztek

**Tesztelendő esetek:**
- Kurzus CRUD: létrehozás, lekérdezés, módosítás
- Beiratkozás: sikeres, duplikált (409), kiiratkozás
- GitHub API mock: sikeres check, failed check, nem létező repó
- Dashboard: helyes százalék számítás, üres kurzus, részben kész kurzus
- Jogosultság: admin CRUD, student nem tud kurzust létrehozni

**Feladat:**
- Írj teszteket minden fenti esetre
- A GitHub API-t mockold (`httpx` mock vagy `respx` library)
- `pytest -v` → minden zöld

## Háttéranyag

Ezeket nem kell elejétől végig elolvasni — használd referenciaként, amikor az adott témánál tartasz.

| Téma | Link | Miért hasznos |
|------|------|---------------|
| GitHub REST API | [docs.github.com/en/rest](https://docs.github.com/en/rest) | Repó, workflow, check-run lekérdezések |
| GitHub Actions API | [docs.github.com/en/rest/actions](https://docs.github.com/en/rest/actions) | CI workflow státusz programozott lekérése |
| FastAPI Background Tasks | [fastapi.tiangolo.com/tutorial/background-tasks](https://fastapi.tiangolo.com/tutorial/background-tasks/) | Háttérben futó progress check feladatok |
| SQLAlchemy Relationships | [docs.sqlalchemy.org/en/20/orm/relationships.html](https://docs.sqlalchemy.org/en/20/orm/relationships.html) | Összetett adatmodellek közti kapcsolatok |
| httpx async | [www.python-httpx.org/async](https://www.python-httpx.org/async/) | Aszinkron HTTP hívások a GitHub API felé |

## Verifikációs tesztek

A modul végén futtasd a verifikációs teszteket:

```bash
cd openschool-platform
pytest tesztek/modul-03/ -v
```

**Mit ellenőriznek a tesztek:**

| Tesztfájl | Ellenőrzések |
|-----------|---------------|
| `test_courses.py` | Course, Module, Exercise, Enrollment, Progress modellek léteznek; `GET /api/courses` nyilvános és listát ad vissza; beiratkozás auth-ot igényel |
| `test_progress.py` | Dashboard és my-courses endpoint-ok auth-ot igényelnek; GitHub API és progress service modulok léteznek |

> **Megjegyzés:** Ezek a tesztek a végeredményt ellenőrzik. A modul során írt **saját tesztek** (GitHub API mock, dashboard százalék számítás, CRUD részletei) részletesebbek.

## Ellenőrzőlista

- [ ] Kurzus/Modul/Exercise adatmodellek létrejönnek migrációval
- [ ] Admin tud kurzust, modult, feladatot létrehozni
- [ ] Felhasználó tud beiratkozni és kiiratkozni
- [ ] GitHub API integráció működik (legalább manuálisan tesztelve)
- [ ] Dashboard endpoint helyes haladási adatokat ad vissza
- [ ] Saját tesztek lefedik a CRUD, beiratkozás, GitHub mock, dashboard eseteket
- [ ] `pytest tesztek/modul-03/ -v` → minden zöld (verifikációs tesztek)
