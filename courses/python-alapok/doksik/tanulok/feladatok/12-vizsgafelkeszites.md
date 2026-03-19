# Kiegészítő gyakorlatok – 12. hét: Vizsgafelkészítés

> Ezek a feladatok a heti házi feladat melletti **extra gyakorlást** szolgálják.
> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz

---

### 12.1 – Gyors kódolás ⭐
Mérd az időt! Készítsd el az alábbiakat minél gyorsabban:
1. Kérj be egy nevet, írd ki nagybetűvel és a monogramját (2 perc)
2. Kérj be 5 számot listába, írd ki az átlagot és a legnagyobbat (3 perc)
3. Olvasd be egy fájl sorait és írd ki sorszámozva (3 perc)

### 12.2 – Hibakeresés ⭐⭐
Az alábbi kódrészletekben hibák vannak. Keresd meg és javítsd ki mindegyiket!

**a)** Típushiba
```python
ev = input("Születési éved: ")
kor = 2026 - ev
print(f"Te {kor} éves vagy.")
```

**b)** Logikai hiba
```python
szamok = [3, 7, 2, 9, 1]
legnagyobb = 0
for sz in szamok:
    if sz > legnagyobb:
        legnagyobb = sz
print(f"Legnagyobb: {legnagyobb}")
# Mi a gond, ha a lista [-5, -2, -8]?
```

**c)** Fájlkezelési hiba
```python
with open("adatok.txt") as f:
    for sor in f:
        mezok = sor.split(";")
        nev = mezok[0]
        kor = mezok[1]
        print(f"{nev} {kor + 1} éves lesz")
```

**d)** Szótár hiba
```python
tanulok = [
    {"nev": "Anna", "jegyek": [4, 5, 3]},
    {"nev": "Béla", "jegyek": [3, 2, 4]}
]
for t in tanulok:
    atlag = sum(t["jegyek"]) / len(t)
    print(f"{t['nev']}: {atlag}")
```

### 12.3 – Függvény írás gyakorlás ⭐⭐
Írj meg mindegyik függvényt **5 perc** alatt (mérd az időt!):
1. `forditott_szoveg(s)` – visszaadja a szöveget fordítva
2. `darabszam(lista, elem)` – megszámolja, hányszor szerepel az elem a listában (ne használj `.count()`-ot)
3. `egyedi_elemek(lista)` – visszaad egy új listát, amelyben minden elem csak egyszer szerepel

### 12.4 – Mini vizsga ⭐⭐⭐
Oldd meg az alábbi 3 feladatot **60 perc** alatt vizsga körülmények között:

**1. feladat (8 pont):** Írj programot 3 függvénnyel:
- `bekeres()` – bekéri a vezeték- és keresztnevet, kedvenc számot
- `generalas(vnev, knev, szam)` – 3 becenevet generál (legyél kreatív!)
- `kiiras(nevek)` – kiírja a beceneveket sorszámozva

**2. feladat (14 pont):** Készíts egy matematikai kvízt! A program generál 5 véletlenszerű összeadás/kivonás/szorzás feladatot (1–20 közötti számokkal). A felhasználó válaszol, és a program pontozza. A végén kiírja: „5/5 – Gratulálok!" vagy „3/5 – Gyakorolj még!"

**3. feladat (18 pont):** Olvasd be a `konyvek.txt` (vagy `filmek.txt`) fájlt szótárak listájába. Készíts moduláris megoldást:
- Hány elem van? Kategóriánként hány?
- Melyik a legjobb értékelésű?
- Keresés cím alapján, eredmény fájlba írás
- Szűrés kategória alapján

### 12.5 – Önellenőrzés ⭐
Készíts egy „cheat sheet"-et: írj egy `osszefoglalas.txt` fájlt, amelybe a félév legfontosabb fogalmait és kódrészleteit írod (változók, input, if, for, while, lista, szótár, fájl, függvény, modul). Fogalmanként 2-3 soros példakóddal.
