# Kiegészítő gyakorlatok – 8. hét: Fájlkezelés

> Ezek a feladatok a heti házi feladat melletti **extra gyakorlást** szolgálják.
> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz

---

### 8.1 – Bevásárlólista fájlba ⭐
Kérd be a felhasználótól 5 bevásárlnivaló nevét és becsült árát. Mentsd el egy `bevasarlolista.txt` fájlba ilyen formában:
```
1. Kenyér - 350 Ft
2. Tej - 280 Ft
...
Összesen: 1520 Ft
```

### 8.2 – Fájl másoló ⭐
Írj programot, amely beolvassa az előző feladatban készült `bevasarlolista.txt` tartalmát és kiírja egy `masolat.txt` fájlba úgy, hogy minden sort nagybetűsít.

### 8.3 – Szöveg csere ⭐⭐
Kérd be egy fájl nevét, egy keresett szót és egy csere szót! A program olvassa be a fájlt, cserélje ki benne a keresett szót a cserére, és írja vissza a fájlba. Írd ki, hány cserét végzett.

### 8.4 – CSV feldolgozás ⭐⭐
Hozz létre egy `jegyek.csv` fájlt az alábbi tartalommal:
```
nev;matek;magyar;tortenelem
Kiss Anna;4;5;3
Nagy Béla;3;4;5
Tóth Csaba;5;3;4
Szabó Dóra;4;4;4
```
Írj programot, amely beolvassa, kiszámolja minden diák átlagát, és kiírja az eredményeket a képernyőre formázottan. Írd ki a tantárgyankénti átlagokat is.

### 8.5 – Napi napló ⭐⭐⭐
Készíts egy interaktív naplóalkalmazást:
1. Új bejegyzés hozzáfűzése dátummal (`naplo.txt`)
2. Keresés kulcsszó alapján a naplóban
3. Adott dátumú bejegyzések listázása
4. A napló utolsó 5 bejegyzésének kiírása
5. Kilépés

A program menüből vezérelt legyen, és minden bejegyzés elé kerüljön az aktuális dátum és idő automatikusan.

> Tipp: `from datetime import datetime` és `datetime.now().strftime("%Y-%m-%d %H:%M")`
