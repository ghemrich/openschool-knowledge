# 📘 Lecke 03 – Feltételes elágazások

> 📚 Dokumentáció:  
> https://www.w3schools.com/python/python_conditions.asp ·  
> https://www.w3schools.com/python/python_operators.asp

---

# 5. óra: Az `if` utasítás

## 🔀 Alapszerkezet

```python
kor = int(input("Hány éves vagy? "))

if kor >= 18:
    print("Felnőtt vagy.")
else:
    print("Kiskorú vagy.")
```

### 🧠 Részletes Magyarázat

**if** – „Ha" feltétel. A Python megvizsgálja a feltételt, és ha igaz (`True`), végrehajtja a behúzott kódblokkot.

**else** – „Különben". Ha az `if` feltétel nem igaz (`False`), ez a blokk fut le.

**Behúzás (indentation)** – A Pythonban a behúzás (4 szóköz vagy 1 Tab) jelöli, melyik kód tartozik az `if`-hez. Ez nem opcionális – KÖTELEZŐ!

```python
if True:
    print("Ez az if-hez tartozik")     # 4 szóköz behúzás
    print("Ez is!")                     # Szintén behúzva = szintén az if-hez tartozik
print("Ez már nem tartozik az if-hez")  # Nincs behúzás = mindig lefut
```

**A kettőspont `:`** – Az `if` és `else` sor végén kötelező! Ha elfelejtjük: `SyntaxError`.

---

## ⚖️ Összehasonlító operátorok

| Operátor | Jelentés | Példa | Eredmény |
|----------|----------|-------|----------|
| `==` | egyenlő | `5 == 5` | `True` |
| `!=` | nem egyenlő | `5 != 3` | `True` |
| `<` | kisebb | `3 < 5` | `True` |
| `>` | nagyobb | `5 > 3` | `True` |
| `<=` | kisebb vagy egyenlő | `5 <= 5` | `True` |
| `>=` | nagyobb vagy egyenlő | `3 >= 5` | `False` |

### 🧠 Részletes Magyarázat

**`==` vs `=`** – Ez a leggyakoribb hiba! Kettő különböző dolog:
- `=` → értékadás (változó létrehozása): `x = 5`
- `==` → összehasonlítás (egyenlő-e?): `x == 5`

```python
x = 5      # x értéke most 5 (értékadás)
print(x == 5)   # True (összehasonlítás: x egyenlő 5-tel?)
print(x == 3)   # False
```

**Szövegek összehasonlítása** is működik:
```python
szin = input("Kedvenc szín: ")
if szin == "kék":
    print("Nekem is a kék!")
```

---

## 🔗 Logikai operátorok

```python
kor = 16
diak = True

if kor >= 14 and diak:
    print("Diákigazolvány jár!")

szam = 15
if szam < 10 or szam > 20:
    print("A szám a tartományon kívül van")
```

### 🧠 Részletes Magyarázat

**and** – Mindkét feltételnek igaznak kell lennie:
```python
if kor >= 18 and jogositvany == True:
    print("Vezethet")
# Csak akkor ír ki, ha 18+ ÉS van jogosítványa
```

**or** – Elég, ha az egyik feltétel igaz:
```python
if nap == "szombat" or nap == "vasárnap":
    print("Hétvége!")
# Kiír, ha szombat VAGY vasárnap
```

**not** – Megfordítja a feltételt:
```python
if not aktiv:
    print("A felhasználó inaktív")
# Kiír, ha aktiv == False
```

**Igazságtáblázat:**

| `a` | `b` | `a and b` | `a or b` | `not a` |
|-----|-----|-----------|----------|---------|
| True | True | True | True | False |
| True | False | False | True | False |
| False | True | False | True | True |
| False | False | False | False | True |

---

## ✏️ Gyakorlat: Páros/páratlan

```python
szam = int(input("Adj meg egy számot: "))

if szam % 2 == 0:
    print(f"{szam} páros szám.")
else:
    print(f"{szam} páratlan szám.")
```

### 🧠 Részletes Magyarázat

**`%` (modulo)** – A maradékos osztás eredményét adja. Ha `szam % 2` eredménye `0`, akkor a szám páros (maradék nélkül osztható 2-vel).

```python
10 % 2  # 0 → páros
7 % 2   # 1 → páratlan
15 % 3  # 0 → osztható 3-mal
```

---

# 6. óra: Többágú elágazás

## 🔀 `elif` használata

Ha több mint két eset van, az `elif` (else if = „különben ha") használható:

```python
pontszam = int(input("Pontszám: "))

if pontszam >= 90:
    print("Jeles (5)")
elif pontszam >= 75:
    print("Jó (4)")
elif pontszam >= 60:
    print("Közepes (3)")
elif pontszam >= 40:
    print("Elégséges (2)")
else:
    print("Elégtelen (1)")
```

### 🧠 Részletes Magyarázat

**elif** – Az `if` és `else` között tetszőleges számú `elif` ág állhat. A Python felülről lefelé vizsgálja a feltételeket, és **az első igaz** ágnál megáll – a többit kihagyja.

**A sorrend számít!** Figyeld meg, hogy `>= 90`-nel kezdünk és lefelé haladunk. Ha fordítva lenne:

```python
# ROSSZ SORREND:
if pontszam >= 40:
    print("Elégséges")   # 95 pontnál is ez futna le! Mert 95 >= 40 igaz!
elif pontszam >= 90:
    print("Jeles")        # Ide soha nem jutna el!
```

**else** – Opcionális. Ha az összes `if`/`elif` feltétel hamis, az `else` fut le. Ez a „minden más" eset.

---

## 🔧 Összetett feltételek

```python
ho = int(input("Hónap (1-12): "))

if ho >= 3 and ho <= 5:
    print("Tavasz")
elif ho >= 6 and ho <= 8:
    print("Nyár")
elif ho >= 9 and ho <= 11:
    print("Ősz")
else:
    print("Tél")
```

### 🧠 Részletes Magyarázat

Több feltételt kombinálhatunk az `and`, `or` operátorokkal. Az `and` azt jelenti: mindkettő igaz legyen.

Pythonban a tartomány-ellenőrzésre van egy elegánsabb forma is:
```python
# Hagyományos:
if ho >= 3 and ho <= 5:
    print("Tavasz")

# Pythonos rövidítés (láncolás):
if 3 <= ho <= 5:
    print("Tavasz")
```

Mindkettő ugyanazt csinálja, de a láncolás olvashatóbb.

---

## ✏️ Gyakorlat: Belépőjegy árazás

```python
kor = int(input("Életkor: "))
diak = input("Tanuló vagy? (igen/nem): ")

if kor < 6:
    print("Ingyenes")
elif kor < 18 or diak == "igen":
    print("Kedvezményes: 500 Ft")
elif kor >= 65:
    print("Nyugdíjas: 800 Ft")
else:
    print("Teljes ár: 1500 Ft")
```

### 🧠 Részletes Magyarázat

Ez a program egy jó példa a valós élethez közeli logikára:
- **6 év alatt** → ingyenes (a legkisebbeknél ez az első vizsgált eset)
- **18 alatt VAGY diák** → kedvezményes (az `or` miatt elég, ha az egyik igaz)
- **65 felett** → nyugdíjas kedvezmény
- **Minden más** → teljes ár

Figyeld meg az `or` használatát: `kor < 18 or diak == "igen"`. Ha a diák 25 éves, de tanuló, akkor is kedvezményes jegyet kap!
