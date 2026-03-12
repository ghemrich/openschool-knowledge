# Modul 2 — Felhasználókezelés

## Cél

GitHub OAuth alapú bejelentkezés, JWT session kezelés, és szerepkör-rendszer. A modul végére:

- A felhasználó tud GitHub-bal belépni
- A rendszer JWT-vel kezeli a session-t
- Három szerepkör: tanuló, mentor, admin
- A védett endpoint-ok tesztelve vannak

## 2.1 GitHub OAuth flow

Az OpenSchool nem saját jelszavakat kezel — a felhasználók GitHub-bal lépnek be.

**Az OAuth 2.0 flow lépései:**

```
1. Felhasználó kattint → "Belépés GitHub-bal"
2. Átirányítás → github.com/login/oauth/authorize?client_id=...
3. Felhasználó engedélyezi → GitHub visszairányít egy code-dal
4. Backend elküldi a code-ot → github.com/login/oauth/access_token
5. GitHub visszaadja az access_token-t
6. Backend lekéri a felhasználó adatait → api.github.com/user
7. Backend létrehozza/frissíti a felhasználót az adatbázisban
8. Backend JWT-t generál és visszaküldi a frontendnek
```

**Előkészítés:**
- GitHub Developer Settings → OAuth App létrehozása
- `Authorization callback URL`: `http://localhost:8000/api/auth/callback` (dev)
- `GITHUB_CLIENT_ID` és `GITHUB_CLIENT_SECRET` → `.env`

**Feladat:**
- Hozd létre a GitHub OAuth App-ot
- Implementáld az `/api/auth/login` és `/api/auth/callback` endpoint-okat
- Az `/api/auth/login` generálja az authorization URL-t és irányítsa át a felhasználót
- Az `/api/auth/callback` kezelje a code → token cserét

## 2.2 User modell

```python
# app/models/user.py
from sqlalchemy import Column, Integer, String, DateTime, Enum
from app.database import Base
import enum
from datetime import datetime, timezone

class UserRole(enum.StrEnum):
    student = "student"
    mentor = "mentor"
    admin = "admin"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    github_id = Column(Integer, unique=True, nullable=False)
    username = Column(String, unique=True, nullable=False)
    email = Column(String)
    avatar_url = Column(String)
    role = Column(Enum(UserRole), default=UserRole.student, nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    last_login = Column(DateTime)
    github_token = Column(String)
```

**Feladat:**
- Hozd létre a User modellt
- Generálj Alembic migrációt: `alembic revision --autogenerate -m "add users table"`
- Futtasd: `alembic upgrade head`

## 2.3 JWT tokenek

Két token típus:

| Token | Élettartam | Cél |
|-------|-----------|-----|
| Access token | 30 perc | API hívások autentikálása |
| Refresh token | 7 nap | Új access token kérése |

```python
# app/auth/jwt.py
from datetime import datetime, timedelta, timezone
from jose import jwt
from app.config import settings

def create_access_token(user_id: int) -> str:
    expire = datetime.now(timezone.utc) + timedelta(minutes=30)
    return jwt.encode(
        {"sub": str(user_id), "exp": expire},
        settings.secret_key,
        algorithm="HS256"
    )

def create_refresh_token(user_id: int) -> str:
    expire = datetime.now(timezone.utc) + timedelta(days=7)
    return jwt.encode(
        {"sub": str(user_id), "exp": expire, "type": "refresh"},
        settings.secret_key,
        algorithm="HS256"
    )
```

**Feladat:**
- Implementáld a token generálás és validálás logikát
- Az access token a válasz body-ban menjen vissza
- A refresh token HttpOnly cookie-ban

## 2.4 Auth endpoint-ok

| Endpoint | Metódus | Leírás |
|----------|---------|--------|
| `/api/auth/login` | GET | GitHub OAuth URL generálás + redirect |
| `/api/auth/callback` | GET | OAuth code → token csere, JWT generálás |
| `/api/auth/me` | GET | Aktuális felhasználó adatai (védett) |
| `/api/auth/refresh` | POST | Új access token kérése refresh token-nel |
| `/api/auth/logout` | POST | Refresh token törlése |

**Feladat:**
- Implementáld mind az 5 endpoint-ot
- Az `/api/auth/me` használjon `Depends`-et a felhasználó kinyeréséhez
- A logout törölje a refresh token cookie-t

## 2.5 Auth middleware

```python
# app/auth/dependencies.py
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.auth.jwt import verify_token
from app.models.user import User, UserRole

security = HTTPBearer()

def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
) -> User:
    token_data = verify_token(credentials.credentials)
    user = db.query(User).filter(User.id == token_data.user_id).first()
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    return user

def require_role(required_role: UserRole):
    def role_checker(user: User = Depends(get_current_user)):
        if user.role != required_role and user.role != UserRole.admin:
            raise HTTPException(status_code=403, detail="Insufficient permissions")
        return user
    return role_checker
```

**Feladat:**
- Implementáld a `get_current_user` dependency-t
- Implementáld a `require_role` dependency-t
- Használat: `@router.get("/admin", dependencies=[Depends(require_role(UserRole.admin))])`

## 2.6 Tesztek

Tesztelendő esetek:

**Auth flow tesztek:**
- OAuth callback helyes code-dal → user létrejön + JWT visszajön
- OAuth callback hibás code-dal → 401
- Már létező user újra belép → `last_login` frissül, nem duplikálódik

**Védett endpoint tesztek:**
- `/api/auth/me` érvényes token-nel → 200 + user adatok
- `/api/auth/me` token nélkül → 401
- `/api/auth/me` lejárt token-nel → 401

**Szerepkör tesztek:**
- Admin endpoint student token-nel → 403
- Admin endpoint admin token-nel → 200

**Mock stratégia:**
- A GitHub API hívásokat mockold (ne függj a GitHub-tól a tesztekben)
- Hozz létre egy `create_test_user` fixture-t, ami JWT-t is generál

**Feladat:**
- Írj teszteket minden fenti esetre
- A tesztek fussanak SQLite-tal, GitHub API mock-kal
- `pytest -v` → minden zöld

## Háttéranyag

Ezeket nem kell elejétől végig elolvasni — használd referenciaként, amikor az adott témánál tartasz.

| Téma | Link | Miért hasznos |
|------|------|---------------|
| OAuth 2.0 áttekintés | [oauth.net/2](https://oauth.net/2/) | Az OAuth flow megértése általánosan |
| GitHub OAuth Apps | [docs.github.com/en/apps/oauth-apps](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/creating-an-oauth-app) | GitHub OAuth app létrehozása, client_id/secret |
| JWT bevezetés | [jwt.io/introduction](https://jwt.io/introduction/) | Token struktúra, aláírás, claims |
| python-jose | [github.com/mpdavis/python-jose](https://github.com/mpdavis/python-jose) | JWT generálás és validálás Python-ban |
| httpx | [www.python-httpx.org](https://www.python-httpx.org/) | HTTP kliens a GitHub API hívásokhoz (async támogatás) |
| FastAPI Security | [fastapi.tiangolo.com/tutorial/security](https://fastapi.tiangolo.com/tutorial/security/) | OAuth2 és JWT integráció FastAPI-ban |

## Verifikációs tesztek

A modul végén futtasd a verifikációs teszteket:

```bash
cd openschool-platform
pytest tesztek/modul-02/ -v
```

**Mit ellenőriznek a tesztek:**

| Tesztfájl | Ellenőrzések |
|-----------|---------------|
| `test_auth_flow.py` | Auth login, callback, me endpoint-ok léteznek; User és UserRole modellek; JWT modul létezik |
| `test_protected.py` | `/api/auth/me` 401-et ad token nélkül és érvénytelen token-nel; `get_current_user` és `require_role` dependency-k léteznek |
| `test_roles.py` | UserRole enum-nak 3 értéke van; alapértelmezett role student; JWT token generálás működik |

> **Megjegyzés:** Ezek a tesztek a struktúrát és az alapvető viselkedést ellenőrzik. A modul során írt **saját tesztek** (mock OAuth, részletes role tesztelés) részletesebbek — mindkettőnek zöldnek kell lennie.

## Ellenőrzőlista

- [ ] GitHub OAuth login működik (dev környezetben)
- [ ] JWT access + refresh token pár generálódik
- [ ] `/api/auth/me` visszaadja a bejelentkezett felhasználót
- [ ] Szerepkör-alapú hozzáférés-vezérlés működik
- [ ] Saját tesztek lefedik az auth flow-t, védett endpoint-okat, és szerepköröket
- [ ] Alembic migráció létrehozza a users táblát
- [ ] `pytest tesztek/modul-02/ -v` → minden zöld (verifikációs tesztek)
