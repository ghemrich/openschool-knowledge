# Kiegészítő gyakorlatok – 6. hét: Függvények

> Ezek a feladatok a heti házi feladat melletti **extra gyakorlást** szolgálják.
> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz

---

### 6.1 – Páros-e? ⭐
Írj egy `paros_e(szam)` függvényt, amely `True`-t ad vissza, ha a szám páros, `False`-t ha páratlan. Teszteld 5 különböző számmal a főprogramban.

### 6.2 – Átváltók ⭐
Írj függvényeket az alábbi átváltásokhoz:
- `km_merfold(km)` → km-ből mérföld
- `kg_font(kg)` → kg-ból font (1 kg = 2.20462 font)
- `celsius_kelvin(c)` → Celsiusból Kelvin (K = C + 273.15)

Kérd be az értékeket a főprogramban és hívd meg a függvényeket.

### 6.3 – Szöveg elemző ⭐⭐
Írj egy `szoveg_elemzo(szoveg)` függvényt, amely visszaad egy szótárat:
```python
{"karakterek": 15, "szavak": 3, "maganhangzok": 5, "nagybetuk": 1}
```
A főprogramban kérj be egy mondatot, és írd ki az eredményeket formázottan.

### 6.4 – Medián számítás ⭐⭐
Írj egy `median(szamok)` függvényt, amely egy számlistából kiszámítja a mediánt:
- Páratlan elemszámnál a középső elem
- Páros elemszámnál a két középső elem átlaga

Ne használj beépített statisztikai modult! Teszteld mindkét esettel.

### 6.5 – Jelszó erősség ⭐⭐⭐
Írj egy `jelszo_erosség(jelszo)` függvényt, amely 0–5 közötti pontszámot ad. Pontozási szabályok:
- +1 ha legalább 8 karakter
- +1 ha tartalmaz kisbetűt
- +1 ha tartalmaz nagybetűt
- +1 ha tartalmaz számot
- +1 ha tartalmaz speciális karaktert (`!@#$%&*`)

Írj egy `ertekeles(pont)` függvényt, amely szöveges értékelést ad: 0–1: „Nagyon gyenge", 2: „Gyenge", 3: „Közepes", 4: „Erős", 5: „Nagyon erős". A főprogram kérjen be jelszavakat, amíg nem kap legalább „Erős" értékelésűt.

### 6.6 – Fibonacci ⭐⭐⭐
Írj egy `fibonacci(n)` függvényt, amely visszaadja az első `n` Fibonacci számot listában (1, 1, 2, 3, 5, 8, ...). Írd ki az eredményt. Írj egy másik `fibonacci_osszeg(n)` függvényt, amely az első `n` Fibonacci szám összegét adja vissza.
