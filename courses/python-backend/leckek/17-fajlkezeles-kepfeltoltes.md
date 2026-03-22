# 📘 Lecke 17 – Fájlkezelés és képfeltöltés

> 📚 Dokumentáció:
> https://fastapi.tiangolo.com/tutorial/request-files/
> https://fastapi.tiangolo.com/tutorial/request-files/#uploadfile
> https://github.com/andrew-d/python-multipart

---

## 103–104. óra: Fájlok fogadása

### python-multipart telepítése

```bash
pip install python-multipart
```

### 🧠 Részletes Magyarázat

- **`python-multipart`** – A fájlfeltöltés `multipart/form-data` formátumot használ (nem JSON-t!). A FastAPI a `python-multipart` könyvtárat használja a fájlok kiolvasásához. Nélküle `422 Unprocessable Entity` hibát kapunk fájl feltöltésnél.

### Egyszerű fájl feltöltés

```python
from fastapi import APIRouter, UploadFile, File

router = APIRouter(prefix="/fajlok", tags=["Fájlok"])

@router.post("/feltoltes")
async def fajl_feltoltes(fajl: UploadFile = File(...)):
    return {
        "fajlnev": fajl.filename,
        "tipus": fajl.content_type,
        "meret": fajl.size
    }
```

### 🧠 Részletes Magyarázat

- **`UploadFile`** – FastAPI típus a fájl fogadásához. Tulajdonságai:
  - `filename` – Az eredeti fájlnév (amit az ügyfél küldött)
  - `content_type` – MIME típus (pl. `image/png`, `text/plain`)
  - `size` – Fájlméret bájtokban
  - `read()` – A fájl tartalmát olvassa (async)
  - `seek(0)` – Visszaáll a fájl elejére (ha többször akarjuk olvasni)
- **`File(...)`** – A `...` (Ellipsis) kötelezővé teszi a paramétert. `File(None)` opcionálissá tenné.
- **`async def`** – Fájlolvasáshoz az `async` verzió ajánlott, mert az `await fajl.read()` nem blokkolja a szervert.

### Fájl mentése lemezre

```python
import os
import uuid

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/feltoltes/mentes")
async def fajl_mentes(fajl: UploadFile = File(...)):
    # Egyedi fájlnév generálás
    kiterjesztes = fajl.filename.split(".")[-1]
    uj_nev = f"{uuid.uuid4()}.{kiterjesztes}"
    fajl_utvonal = os.path.join(UPLOAD_DIR, uj_nev)

    # Fájl mentése
    tartalom = await fajl.read()
    with open(fajl_utvonal, "wb") as f:
        f.write(tartalom)

    return {"fajlnev": uj_nev, "utvonal": fajl_utvonal}
```

### 🧠 Részletes Magyarázat

- **`uuid.uuid4()`** – Véletlenszerű egyedi azonosítót generál (pl. `a3b2c1d4-e5f6-7890-abcd-ef1234567890`). Ezzel a feltöltött fájl **nem a felhasználó által adott nevet** kapja, hanem egyedit. Ez megakadályozza: (1) fájlnév-ütközést, (2) path traversal támadást (pl. `../../etc/passwd`).
- **`fajl.filename.split(".")[-1]`** – A kiterjesztést az eredeti fájlnévből veszi ki (pl. `kep.png` → `png`). Figyelem: éles projektben a MIME type alapján kell validálni, nem a kiterjesztés alapján!
- **`os.makedirs(UPLOAD_DIR, exist_ok=True)`** – Létrehozza az `uploads/` mappát, ha még nem létezik. Az `exist_ok=True` megakadályozza a hibát, ha a mappa már létezik.
- **`"wb"` mód** – Binary write: bináris fájlokat (képek, PDF) így kell írni. A `"w"` (text mode) elrontaná a bináris adatokat.

### Fájlméret és típus validáció

```python
MEGENGEDETT_TIPUSOK = ["image/jpeg", "image/png", "image/webp"]
MAX_MERET = 5 * 1024 * 1024  # 5 MB

@router.post("/kep/feltoltes")
async def kep_feltoltes(fajl: UploadFile = File(...)):
    # Típus ellenőrzés
    if fajl.content_type not in MEGENGEDETT_TIPUSOK:
        raise HTTPException(400, "Csak JPEG, PNG vagy WebP kép engedélyezett")

    # Méret ellenőrzés
    tartalom = await fajl.read()
    if len(tartalom) > MAX_MERET:
        raise HTTPException(400, "A fájl mérete max 5 MB lehet")

    # Mentés
    kiterjesztes = fajl.content_type.split("/")[-1]
    nev = f"{uuid.uuid4()}.{kiterjesztes}"
    with open(os.path.join(UPLOAD_DIR, nev), "wb") as f:
        f.write(tartalom)

    return {"fajlnev": nev}
```

### 🧠 Részletes Magyarázat

- **MIME típus validáció** – A `content_type` a kliens által küldött MIME típus. Csak a megengedett típusok fogadhatók el. **Biztonsági szempont:** a kliens hazudhat a MIME típusról! Éles rendszerben a fájl tartalmát is érdemes ellenőrizni (magic bytes).
- **Méret validáció** – A `len(tartalom)` bájtokban adja a méretet. `5 * 1024 * 1024 = 5,242,880 bájt = 5 MB`. A validációt a tartalom beolvasása **után** végezzük – nagy fájloknál érdemes streaming megoldást használni.
- **Kiterjesztés a MIME-ből** – A `"image/png".split("/")[-1]` → `"png"`. Ez megbízhatóbb, mint a fájlnév kiterjesztésének használata.

---

## 105–106. óra: Statikus fájlok kiszolgálása

### Fájlok letöltése

```python
from fastapi.responses import FileResponse

@router.get("/letoltes/{fajlnev}")
def fajl_letoltes(fajlnev: str):
    fajl_utvonal = os.path.join(UPLOAD_DIR, fajlnev)
    if not os.path.exists(fajl_utvonal):
        raise HTTPException(404, "Fájl nem található")
    return FileResponse(fajl_utvonal)
```

### 🧠 Részletes Magyarázat

- **`FileResponse`** – A FastAPI speciális válasz típusa fájlok küldésére. Automatikusan beállítja a `Content-Type` fejlécet a fájl kiterjesztése alapján.
- **`os.path.join(UPLOAD_DIR, fajlnev)`** – Biztonságosan összekapcsolja az upload könyvtárat és a fájlnevet. **Fontos:** éles rendszerben ellenőrizni kell, hogy a `fajlnev` nem tartalmaz `..`-ot (path traversal támadás elleni védelem).
- **404 kezelés** – Ha a fájl nem létezik, 404-et adunk vissza (nem 500-at).

### StaticFiles mount

```python
from fastapi.staticfiles import StaticFiles

app.mount("/static", StaticFiles(directory="uploads"), name="static")
# Elérhető: http://localhost:8000/static/kep123.jpg
```

### 🧠 Részletes Magyarázat

- **`app.mount()`** – Egy alkönyvtárat „csatol" egy URL útvonalra. Az `uploads/` mappa tartalma a `/static/` URL alatt lesz elérhető.
- **Különbség a `FileResponse`-tól** – A `FileResponse` egyedi végpont, egyenkénti logikával. A `StaticFiles` az egész mappát kiszolgálja – nincs egyedi logika (validáció, jogosultság). Egyszerű, de kevésbé kontrollálható.
- **Mikor melyiket?** – `StaticFiles`: publikus képek, CSS, JS. `FileResponse`: jogosultságellenőrzés, letöltés számolás, vízjel hozzáadás.

### Kép hozzárendelése entitáshoz

```python
# app/models.py
class Termek(Base):
    __tablename__ = "termekek"
    id = Column(Integer, primary_key=True, index=True)
    nev = Column(String, nullable=False)
    ar = Column(Integer, nullable=False)
    kep_url = Column(String, nullable=True)
```

```python
@router.post("/{termek_id}/kep")
async def termek_kep_feltoltes(
    termek_id: int,
    fajl: UploadFile = File(...),
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    termek = db.query(models.Termek).filter(models.Termek.id == termek_id).first()
    if not termek:
        raise HTTPException(404, "Termék nem található")

    nev = f"{uuid.uuid4()}.{fajl.filename.split('.')[-1]}"
    with open(os.path.join(UPLOAD_DIR, nev), "wb") as f:
        f.write(await fajl.read())

    termek.kep_url = f"/static/{nev}"
    db.commit()
    db.refresh(termek)
    return termek
```

### 🧠 Részletes Magyarázat

- **`kep_url = Column(String, nullable=True)`** – A `nullable=True` lehetővé teszi, hogy a terméknek ne legyen képe (NULL az adatbázisban). A kép URL-jét tároljuk, nem magát a képet – a bináris adat a fájlrendszeren marad.
- **Két lépés:** (1) fájl mentése a lemezre, (2) URL elmentése az adatbázisba. Ha a fájlmentés sikeres, de a DB commit nem, árva fájl marad. Éles rendszerben ezt tranzakcióval/cleanup-pal kell kezelni.
- **`/static/{nev}`** – A kép URL-je a `StaticFiles` mount útvonalán érhető el. A kliens ezt az URL-t kapja a JSON válaszban, és közvetlenül megnyithatja a böngészőben.

---

## 107–108. óra: Fájlfeltöltés tesztelése

### Teszt fájl feltöltéshez

```python
import io

def test_fajl_feltoltes(client, auth_headers):
    fajl_tartalom = b"teszt fajl tartalom"
    response = client.post(
        "/fajlok/feltoltes",
        files={"fajl": ("teszt.txt", io.BytesIO(fajl_tartalom), "text/plain")}
    )
    assert response.status_code == 200
    assert response.json()["fajlnev"] == "teszt.txt"

def test_kep_feltoltes(client, auth_headers):
    # 1x1 pixel PNG
    png_bytes = (
        b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01'
        b'\x00\x00\x00\x01\x08\x02\x00\x00\x00\x90wS\xde\x00'
        b'\x00\x00\x0cIDATx\x9cc\xf8\x0f\x00\x00\x01\x01\x00'
        b'\x05\x18\xd8N\x00\x00\x00\x00IEND\xaeB`\x82'
    )
    response = client.post(
        "/fajlok/kep/feltoltes",
        files={"fajl": ("kep.png", io.BytesIO(png_bytes), "image/png")}
    )
    assert response.status_code == 200

def test_rossz_fajltipus(client):
    response = client.post(
        "/fajlok/kep/feltoltes",
        files={"fajl": ("virus.exe", io.BytesIO(b"bad"), "application/exe")}
    )
    assert response.status_code == 400
```

### 🧠 Részletes Magyarázat

- **`files=` paraméter** – A TestClient fájl feltöltésnél az `files` paramétert használja (nem `json=`). A formátum: `{"paraméter_név": ("fájlnév", tartalom, MIME_típus)}`.
- **`io.BytesIO`** – Memóriában lévő bináris „fájl-objektum". A TestClient ezt olvassa, mintha valódi fájl lenne. Nem kell tényleges fájlt létrehozni a lemezen.
- **1x1 PNG** – A `png_bytes` egy minimális, de **érvényes** PNG kép. A tesztben érdemes valódi formátumú fájlt használni, mert a szerver ellenőrizheti a magic bytes-ot.
- **Negatív teszt** – A `test_rossz_fajltipus` ellenőrzi, hogy `.exe` fájlt nem fogad el a szerver. Ez biztonsági teszt – ha átmenne, a szerverre tetszőleges fájlt lehetne feltölteni.

---

## Gyakorlat

1. Készíts fájl feltöltő végpontot
2. Adj hozzá fájlméret és típus validációt (max 5 MB, csak képek)
3. Készíts letöltő végpontot és mountolj StaticFiles-t
4. Rendeld hozzá a feltöltött képet egy modellhez (pl. Termék)
5. Írj tesztet a feltöltéshez és a validációhoz
6. Commitold és pushold
