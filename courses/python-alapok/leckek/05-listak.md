# 📘 Lecke 05 – Listák

> 📚 Dokumentáció:  
> https://www.w3schools.com/python/python_lists.asp ·  
> https://www.w3schools.com/python/python_lists_methods.asp ·  
> https://www.w3schools.com/python/python_lists_comprehension.asp

---

# 9. óra: Listák alapjai

## 📋 Lista létrehozása

```python
gyumolcsok = ["alma", "körte", "szilva"]
szamok = [10, 20, 30, 40, 50]
ures_lista = []
```

### 🧠 Részletes Magyarázat

**Lista** – Rendezett elemgyűjtemény, szögletes zárójelekkel `[]`. Egy listában bármilyen típusú adat lehet (szöveg, szám, akár másik lista is).

**Miért használunk listát?** – Ha több összetartozó adatot akarunk tárolni, nem érdemes minden egyes értéknek külön változót létrehozni:
```python
# ROSSZ - sok külön változó:
gyumolcs1 = "alma"
gyumolcs2 = "körte"
gyumolcs3 = "szilva"

# JÓ - egy lista:
gyumolcsok = ["alma", "körte", "szilva"]
```

**Üres lista** – `[]` vagy `list()` – ha később akarunk elemeket hozzáadni.

---

## 🔢 Indexelés és hossz

```python
gyumolcsok = ["alma", "körte", "szilva"]
print(gyumolcsok[0])    # alma
print(gyumolcsok[-1])   # szilva
print(len(gyumolcsok))  # 3
```

### 🧠 Részletes Magyarázat

**Indexelés** – A lista elemeit sorszámmal (index) érjük el. **A számozás 0-tól indul!**

```
          Index:    0       1       2
gyumolcsok = [ "alma", "körte", "szilva" ]
     Negatív:   -3      -2      -1
```

**Negatív index** – Hátulról számol. `-1` az utolsó, `-2` az utolsó előtti elem.

**len()** – Megadja a lista hosszát (elemek számát). A legnagyobb érvényes index mindig `len(lista) - 1`.

**IndexError** – Ha nem létező indexet használsz:
```python
gyumolcsok[5]  # IndexError: list index out of range
```

---

## ➕ Elem hozzáadása: `append()`

```python
szamok = [1, 2, 3]
szamok.append(4)
print(szamok)  # [1, 2, 3, 4]
```

### 🧠 Részletes Magyarázat

**append()** – A lista végére illeszt egy új elemet. Ez egy **metódus** (a listához tartozó függvény), ezért ponttal hívjuk: `lista.append(érték)`.

Más hasznos lista-metódusok:
```python
szamok = [1, 2, 3]
szamok.insert(1, 99)    # Beszúr: [1, 99, 2, 3] (1-es indexre)
szamok.remove(99)       # Eltávolít értéket: [1, 2, 3]
szamok.pop()            # Utolsó elemet kiveszi: [1, 2], visszaadja: 3
szamok.clear()          # Kiüríti: []
```

---

## 🔄 Lista bejárása

```python
nevek = ["Anna", "Béla", "Csaba"]

for nev in nevek:
    print(f"Szia, {nev}!")
```

### 🧠 Részletes Magyarázat

**for ciklus listán** – A `for` ciklus végigmegy a lista minden elemén, és az aktuális elemet a ciklusváltozóba (`nev`) teszi.

```
1. kör: nev = "Anna"  → kiír: Szia, Anna!
2. kör: nev = "Béla"  → kiír: Szia, Béla!
3. kör: nev = "Csaba" → kiír: Szia, Csaba!
```

**enumerate()** – Ha az indexre is szükségünk van:
```python
for i, nev in enumerate(nevek):
    print(f"{i}. {nev}")
# 0. Anna
# 1. Béla
# 2. Csaba
```

---

## 📊 Hasznos függvények

```python
szamok = [5, 2, 8, 1, 9]

print(len(szamok))  # 5 (elemek száma)
print(sum(szamok))  # 25 (összeg)
print(min(szamok))  # 1 (legkisebb)
print(max(szamok))  # 9 (legnagyobb)
```

### 🧠 Részletes Magyarázat

| Függvény | Mit csinál | Példa | Eredmény |
|----------|-----------|-------|----------|
| `len()` | Elemek száma | `len([5, 2, 8])` | `3` |
| `sum()` | Elemek összege | `sum([5, 2, 8])` | `15` |
| `min()` | Legkisebb elem | `min([5, 2, 8])` | `2` |
| `max()` | Legnagyobb elem | `max([5, 2, 8])` | `8` |

**Átlagszámítás** – Nincs beépített `avg()`, de egyszerű:
```python
atlag = sum(szamok) / len(szamok)
```

---

## ✏️ Gyakorlat: Bevásárlólista

```python
lista = []

while True:
    elem = input("Mit vegyek? (kilépés: 'vége'): ")
    if elem == "vége":
        break
    lista.append(elem)

print(f"\nBevásárlólista ({len(lista)} tétel):")
for i, elem in enumerate(lista, 1):
    print(f"  {i}. {elem}")
```

### 🧠 Részletes Magyarázat

**while True** – Végtelen ciklus, ami csak `break`-kel áll le. Hasznos, ha nem tudjuk előre, hányszor kell ismételni.

**break** – Kilép a ciklusból, ha a felhasználó „vége"-t ír.

**enumerate(lista, 1)** – A második paraméter a kezdő sorszám. Alapból 0-tól számoz, de `1`-et adva 1-től indul (emberbarátabb kiírás).

---

# 10. óra: Listaműveletek

## ✂️ Szeletelés

```python
szamok = [10, 20, 30, 40, 50]
print(szamok[1:3])   # [20, 30]
print(szamok[:3])    # [10, 20, 30]
print(szamok[2:])    # [30, 40, 50]
```

### 🧠 Részletes Magyarázat

**Szeletelés (slicing)** – Egy lista részét kapjuk meg. A szintaxis: `lista[kezdet:vég]`

```
Index:      0    1    2    3    4
szamok = [ 10,  20,  30,  40,  50 ]

szamok[1:3]  → [20, 30]    (1-es indextől a 3. ELŐTT-ig)
szamok[:3]   → [10, 20, 30] (elejétől 3. előttig)
szamok[2:]   → [30, 40, 50] (2-es indextől végig)
szamok[:]    → [10, 20, 30, 40, 50] (az egész lista másolata)
```

**A vég index nem tartozik bele** – Pont mint a `range()`-nél!

---

## 🔍 Az `in` operátor

```python
gyumolcsok = ["alma", "körte", "szilva"]

if "alma" in gyumolcsok:
    print("Van alma!")

if "banán" not in gyumolcsok:
    print("Nincs banán.")
```

### 🧠 Részletes Magyarázat

**in** – Megvizsgálja, hogy egy elem benne van-e a listában. Visszaad `True` vagy `False` értéket.

**not in** – Az ellenkezője: igaz, ha az elem NINCS a listában.

```python
szamok = [1, 2, 3, 4, 5]
print(3 in szamok)      # True
print(99 in szamok)     # False
print(99 not in szamok) # True
```

---

## 📈 Rendezés

```python
szamok = [5, 2, 8, 1, 9]

# Helyben rendezés
szamok.sort()
print(szamok)  # [1, 2, 5, 8, 9]

# Csökkenő sorrend
szamok.sort(reverse=True)
print(szamok)  # [9, 8, 5, 2, 1]

# Új listát ad vissza
rendezett = sorted([5, 2, 8])
print(rendezett)  # [2, 5, 8]
```

### 🧠 Részletes Magyarázat

**sort() vs sorted()** – Két különböző megközelítés:

| | `sort()` | `sorted()` |
|-|----------|------------|
| Típus | Metódus | Függvény |
| Módosítja az eredetit? | Igen | Nem |
| Visszaadott érték | `None` | Új lista |

```python
szamok = [5, 2, 8]
szamok.sort()           # szamok most [2, 5, 8] (módosítva!)

szamok = [5, 2, 8]
uj = sorted(szamok)     # uj = [2, 5, 8], szamok marad [5, 2, 8]
```

**Szövegek rendezése** – ABC sorrendbe:
```python
nevek = ["Csaba", "Anna", "Béla"]
nevek.sort()
print(nevek)  # ['Anna', 'Béla', 'Csaba']
```

---

## 🧩 Lista comprehension

```python
# Hagyományos módszer
parosak = []
for i in range(1, 11):
    if i % 2 == 0:
        parosak.append(i)

# Ugyanaz tömörebben
parosak = [i for i in range(1, 11) if i % 2 == 0]
print(parosak)  # [2, 4, 6, 8, 10]
```

### 🧠 Részletes Magyarázat

**Lista comprehension** – Egy tömör, egysoros módja lista létrehozásának. Szintaxis:

```python
[kifejezés for elem in bejárható if feltétel]
```

Kibontva:
```python
eredmeny = []
for elem in bejárható:
    if feltétel:
        eredmeny.append(kifejezés)
```

Több példa:
```python
# Számok négyzete
negyzetek = [x**2 for x in range(1, 6)]
# [1, 4, 9, 16, 25]

# Nagybetűs nevek
nevek = ["anna", "béla"]
nagybetus = [nev.upper() for nev in nevek]
# ["ANNA", "BÉLA"]
```

---

## ✏️ Gyakorlat: Osztályzatok elemzése

```python
jegyek = []

while True:
    bemenet = input("Jegy (1-5, vagy 'vége'): ")
    if bemenet == "vége":
        break
    jegyek.append(int(bemenet))

print(f"Jegyek száma: {len(jegyek)}")
print(f"Átlag: {sum(jegyek) / len(jegyek):.2f}")
print(f"Legjobb: {max(jegyek)}")
print(f"Legrosszabb: {min(jegyek)}")
```

### 🧠 Részletes Magyarázat

Ez a program összefoglalja a lecke minden fontos elemét:
- **Üres lista `[]`** – Kezdetben üres, ciklusban töltjük fel
- **while True + break** – Addig kérdez, amíg „vége"-t nem írunk
- **append()** – Minden jegyet hozzáfűz a listához
- **len(), sum(), max(), min()** – Statisztikákat számít
- **:.2f** – Két tizedesjegyre formázza az átlagot
