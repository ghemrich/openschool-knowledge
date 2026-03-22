# 📘 Lecke 09 – Összetett adatszerkezetek

> 📚 Dokumentáció:  
> https://www.w3schools.com/python/python_dictionaries.asp ·  
> https://www.w3schools.com/python/python_lists_access.asp

---

# 17. óra: Lista listája

## 📦 Mi az a lista listája?

Olyan lista, amelynek minden eleme szintén egy lista.

```python
tanulok = [
    ["Kiss Anna", 16, "Budapest"],
    ["Nagy Béla", 17, "Debrecen"],
    ["Tóth Csaba", 16, "Szeged"]
]
```

### 🧠 Részletes Magyarázat

**Lista listája (nested list)** – Egy kétdimenziós adatszerkezet: a „külső" lista tartalmazza a sorokat, a „belső" listák tartalmazzák az egyes adatokat.

Gondolj rá úgy, mint egy táblázat:

| Index | Név | Kor | Város |
|-------|-----|-----|-------|
| `[0]` | Kiss Anna | 16 | Budapest |
| `[1]` | Nagy Béla | 17 | Debrecen |
| `[2]` | Tóth Csaba | 16 | Szeged |

**Mikor használjuk?** – Amikor fájlból olvasunk be strukturált adatokat (pl. CSV), az egyes sorokat listákba tesszük, és ezeket egy nagy listába gyűjtjük.

---

## 🔢 Hozzáférés

```python
print(tanulok[0])       # ["Kiss Anna", 16, "Budapest"]
print(tanulok[0][0])    # Kiss Anna
print(tanulok[1][2])    # Debrecen
```

### 🧠 Részletes Magyarázat

**Dupla indexelés** – Az első index a „sort" (melyik belső lista), a második az „oszlopot" (melyik elem a belső listából) választja ki.

```
tanulok[0]      → ["Kiss Anna", 16, "Budapest"]     (0. sor = 1. tanuló)
tanulok[0][0]   → "Kiss Anna"                        (0. sor, 0. oszlop = név)
tanulok[0][1]   → 16                                 (0. sor, 1. oszlop = kor)
tanulok[1][2]   → "Debrecen"                         (1. sor, 2. oszlop = város)
```

---

## 📂 Fájlból beolvasás lista listába

```python
filmek = []

with open("filmek.txt", "r", encoding="utf-8") as f:
    for sor in f:
        adatok = sor.strip().split(";")
        # Típuskonverzió!
        adatok[2] = int(adatok[2])    # év
        adatok[3] = int(adatok[3])    # hossz
        adatok[4] = float(adatok[4])  # értékelés
        filmek.append(adatok)

# Használat
print(filmek[0][0])  # Első film címe
print(filmek[0][4])  # Első film értékelése
```

### 🧠 Részletes Magyarázat

**Típuskonverzió** – A `split()` után MINDEN adat szöveg (`str`). Ha számokkal akarunk dolgozni (összehasonlítás, átlagszámítás), konvertálni kell:
- `int()` – egész számokhoz (év, darabszám)
- `float()` – tizedes számokhoz (értékelés, ár)

```python
"2020"          # Ez egy szöveg!
int("2020")     # Ez egy szám: 2020
float("7.5")    # Ez egy szám: 7.5
```

**Miért fontos?** Ha nem konvertálunk:
```python
"2020" > "1990"   # True, de szöveg-összehasonlítás! (ABC sorrend)
"9" > "1990"      # True – mert "9" > "1" (karakter szinten!)
int("9") > int("1990")  # False – helyes szám-összehasonlítás
```

---

# 18. óra: Szótárak és szótárak listája

## 📕 Szótár (`dict`) alapok

```python
tanulo = {
    "nev": "Kiss Anna",
    "kor": 16,
    "varos": "Budapest"
}

print(tanulo["nev"])    # Kiss Anna
print(tanulo["kor"])    # 16
```

### 🧠 Részletes Magyarázat

**Szótár (dictionary)** – Kulcs-érték párok gyűjteménye, kapcsos zárójelek `{}` között. A kulcs mindig szöveg (idézőjelben), az érték bármi lehet.

```python
{
    "kulcs": "érték",
    "nev": "Kiss Anna",   # kulcs: "nev", érték: "Kiss Anna"
    "kor": 16,             # kulcs: "kor", érték: 16
}
```

**Hozzáférés** – A kulccsal érjük el az értéket: `szótár["kulcs"]`. Ez sokkal olvashatóbb, mint `lista[0]`!

```python
# Lista: mit jelent a [1]?
tanulo = ["Kiss Anna", 16, "Budapest"]
print(tanulo[1])         # 16 – de mi ez? Kor? Osztály?

# Szótár: egyértelmű!
tanulo = {"nev": "Kiss Anna", "kor": 16, "varos": "Budapest"}
print(tanulo["kor"])     # 16 – egyértelmű, hogy ez a kor
```

**KeyError** – Ha nem létező kulcsot keresünk:
```python
tanulo["email"]  # KeyError: 'email'
```

---

## 📚 Szótárak listája

Sokkal olvashatóbb, mint a lista listája!

```python
filmek = [
    {"cim": "Film A", "kategoria": "akció", "ev": 2020, "ertekeles": 7.5},
    {"cim": "Film B", "kategoria": "dráma", "ev": 2019, "ertekeles": 8.2}
]

# Hozzáférés
print(filmek[0]["cim"])       # Film A
print(filmek[1]["ertekeles"]) # 8.2
```

### 🧠 Részletes Magyarázat

**Szótárak listája** – Minden listaelem egy szótár. Indexszel választjuk ki a szótárat, kulccsal az adatot.

```python
filmek[0]            # {"cim": "Film A", "kategoria": "akció", ...}
filmek[0]["cim"]     # "Film A"
filmek[0]["ev"]      # 2020
```

**Bejárás:**
```python
for film in filmek:
    print(f"{film['cim']} ({film['ev']}) - {film['ertekeles']}")
```

---

## 📂 Beolvasás szótárak listájába

```python
filmek = []

with open("filmek.txt", "r", encoding="utf-8") as f:
    for sor in f:
        adatok = sor.strip().split(";")
        film = {
            "cim": adatok[0],
            "kategoria": adatok[1],
            "ev": int(adatok[2]),
            "hossz": int(adatok[3]),
            "ertekeles": float(adatok[4])
        }
        filmek.append(film)

# Sokkal olvashatóbb!
for film in filmek:
    print(f"{film['cim']} ({film['ev']}) - {film['ertekeles']}")
```

### 🧠 Részletes Magyarázat

Ez a minta a vizsgafeladatok 3. feladatához kell:
1. Üres lista létrehozása
2. Fájl megnyitása `with open()`
3. Soronkénti olvasás `for sor in f`
4. `strip().split(";")` → lista
5. Szótár összeállítása a megfelelő kulcsokkal
6. `append()` a nagy listába

**Típuskonverzió a szótárban** – A számértékeket rögtön konvertáljuk a szótár létrehozásakor, így később nem kell folyton `int()`-ezni.

---

## 📊 Összehasonlítás

| | Lista listája | Szótárak listája |
|---|---|---|
| Hozzáférés | `film[0]` | `film["cim"]` |
| Olvashatóság | Nehezebb | Könnyebb |
| Memória | Kevesebb | Több |
| Vizsgán | Elfogadott | Elfogadott |

### 🧠 Részletes Magyarázat

Mindkét megközelítés elfogadott a vizsgán. A **szótárak listája** olvashatóbb (tudjuk, mit jelent `film["cim"]`), de a **lista listája** kompaktabb. Válaszd azt, amelyikkel magabiztosabb vagy!
