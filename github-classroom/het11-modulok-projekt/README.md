# 11. hét – Modulok és összefoglaló projekt

> **Határidő:** a következő óra előtt
> **Beadás:** commitold és pushold a megoldásaidat ebbe a repoba!
> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz

---

## 11.1 – Első modul ⭐
Hozz létre egy `matek.py` modult az alábbi függvényekkel:
- `osszeg(a, b)`
- `szorzat(a, b)`
- `hatvany(alap, kitevo)`

A főprogramban (`foprogram.py`) importáld és teszteld mindhárom függvényt.

## 11.2 – Szöveg modul ⭐⭐
Hozz létre egy `szoveg_eszkozok.py` modult:
- `nagybetus(szoveg)` – nagybetűsre alakít
- `szavak_szama(szoveg)` – visszaadja a szavak számát
- `forditott(szoveg)` – megfordítja a szöveget

A főprogramban (`foprogram2.py`) kérj be egy mondatot és teszteld mindhárom függvényt!

## 11.3 – Teljes vizsgafeladat gyakorlás ⭐⭐⭐
Oldd meg a teljes 3. vizsga feladatot a `filmek.txt` alapján:
1. Beolvasás összetett adatszerkezetbe
2. Darabszám kiírása
3. Kategória szerinti számlálás
4. Legjobb/legrosszabb keresése
5. Cím szerinti keresés + fájlba írás
6. Kategória szerinti szűrés

A függvényeket `fgv.py` modulban helyezd el, a főprogramot `feladat3.py`-ban!

## 11.4 – Saját projekt ⭐⭐⭐
Válassz egy saját témát (pl. zenék, sportolók, receptek), és készíts hozzá:
1. Egy `.txt` adatfájlt legalább 15 rekorddal
2. Egy `sajat_fgv.py` modult legalább 4 függvénnyel (beolvasás, számlálás, keresés, szűrés)
3. Egy `sajat_foprogram.py` főprogramot, amely használja a modult

---

## A `filmek.txt` formátuma

```
cím;kategória;év;hossz_perc;értékelés
```

Példa: `Végső visszaszámlálás;akció;2005;118;7.2`

## Dokumentáció

- [Python modulok](https://www.w3schools.com/python/python_modules.asp)
- [Python import](https://www.w3schools.com/python/ref_keyword_import.asp)
- [Python fájlkezelés](https://www.w3schools.com/python/python_file_handling.asp)

## Beadás

1. Modul fájlokat és főprogramokat is commitold!
2. Commitolj értelmes üzenetekkel
3. `git push` – ez a beadás!
