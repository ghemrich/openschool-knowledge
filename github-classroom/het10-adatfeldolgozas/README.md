# 10. hét – Adatfeldolgozás

> **Határidő:** a következő óra előtt
> **Beadás:** commitold és pushold a megoldásaidat ebbe a repoba!
> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz

---

## 10.1 – Számlálás ⭐
Írj programot (`feladat1.py`). Adott egy szavakat tartalmazó lista: `["alma", "körte", "alma", "szilva", "körte", "alma"]`. Számold meg, melyik szó hányszor fordul elő! Használj szótárat.

## 10.2 – Szűrés ⭐⭐
Írj programot (`feladat2.py`). Adott szótárak listája (termékek: név, ár, kategória). Kérd be egy kategóriát, és írd ki a hozzá tartozó termékeket.

## 10.3 – Min/max keresés ⭐⭐
Írj programot (`feladat3.py`). Adott szótárak listája (diákok: név, pontszám). Keresd meg és írd ki a legjobb és legrosszabb pontszámú diákot (ne használj `min()`/`max()` beépített függvényt!).

## 10.4 – Statisztika fájlból ⭐⭐
Írj programot (`feladat4.py`). Olvasd be a `filmek.txt` fájlt, és írd ki:
- Hány film van összesen
- A kategóriák szerinti darabszámot
- A legjobb és legrosszabb értékelésű filmet

## 10.5 – Top 5 lista ⭐⭐⭐
Írj programot (`feladat5.py`). Olvasd be a `filmek.txt` fájlt! Kérd be egy kategóriát, és írd ki az adott kategória **5 legjobb értékelésű** filmjét csökkenő sorrendben.

## 10.6 – Összesítő riport ⭐⭐⭐
Írj programot (`feladat6.py`). Olvasd be a `filmek.txt` fájlt! Készíts egy összesítő riportot, amelyet egy `riport.txt` fájlba írsz:
- Összesen hány film van
- Kategóriánként: db, átlagos értékelés, legjobb film címe
- A 3 legjobb és 3 legrosszabb film

---

## A `filmek.txt` formátuma

```
cím;kategória;év;hossz_perc;értékelés
```

Példa: `Végső visszaszámlálás;akció;2005;118;7.2`

## Dokumentáció

- [Python szótárak](https://www.w3schools.com/python/python_dictionaries.asp)
- [Python rendezés](https://www.w3schools.com/python/ref_list_sort.asp)
- [Python fájlkezelés](https://www.w3schools.com/python/python_file_handling.asp)

## Beadás

1. Minden feladatot külön `.py` fájlba írj
2. A `riport.txt`-t is commitold!
3. `git push` – ez a beadás!
