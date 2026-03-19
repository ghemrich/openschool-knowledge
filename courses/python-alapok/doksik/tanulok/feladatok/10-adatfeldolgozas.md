# Kiegészítő gyakorlatok – 10. hét: Adatfeldolgozás

> Ezek a feladatok a heti házi feladat melletti **extra gyakorlást** szolgálják.
> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz

---

### 10.1 – Szógyakoriság ⭐
Adott egy hosszabb szöveg (legalább 3 mondat, változóban). Számold meg szótárral, melyik szó hányszor fordul elő. Írd ki a szavakat gyakoriság szerint csökkenő sorrendben.

### 10.2 – Átlag felett ⭐⭐
Adott szótárak listája (tanulók: név, pontszám). Számold ki az átlagos pontszámot, és írd ki azon tanulók nevét, akik az átlag **felett** teljesítettek. Írd ki az átlag alatti tanulókat is külön listában.

### 10.3 – Csoportosítás ⭐⭐
Adott szótárak listája (könyvek: cim, szerzo, oldalszam, mufaj). Csoportosítsd a könyveket műfaj szerint! Írd ki műfajonként a könyvek címeit és az átlagos oldalszámot.

### 10.4 – Időjárás elemzés ⭐⭐
Hozz létre egy `idojaras.txt` fájlt a következő formátumban:
```
datum;homerseklet;csapadek_mm;szel_kmh
2026-03-01;8;0;15
2026-03-02;12;5;22
...
```
Legalább 14 napot írj bele. Írd ki:
- Az átlaghőmérsékletet
- A legmelegebb és leghidegebb napot
- A csapadékos napok számát
- Az összesített csapadékmennyiséget

### 10.5 – Top lista fájlba ⭐⭐⭐
Olvasd be az `idojaras.txt` fájlt. Kérd be a felhasználótól egy hőmérsékleti küszöböt. Szűrd ki a küszöb feletti napokat, rendezd csökkenő hőmérséklet szerint, és írd ki az eredményt egy `meleg_napok.txt` fájlba:
```
=== MELEG NAPOK (15°C felett) ===
1. 2026-03-15 - 22°C (csapadék: 0mm, szél: 10km/h)
2. 2026-03-12 - 19°C (csapadék: 2mm, szél: 18km/h)
...
Összesen: 5 nap, átlag: 19.4°C
```

### 10.6 – Összehasonlító elemzés ⭐⭐⭐
Készíts két különböző adatfájlt (pl. `konyvek.txt` és `filmek.txt`, mindkettő pontszámmal). Készíts egy összehasonlító riportot, amely mindkét fájlból kiemeli a top 3 elemet, az átlagos pontszámot és a kategóriák eloszlását. A riportot írd `osszehasonlitas.txt` fájlba.
