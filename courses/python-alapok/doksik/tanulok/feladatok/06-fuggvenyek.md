# Feladatok – 6. hét: Függvények

> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz
> A megoldásokat commitold és pushold a GitHub repódba.

---

### 6.1 – Köszöntő függvény ⭐
Írj egy `koszont(nev)` függvényt, amely kiírja: „Szia, [név]! Üdv a programban!" Hívd meg 3 különböző névvel.

### 6.2 – Területszámítók ⭐
Írj függvényeket a következő alakzatok területének kiszámítására:
- `teglalap_terulet(a, b)`
- `kor_terulet(r)`
- `haromszog_terulet(a, m)`

Teszteld mindegyiket!

### 6.3 – Hőmérséklet átváltó ⭐⭐
Írj két függvényt:
- `celsius_fahrenheit(c)` → átváltás Fahrenheitre
- `fahrenheit_celsius(f)` → átváltás Celsiusra

A főprogramban kérd be az értéket és az irányt, majd hívd meg a megfelelő függvényt.

### 6.4 – Legkisebb keresés ⭐⭐
Írj egy `legkisebb(szamok)` függvényt, amely egy számlistából visszaadja a legkisebb elemet (ne használj `min()`-t!). A főprogramban kérj be 5 számot, és hívd meg a függvényt.

### 6.5 – Névgenerátor ⭐⭐⭐
Írj programot **három függvénnyel** (pont mint a vizsga 1. feladatában):
1. `bekeres()` – bekéri a vezetéknevet, keresztnevet, kedvenc állatot
2. `generalas(vnev, knev, allat)` – előállít 3 felhasználónevet (legyél kreatív a formátumokkal!)
3. `kiiras(nev1, nev2, nev3)` – kiírja a neveket

A főprogram hívja meg a három függvényt a megfelelő sorrendben.

### 6.6 – Prímszám ellenőrző ⭐⭐⭐
Írj egy `prim_e(szam)` függvényt, amely `True`-t ad vissza, ha a szám prím, `False`-t ha nem. A főprogramban írd ki az összes prímet 1 és 100 között!
