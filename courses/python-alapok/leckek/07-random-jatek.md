# 📘 Lecke 07 – Random modul és játéklogika

> 📚 Dokumentáció:  
> https://www.w3schools.com/python/module_random.asp

---

# 13. óra: A `random` modul

## 📦 Modul importálása

```python
import random
```

### 🧠 Részletes Magyarázat

**import** – Betölt egy modult (kódkönyvtárat). A `random` egy beépített Python modul, ami véletlenszám-generáló függvényeket tartalmaz. Az `import` után a modul nevével és ponttal érjük el a függvényeit: `random.randint()`.

---

## 🎲 `random.randint(a, b)`

Véletlenszerű egész szám `a` és `b` között (mindkettő beleértve):

```python
import random

dobas = random.randint(1, 6)
print(f"Dobtál: {dobas}")
```

### 🧠 Részletes Magyarázat

**randint(a, b)** – „Random integer". Visszaad egy véletlenszerű egész számot `a`-tól `b`-ig, mindkét határ beleértve.

```python
random.randint(1, 6)    # 1, 2, 3, 4, 5, vagy 6
random.randint(0, 100)  # 0 és 100 között bármi
random.randint(1, 1)    # Mindig 1 (nincs választás)
```

**Minden hívás más eredményt adhat!** A véletlenszám generátor minden futtatásnál más kimenetet produkál.

---

## 🎯 `random.choice()`

Véletlenszerű elem kiválasztása listából:

```python
import random

szinek = ["piros", "kék", "zöld", "sárga"]
valasztott = random.choice(szinek)
print(f"A szín: {valasztott}")
```

### 🧠 Részletes Magyarázat

**choice()** – Véletlenszerűen kiválaszt egy elemet egy listából (vagy bármilyen sorozatból). Minden elemnek azonos esélye van.

```python
random.choice(["fej", "írás"])           # Pénzfeldobás
random.choice("abcdefghijklmnopqrstuv")  # Véletlen betű
```

**Egyéb hasznos random függvények:**

| Függvény | Mit csinál | Példa |
|----------|-----------|-------|
| `randint(a, b)` | Véletlen egész szám | `randint(1, 6)` → 4 |
| `choice(lista)` | Véletlen elem | `choice(["a","b"])` → "b" |
| `shuffle(lista)` | Lista megkeverése | Helyben kever |
| `sample(lista, n)` | n db véletlen elem | Nem ismétlődő |

---

## 📋 Lista feltöltése véletlenszámokkal

```python
import random

szamok = []
for i in range(3):
    szamok.append(random.randint(1, 13))
print(szamok)

# Vagy tömörebben lista comprehension-nel
szamok = [random.randint(1, 13) for _ in range(3)]
```

### 🧠 Részletes Magyarázat

**_ (aláhúzás)** – Konvenció: ha a ciklusváltozóra nincs szükségünk, `_`-t írunk az `i` helyett. Jelzi, hogy „nem használjuk a változót, csak ismétlünk".

```python
# Mindkettő 3x ismétel:
for i in range(3):    # i = 0, 1, 2 (de nem használjuk)
for _ in range(3):    # Ugyanaz, de jelzi: nem érdekel az érték
```

**Lista comprehension emlékeztető:**
```python
[random.randint(1, 13) for _ in range(3)]
# ↑ Mit csináljon       ↑ Hányszor
```

---

## ✏️ Gyakorlat: Dobókocka szimulátor

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

### 🧠 Részletes Magyarázat

**"=" * 20** – Szöveg szorzása: `"="` karakter 20-szor ismétlődik → `"===================="`. Hasznos egyszerű vonalak rajzolásához.

**i+1** – Mivel a `range(5)` 0-tól indul, de a felhasználónak 1-től akarjuk számozni a dobásokat.

---

# 14. óra: Játékprogram építése

## 🃏 Tippelős játék (vizsgafeladat típus!)

A 2. feladat tipikus lépései:
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

### 🧠 Részletes Magyarázat

**A program felépítése:**

| Függvény | Feladata |
|----------|----------|
| `kartyak_huzasa()` | 3 véletlen szám generálása, listában visszaadva |
| `tipp_bekerese()` | Felhasználó tippjének bekérése |
| `tipp_kiertekeles()` | Érvényesség + összehasonlítás, `True`/`False` visszaadása |
| `jatek()` | A főlogika: ciklus, számláló, végeredmény |

**Miért `True`/`False` visszatérés?** – A `tipp_kiertekeles()` nem csak kiír, hanem jelzi a `jatek()` függvénynek, hogy találat volt-e. A `while not talalt` ciklus addig fut, amíg `talalt` nem lesz `True`.

**Érvényesség-ellenőrzés** – A minimum összeg 3 (három darab 1-es), a maximum 39 (három darab 13-as). Bármi ezeken kívül lehetetlen, ezért hibaüzenetet adunk.

**while not talalt** – Leolvasva: „amíg NEM talált". A `not` megfordítja a logikai értéket:
- `talalt = False` → `not False` = `True` → ciklus fut
- `talalt = True` → `not True` = `False` → ciklus megáll
