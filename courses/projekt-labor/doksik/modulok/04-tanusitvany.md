# Modul 4 — Tanúsítvány rendszer

## Cél

Automatikus tanúsítvány generálás kurzus befejezésekor. A modul végére:

- A rendszer felismeri, mikor fejezte be valaki a kurzust
- PDF tanúsítvány generálódik egyedi azonosítóval és QR kóddal
- Publikus verifikációs endpoint: bárki ellenőrizheti a tanúsítvány hitelességét

## 4.1 Completion logika

Mikor tekinthető befejezettnek egy kurzus?

**Szabály:** Minden kötelező feladat (`Exercise`) `completed` státuszban van.

```python
# app/services/certificate.py

def is_course_completed(db: Session, user_id: int, course_id: int) -> bool:
    total = db.query(Exercise).join(Module).filter(
        Module.course_id == course_id,
        Exercise.required == True
    ).count()

    completed = db.query(Progress).join(Exercise).join(Module).filter(
        Module.course_id == course_id,
        Progress.user_id == user_id,
        Progress.status == ProgressStatus.completed,
        Exercise.required == True
    ).count()

    return total > 0 and total == completed
```

**Feladat:**
- Adj hozzá egy `required` mezőt az `Exercise` modellhez (default: `True`)
- Implementáld a completion check logikát
- Teszteld: részben kész kurzus → False, teljesen kész → True

## 4.2 Certificate modell

```python
# app/models/certificate.py
import uuid
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from app.database import Base
from datetime import datetime, timezone

class Certificate(Base):
    __tablename__ = "certificates"

    id = Column(Integer, primary_key=True)
    cert_id = Column(String, unique=True, nullable=False,
                     default=lambda: str(uuid.uuid4()))
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    course_id = Column(Integer, ForeignKey("courses.id"), nullable=False)
    issued_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    pdf_path = Column(String)
```

**Feladat:**
- Hozd létre a Certificate modellt
- A `cert_id` UUID formátumú, egyedi azonosító
- Generálj Alembic migrációt
- Egyedi constraint: egy user egy kurzushoz csak egy tanúsítványt kaphat

## 4.3 PDF generálás

Két lehetőség:

| Könyvtár | Előny | Hátrány |
|----------|-------|---------|
| fpdf2 | Könnyű, nincs rendszer-függőség, natív PDF rajzolás | Alacsony szintű API |
| WeasyPrint | HTML/CSS → PDF, szép eredmény | Rendszer-függőségek (GTK, Pango) |

**Ajánlott: fpdf2** — könnyű, nincs rendszer-függőség, és natív PDF elemeket (szöveg, QR kód) rajzol közvetlenül.

```python
# app/services/pdf.py
from fpdf import FPDF

def generate_certificate_pdf(
    name: str,
    course_name: str,
    cert_id: str,
    issued_date: str,
    verify_url: str,
    qr_base64: str,
) -> bytes:
    """Generate a certificate PDF using fpdf2."""
    pdf = FPDF(orientation="L", unit="mm", format="A4")
    pdf.add_page()
    pdf.set_auto_page_break(auto=False)

    # Title
    pdf.set_font("Helvetica", "B", 36)
    pdf.set_y(30)
    pdf.cell(0, 15, "OpenSchool", ln=True, align="C")

    # Recipient
    pdf.set_font("Helvetica", "B", 28)
    pdf.cell(0, 15, name, ln=True, align="C")

    # Course
    pdf.set_font("Helvetica", "B", 22)
    pdf.cell(0, 12, course_name, ln=True, align="C")

    # Date + Certificate ID
    pdf.set_font("Helvetica", "", 12)
    pdf.cell(0, 8, f"Issued: {issued_date}", ln=True, align="C")
    pdf.cell(0, 5, f"Certificate ID: {cert_id}", ln=True, align="C")
    pdf.cell(0, 5, f"Verify: {verify_url}", ln=True, align="C")

    return pdf.output()
```

**Feladat:**
- Add hozzá az `fpdf2` csomagot a `requirements.txt`-hez
- Implementáld a PDF generálást az fpdf2-vel
- A tanúsítvány tartalmazza: név, kurzus neve, dátum, tanúsítvány ID, QR kód
- Teszteld: generálj egy minta PDF-et

## 4.4 QR kód

A tanúsítványon legyen egy QR kód, ami a verifikációs URL-re mutat.

```python
# app/services/qr.py
import qrcode
import io
import base64

def generate_qr_base64(url: str) -> str:
    qr = qrcode.make(url)
    buffer = io.BytesIO()
    qr.save(buffer, format="PNG")
    return base64.b64encode(buffer.getvalue()).decode()
```

**Feladat:**
- Add hozzá a `qrcode` csomagot a `requirements.txt`-hez
- A QR kód a verifikációs URL-re mutasson: `https://openschool.hu/verify/{cert_id}`
- A QR kódot base64 PNG-ként ágyazd be a HTML sablonba

## 4.5 API endpoint-ok

| Endpoint | Metódus | Jogosultság | Leírás |
|----------|---------|-------------|--------|
| `/api/me/certificates` | GET | autentikált | Saját tanúsítványaim listája |
| `/api/me/courses/{id}/certificate` | POST | autentikált | Tanúsítvány igénylése (ha kész a kurzus) |
| `/api/me/certificates/{cert_id}/pdf` | GET | autentikált | PDF letöltése |
| `/api/verify/{cert_id}` | GET | nyilvános | Tanúsítvány hitelesítés |

**A tanúsítvány igénylés flow-ja:**
1. Felhasználó hívja: `POST /api/me/courses/{id}/certificate`
2. Backend ellenőrzi: minden kötelező feladat kész?
3. Ha igen → Certificate rekord létrejön + PDF generálódik
4. Ha nem → 400 hibaüzenet: "A kurzus még nincs befejezve"
5. Ha már van tanúsítvány → 409: "Már van tanúsítványod ehhez a kurzushoz"

**Verifikációs endpoint válasz:**
```json
{
  "valid": true,
  "name": "Kiss Péter",
  "course": "Python alapok",
  "issued_at": "2025-06-15T12:00:00Z",
  "cert_id": "a1b2c3d4-..."
}
```

**Feladat:**
- Implementáld mind a 4 endpoint-ot
- A PDF fájlokat tárold a szerveren (pl. `data/certificates/` mappa)
- A verifikációs endpoint legyen publikus (nem kell token)

## 4.6 Tesztek

**Tesztelendő esetek:**
- Completion check: részben kész → False, teljesen kész → True
- Tanúsítvány igénylés: kész kurzus → 201, nem kész → 400, duplikált → 409
- Verifikáció: létező cert_id → valid, nem létező → 404
- PDF generálás: a fájl létrejön és nem üres

**Feladat:**
- Írj teszteket minden fenti esetre
- A PDF generálást mockold a tesztekben (gyorsabb)
- `pytest -v` → minden zöld

## Háttéranyag

Ezeket nem kell elejétől végig elolvasni — használd referenciaként, amikor az adott témánál tartasz.

| Téma | Link | Miért hasznos |
|------|------|---------------|
| fpdf2 | [py-pdf.github.io/fpdf2](https://py-pdf.github.io/fpdf2/) | Könnyű PDF generálás Python-ban |
| python-qrcode | [github.com/lincolnloop/python-qrcode](https://github.com/lincolnloop/python-qrcode) | QR kód generálás a verifikációs URL-hez |
| Jinja2 Templates | [jinja.palletsprojects.com](https://jinja.palletsprojects.com/) | HTML sablonok a tanúsítványhoz |
| UUID | [docs.python.org/3/library/uuid.html](https://docs.python.org/3/library/uuid.html) | Egyedi tanúsítvány azonosítók generálása |

## Verifikációs tesztek

A modul végén futtasd a verifikációs teszteket:

```bash
cd openschool-platform
pytest tesztek/modul-04/ -v
```

**Mit ellenőriznek a tesztek:**

| Tesztfájl | Ellenőrzések |
|-----------|---------------|
| `test_completion.py` | Certificate modell létezik (cert_id, user_id, course_id); `is_course_completed` függvény; Exercise-nek van `required` mezője; PDF és certificate HTML sablon létezik |
| `test_verify.py` | Verifikációs endpoint létezik; nem létező cert_id → 404; tanúsítvány igénylés és listázás auth-ot igényel; QR modul létezik |

> **Megjegyzés:** A verifikációs tesztek a PDF generálást nem futtatják, csak a fájlok létezését ellenőrzik. A részletes PDF teszt a **saját tesztek** feladata.

## Ellenőrzőlista

- [ ] Completion logika helyesen működik
- [ ] Certificate modell és migráció kész
- [ ] PDF tanúsítvány generálódik QR kóddal
- [ ] Tanúsítvány igénylés API működik (kész kurzus kell hozzá)
- [ ] Verifikációs endpoint publikusan elérhető
- [ ] Saját tesztek lefedik a completion, igénylés, verifikáció eseteket
- [ ] `pytest tesztek/modul-04/ -v` → minden zöld (verifikációs tesztek)
