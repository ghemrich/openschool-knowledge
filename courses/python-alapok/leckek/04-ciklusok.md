# 📘 Lecke 04 – Ciklusok

> 📚 Dokumentáció:  
> https://www.w3schools.com/python/python_while_loops.asp ·  
> https://www.w3schools.com/python/python_for_loops.asp

---

# 7. óra: A `while` ciklus

## 🔁 Alapszerkezet

A `while` ciklus addig ismétel, amíg a feltétel igaz.

```python
szam = 5
while szam > 0:
    print(szam)
    szam -= 1
print("Start!")
```

### 🧠 Részletes Magyarázat

**while** – „Amíg". A Python megvizsgálja a feltételt. Ha igaz (`True`), végrehajtja a behúzott blokkot, majd VISSZAUGRIK a feltétel vizsgálatához. Ez addig ismétlődik, amíg a feltétel hamissá nem válik.

**szam -= 1** – Rövidítés: `szam = szam - 1`. Minden körben eggyel csökkenti `szam` értékét. Ez biztosítja, hogy a ciklus egyszer véget ér!

**⚠️ Végtelen ciklus veszélye** – Ha elfelejtjük a `szam -= 1` sort, a feltétel örökre igaz marad, és a program soha nem áll le. Ha ez megtörténik: `Ctrl+C` a terminálban.

```
Futás lépésről lépésre:
szam = 5 → 5 > 0? Igen → kiír: 5, szam = 4
szam = 4 → 4 > 0? Igen → kiír: 4, szam = 3
szam = 3 → 3 > 0? Igen → kiír: 3, szam = 2
szam = 2 → 2 > 0? Igen → kiír: 2, szam = 1
szam = 1 → 1 > 0? Igen → kiír: 1, szam = 0
szam = 0 → 0 > 0? NEM → kilép a ciklusból
Kiír: "Start!"
```

---

## 🔢 Számláló változó

```python
i = 1
while i <= 10:
    print(i)
    i += 1
```

### 🧠 Részletes Magyarázat

**Számláló (counter)** – Az `i` változót számlálónak nevezzük. Ez egy elterjedt konvenció a programozásban – az `i` az „index" vagy „iterator" rövidítése.

**i += 1** – Rövidítés: `i = i + 1`. Hasonlók: `i -= 1` (csökkentés), `i *= 2` (duplázás), `i /= 3` (harmadolás).

---

## 👤 Felhasználói bemenet ciklusban

```python
jelszo = ""
while jelszo != "titok":
    jelszo = input("Add meg a jelszót: ")
print("Helyes jelszó!")
```

### 🧠 Részletes Magyarázat

Ez a minta nagyon gyakori: addig kérdezzük a felhasználót, amíg helyes választ nem ad.

**jelszo = ""** – Kezdőérték azért kell, mert a `while` feltétele a ciklus elején vizsgálja a változót. Ha nem létezne, `NameError`-t kapnánk.

**A ciklus logikája:**
1. `jelszo` üres string → `"" != "titok"` → igaz → belép a ciklusba
2. Bekéri a jelszót
3. Visszaugrik a feltételhez → ha nem „titok", újra kérdez
4. Ha „titok" → feltétel hamis → kilép → „Helyes jelszó!"

---

## ✏️ Gyakorlat: Számkitalálós játék

```python
import random

gondolt = random.randint(1, 20)
tipp = 0

while tipp != gondolt:
    tipp = int(input("Tippelj (1-20): "))
    if tipp < gondolt:
        print("Nagyobbra gondoltam!")
    elif tipp > gondolt:
        print("Kisebbre gondoltam!")

print(f"Eltaláltad! A szám: {gondolt}")
```

### 🧠 Részletes Magyarázat

**import random** – Betölti a `random` modult (beépített könyvtár). A `random.randint(1, 20)` egy véletlenszerű egész számot ad 1 és 20 között (mindkettő beleértve).

**tipp = 0** – Kezdőértéknek 0-t adunk, ami biztosan nem egyenlő a gondolt számmal (az 1-20 között van), így a ciklus elindul.

**Cikluson belüli elágazás** – Egy ciklus belsejében bármilyen Python kód lehet, akár `if`/`elif`/`else` is. A behúzás szintjei jelzik a struktúrát:
```python
while feltétel:          # 0 szóköz – ciklus
    if másik_feltétel:   # 4 szóköz – elágazás a ciklusban
        print("...")     # 8 szóköz – ez az if-hez tartozik
```

---

# 8. óra: A `for` ciklus és `range()`

## 🔤 `for` ciklus szövegen

```python
szo = "Python"
for betu in szo:
    print(betu)
```

### 🧠 Részletes Magyarázat

**for ... in ...** – A `for` ciklus végigmegy egy „bejárható" (iterable) elemen, és minden egyes elemmel végrehajt valamit.

**Szöveg bejárása** – A Python a szöveget karakterek sorozatának tekinti. A `for betu in szo` sorban a `betu` változó felveszi a szöveg minden egyes karakterét:
```
1. kör: betu = "P" → kiír: P
2. kör: betu = "y" → kiír: y
3. kör: betu = "t" → kiír: t
...
```

**while vs for:**
- `while` → ha nem tudjuk előre, hányszor kell ismételni (pl. jelszó bekérés)
- `for` → ha tudjuk, min kell végigmenni (pl. szöveg betűi, szám tartomány)

---

## 🔢 `range()` függvény

```python
# 0-tól 4-ig (5 nem tartozik bele)
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# 1-től 10-ig
for i in range(1, 11):
    print(i)

# Páros számok 2-től 20-ig
for i in range(2, 21, 2):
    print(i)
```

### 🧠 Részletes Magyarázat

**range()** – Számsorozatot generál. Három formája van:

| Használat | Jelentés | Eredmény |
|-----------|----------|----------|
| `range(5)` | 0-tól 4-ig | 0, 1, 2, 3, 4 |
| `range(1, 11)` | 1-től 10-ig | 1, 2, 3, ..., 10 |
| `range(2, 21, 2)` | 2-től 20-ig, kettesével | 2, 4, 6, ..., 20 |

**Fontos:** A végérték SOHA nem tartozik bele! Ez a Python konvenciója. `range(5)` → 0, 1, 2, 3, 4 (az 5 már nincs benne). Ezért írunk `range(1, 11)`-et, ha 1-10-ig akarunk menni.

**Visszafelé számlálás:**
```python
for i in range(10, 0, -1):
    print(i)  # 10, 9, 8, ..., 1
```

---

## ⏹️ `break` és `continue`

```python
# break – kilépés a ciklusból
for i in range(1, 100):
    if i == 5:
        break
    print(i)  # 1, 2, 3, 4

# continue – ugrás a következő ismétlésre
for i in range(1, 6):
    if i == 3:
        continue
    print(i)  # 1, 2, 4, 5
```

### 🧠 Részletes Magyarázat

**break** – Azonnal kilép a ciklusból, nem vizsgál több elemet. Hasznos, ha megtaláltuk, amit kerestünk.

**continue** – Átugorja az aktuális kör hátralévő részét, és a következő körrel folytatja. Hasznos, ha egy adott elemet ki akarunk hagyni.

```
break működése:               continue működése:
i=1 → kiír 1                  i=1 → kiír 1
i=2 → kiír 2                  i=2 → kiír 2
i=3 → kiír 3                  i=3 → ÁTUGORJA (continue)
i=4 → kiír 4                  i=4 → kiír 4
i=5 → KILÉP (break)           i=5 → kiír 5
```

---

## ✏️ Gyakorlat: Szorzótábla

```python
szam = int(input("Melyik szorzótáblát írassam ki? "))

for i in range(1, 11):
    print(f"{szam} x {i} = {szam * i}")
```

### 🧠 Részletes Magyarázat

A `range(1, 11)` 1-től 10-ig ad számokat. Minden körben az `i` változó a szorzót tartalmazza, és az f-string-ben kiszámítjuk és kiírjuk az eredményt.

**Kimenet (ha szam = 7):**
```
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
...
7 x 10 = 70
```
