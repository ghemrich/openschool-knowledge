# Lecke 02 – FastAPI bevezetés

> **Dokumentáció:** [FastAPI](https://fastapi.tiangolo.com/) · [HTTP metódusok](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods) · [HTTP státuszkódok](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

---

## 13–14. óra: Mi az a REST API?

### HTTP protokoll

A web alapja a **HTTP** (HyperText Transfer Protocol). Minden webes kommunikáció kérés–válasz (request–response) alapú:

```
Kliens  →  HTTP kérés  →  Szerver
Kliens  ←  HTTP válasz ←  Szerver
```

### HTTP metódusok

| Metódus | Jelentés | Példa |
|---------|----------|-------|
| `GET` | Adat lekérése | Felhasználók listázása |
| `POST` | Új adat létrehozása | Új felhasználó regisztráció |
| `PUT` | Meglévő adat módosítása | Profil frissítése |
| `DELETE` | Adat törlése | Felhasználó törlése |

### Státuszkódok

| Kód | Jelentés | Mikor |
|-----|----------|-------|
| `200` | OK | Sikeres GET/PUT |
| `201` | Created | Sikeres POST |
| `204` | No Content | Sikeres DELETE |
| `400` | Bad Request | Hibás kérés |
| `404` | Not Found | Nem található |
| `422` | Unprocessable Entity | Validációs hiba |
| `500` | Internal Server Error | Szerverhiba |

### JSON formátum

Az API-k **JSON** formátumban kommunikálnak:

```json
{
    "id": 1,
    "nev": "Kiss Anna",
    "email": "anna@example.com",
    "aktiv": true
}
```

---

## 15–16. óra: Első FastAPI alkalmazás

### Telepítés

```bash
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows
pip install fastapi uvicorn
pip freeze > requirements.txt
```

### Első alkalmazás

Hozd létre a `main.py` fájlt:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Helló, FastAPI!"}
```

### Futtatás

```bash
uvicorn main:app --reload
```

- `main` → a fájl neve (`main.py`)
- `app` → a FastAPI példány neve
- `--reload` → automatikus újraindítás módosításkor

### Swagger UI

Nyisd meg a böngészőben: `http://127.0.0.1:8000/docs`

Ez egy **automatikusan generált** interaktív API dokumentáció! Innen ki tudod próbálni a végpontjaidat.

Alternatív dokumentáció: `http://127.0.0.1:8000/redoc`

---

## 17–18. óra: Több végpont, visszatérési értékek

```python
from fastapi import FastAPI

app = FastAPI()

# Egyszerű üdvözlés
@app.get("/")
def root():
    return {"message": "Helló, FastAPI!"}

# Információs végpont
@app.get("/info")
def info():
    return {
        "alkalmazas": "Backend kurzus API",
        "verzio": "1.0.0",
        "szerzo": "OpenSchool"
    }

# Lista visszaadása
@app.get("/gyumolcsok")
def gyumolcsok():
    return [
        {"nev": "alma", "szin": "piros"},
        {"nev": "banán", "szin": "sárga"},
        {"nev": "szőlő", "szin": "zöld"}
    ]
```

Minden végpont automatikusan megjelenik a Swagger UI-ban!

---

## Gyakorlat

1. Hozz létre egy FastAPI projektet virtuális környezettel
2. Készíts 3 GET végpontot különböző adatokkal
3. Teszteld a Swagger UI-ban (`/docs`)
4. Commitold és pushold
