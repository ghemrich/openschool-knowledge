# Kiegészítő gyakorlatok – 9. hét: Összetett adatszerkezetek

> Ezek a feladatok a heti házi feladat melletti **extra gyakorlást** szolgálják.
> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz

---

### 9.1 – Telefonkönyv ⭐
Hozz létre egy szótárat, ahol a kulcs a név, az érték a telefonszám (5 bejegyzés). Kérd be egy nevet, és írd ki a hozzá tartozó számot. Ha nincs benne, írd ki: „Nincs ilyen bejegyzés."

### 9.2 – Szavazás szótárral ⭐
Adott a szavazatok listája: `["Anna", "Béla", "Anna", "Csaba", "Anna", "Béla", "Csaba", "Csaba", "Béla", "Anna"]`. Számold meg szótárral, ki hány szavazatot kapott, és keresd meg a nyertest!

### 9.3 – Receptkönyv ⭐⭐
Hozz létre egy szótárak listáját 3 recepttel. Minden recept tartalmazza: `nev`, `hozzavalok` (lista), `elkeszitesi_ido` (percben), `nehezseg` (könnyű/közepes/nehéz). Írd ki az összes receptet formázottan, és keresd meg a leggyorsabb receptet.

### 9.4 – Jegynyilvántartás ⭐⭐
Készíts programot, ahol:
- A felhasználó tanulókat ad hozzá (név)
- Mindegyik tanulóhoz jegyeket rögzít (listában)
- Kiírja minden tanuló átlagát
- Kiírja a legjobb és legrosszabb átlagú tanulót

Használj szótárat, ahol a kulcs a név, az érték a jegyek listája.

### 9.5 – Beágyazott szótár ⭐⭐⭐
Hozz létre egy komplex adatszerkezetet, amely egy iskola osztályait tartalmazza:
```python
iskola = {
    "9.A": {"osztalyfonok": "Kovács Mária", "tanulok": [...]},
    "9.B": {"osztalyfonok": "Tóth Péter", "tanulok": [...]}
}
```
Minden tanulónak legyen neve és átlaga. Írd ki osztályonként a tanulók névsorát és az osztályátlagot. Keresd meg az iskola legjobb tanulóját (név, osztály, átlag).
