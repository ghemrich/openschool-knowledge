# 📘 Lecke 12 – Vizsgafelkészítés

> 📚 Dokumentáció:  
> https://www.w3schools.com/python/python_reference.asp

---

# 23. óra: Próbavizsga

Oldd meg az alábbi feladatokat önállóan, 90 perc alatt!

A vizsgát a **GitHub Classroom**-on kapod: a mentorod megadja a meghívó linket.

## 📋 Vizsga menete

1. Fogadd el a GitHub Classroom feladatot (a kapott linken)
2. Klónozd le a repot: `git clone <link>`
3. A repóban már ott van a forrásfájl (`filmek.txt` vagy `konyvek.txt`) és a feladatleírás
4. Dolgozz, és rendszeresen commitolj!
5. Az utolsó `git push` a beadás

### 🧠 Részletes Magyarázat

**Git Classroom munkafolyamat:**
```bash
# 1. Link megnyitása böngészőben → „Accept this assignment"
# 2. Klónozás:
git clone https://github.com/OrgName/feladat-neved.git
cd feladat-neved

# 3. Munka közben rendszeresen:
git add .
git commit -m "1. feladat kész"
git push

# 4. Végén:
git add .
git commit -m "Minden feladat kész"
git push
```

---

## 📏 Szabályok

- Internet használható
- Saját jegyzet használható
- 90 perc áll rendelkezésre
- Feladatonként külön fájl (`feladat1.py`, `feladat2.py`, `feladat3.py`, `fgv.py`)
- Rendszeresen commitolj és pusholj (ne csak a végén)!

### 🧠 Részletes Magyarázat

**Miért rendszeres commit?**
- Ha az utolsó pillanatban hiba történik (internet kiesés, gép lefagy), az addig pusholt munka megmarad
- A mentor látja a commit-történetet – ez bizonyítja, hogy te dolgoztál
- Jó szokás: minden befejezett részfeladat után commit + push

**Fájl struktúra a repóban:**
```
📁 vizsga-repo/
  ├── feladat1.py     ← 1. feladat (bekérés + feldolgozás)
  ├── feladat2.py     ← 2. feladat (random + játék)
  ├── feladat3.py     ← 3. feladat (főprogram)
  ├── fgv.py          ← 3. feladat (modul/függvények)
  └── filmek.txt      ← Adatfájl (már benne van a repóban!)
```

---

# 24. óra: Próbavizsga megbeszélése

## ⚠️ Tipikus hibák és megoldásuk

### 1. feladat – gyakori hibák

```python
# ❌ Elfelejtett .lower():
nev1 = keresztnev + vezeteknev[0]
# Eredmény: "AnnáK" (nagybetűs marad!)

# ✅ Helyes:
nev1 = keresztnev.lower() + vezeteknev[0].lower()
# Eredmény: "annak"
```

```python
# ❌ input() eredménye nem tárolva:
input("Név: ")           # Bekéri, de eldobja!

# ✅ Helyes:
nev = input("Név: ")     # Változóba tároljuk
```

```python
# ❌ Nincs függvényekre bontás:
nev = input("Név: ")
szam = input("szám: ")
print(nev + szam)

# ✅ Helyes: bekeres() + feldolgozas() + megjelenites()
```

### 🧠 Részletes Magyarázat

Az 1. feladat tipikusan: bekérés → szövegmanipuláció → kiírás. Három függvényre kell bontani!

---

### 2. feladat – gyakori hibák

```python
# ❌ random import hiányzik:
szam = random.randint(1, 10)  # NameError: name 'random' is not defined

# ✅ Helyes: fájl elejére:
import random
```

```python
# ❌ Érvénytelen tipp nem ellenőrzött:
tipp = int(input("Tipp: "))
# Mi van, ha 0-t vagy 100-at ír be?

# ✅ Helyes:
if tipp < 3 or tipp > 39:
    print("Érvénytelen tipp!")
```

```python
# ❌ Végtelen ciklus – rossz feltétel:
while True:
    tipp = int(input("Tipp: "))
    # Nincs break és nincs kilépési feltétel!

# ✅ Helyes:
while not talalt:
    tipp = int(input("Tipp: "))
    talalt = tipp_kiertekeles(tipp, osszeg)
```

### 🧠 Részletes Magyarázat

A 2. feladat tipikusan: random generálás → while ciklus → tipp bekérés → összehasonlítás → számláló → eredmény.

---

### 3. feladat – gyakori hibák

```python
# ❌ encoding hiányzik:
with open("filmek.txt", "r") as f:
    # Ékezetes karakterek hibásak!

# ✅ Helyes:
with open("filmek.txt", "r", encoding="utf-8") as f:
```

```python
# ❌ strip() hiányzik:
adatok = sor.split(";")
# Az utolsó adat: "7.5\n" (sortörés benne marad!)

# ✅ Helyes:
adatok = sor.strip().split(";")
```

```python
# ❌ Típuskonverzió hiányzik:
if film["ev"] > 2015:  # "2020" > 2015 → TypeError!

# ✅ Helyes – beolvasáskor konvertálunk:
film["ev"] = int(adatok[2])
```

```python
# ❌ fgv. előtag hiányzik:
filmek = beolvasas("filmek.txt")  # NameError!

# ✅ Helyes:
filmek = fgv.beolvasas("filmek.txt")
```

### 🧠 Részletes Magyarázat

A 3. feladat a legnehezebb, mert összekapcsolja az összes tanultat: fájlkezelés + szótárak + függvények + modul. A leggyakoribb hibák mind elkerülhetők, ha betartjuk az alábbi ellenőrző listát.

---

## 📊 Pontozási tippek

| Feladat | Max pont | Minimum a teljesítéshez |
|---------|----------|------------------------|
| 1. feladat | 8 | 4 |
| 2. feladat | 14 | 7 |
| 3. feladat | 18 | 9 |
| **Összesen** | **40** | **20 (50%)** |

### 🧠 Részletes Magyarázat

**Stratégia:** Ha időben szorulsz:
1. Kezdd a **3. feladattal** (legtöbb pont) – a beolvasás + darabszám már 4-5 pont
2. Folytasd az **1. feladattal** (legegyszerűbb)
3. A **2. feladatot** hagyd utoljára (összetett logika)

Vagy ha biztosra mész: 1 → 2 → 3 sorrendben, és rendszeresen push-olj!

---

## ✅ Ellenőrző lista a vizsgához

**Python:**
- [ ] Minden feladatot külön fájlba írtam
- [ ] A függvények definiálva vannak és meg is hívom őket
- [ ] A `random` modult importáltam
- [ ] A fájl megnyitásnál `encoding="utf-8"` szerepel
- [ ] Minden `.split()` előtt `.strip()` van
- [ ] A számokat `int()`-tel vagy `float()`-tal konvertáltam
- [ ] A `fgv.py` modult létrehoztam és importáltam
- [ ] A program lefut hiba nélkül

**Git:**
- [ ] Rendszeresen commitoltam (nem csak a végén)
- [ ] Értelmes commit üzeneteket írtam
- [ ] Az utolsó `git push` megtörtént
- [ ] A GitHubon ellenőriztem, hogy minden fájl feltöltődött
