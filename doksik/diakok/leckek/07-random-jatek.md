# 7. hét – Random modul és játéklogika

> **Dokumentáció:** [W3Schools – Random modul](https://www.w3schools.com/python/module_random.asp)

## 13. óra: A `random` modul

### Modul importálása

```python
import random
```

### `random.randint(a, b)`
Véletlenszerű egész szám `a` és `b` között (mindkettő beleértve):

```python
import random

dobas = random.randint(1, 6)
print(f"Dobtál: {dobas}")
```

### `random.choice()`
Véletlenszerű elem kiválasztása listából:

```python
import random

szinek = ["piros", "kék", "zöld", "sárga"]
valasztott = random.choice(szinek)
print(f"A szín: {valasztott}")
```

### Lista feltöltése véletlenszámokkal

```python
import random

szamok = []
for i in range(3):
    szamok.append(random.randint(1, 13))
print(szamok)

# Vagy tömörebben
szamok = [random.randint(1, 13) for _ in range(3)]
```

### Gyakorlat: Dobókocka szimulátor

```python
import random

print("Dobókocka szimulátor")
print("=" * 20)

dobasok = []
for i in range(5):
    dobas = random.randint(1, 6)
    dobasok.append(dobas)
    print(f"{i+1}. dobás: {dobas}")

print(f"\nÖsszeg: {sum(dobasok)}")
print(f"Legnagyobb: {max(dobasok)}")
```

---

## 14. óra: Játékprogram építése

### Tippelős játék (vizsgafeladat típus!)

A 2. feladat lépései:
1. Véletlen számok generálása → listába
2. Tipp bekérése ciklusban
3. Tipp kiértékelése (érvényesség + összehasonlítás)
4. Számláló növelése
5. Végeredmény kiírása

```python
import random


def kartyak_huzasa():
    kartyak = [random.randint(1, 13) for _ in range(3)]
    return kartyak


def tipp_bekerese():
    tipp = int(input("Tippelj, mennyi a három kártya összege: "))
    return tipp


def tipp_kiertekeles(tipp, osszeg):
    if tipp < 3 or tipp > 39:
        print("HIBA: nem lehetséges érték!")
        return False
    elif tipp < osszeg:
        print("Ennél több")
        return False
    elif tipp > osszeg:
        print("Ennél kevesebb")
        return False
    else:
        print("Talált!")
        return True


def jatek():
    kartyak = kartyak_huzasa()
    osszeg = sum(kartyak)
    tippek_szama = 0
    talalt = False

    while not talalt:
        tipp = tipp_bekerese()
        tippek_szama += 1
        talalt = tipp_kiertekeles(tipp, osszeg)

    print(f"\nA húzott kártyák: {kartyak}")
    print(f"A tippek száma: {tippek_szama}")
    print("Köszönjük a játékot!")


jatek()
```

### A program felépítése – miért így?

| Függvény | Feladata |
|----------|----------|
| `kartyak_huzasa()` | 3 véletlen szám generálása, listában visszaadva |
| `tipp_bekerese()` | Felhasználó tippjének bekérése |
| `tipp_kiertekeles()` | Érvényesség + összehasonlítás, `True`/`False` visszaadása |
| `jatek()` | A főlogika: ciklus, számláló, végeredmény |
