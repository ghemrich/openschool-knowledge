# 12. hét – Vizsgafelkészítés (próbavizsga)

> **Határidő:** az óra végén (90 perc)
> **Beadás:** az utolsó `git push` az óra végén = beadás!
> Ez egy próbavizsga – vizsga körülmények között dolgozz!

---

## Próbavizsga szabályok

- **Idő:** 90 perc
- **Összpontszám:** 40 pont
- **Internet használható** (dokumentáció, W3Schools stb.)
- Egymásnak NEM segíthettek!
- Rendszeresen commitolj!

---

## 1. feladat – Felhasználónév generátor (8 pont)

Írj programot (`feladat1.py`) három függvénnyel:

### `bekeres()`
Kérd be a felhasználó **vezetéknevét**, **keresztnevét** és **születési évét**.

### `generalas(vnev, knev, ev)`
Generálj **3 felhasználónevet** az alábbi szabályok szerint:
1. Vezetéknév első 3 betűje + keresztnév első 2 betűje + születési év utolsó 2 számjegye (pl. `KisAn10`)
2. Keresztnév kisbetűvel + `.` + vezetéknév kisbetűvel (pl. `anna.kiss`)
3. Vezetéknév nagybetűvel + születési év (pl. `KISS2010`)

### `kiiras(nev1, nev2, nev3)`
Írd ki a generált felhasználóneveket sorszámozva.

A főprogram hívja meg a függvényeket!

---

## 2. feladat – Számkitaláló játék (14 pont)

Írj programot (`feladat2.py`)!

A program gondol egy **véletlenszerű egész számra 1 és 20 között**. A játékos addig tippelhet, amíg el nem találja, vagy el nem fogy a tippje (max 5 tipp).

- Minden tipp után írd ki: „Túl kicsi!" vagy „Túl nagy!"
- Ha eltalálta: „Gratulálok! [X] tippből kitaláltad!"
- Ha elfogytak a tippjei: „Sajnos nem sikerült. A szám [X] volt."
- A végén kérdezd meg: „Újra játszol? (i/n)" – ha igen, kezdjen új játékot

---

## 3. feladat – Filmek feldolgozása (18 pont)

Írj programot, a függvényeket a `fgv.py` fájlba, a főprogramot a `feladat3.py` fájlba!

A `filmek.txt` formátuma: `cím;kategória;év;hossz_perc;értékelés`

### Részfeladatok:
1. Olvasd be a fájlt szótárak listájába
2. Írd ki, hány film van összesen
3. Írd ki kategóriánként, hány film van
4. Keresd meg a legjobb értékelésű filmet (cím + értékelés)
5. Kérd be egy film címét, és írd ki az adatait. Ha nem létezik, írd ki, hogy nem található
6. Kérd be egy kategóriát, és írd ki az összes hozzá tartozó filmet

---

## Hibakeresés gyakorlás

Az alábbi kódrészletekben hibák vannak. Keresd meg és javítsd ki őket (`hibak.py`)!

**a)**
```python
nev = input("Neved: ")
print("Szia, " + nev + "! Te " + 16 + " éves vagy.")
```

**b)**
```python
import random
szam = random.randint(1, 10)
tipp = input("Tippelj: ")
if tipp == szam:
    print("Talált!")
```

**c)**
```python
with open("adatok.txt", "r") as f:
    for sor in f:
        adatok = sor.split(";")
        ev = adatok[2]
        print(ev + 1)
```

**d)**
```python
def beolvas(fajl):
    lista = []
    with open(fajl) as f:
        for sor in f:
            adat = sor.split(";")
            lista.append(adat)
    return lista

adatok = beolvas("adatok.txt")
print(adatok[0]["nev"])
```

---

## Git gyakorlás

Készíts egy `hello.py` fájlt. Végezd el az alábbi lépéseket, és minden lépés után futtasd a `git log --oneline` parancsot:
1. Hozd létre a fájlt egy `print("Hello")` sorral → commit
2. Adj hozzá egy második `print()` sort → commit
3. Adj hozzá egy `input()` bekérést → commit
4. Pushold az egészet

---

## Beadás

1. `git add .` → `git commit -m "próbavizsga megoldás"` → `git push`
2. Az utolsó push az óra végén = beadás!
