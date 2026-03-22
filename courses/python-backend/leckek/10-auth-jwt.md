# 📘 Lecke 10 – Authentikáció és JWT

> 📚 Dokumentáció:
> https://fastapi.tiangolo.com/tutorial/security/
> https://github.com/mpdavis/python-jose
> https://passlib.readthedocs.io/

---

## 61–62. óra: Authentikáció alapok

### Mi az authentikáció és autorizáció?

| Fogalom | Kérdés | Példa |
|---------|--------|-------|
| **Authentikáció** | Ki vagy te? | Bejelentkezés (email + jelszó) |
| **Autorizáció** | Mit tehetsz? | Admin jogosultság |

### 🧠 Részletes Magyarázat

- **Authentikáció (AuthN)** – Személyazonosság igazolása. Megmutatod, hogy te vagy, aki állítod magadról (pl. email + jelszó, ujjlenyomat, arcfelismerés). Az API szempontjából: a kliens bizonyítja, hogy egy adott felhasználóhoz tartozik.
- **Autorizáció (AuthZ)** – Jogosultságok ellenőrzése. Már tudjuk, ki vagy, de mi az, amit tehetsz? Pl. egy „normál" felhasználó láthatja a termékeit, de nem törölhet más felhasználó adatait. Az admin mindent tehet.
- **Sorrend:** Mindig először authentikáció, aztán autorizáció. Nem tudjuk ellenőrizni a jogosultságot, ha nem tudjuk, ki a felhasználó.

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

### 🧠 Részletes Magyarázat

- **Hash-elés** – Egyirányú kriptográfiai művelet. A `"titok123"` jelszóból lesz pl. `"$2b$12$LJ3m..."`, de a hash-ből **nem lehet visszafejteni** az eredeti jelszót. Ha valaki feltöri az adatbázist, a jelszó hash-eket nem tudja használni.
- **bcrypt** – Az egyik legbiztonságosabb hash-elő algoritmus. Lassú szándékosan (kb. 100ms/hash), így a brute-force támadás rendkívül lassú lenne (összehasonlításul: MD5 milliárdokat hash-el másodpercenként, bcrypt csak százakat).
- **`CryptContext`** – A passlib „okos" kontextusa, ami kezeli az algoritmusokat. A `deprecated="auto"` automatikusan újra hash-eli a jelszót, ha régebbi algoritmust használtunk.
- **`hash()`** – Jelszó hash létrehozása (regisztrációnál). Ugyanaz a jelszó mindig más hash-t ad (salt miatt), ezért nem lehet hash-eket összehasonlítani – a `verify()` kell hozzá.
- **`verify()`** – Ellenőrzi, hogy a sima szöveg jelszó megegyezik-e a tárolt hash-sel. Bejelentkezésnél használjuk.

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

### 🧠 Részletes Magyarázat

A regisztráció munkafolyamata lépésről lépésre:

1. **Kliens küld** – `{"nev": "Kiss Béla", "email": "bela@example.com", "jelszo": "titok123"}`
2. **Duplikátum ellenőrzés** – Megnézzük, van-e már ilyen email az adatbázisban. Ha van → 400 hiba.
3. **Hash-elés** – A `"titok123"` → `"$2b$12$LJ3m..."`. A sima jelszó **soha nem kerül** az adatbázisba!
4. **Mentés** – Az ORM objektum létrehozása és az adatbázisba írása.
5. **Válasz** – A `response_model=FelhasznaloValasz` biztosítja, hogy a jelszó hash NEM szerepel a válaszban.

- **`status_code=400`** – „Bad Request": a kliens hibája, hogy már létező email-t próbál regisztrálni. A 409 (Conflict) is elfogadott lenne erre a célra.
- **Miért `jelszo_hash` és nem `jelszo`?** – Az adatbázis mező neve egyértelműen jelzi, hogy hash-elt értéket tartalmaz. A Pydantic input séma (`FelhasznaloLetrehozas`) tartalmazza a `jelszo` mezőt, amit hash-elés után `jelszo_hash` néven mentünk.

---

## 63–64. óra: JWT tokenek

### Mi a JWT?

A **JWT** (JSON Web Token) egy kompakt, önálló token, ami tartalmazza a felhasználó azonosítóját. Három részből áll: **header.payload.signature**

### 🧠 Részletes Magyarázat

- **JWT felépítése** – Három Base64-kódolt rész ponttal elválasztva:
```
eyJhbGci... . eyJzdWIi... . SflKxwRJ...
  header      payload      signature
```

| Rész | Tartalom | Példa |
|------|----------|-------|
| **Header** | Algoritmus és típus | `{"alg": "HS256", "typ": "JWT"}` |
| **Payload** | Adatok (claims) | `{"sub": "42", "exp": 1700000000}` |
| **Signature** | Aláírás (hitelesítés) | HMAC-SHA256(header + payload, SECRET_KEY) |

- **Önálló (self-contained)** – A token tartalmazza a felhasználó adatait (pl. `sub: "42"` = user ID). A szerver nem kell adatbázist kérdezzen a token ellenőrzéséhez, elég a titkos kulccsal hitelesíteni az aláírást.
- **`sub` (subject)** – Standard JWT claim, ami az „alany" azonosítóját tartalmazza. Konvenció: a felhasználó ID-ja string-ként.
- **`exp` (expiration)** – A token lejárati ideje UTC timestamp-ként. Lejárt token = 401 hiba. Ezért van 30 perces érvényesség.

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

### 🧠 Részletes Magyarázat

- **`SECRET_KEY`** – A szerver titkos kulcsa. Ezzel írjuk alá a tokent, és ezzel ellenőrizzük. Ha valaki megszerzi, hamis tokeneket tudna gyártani. **Mindig .env-ből** olvassuk, soha nincs a kódban!
- **`HS256`** – HMAC-SHA256 szimmetrikus aláírási algoritmus. Ugyanaz a kulcs írja alá és ellenőrzi. Egyszerű és gyors, kisebb alkalmazásokhoz ideális.
- **`data.copy()`** – Az eredeti dict-et nem módosítjuk (tiszta függvény), hanem másolatot készítünk és ahhoz adjuk az `exp` mezőt.
- **`jwt.encode()`** – A payload-ot és az `exp`-et kódolja, aláírja a SECRET_KEY-jel, és visszaadja a JWT string-et.
- **`jwt.decode()`** – Ellenőrzi az aláírást és a lejáratot. Ha bármi nem stimmel (módosított token, lejárt, rossz kulcs), `JWTError` kivételt dob.

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

### 🧠 Részletes Magyarázat

- **`OAuth2PasswordRequestForm`** – FastAPI beépített form osztálya, ami `username` és `password` mezőket vár `application/x-www-form-urlencoded` formátumban (nem JSON!). A Swagger UI automatikusan mutatja a bejelentkezési űrlapot.
- **`form.username`** – Az OAuth2 szabvány `username`-et használ, de mi email-hez kötjük. A `form.username` értéke az, amit a felhasználó a „username" mezőbe ír.
- **Egybevont hibaüzenet** – `"Hibás email vagy jelszó"` – szándékosan nem mondjuk meg, hogy az email nem létezik VAGY a jelszó rossz. Biztonsági okokból: ne segítsük a támadót, hogy kitalálja, melyik email regisztrálva van.
- **`status_code=401`** – `401 Unauthorized`: nincs érvényes hitelesítő adat (rossz email/jelszó). Nem azonos a `403 Forbidden`-nel (az azt jelenti: tudjuk ki vagy, de nincs jogod).
- **`"token_type": "bearer"`** – A token típusa. A „bearer" azt jelenti: „aki bemutaja ezt a tokent, az hozzáférhet" – mint egy belépőjegy. A kliens a `Authorization: Bearer <token>` fejlécben küldi.

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

### 🧠 Részletes Magyarázat

- **`OAuth2PasswordBearer(tokenUrl="/auth/login")`** – Ez egy FastAPI dependency, ami automatikusan kiolvassa a tokent az `Authorization: Bearer <token>` fejlécből. A `tokenUrl` paraméter a Swagger UI-nak jelzi, hol van a login végpont (a „lakat" ikon megjelenik).
- **`get_current_user` dependency lánc:**
```
Kérés fejléc: "Authorization: Bearer eyJ..."
  → oauth2_scheme: kiszedi a tokent ("eyJ...")
  → token_dekodolas: ellenőrzi és dekódolja
  → payload.get("sub"): user ID kinyerése
  → db.query: felhasználó betöltése az adatbázisból
  → return user: a végpont megkapja a felhasználó objektumot
```
- **Három szintű ellenőrzés:**
  1. Van-e token? (oauth2_scheme – ha nincs `Authorization` fejléc → 401)
  2. Érvényes-e a token? (jwt.decode – lejárt/módosított → JWTError → 401)
  3. Létezik-e a felhasználó? (db.query – ha törölték közben → 401)
- **`headers={"WWW-Authenticate": "Bearer"}`** – HTTP szabvány: 401-es válasznál meg kell mondani, milyen authentikációs módot várunk. A böngésző/kliens ebből tudja, hogy Bearer tokent kell küldenie.

### Használat végpontokban

```python
@router.get("/profil", response_model=schemas.FelhasznaloValasz)
def profil(current_user = Depends(get_current_user)):
    return current_user
```

### 🧠 Részletes Magyarázat

- **`Depends(get_current_user)`** – Bármelyik végpontban használhatjuk. Ha a végpont paraméterlistájában szerepel, az adott végpont **védett** lesz: token nélkül 401-et ad.
- **Swagger UI használata:** A Swagger felületén a „lakat" ikonra kattintva beírhatod a tokent. Ezután minden kéréshez automatikusan hozzáadja az `Authorization: Bearer <token>` fejlécet.
- **Minimális kód** – A végpont maga egyetlen sor: `return current_user`. Az összes authentikációs logika a dependency-ben van. Ez a Separation of Concerns elv: a végpont csak az üzleti logikáért felel.

---

## Gyakorlat

1. Hozd létre az `app/auth.py` modult a jelszó hash-elő és JWT függvényekkel
2. Készítsd el a regisztráció és login végpontokat
3. Készíts védett `/profil` végpontot
4. Teszteld a Swagger UI-ban: regisztrálj, lépj be, használd a tokent
5. Commitold és pushold
