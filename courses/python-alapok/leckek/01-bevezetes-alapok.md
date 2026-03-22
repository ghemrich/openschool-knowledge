# 📘 Lecke 01 – Bevezetés és alapok

> 📚 Dokumentáció:  
> https://www.w3schools.com/python/python_intro.asp ·  
> https://www.w3schools.com/python/python_variables.asp ·  
> https://www.w3schools.com/python/python_datatypes.asp

---

# 1. óra: A Python világa

## ❓ Mi a programozás?

A programozás azt jelenti, hogy utasításokat írunk a számítógépnek, amelyeket sorban végrehajt. A Python egy **magas szintű programozási nyelv** – közel áll az emberi nyelvhez, ezért könnyű tanulni.

---

## 🖨️ Első program

```python
# Ez egy megjegyzés – a Python nem futtatja
print("Hello, világ!")
print("Üdv a Python világában!")
```

### 🧠 Részletes Magyarázat

**# megjegyzés (comment)**  
A `#` jel utáni szöveget a Python figyelmen kívül hagyja. Arra szolgál, hogy magadnak (vagy másoknak) jegyzeteket írj a kódba. Használd bátran!

**print()**  
A `print()` függvény szöveget ír ki a képernyőre (a terminálba). A szöveget idézőjelek közé kell tenni.

```python
print("Ez egy szöveg")          # Dupla idézőjel – ez a leggyakoribb
print('Ez is szöveg')           # Szimpla idézőjel – ugyanúgy működik
print("Eredmény:", 2 + 3)      # Szöveget és számot is kiírhatsz egyszerre
```

Az idézőjelek közötti szöveget **stringnek** (szövegnek) nevezzük. A `print()` többféle érték kiírására is képes – vesszővel elválasztva:
```python
print("Alma", "Körte", "Szilva")   # Alma Körte Szilva (szóközökkel elválasztva)
print("3 + 5 =", 3 + 5)            # 3 + 5 = 8
```

---

# 2. óra: Változók és típusok

## 📦 Változók

A változó egy „doboz", amiben adatot tárolunk. A Python-ban nem kell előre megmondani, milyen típusú a változó – a Python kitalálja magától.

```python
nev = "Anna"
kor = 16
atlag = 4.5
diak = True
```

### 🧠 Részletes Magyarázat

**Változó létrehozása**  
Pythonban egy változót úgy hozol létre, hogy nevet adsz neki és értéket rendelsz hozzá az `=` jelöl:
```python
nev = "Anna"       # A nev változóban most az "Anna" szöveg van
kor = 16            # A kor változóban a 16-os szám van
```

**Változó elnevezési szabályok:**
- Csak betűvel vagy `_` aláhúzással kezdődhet (nem számmal!)
- Tartalmazhat betűket, számokat és aláhúzást
- Kis- és nagybetű különbözik! (`nev` ≠ `Nev` ≠ `NEV`)
- Ékezetes karaktereket Pythonban technicalleg használhatsz, de kerüld el!

**Jó nevek:**
```python
felhasznalo_nev = "Kiss Anna"     # Értelmes, olvasható
szamla_osszeg = 15000             # Leíró név
```

**Rossz nevek:**
```python
x = "Kiss Anna"                   # Nem leíró – mire való?
2szam = 15                        # HIBA! Nem kezdődhet számmal
```

---

## 📊 Alaptípusok

| Típus | Leírás | Példa |
|-------|--------|-------|
| `int` | Egész szám | `42`, `-7`, `0` |
| `float` | Tizedes tört | `3.14`, `-0.5`, `100.0` |
| `str` | Szöveg (string) | `"alma"`, `'hello'` |
| `bool` | Logikai érték | `True`, `False` |

### 🧠 Részletes Magyarázat

**int (integer = egész szám)**  
Egész számok, tizedes pont nélkül. Lehet pozitív, negatív, vagy nulla.
```python
eletkor = 16
homerseklet = -5
pontszam = 0
```

**float (lebegőpontos szám = tizedes tört)**  
Számok tizedesponttal. Figyelem: Pythonban **pont** van, nem vessző!
```python
atlag = 4.5         # Jó ✅
pi = 3.14159        # Jó ✅
# atlag = 4,5       # HIBA ❌ – a vessző nem tizedespont!
```

**str (string = szöveg)**  
Idézőjelek közötti szöveg. Lehet dupla `"` vagy szimpla `'` idézőjel.
```python
nev = "Kiss Anna"
varos = 'Budapest'
ures = ""            # Üres string – ez is érvényes!
```

**bool (boolean = logikai érték)**  
Csak két értéke lehet: `True` (igaz) vagy `False` (hamis). Nagybetűvel kezdődik!
```python
aktiv = True
admin = False
```

---

## 🔎 A `type()` függvény

A `type()` megmondja, milyen típusú egy változó:

```python
x = 42
print(type(x))  # <class 'int'>

y = "hello"
print(type(y))  # <class 'str'>

z = 3.14
print(type(z))  # <class 'float'>

w = True
print(type(w))  # <class 'bool'>
```

### 🧠 Részletes Magyarázat

**type()** – Nagyon hasznos, ha nem vagy benne biztos, hogy egy változó milyen típusú. Különösen fontos lesz, amikor a felhasználótól kaptál adatot (az `input()` mindig `str`-t ad vissza – erről a következő héten tanulunk).

A kimenet formátuma: `<class 'típusnév'>`. Ami igazán számít az a típusnév: `int`, `float`, `str`, `bool`.

---

## 🔢 Alapműveletek

```python
# Számolás
print(10 + 3)    # 13 – összeadás
print(10 - 3)    # 7 – kivonás
print(10 * 3)    # 30 – szorzás
print(10 / 3)    # 3.333... – osztás (mindig float-ot ad!)
print(10 // 3)   # 3 – egész osztás (lefelé kerekít)
print(10 % 3)    # 1 – maradékos osztás (modulo)
print(2 ** 3)    # 8 – hatványozás (2 a 3-on)
```

### 🧠 Részletes Magyarázat

**/** (osztás) – Mindig `float`-ot ad eredményül, még ha az eredmény kerek szám is:
```python
print(10 / 2)    # 5.0 (nem 5!)
```

**//** (egész osztás) – Levágja a tizedes részt (lefelé kerekít):
```python
print(7 // 2)    # 3 (nem 3.5!)
```

**%** (modulo = maradék) – Megadja az osztás maradékát:
```python
print(7 % 2)     # 1, mert 7 = 3*2 + 1
print(10 % 5)    # 0, mert 10 = 2*5 + 0 (maradék nélkül osztható!)
```
A modulo nagyon hasznos: pl. páros-páratlan eldöntése (`szam % 2 == 0`), vagy oszthatóság vizsgálata.

**\*\*** (hatványozás):
```python
print(2 ** 10)   # 1024 (2 a 10-re)
print(9 ** 0.5)  # 3.0 (négyzetgyök!)
```

---

## ✏️ Gyakorlat

Készíts programot, amely kiírja a neved, a korod és a kedvenc tantárgyadat!

```python
nev = "Kiss Anna"
kor = 16
tantargy = "informatika"

print("Név:", nev)
print("Kor:", kor)
print("Kedvenc tantárgy:", tantargy)
```

### 🧠 Részletes Magyarázat

Figyeld meg, hogy a `print()` függvénynek vesszővel elválasztva adunk át szöveget és változót. A vessző automatikusan szóközt tesz közéjük:
```python
print("Név:", nev)    # Kimenet: Név: Kiss Anna
```

Ez egyenértékű lenne ezzel:
```python
print("Név: " + nev)  # Ugyanaz a kimenet, de szöveg-összefűzéssel
```

A különbség: a vesszős módszer mindenféle típust elfogad (szöveg, szám, stb.), míg a `+` összefűzésnél mindkét elemnek szövegnek kell lennie.
