# Lecke 17 – Fájlkezelés és képfeltöltés

> **Dokumentáció:** [FastAPI File Upload](https://fastapi.tiangolo.com/tutorial/request-files/) · [UploadFile](https://fastapi.tiangolo.com/tutorial/request-files/#uploadfile) · [python-multipart](https://github.com/andrew-d/python-multipart)

---

## 103–104. óra: Fájlok fogadása

### python-multipart telepítése

```bash
pip install python-multipart
```

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

### StaticFiles mount

```python
from fastapi.staticfiles import StaticFiles

app.mount("/static", StaticFiles(directory="uploads"), name="static")
# Elérhető: http://localhost:8000/static/kep123.jpg
```

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

---

## Gyakorlat

1. Készíts fájl feltöltő végpontot
2. Adj hozzá fájlméret és típus validációt (max 5 MB, csak képek)
3. Készíts letöltő végpontot és mountolj StaticFiles-t
4. Rendeld hozzá a feltöltött képet egy modellhez (pl. Termék)
5. Írj tesztet a feltöltéshez és a validációhoz
6. Commitold és pushold
