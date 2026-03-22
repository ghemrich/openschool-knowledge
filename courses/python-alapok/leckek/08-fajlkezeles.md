# 📘 Lecke 08 – Fájlkezelés

> 📚 Dokumentáció:  
> https://www.w3schools.com/python/python_file_handling.asp ·  
> https://www.w3schools.com/python/python_file_open.asp ·  
> https://www.w3schools.com/python/python_file_write.asp

---

# 15. óra: Fájlból olvasás

## 📂 A `with open()` szerkezet

```python
with open("adatok.txt", "r", encoding="utf-8") as f:
    tartalom = f.read()
    print(tartalom)
```

### 🧠 Részletes Magyarázat

**with open()** – Megnyit egy fájlt, és automatikusan be is zárja, amikor a blokk véget ér. Ez a biztonságos módja fájlkezelésnek Pythonban.

**Paraméterek:**
| Paraméter | Jelentés | Példa |
|-----------|----------|-------|
| Fájlnév | A fájl elérési útja | `"adatok.txt"` |
| Mód | Olvasás/Írás | `"r"` = read (olvasás) |
| encoding | Karakterkódolás | `"utf-8"` (magyar ékezetek!) |

**as f** – A megnyitott fájlt `f` néven használjuk a blokkban (ez egy fájlobjektum).

**f.read()** – Az egész fájl tartalmát egyetlen szövegként olvassa be.

**⚠️ encoding="utf-8"** – Ezt MINDIG add meg, különben a magyar ékezetes karakterek (á, é, ő, ű) hibásan jelenhetnek meg!

---

## 📖 Soronkénti olvasás

```python
with open("adatok.txt", "r", encoding="utf-8") as f:
    for sor in f:
        print(sor.strip())  # .strip() eltávolítja a sortörést
```

### 🧠 Részletes Magyarázat

**for sor in f** – A fájlobjektumon végigiterálhatunk `for` ciklussal, és minden körben egy sort kapunk.

**strip()** – Eltávolítja a sor elejéről és végéről a felesleges szóközöket és a sortörés karaktert (`\n`). A fájl minden sora tartalmaz egy sortörés karaktert a végén:
```
"Kiss Anna;16;Budapest\n"  →  strip()  →  "Kiss Anna;16;Budapest"
```

**Különbség:**
```python
# read() – egész fájl EGYBEN:
tartalom = f.read()            # Egy nagy szöveg

# for ciklus – soronként:
for sor in f:                   # Minden kör = 1 sor
    print(sor.strip())
```

---

## ✂️ `.split()` – sor darabolása

Ha a fájl pontosvesszővel tagolt (CSV-szerű):
```
Kiss Anna;16;Budapest
Nagy Béla;17;Debrecen
```

```python
with open("tanulok.txt", "r", encoding="utf-8") as f:
    for sor in f:
        adatok = sor.strip().split(";")
        nev = adatok[0]
        kor = int(adatok[1])
        varos = adatok[2]
        print(f"{nev} ({kor} éves) – {varos}")
```

### 🧠 Részletes Magyarázat

**split(elválasztó)** – Szétdarabolja a szöveget az elválasztó mentén, és egy **listát** ad vissza.

```python
"Kiss Anna;16;Budapest".split(";")
# Eredmény: ["Kiss Anna", "16", "Budapest"]
#             adatok[0]  adatok[1]  adatok[2]
```

**Láncolás:** `sor.strip().split(";")` – Először `strip()` (sortörés eltávolítás), majd `split()` (darabolás). Balról jobbra hajtódik végre.

**int() konverzió** – A fájlból MINDEN adat szövegként jön! Ha számként szeretnénk használni (pl. összehasonlítás, összeadás), konvertálni kell: `int(adatok[1])`.

---

## ✏️ Gyakorlat: Szövegfájl beolvasása

```python
# Olvassuk be a fájlt, és számoljuk meg a sorokat
sorok_szama = 0

with open("szoveg.txt", "r", encoding="utf-8") as f:
    for sor in f:
        sorok_szama += 1
        print(f"{sorok_szama}. sor: {sor.strip()}")

print(f"\nÖsszesen {sorok_szama} sor.")
```

### 🧠 Részletes Magyarázat

A `sorok_szama` változó a `with` blokk ELŐTT van definiálva, ezért a blokk UTÁN is használható. A ciklus minden körében növeljük eggyel, így végül megkapjuk az összes sor számát.

---

# 16. óra: Fájlba írás

## ✍️ Fájl megnyitása írásra

```python
with open("kimenet.txt", "w", encoding="utf-8") as f:
    f.write("Ez az első sor.\n")
    f.write("Ez a második sor.\n")
```

### 🧠 Részletes Magyarázat

**"w" mód** – „Write" (írás). Létrehozza a fájlt, ha nem létezik. **⚠️ Ha létezik, FELÜLÍRJA az egész tartalmát!**

**"a" mód** – „Append" (hozzáfűzés). A meglévő tartalom megmarad, az új adat a végére kerül.

| Mód | Jelentés | Ha létezik a fájl | Ha nem létezik |
|-----|----------|-------------------|----------------|
| `"r"` | Olvasás | Megnyitja | `FileNotFoundError` |
| `"w"` | Írás | **Felülírja!** | Létrehozza |
| `"a"` | Hozzáfűzés | Végére ír | Létrehozza |

**f.write()** – Szöveget ír a fájlba. **Nem tesz automatikusan sortörést!** A `\n`-t nekünk kell kiírni.

```python
f.write("alma")          # Ír: alma
f.write("körte")         # Ír: almakörte (nincs sortörés!)
f.write("szilva\n")      # Ír: almakörte szilva↵
```

---

## 💾 Lista mentése fájlba

```python
nevek = ["Anna", "Béla", "Csaba"]

with open("nevek.txt", "w", encoding="utf-8") as f:
    for nev in nevek:
        f.write(nev + "\n")

print("Fájl sikeresen létrehozva!")
```

### 🧠 Részletes Magyarázat

A `for` ciklus végigmegy a listán, és minden elemet egy sorba ír. A `+ "\n"` biztosítja, hogy minden név külön sorba kerüljön.

**Eredmény fájl (nevek.txt):**
```
Anna
Béla
Csaba
```

---

## ✏️ Gyakorlat: Beolvasás és visszaírás

```python
# 1. Beolvasás listába
tanulok = []
with open("tanulok.txt", "r", encoding="utf-8") as f:
    for sor in f:
        adatok = sor.strip().split(";")
        tanulok.append(adatok)

# 2. Egy kiválasztott tanuló fájlba írása
keresett = input("Kit keresünk? ")
with open("eredmeny.txt", "w", encoding="utf-8") as f:
    for tanulo in tanulok:
        if tanulo[0] == keresett:
            f.write(";".join(tanulo))
            print("Adat kiírva a fájlba!")
```

### 🧠 Részletes Magyarázat

**join()** – A `split()` ellentéte. Összefűzi a lista elemeit egy elválasztóval:
```python
";".join(["Anna", "16", "Budapest"])
# Eredmény: "Anna;16;Budapest"
```

**A program két lépésben dolgozik:**
1. **Beolvasás** – A teljes fájlt beolvassa egy lista listába (minden sor egy belső lista)
2. **Szűrés + írás** – Megkeresi a keresett nevet, és kiírja egy új fájlba

Ez a minta nagyon gyakori a vizsgafeladatokban: fájl beolvasás → feldolgozás → eredmény kiírás.
