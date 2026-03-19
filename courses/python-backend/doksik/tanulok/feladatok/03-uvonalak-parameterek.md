# Kiegészítő gyakorlatok – 3. hét: Útvonalak és paraméterek

> Ezek a feladatok a heti házi feladat melletti **extra gyakorlást** szolgálják.
> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz

---

### 3.1 – Mértékegység átváltó ⭐
Készíts végpontot: `GET /atvaltas/{ertek}/{egyseg}` ahol `egyseg` Enum (km, merfold, meter). Adja vissza az értéket a többi mértékegységben.

### 3.2 – Dátumformázó ⭐
Készíts végpontot: `GET /datum/{ev}/{honap}/{nap}` amely visszaadja a dátumot többféle formátumban:
- `"magyar": "2024. január 15."`
- `"iso": "2024-01-15"`
- `"het_napja": "hétfő"`

Adj 400-as hibát érvénytelen dátumra.

### 3.3 – Szűrt napló ⭐⭐
Készíts in-memory naplóbejegyzéseket (időbélyeg, szint, üzenet). `GET /naplo` végpont a következő query paraméterekkel:
- `szint` (opcionális Enum: info, warning, error)
- `kulcsszo` (opcionális string, szűrés az üzenetben)
- `utolso_n` (opcionális int, utolsó N bejegyzés)

### 3.4 – Szöveg átalakító ⭐⭐
Készíts végpontot: `GET /szoveg/{szoveg}` a következő query paraméterekkel:
- `muvelet` (Enum: nagybetus, kisbetus, forditott, cimsor)
- `ismetles` (opcionális int, default 1)

Adja vissza az átalakított szöveget: `{"eredeti": "...", "eredmeny": "..."}`.

### 3.5 – Receptkereső ⭐⭐⭐
Készíts in-memory receptgyűjteményt (legalább 10 recept). `GET /receptek` végpont:
- `kategoria` path-ban VAGY query-ben (Enum: leves, foetel, desszert)
- `max_ido` (opcionális int, elkészítési idő percben)
- `nehezseg` (opcionális Enum: konnyu, kozepes, nehez)
- `rendezés` (opcionális Enum: nev, ido_novekvo, ido_csökkeno)
- `oldal` és `meret` query paraméterek lapozáshoz

Adja vissza a szűrt recepteket az összes szűrési feltétellel együtt.
