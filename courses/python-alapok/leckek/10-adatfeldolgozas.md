# 📘 Lecke 10 – Adatfeldolgozás

> 📚 Dokumentáció:  
> https://www.w3schools.com/python/python_dictionaries_methods.asp ·  
> https://www.w3schools.com/python/python_lists_loop.asp

---

# 19. óra: Számlálás, szűrés

## 📊 Elemek számlálása

```python
filmek = [
    {"cim": "Film A", "kategoria": "akció", "ertekeles": 7.5},
    {"cim": "Film B", "kategoria": "dráma", "ertekeles": 8.2},
    {"cim": "Film C", "kategoria": "akció", "ertekeles": 6.1},
    {"cim": "Film D", "kategoria": "horror", "ertekeles": 7.0}
]

# Hány darab van összesen?
print(f"Összesen {len(filmek)} film van.")
```

### 🧠 Részletes Magyarázat

**len()** – A legegyszerűbb számlálás: hány elem van a listában. Ez a vizsgafeladatokban szinte mindig az első kérdés: „Hány film/könyv/sportolójáték van a listában?"

---

## 🔢 Számlálás kategóriánként

```python
# 1. módszer: kézi számlálás
akcio = 0
drama = 0
for film in filmek:
    if film["kategoria"] == "akció":
        akcio += 1
    elif film["kategoria"] == "dráma":
        drama += 1

# 2. módszer: szótár alapú (rugalmasabb!)
szamlalo = {}
for film in filmek:
    kat = film["kategoria"]
    szamlalo[kat] = szamlalo.get(kat, 0) + 1

for kat, db in szamlalo.items():
    print(f"{kat}: {db} db")
```

### 🧠 Részletes Magyarázat

**1. módszer – kézi számlálás:** Minden kategóriához külön változó. Egyszerű, de ha sok kategória van, sok változóra van szükség.

**2. módszer – szótár alapú:** Rugalmasabb, mert bármennyi kategóriával működik, anélkül hogy előre ismernénk őket.

**`.get(kulcs, alapérték)`** – A szótár `.get()` metódusa. Ha a kulcs létezik, visszaadja az értékét. Ha nem létezik, az alapértéket adja vissza (itt `0`).

```python
szamlalo = {}
# 1. kör: kat = "akció"
# szamlalo.get("akció", 0) → 0 (nem létezik) → szamlalo["akció"] = 0 + 1 = 1

# 2. kör: kat = "dráma"
# szamlalo.get("dráma", 0) → 0 (nem létezik) → szamlalo["dráma"] = 0 + 1 = 1

# 3. kör: kat = "akció"
# szamlalo.get("akció", 0) → 1 (létezik!) → szamlalo["akció"] = 1 + 1 = 2

# Eredmény: {"akció": 2, "dráma": 1, "horror": 1}
```

**`.items()`** – A szótár kulcs-érték párjait adja vissza, `for` ciklussal bejárhatjuk:
```python
for kat, db in szamlalo.items():
    # kat = "akció", db = 2
    # kat = "dráma", db = 1
    # kat = "horror", db = 1
```

---

## 🔍 Szűrés kategória szerint

```python
kategoria = input("Kategória: ")

for film in filmek:
    if film["kategoria"] == kategoria:
        print(f"  {film['cim']} ({film['ev']})")
```

### 🧠 Részletes Magyarázat

**Szűrés** – Végigmegyünk az összes elemen, és csak azokat írjuk ki, amelyek megfelelnek a feltételnek. Ez a minta a vizsgafeladatok utolsó kérdésénél szinte mindig előjön.

Lista comprehension-nel is megoldható:
```python
akcio_filmek = [f for f in filmek if f["kategoria"] == "akció"]
```

---

# 20. óra: Keresés, min/max

## 🔎 Lineáris keresés

```python
def film_keresese(filmek, keresett_cim):
    for film in filmek:
        if film["cim"] == keresett_cim:
            return film
    return None

cim = input("Film címe: ")
talalat = film_keresese(filmek, cim)

if talalat:
    print(f"Megtalálva: {talalat}")
else:
    print("Nincs ilyen cím a listában")
```

### 🧠 Részletes Magyarázat

**Lineáris keresés** – Az adatok voltak vizsgálata egyenként, amíg megtaláljuk a keresett elemet. Ez a legegyszerűbb keresési algoritmus.

**return film** – Ha megtaláltuk, azonnal visszaadjuk és kilépünk a függvényből. Nem kell a többi elemet vizsgálni.

**return None** – Ha a ciklus véget ér anélkül, hogy találtunk volna, `None`-t adunk vissza. A `None` a Python „semmi" értéke.

**if talalat:** – A `None` hamis értékű (`falsy`), a szótár (ha talált) igaz (`truthy`). Ezért egyszerűen `if talalat:` kell, nem `if talalat != None:`.

---

## 📈 Minimum és maximum keresés

```python
def legjobb_legrosszabb(filmek):
    legjobb = filmek[0]
    legrosszabb = filmek[0]

    for film in filmek:
        if film["ertekeles"] > legjobb["ertekeles"]:
            legjobb = film
        if film["ertekeles"] < legrosszabb["ertekeles"]:
            legrosszabb = film

    return legjobb, legrosszabb

legjobb, legrosszabb = legjobb_legrosszabb(filmek)
print(f"Legjobb: {legjobb['cim']} ({legjobb['ertekeles']})")
print(f"Legrosszabb: {legrosszabb['cim']} ({legrosszabb['ertekeles']})")
```

### 🧠 Részletes Magyarázat

**Az algoritmus logikája:**
1. Feltételezzük, hogy az első elem a legjobb ÉS a legrosszabb is
2. Végigmegyünk az összes elemen
3. Ha jobbat találunk → frissítjük a „legjobb"-at
4. Ha rosszabbat találunk → frissítjük a „legrosszabb"-at

**Miért nem `max()` és `min()`?** – A beépített `max()/min()` egyszerű listákon működik (`max([5, 2, 8])` → 8). De szótárak listáján nem tudja automatikusan, melyik mezőt hasonlítsa össze. Ezért kézia keresés kell, vagy:

```python
# Haladó: max() kulcs paraméterrel
legjobb = max(filmek, key=lambda f: f["ertekeles"])
```

---

## 🔄 Teljes munkafolyamat (3. feladat előkészítés)

```python
# 1. Beolvasás
filmek = beolvasas("filmek.txt")

# 2. Darabszám
print(f"Összesen: {len(filmek)} film")

# 3. Kategóriánként
szamlalo = kategoriak_szama(filmek)

# 4. Min/max
legjobb, legrosszabb = legjobb_legrosszabb(filmek)

# 5. Keresés + fájlba írás
# 6. Szűrés kategóriára
```

### 🧠 Részletes Magyarázat

Ez a tipikus vizsgafeladat-struktúra. A 3. feladat mindig hasonló lépésekből áll:
1. **Beolvasás** – Fájlból szótárak listájába
2. **Darabszám** – `len()` használata
3. **Csoportosítás** – Szótár alapú számlálás (`.get()`)
4. **Min/max** – Legjobb/legrosszabb keresés ciklussal
5. **Keresés** – Lineáris keresés + fájlba írás
6. **Szűrés** – Adott kategóriához tartozó elemek kiírása
