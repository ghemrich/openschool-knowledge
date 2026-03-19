# Kiegészítő gyakorlatok – 5. hét: Response modellek és hibakezelés

> Ezek a feladatok a heti házi feladat melletti **extra gyakorlást** szolgálják.
> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz

---

### 5.1 – Különböző response modellek ⭐
Készíts `Alkalmazott` belső modellt (nev, email, fizetes, adoazonosito). Hozz létre két response modellt:
- `AlkalmazottPublikus`: csak nev és email
- `AlkalmazottAdmin`: minden mező

Készíts két végpontot, amelyek ugyanazt az adatot különböző response_model-lel adják vissza.

### 5.2 – Egyedi hibaformátum ⭐⭐
Készíts egy egységes hibaformátumot: `{"siker": false, "hibakod": "...", "uzenet": "...", "reszletek": {...}}`. Készíts `exception_handler`-eket a következő hibákhoz:
- `RequestValidationError` → 422, hibakód: "VALIDATION_ERROR"
- `HTTPException` → az eredeti status kód, hibakód: "HTTP_ERROR"
- Általános `Exception` → 500, hibakód: "INTERNAL_ERROR"

### 5.3 – Borítékolt válaszok ⭐⭐
Készíts egy generikus "boríték" response modellt:
```python
class ApiValasz(BaseModel):
    siker: bool
    adat: Any | None = None
    uzenet: str | None = None
```
Minden végpont ezt a formátumot használja. Sikeres műveletnél `siker=True, adat={...}`, hibánál `siker=False, uzenet="..."`.

### 5.4 – Validációs hibaüzenetek ⭐⭐
Készíts `Regisztracio` modellt részletes magyar nyelvű hibaüzenetekkel:
- `email`: `Field(description="Érvényes email cím")`
- `jelszo`: min 8 karakter, tartalmaz nagybetűt és számot (custom validator, magyar hibaüzenettel)

### 5.5 – Hibakatalógus ⭐⭐⭐
Készíts egy `errors.py` modult, amely tartalmaz egy `AppError` Enum-ot:
```python
class AppError(Enum):
    USER_NOT_FOUND = (404, "Felhasználó nem található")
    DUPLICATE_EMAIL = (409, "Ez az email már regisztrálva van")
    UNAUTHORIZED = (401, "Bejelentkezés szükséges")
    FORBIDDEN = (403, "Nincs jogosultságod")
    ...
```
Készíts `raise_app_error(error: AppError)` segédfüggvényt és használd a végpontokban. Dokumentáld a lehetséges hibákat a `responses` paraméterrel.
