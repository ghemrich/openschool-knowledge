# Lecke 12 – Félév összefoglalás és próbavizsga

> **Dokumentáció:** Lásd az előző leckék hivatkozásait

---

## 73–74. óra: Félév áttekintés

### Eddig tanultak összefoglalása

| Hét | Téma | Kulcs fogalmak |
|-----|------|----------------|
| 0 | Git, GitHub, parancssor | CLI, git branch, GitHub Classroom |
| 1 | Python, venv | venv, pip, requirements.txt |
| 2 | FastAPI bevezetés | REST, HTTP methods, Swagger UI |
| 3 | Útvonalak, paraméterek | Path params, Query params |
| 4 | Request body, Pydantic | BaseModel, Field, validation |
| 5 | Response, hibakezelés | response_model, HTTPException |
| 6 | DI, Router, Config | Depends(), APIRouter, BaseSettings |
| 7 | Docker, PostgreSQL | Dockerfile, docker-compose, SQL |
| 8 | SQLAlchemy ORM | Models, engine, Alembic |
| 9 | CRUD műveletek | crud.py, schemas, get_db |
| 10 | Auth, JWT | bcrypt, JWT, OAuth2 |
| 11 | Middleware, CORS | Middleware, CORS, lifespan |

### Teljes projekt struktúra

```
backend-projekt/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI app, middleware, routerek
│   ├── config.py             # BaseSettings, .env
│   ├── database.py           # engine, SessionLocal, Base, get_db
│   ├── auth.py               # hash, JWT
│   ├── dependencies.py       # get_current_user
│   ├── models.py             # SQLAlchemy modellek
│   ├── schemas.py            # Pydantic sémák
│   └── routers/
│       ├── __init__.py
│       ├── auth.py
│       └── items.py
├── alembic/                  # Migrációk
│   └── versions/
├── alembic.ini
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── .env
└── .env.example
```

---

## 75–76. óra: Teljes API építés (gyakorlás)

### Feladat: Jegyzet API

Építs egy teljes **Jegyzet API**-t a nulláról 2 óra alatt:

**Adatmodell:**
```python
class Jegyzet(Base):
    __tablename__ = "jegyzetek"
    id = Column(Integer, primary_key=True, index=True)
    cim = Column(String, nullable=False)
    tartalom = Column(String, nullable=False)
    szerzo_id = Column(Integer, ForeignKey("felhasznalok.id"))
    letrehozva = Column(DateTime, default=func.now())
```

**Végpontok:**
- `POST /auth/regisztracio` – regisztráció
- `POST /auth/login` – bejelentkezés
- `GET /jegyzetek` – összes jegyzet listázás
- `POST /jegyzetek` – új jegyzet (védett)
- `GET /jegyzetek/{id}` – egy jegyzet
- `PUT /jegyzetek/{id}` – módosítás (csak saját, védett)
- `DELETE /jegyzetek/{id}` – törlés (csak saját, védett)

---

## 77–78. óra: Próbavizsga

### Próbavizsga feladat (60 pont, 120 perc)

Ez a próbavizsga az első félév anyagát (1–11. hét) fedi le. A valódi vizsga (24. hét) 240 perc és 5 feladatból áll — a próbavizsga az első 3 feladattípust (API, DB, Auth) gyakoroltatja.

#### 1. feladat – Alap végpontok (15 pont)

Készíts egy FastAPI alkalmazást könyv-nyilvántartásra:
- `GET /` – üdvözlő üzenet (3 pont)
- `GET /konyvek` – összes könyv listázása (4 pont)
- `GET /konyvek/{id}` – egy könyv lekérése, 404 ha nem létezik (4 pont)
- `POST /konyvek` – új könyv hozzáadása (4 pont)

#### 2. feladat – Adatbázis integráció (20 pont)

- SQLAlchemy modell: Konyv (id, cim, szerzo, ev, ar) (5 pont)
- Pydantic sémák (Create, Update, Response) (5 pont)
- CRUD műveletek (crud.py) (5 pont)
- Alembic migráció (5 pont)

#### 3. feladat – Auth és védett végpontok (25 pont)

- Felhasznalo modell és regisztráció (5 pont)
- JWT login (5 pont)
- `POST /konyvek` csak bejelentkezett felhasználóknak (5 pont)
- `PUT /konyvek/{id}` és `DELETE /konyvek/{id}` védett (5 pont)
- Helyes hibakódok (401, 403, 404) (5 pont)

---

## Gyakorlat

1. Ismételd át az eddigi leckéket – nézd végig a kód példákat
2. Oldd meg a Jegyzet API feladatot önállóan
3. Próbáld meg a próbavizsga feladatot 120 perc alatt
4. Commitold és pushold mindkét projektet
