# 📘 Lecke 21 – Projekt tervezés

> 📚 Dokumentáció:
> https://fastapi.tiangolo.com/tutorial/
> https://restfulapi.net/

---

## 127–128. óra: Projekt kiválasztása

### Záró projekt

Az utolsó 4 hétben egy **komplett backend API projektet** építesz a nulláról, amely tartalmazza az összes tanult technológiát.

### Projekt témák (válassz egyet)

| Téma | Leírás |
|------|--------|
| **Todo API** | Feladatkezelő, kategóriákkal, határidővel, prioritással |
| **Blog API** | Blog posztok, kommentek, címkék, szerzők |
| **Webshop API** | Termékek, kosár, rendelések, kategóriák |
| **Recept API** | Receptek, hozzávalók, kategóriák, értékelések |

### 🧠 Részletes Magyarázat

- **Miért projekt?** – Az elmúlt 20 leckében elszigetelt koncepciókat tanultunk. A projekt az egyetlen alkalom, hogy **mindent összerakj** egy működő alkalmazásba: adatmodell, CRUD, auth, tesztek, Docker, CI.
- **Témák egyenlő nehézségűek** – Mindegyik 3+ táblát, ForeignKey kapcsolatot, és teljes CRUD-ot igényel. A választás az érdeklődéstől függ.
- **Saját téma** – A megadott témák helyett választhatsz sajátot is, de a követelményeknek meg kell felelnie (legalább 3 tábla, auth, stb.).

### Követelmények (minden projektre)

| Szempont | Minimum |
|----------|---------|
| Modellek | Legalább 3 tábla, legalább 1 kapcsolat (ForeignKey) |
| CRUD | Minden modellhez teljes CRUD |
| Auth | Regisztráció, login, JWT, védett végpontok |
| Validáció | Pydantic sémák, hibaüzenetek |
| Tesztek | Legalább 15 teszt, mock DB |
| Docker | docker-compose.yml (API + PostgreSQL) |
| CI | GitHub Actions workflow |
| Dokumentáció | README.md a végpontok leírásával |

### 🧠 Részletes Magyarázat

| Követelmény | Melyik leckéből jön | Miért fontos |
|-------------|---------------------|-------------|
| 3+ tábla, ForeignKey | 8-9. lecke (SQLAlchemy, CRUD) | Relációs adatmodell tervezés |
| Teljes CRUD | 9. lecke | REST API alap |
| Auth + JWT | 10. lecke | Biztonság |
| Pydantic | 4-5. lecke | Input validáció, output formázás |
| 15+ teszt, mock DB | 13-16. lecke | Minőségbiztosítás |
| Docker Compose | 7, 19. lecke | Környezetfüggetlenség |
| GitHub Actions | 20. lecke | Automatikus CI |
| README | — | Dokumentáció = professzionalizmus |

---

## 129–130. óra: Tervezés

### 1. Adatmodell tervezés

Rajzold meg az adatmodellt. Példa – **Blog API**:

```
Felhasznalo          Poszt                  Komment
-----------          -----                  -------
id (PK)              id (PK)                id (PK)
nev                  cim                    tartalom
email (unique)       tartalom               szerzo_id (FK → Felhasznalo)
jelszo_hash          szerzo_id (FK)         poszt_id (FK → Poszt)
letrehozva           letrehozva             letrehozva
                     modositva

Cimke                PosztCimke
-----                ----------
id (PK)              poszt_id (FK)
nev (unique)         cimke_id (FK)
```

### 🧠 Részletes Magyarázat

- **PK (Primary Key)** – Egyedi azonosító, az `id` oszlop. Automatikusan generálódik (autoincrement).
- **FK (Foreign Key)** – Hivatkozás másik táblára. A `szerzo_id` a `Felhasznalo` tábla `id`-jére mutat. Ezzel a poszt „tudja", ki írta.
- **`PosztCimke`** (kötőtábla) – Több-a-többhöz (many-to-many) kapcsolat: egy posztnak több címkéje lehet, egy címke több poszthoz tartozhat. Ezt egy köztes tábla oldja meg, ami két FK-t tartalmaz.
- **`unique`** – Az `email` és a címke `nev` egyedi: nem lehet két felhasználó ugyanazzal az email-lel, és nem lehet két azonos nevű címke.

### 2. Végpont lista

Írd össze az API végpontjait:

```
POST   /auth/regisztracio    → Regisztráció
POST   /auth/login           → Bejelentkezés
GET    /auth/profil           → Saját profil [védett]

GET    /posztok               → Összes poszt
POST   /posztok               → Új poszt [védett]
GET    /posztok/{id}          → Egy poszt
PUT    /posztok/{id}          → Módosítás [védett, saját]
DELETE /posztok/{id}          → Törlés [védett, saját]

POST   /posztok/{id}/komment → Komment írás [védett]
GET    /posztok/{id}/komment  → Poszt kommentjei
DELETE /kommentek/{id}        → Komment törlés [védett, saját]

GET    /cimkek                → Összes címke
POST   /cimkek                → Új címke [védett]
```

### 🧠 Részletes Magyarázat

- **`[védett]`** – JWT token szükséges (`Authorization: Bearer <token>`)
- **`[saját]`** – Csak a saját erőforrást módosíthatja/törölheti. Ha más felhasználó próbálja: 403 Forbidden.
- **REST konvenciók:**
  - `GET` = olvasás (nem módosít)
  - `POST` = létrehozás (201 Created)
  - `PUT` = teljes módosítás (200 OK)
  - `DELETE` = törlés (200 OK vagy 204 No Content)
- **Beágyazott útvonalak** – `/posztok/{id}/komment` jelzi, hogy a komment a poszthoz tartozik. Ez RESTful nesting: a URL struktúra tükrözi az adatmodellt.

### 3. Projekt struktúra

```
blog-api/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── database.py
│   ├── auth.py
│   ├── dependencies.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── felhasznalo.py
│   │   ├── poszt.py
│   │   ├── komment.py
│   │   └── cimke.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── felhasznalo.py
│   │   ├── poszt.py
│   │   ├── komment.py
│   │   └── cimke.py
│   ├── crud/
│   │   ├── __init__.py
│   │   ├── felhasznalo.py
│   │   ├── poszt.py
│   │   ├── komment.py
│   │   └── cimke.py
│   └── routers/
│       ├── __init__.py
│       ├── auth.py
│       ├── posztok.py
│       ├── kommentek.py
│       └── cimkek.py
├── tests/
│   ├── conftest.py
│   ├── test_auth.py
│   ├── test_posztok.py
│   ├── test_kommentek.py
│   └── test_cimkek.py
├── alembic/
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── .env.example
├── .github/workflows/ci.yml
└── README.md
```

### 🧠 Részletes Magyarázat

A struktúra a **leckékben tanult minták** összessége:

| Mappa | Felelősség | Lecke |
|-------|-----------|-------|
| `models/` | SQLAlchemy tábladefiníciók | 8. lecke |
| `schemas/` | Pydantic input/output sémák | 4-5. lecke |
| `crud/` | Adatbázis műveletek (query, create, update, delete) | 9. lecke |
| `routers/` | API végpontok (APIRouter) | 6. lecke |
| `auth.py` | JWT, bcrypt, OAuth2 | 10. lecke |
| `dependencies.py` | Depends() függvények (get_db, get_current_user) | 6. lecke |
| `config.py` | BaseSettings, .env beolvasás | 6. lecke |
| `database.py` | Engine, SessionLocal, Base | 8. lecke |
| `tests/` | pytest + mock DB | 13-16. lecke |
| `alembic/` | Migrációk | 8. lecke |

- **Model per fájl** – Kisebb, átláthatóbb fájlok. Az `__init__.py`-ban importálhatod az összeset: `from app.models import Felhasznalo, Poszt`.

---

## 131–132. óra: Projekt setup

### 1. Repository létrehozása

```bash
mkdir blog-api && cd blog-api
git init
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows
```

### 🧠 Részletes Magyarázat

- **Sorrend fontos:** (1) mappa létrehozása, (2) git inicializálás, (3) virtuális környezet. Ha a `venv`-et először hozod létre, a git repó tartalmazni fogja (hacsak nincs `.gitignore`).
- **`source venv/bin/activate`** – Aktiválja a virtuális környezetet. Ettől kezdve a `pip install` ebbe a `venv/` mappába telepít, nem a rendszer Python-jába.

### 2. Függőségek

```bash
pip install fastapi uvicorn sqlalchemy alembic psycopg2-binary \
  python-jose[cryptography] passlib[bcrypt] python-dotenv pydantic-settings \
  pytest httpx python-multipart
pip freeze > requirements.txt
```

### 🧠 Részletes Magyarázat

| Csomag | Mire kell |
|--------|----------|
| `fastapi` | Web framework |
| `uvicorn` | ASGI szerver |
| `sqlalchemy` | ORM |
| `alembic` | Migrációk |
| `psycopg2-binary` | PostgreSQL driver |
| `python-jose[cryptography]` | JWT token kezelés |
| `passlib[bcrypt]` | Jelszó hash-elés |
| `python-dotenv` | `.env` fájl beolvasás |
| `pydantic-settings` | BaseSettings |
| `pytest` | Tesztelés |
| `httpx` | TestClient motorja |
| `python-multipart` | Fájl feltöltés |

### 3. Alap fájlok

Hozd létre a könyvtárstruktúrát, a `.env.example`, `docker-compose.yml`, `Dockerfile`, és az alap `main.py` fájlokat az eddigi leckék alapján.

### 4. Első commit

```bash
git add .
git commit -m "Projekt setup: FastAPI + docker-compose + tesztek"
git push
```

### 🧠 Részletes Magyarázat

- **Első commit** – A projekt vázát commitold, mielőtt bármilyen funkciót írnál. Így bármikor visszatérhetsz a „tiszta" állapothoz.
- **Commit üzenet** – Rövid, leíró, angolul vagy magyarul. A lényeg: bárki megérti, mit tartalmaz.
- **Ne felejtsd:** `echo "venv/" >> .gitignore` és `echo ".env" >> .gitignore` **az első commit előtt**.

---

## Gyakorlat

1. Válassz egy projekt témát
2. Tervezd meg az adatmodellt (legalább 3 tábla)
3. Írd össze az összes végpontot
4. Hozd létre a projekt struktúrát és a kezdő fájlokat
5. Commitold és pushold
