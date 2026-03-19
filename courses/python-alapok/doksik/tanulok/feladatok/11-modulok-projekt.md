# Kiegészítő gyakorlatok – 11. hét: Modulok és összefoglaló projekt

> Ezek a feladatok a heti házi feladat melletti **extra gyakorlást** szolgálják.
> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz

---

### 11.1 – Konverter modul ⭐
Hozz létre egy `konverter.py` modult a következő függvényekkel:
- `km_merfold(km)` → km-ből mérföldre
- `kg_font(kg)` → kg-ból fontra
- `celsius_fahrenheit(c)` → Celsiusból Fahrenheitbe
- `liter_gallon(l)` → literből gallonra

A főprogramban (`foprogram.py`) importáld a modult és teszteld mindegyik függvényt.

### 11.2 – Fájl segédmodul ⭐⭐
Hozz létre egy `fajl_eszkozok.py` modult:
- `beolvas_sorok(fajlnev)` → beolvassa a fájlt, visszaadja sorok listájaként
- `sorok_szama(fajlnev)` → visszaadja a sorok számát
- `keres_szot(fajlnev, szo)` → visszaadja, hányszor fordul elő a szó a fájlban

A főprogramban hozz létre egy szöveges fájlt és teszteld a függvényeket.

### 11.3 – Vizsgafeladat másik adatfájllal ⭐⭐⭐
Ha a heti házi feladatban a `filmek.txt`-vel dolgoztál, most oldd meg ugyanazt a `konyvek.txt` (vagy `sportolok.txt`, `zenek.txt`) adatfájllal:
1. Beolvasás szótárak listájába
2. Darabszám kiírása
3. Kategória/műfaj szerinti számlálás
4. Legjobb/legrosszabb elem keresése
5. Keresés cím/név alapján + fájlba írás
6. Szűrés kategória/műfaj alapján

A függvényeket `fgv2.py` modulban, a főprogramot `feladat_extra.py`-ban helyezd el.

### 11.4 – Mini alkalmazás ⭐⭐⭐
Készíts egy „teendő lista" (todo) alkalmazást moduláris felépítéssel:
- `todo_fgv.py` modul: `betoltes(fajl)`, `mentes(fajl, lista)`, `hozzaadas(lista, elem)`, `torles(lista, sorszam)`, `listazas(lista)`
- `todo.py` főprogram: menürendszer (1=listázás, 2=hozzáadás, 3=törlés, 4=kilépés)
- Az adatok `todok.txt` fájlban tárolódjanak. Indításkor betölti, kilépéskor menti.
