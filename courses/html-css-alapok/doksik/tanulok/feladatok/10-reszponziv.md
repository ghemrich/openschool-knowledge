# Feladatok – 10. hét: Reszponzív design

> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz
> A megoldásokat commitold és pushold a GitHub repódba.

---

### 10.1 – Viewport meta ⭐
Készíts egy oldalt a viewport meta tag-gel, és ellenőrizd, hogy mobilon is jól jelenik meg. Használj `max-width: 100%`-ot a képeken.

### 10.2 – Első media query ⭐
Készíts egy oldalt, ahol 768px alatt a háttérszín kékre, felette zöldre változik. Adj hozzá szöveget, ami jelzi az aktuális nézetet.

### 10.3 – Reszponzív navigáció ⭐⭐
Készíts egy navigációs sávot, amely:
- Asztali nézetben vízszintes menü
- 768px alatt függőleges menüvé alakul
- Használj media query-t a váltáshoz

### 10.4 – Reszponzív kártya rács ⭐⭐
Készíts egy kártya rácsot, amely:
- Asztali nézetben 3 oszlopos
- Tableten (768px-1024px) 2 oszlopos
- Mobilon (768px alatt) 1 oszlopos
- Használj Flexbox-ot és media query-ket

### 10.5 – Mobile-first weboldal ⭐⭐⭐
Készíts egy komplett egy oldalas webhelyet mobile-first megközelítéssel:
- Először a mobil nézetet stílusozd (alapértelmezett)
- `min-width` media query-kkel bővítsd a tablet és asztali nézetet
- Legyen fejléc, navigáció, fő tartalom, sidebar és lábléc
- A sidebar mobilon a tartalom alatt, asztalin mellette jelenik meg
