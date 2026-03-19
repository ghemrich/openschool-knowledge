# Kiegészítő gyakorlatok – 12. hét: Félév összefoglalás és próbavizsga

> Ezek a feladatok a heti házi feladat melletti **extra gyakorlást** szolgálják.
> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz

---

### 12.1 – Gyors protótípus ⭐
Építs fel egy "jegyárus" API-t a nulláról 15 perc alatt. Végpontok: `GET /`, `GET /jegyek`, `POST /jegyek`. Pydantic modell: `Jegy(esemeny, datum, ar, foglalt: bool)`. Mérd az időt!

### 12.2 – Fogalom kvíz ⭐⭐
Válaszolj a következő kérdésekre (nem kódolás, hanem elmélet):
1. Mi a különbség a `response_model` és a return type hint között?
2. Miért használunk `yield`-et a `get_db` dependency-ben?
3. Mikor érdemes `APIRouter`-t használni?
4. Mi a `Depends()` előnye a kézi paraméterátadással szemben?
5. Mi a különbség a Pydantic `BaseModel` és az SQLAlchemy `Base` között?

### 12.3 – Hibakeresés ⭐⭐
Az alábbi kódrészletek mindegyikében van hiba. Keresd meg és javítsd ki:
1. `@app.get("/users")` → `def get_users(db = Depends()): ...` (hiányzó függvény)
2. `class User(BaseModel): id: int` használva `response_model`-ként SQLAlchemy modellel (from_attributes?)
3. JWT token, ami `{"sub": user.id}` helyett `{"sub": user.email}`-t használ (mi a probléma?)

### 12.4 – Mini projekt: Tó lista ⭐⭐⭐
Készíts teljes Todo API-t 60 perc alatt:
- SQLAlchemy modell: `Todo(id, cim, leiras, kesz, letrehozva)`
- Pydantic sémák: Create, Update, Response
- CRUD: list (szűrhető: `kesz=true/false`), create, get, update, delete
- Alembic migráció
- Docker Compose (API + DB)

### 12.5 – Önértékelés ⭐⭐⭐
Értékeld a saját tudásod 1-5 skálán minden témakörben, és készíts ter vet a gyenge pontok javítására:
- FastAPI alapok (végpontok, paraméterek)
- Pydantic (modellek, validáció)
- SQLAlchemy + Alembic
- Auth (JWT, hash, védett végpontok)
- Docker (Dockerfile, Compose)
- Middleware, CORS
- Dependency Injection
