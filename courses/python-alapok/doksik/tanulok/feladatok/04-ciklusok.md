# Kiegészítő gyakorlatok – 4. hét: Ciklusok

> Ezek a feladatok a heti házi feladat melletti **extra gyakorlást** szolgálják.
> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz

---

### 4.1 – Szorzótábla ⭐
Kérd be egy számot a felhasználótól! Írd ki 1-től 10-ig a szorzótáblát szép formázásban (pl. „7 × 3 = 21").

### 4.2 – Szám fordító ⭐
Kérd be egy egész számot! Írd ki a számjegyeit fordított sorrendben (pl. 1234 → 4321). Csak ciklussal oldd meg, ne használj szeletelést (`[::-1]`)!

> Tipp: `szam % 10` az utolsó számjegy, `szam // 10` levágja az utolsót.

### 4.3 – Háromszög rajzoló ⭐⭐
Kérd be a sorok számát! Rajzolj jobbra zárt háromszöget csillagokból:
```
    *
   **
  ***
 ****
*****
```

### 4.4 – FizzBuzz ⭐⭐
Írd ki az 1-től 100-ig terjedő számokat, de:
- Ha a szám osztható 3-mal, írd ki helyette: „Fizz"
- Ha osztható 5-tel: „Buzz"
- Ha mindkettővel: „FizzBuzz"
- Egyébként a számot

### 4.5 – Számjegy összegző ⭐⭐
Kérj be számokat a felhasználótól, amíg „vége"-t nem ír. Közben tartsd nyilván:
- Hány számot írt be
- Melyik volt a legkisebb és a legnagyobb
- Mennyi az összegük és az átlaguk

Írd ki az összesítést a végén.

### 4.6 – Amőba pálya ⭐⭐⭐
Kérd be a pálya méretét (n)! Rajzolj ki egy n×n-es amőba (tic-tac-toe) stílusú rácsot:
```
 --- --- ---
|   |   |   |
 --- --- ---
|   |   |   |
 --- --- ---
|   |   |   |
 --- --- ---
```

### 4.7 – Collatz-sejtés ⭐⭐⭐
Kérd be egy pozitív egész számot! Alkalmazd rá a Collatz-szabályt:
- Ha páros, oszd el 2-vel
- Ha páratlan, szorozd meg 3-mal és adj hozzá 1-et

Írd ki minden lépést, amíg el nem jutsz 1-ig. Írd ki a lépések számát is.
