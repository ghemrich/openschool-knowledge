# 📘 Lecke 02 – FastAPI bevezetés

> 📚 Dokumentáció:  
> https://fastapi.tiangolo.com/ ·  
> https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods ·  
> https://developer.mozilla.org/en-US/docs/Web/HTTP/Status

---

# 13–14. óra: Mi az a REST API?

## 🌐 HTTP protokoll

A web alapja a **HTTP** (HyperText Transfer Protocol). Minden webes kommunikáció kérés–válasz (request–response) alapú:

```
Kliens  →  HTTP kérés  →  Szerver
Kliens  ←  HTTP válasz ←  Szerver
```

### 🧠 Részletes Magyarázat

**Kliens** – A kérést küldő fél (böngésző, mobilalkalmazás, vagy akár egy másik szerver).

**Szerver** – A kérést fogadó és feldolgozó fél. EZ az, amit mi fogunk fejleszteni!

**REST API** – „Representational State Transfer Application Programming Interface". Egy szabályrendszer, ami meghatározza, hogyan kommunikáljanak a kliensek a szerverrel. A lényeg:
- Minden erőforrásnak (pl. felhasználó, termék) van egy URL-je
- A HTTP metódusok jelölik, MIT akarunk csinálni
- Az adatok JSON formátumban utaznak

---

## 📮 HTTP metódusok

| Metódus | Jelentés | Példa |
|---------|----------|-------|
| `GET` | Adat lekérése | Felhasználók listázása |
| `POST` | Új adat létrehozása | Új felhasználó regisztráció |
| `PUT` | Meglévő adat módosítása | Profil frissítése |
| `DELETE` | Adat törlése | Felhasználó törlése |

### 🧠 Részletes Magyarázat

Gondolj rá, mint egy könyvtári rendszer:
- **GET** /konyvek → „Mutasd az összes könyvet" (olvasás)
- **POST** /konyvek → „Adj hozzá egy új könyvet" (létrehozás)
- **PUT** /konyvek/5 → „Módosítsd az 5-ös könyvet" (frissítés)
- **DELETE** /konyvek/5 → „Töröld az 5-ös könyvet" (törlés)

Ezeket együtt **CRUD**-nak hívjuk: **C**reate, **R**ead, **U**pdate, **D**elete.

---

## 📊 Státuszkódok

| Kód | Jelentés | Mikor |
|-----|----------|-------|
| `200` | OK | Sikeres GET/PUT |
| `201` | Created | Sikeres POST |
| `204` | No Content | Sikeres DELETE |
| `400` | Bad Request | Hibás kérés |
| `404` | Not Found | Nem található |
| `422` | Unprocessable Entity | Validációs hiba |
| `500` | Internal Server Error | Szerverhiba |

### 🧠 Részletes Magyarázat

A státuszkód egy háromjegyű szám, amit a szerver küld vissza a kérés eredményeként. Az első számjegy jelöli a kategóriát:

| Kezdet | Kategória | Példa |
|--------|-----------|-------|
| 2xx | Siker ✅ | 200 OK, 201 Created |
| 4xx | Kliens hiba ❌ | 404 Not Found, 400 Bad Request |
| 5xx | Szerver hiba 💥 | 500 Internal Server Error |

A 4xx = „te (kliens) rontottad el", 5xx = „én (szerver) rontottam el".

---

## 📋 JSON formátum

Az API-k **JSON** formátumban kommunikálnak:

```json
{
    "id": 1,
    "nev": "Kiss Anna",
    "email": "anna@example.com",
    "aktiv": true
}
```

### 🧠 Részletes Magyarázat

**JSON** (JavaScript Object Notation) – Szöveg-alapú adatcsere formátum. Gyakorlatilag MINDEN modern API JSON-t használ.

**Python szótár ↔ JSON:**
| Python | JSON |
|--------|------|
| `dict` | `object {}` |
| `list` | `array []` |
| `str` | `string` |
| `int`/`float` | `number` |
| `True`/`False` | `true`/`false` |
| `None` | `null` |

A FastAPI automatikusan konvertálja a Python szótárakat JSON-ba!

---

# 15–16. óra: Első FastAPI alkalmazás

## 📦 Telepítés

```bash
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows
pip install fastapi uvicorn
pip freeze > requirements.txt
```

### 🧠 Részletes Magyarázat

**fastapi** – Maga a web framework, ami a végponttokat kezeli.

**uvicorn** – Az ASGI szerver, ami futtatja a FastAPI alkalmazást. A FastAPI önmagában nem tud futni – kell egy szerver, ami fogadja a HTTP kéréseket és továbbítja a FastAPI-nak.

---

## 🚀 Első alkalmazás

Hozd létre a `main.py` fájlt:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Helló, FastAPI!"}
```

### 🧠 Részletes Magyarázat

**from fastapi import FastAPI** – Betölti a FastAPI osztályt a csomagból.

**app = FastAPI()** – Létrehoz egy FastAPI alkalmazáspéldányt. Ez az `app` objektum tartalmazza az összes végpontot.

**@app.get("/")** – Ez egy **dekorátor**. A `@` jellel egy függvényt „dekorálunk" – jelezzük a FastAPI-nak, hogy ez a függvény a `GET /` kérésekre válaszoljon.
- `@app.get` → GET metódus
- `"/"` → gyökér útvonal (pl. `http://127.0.0.1:8000/`)

**return {"message": "Helló, FastAPI!"}** – A visszaadott szótárat a FastAPI automatikusan JSON-ba konvertálja.

---

## ▶️ Futtatás

```bash
uvicorn main:app --reload
```

### 🧠 Részletes Magyarázat

| Rész | Jelentés |
|------|----------|
| `main` | A fájl neve (`main.py`, kiterjesztés nélkül) |
| `app` | A FastAPI példány neve a fájlban |
| `--reload` | Automatikus újraindítás, ha módosítod a kódot |

A szerver elindul: `http://127.0.0.1:8000` – nyisd meg böngészőben!

---

## 📖 Swagger UI

Nyisd meg a böngészőben: `http://127.0.0.1:8000/docs`

Ez egy **automatikusan generált** interaktív API dokumentáció! Innen ki tudod próbálni a végpontjaidat.

### 🧠 Részletes Magyarázat

A Swagger UI a FastAPI egyik legnagyobb előnye: AUTOMATIKUSAN generálja a dokumentációt a kódod alapján. Nem kell külön dokumentációt írni!

- **Try it out** → Kipróbálhatod a végpontot a böngészőből
- **Execute** → Elküldi a kérést, megmutatja a választ
- Alternatív dokumentáció: `http://127.0.0.1:8000/redoc`

---

# 17–18. óra: Több végpont, visszatérési értékek

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

### 🧠 Részletes Magyarázat

Minden `@app.get()` dekorátor egy **új végpontot** hoz létre. A FastAPI rugalmas – visszaadhatsz szótárat, listát, szöveget, számot, vagy ezek bármilyen kombinációját. Mindent automatikusan JSON-ba konvertál.

**Minden végpont automatikusan megjelenik a Swagger UI-ban!** Ha új `@app.get()` függvényt veszel fel, frissítsd a `/docs` oldalt.

---

## ✏️ Gyakorlat

1. Hozz létre egy FastAPI projektet virtuális környezettel
2. Készíts 3 GET végpontot különböző adatokkal
3. Teszteld a Swagger UI-ban (`/docs`)
4. Commitold és pushold
