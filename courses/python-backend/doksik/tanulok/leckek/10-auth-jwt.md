# Lecke 10 – Authentikáció és JWT

> **Dokumentáció:** [FastAPI Security](https://fastapi.tiangolo.com/tutorial/security/) · [python-jose](https://github.com/mpdavis/python-jose) · [passlib](https://passlib.readthedocs.io/)

---

## 61–62. óra: Authentikáció alapok

### Mi az authentikáció és autorizáció?

| Fogalom | Kérdés | Példa |
|---------|--------|-------|
| **Authentikáció** | Ki vagy te? | Bejelentkezés (email + jelszó) |
| **Autorizáció** | Mit tehetsz? | Admin jogosultság |

### Jelszó hash-elés

**Soha ne tárold a jelszót sima szövegként!** Mindig hash-elve:

```bash
pip install passlib[bcrypt]
```

```python
# app/auth.py
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_jelszo(jelszo: str) -> str:
    return pwd_context.hash(jelszo)

def jelszo_ellenorzes(sima_jelszo: str, hash_jelszo: str) -> bool:
    return pwd_context.verify(sima_jelszo, hash_jelszo)
```

### Regisztráció végpont

```python
# app/routers/auth.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app import models, schemas, auth

router = APIRouter(prefix="/auth", tags=["Authentikáció"])

@router.post("/regisztracio", response_model=schemas.FelhasznaloValasz, status_code=201)
def regisztracio(user: schemas.FelhasznaloLetrehozas, db: Session = Depends(get_db)):
    # Ellenőrzés: létezik-e már
    letezik = db.query(models.Felhasznalo).filter(
        models.Felhasznalo.email == user.email
    ).first()
    if letezik:
        raise HTTPException(status_code=400, detail="Ez az email már regisztrálva van")

    # Jelszó hash-elés
    hashed = auth.hash_jelszo(user.jelszo)
    db_user = models.Felhasznalo(
        nev=user.nev,
        email=user.email,
        jelszo_hash=hashed
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
```

---

## 63–64. óra: JWT tokenek

### Mi a JWT?

A **JWT** (JSON Web Token) egy kompakt, önálló token, ami tartalmazza a felhasználó azonosítóját. Három részből áll: **header.payload.signature**

```bash
pip install python-jose[cryptography]
```

```python
# app/auth.py (kiegészítés)
from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt
from app.config import settings

SECRET_KEY = settings.secret_key
ALGORITHM = "HS256"
TOKEN_LEJARAT_PERC = 30

def token_letrehozas(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=TOKEN_LEJARAT_PERC)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def token_dekodolas(token: str) -> dict:
    return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
```

### Login végpont

```python
from fastapi.security import OAuth2PasswordRequestForm

@router.post("/login")
def login(form: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.Felhasznalo).filter(
        models.Felhasznalo.email == form.username
    ).first()

    if not user or not auth.jelszo_ellenorzes(form.password, user.jelszo_hash):
        raise HTTPException(status_code=401, detail="Hibás email vagy jelszó")

    token = auth.token_letrehozas(data={"sub": str(user.id)})
    return {"access_token": token, "token_type": "bearer"}
```

---

## 65–66. óra: Védett végpontok

```python
# app/dependencies.py
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from sqlalchemy.orm import Session
from app.database import get_db
from app import auth, models

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Érvénytelen token",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = auth.token_dekodolas(token)
        user_id = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = db.query(models.Felhasznalo).filter(
        models.Felhasznalo.id == int(user_id)
    ).first()
    if user is None:
        raise credentials_exception
    return user
```

### Használat végpontokban

```python
@router.get("/profil", response_model=schemas.FelhasznaloValasz)
def profil(current_user = Depends(get_current_user)):
    return current_user
```

---

## Gyakorlat

1. Hozd létre az `app/auth.py` modult a jelszó hash-elő és JWT függvényekkel
2. Készítsd el a regisztráció és login végpontokat
3. Készíts védett `/profil` végpontot
4. Teszteld a Swagger UI-ban: regisztrálj, lépj be, használd a tokent
5. Commitold és pushold
