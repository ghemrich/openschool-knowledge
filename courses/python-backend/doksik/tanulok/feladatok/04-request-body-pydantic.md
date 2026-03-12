# Feladatok – 4. hét: Request body és Pydantic

> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz
> A megoldásokat commitold és pushold a GitHub repódba.

---

### 4.1 – Első Pydantic modell ⭐
Hozz létre egy `Diak` Pydantic modellt (nev: str, kor: int, atlag: float). Készíts `POST /diakok` végpontot, amely fogadja és visszaadja az adatokat.

### 4.2 – Validáció ⭐
Egészítsd ki a `Diak` modellt Field validációval: `nev` min 2 karakter, `kor` 14 és 99 között, `atlag` 1.0 és 5.0 között. Teszteld hibás adatokkal.

### 4.3 – In-memory CRUD ⭐⭐
Készíts egy teljes in-memory CRUD API-t `Termek` modellel (nev, ar, leiras):
- `GET /termekek` – listázás
- `POST /termekek` – létrehozás (id-t a szerver generálja)
- `GET /termekek/{id}` – egy termék (404 ha nincs)
- `PUT /termekek/{id}` – módosítás
- `DELETE /termekek/{id}` – törlés

### 4.4 – Beágyazott modell ⭐⭐
Hozz létre egy `Rendeles` modellt, ami tartalmaz egy `cim: Cim` mezőt (Cim: varos, utca, iranyitoszam) és egy `tetelek: list[Tetel]` mezőt (Tetel: termek_nev, mennyiseg, egysegar). Készíts `POST /rendelesek` végpontot.

### 4.5 – Opcionális mezők ⭐⭐⭐
Készíts `TermekUpdate` modellt, ahol **minden mező opcionális** (`nev: str | None = None`, stb.). A `PUT /termekek/{id}` végpont csak a megadott mezőket módosítsa (partial update).
