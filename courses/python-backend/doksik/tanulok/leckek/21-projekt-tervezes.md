# Lecke 21 – Projekt tervezés

> **Dokumentáció:** [FastAPI Best Practices](https://fastapi.tiangolo.com/tutorial/) · [RESTful API Design](https://restfulapi.net/)

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

### 2. Függőségek

```bash
pip install fastapi uvicorn sqlalchemy alembic psycopg2-binary \
  python-jose[cryptography] passlib[bcrypt] python-dotenv pydantic-settings \
  pytest httpx python-multipart
pip freeze > requirements.txt
```

### 3. Alap fájlok

Hozd létre a könyvtárstruktúrát, a `.env.example`, `docker-compose.yml`, `Dockerfile`, és az alap `main.py` fájlokat az eddigi leckék alapján.

### 4. Első commit

```bash
git add .
git commit -m "Projekt setup: FastAPI + docker-compose + tesztek"
git push
```

---

## Gyakorlat

1. Válassz egy projekt témát
2. Tervezd meg az adatmodellt (legalább 3 tábla)
3. Írd össze az összes végpontot
4. Hozd létre a projekt struktúrát és a kezdő fájlokat
5. Commitold és pushold
