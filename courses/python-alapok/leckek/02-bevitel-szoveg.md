# 📘 Lecke 02 – Bevitel és szövegkezelés

> 📚 Dokumentáció:  
> https://www.w3schools.com/python/python_user_input.asp ·  
> https://www.w3schools.com/python/python_strings.asp ·  
> https://www.w3schools.com/python/python_string_formatting.asp

---

# 3. óra: Billentyűzetes bevitel

## ⌨️ Az `input()` függvény

A felhasználótól kér be adatot. Mindig szöveget (`str`) ad vissza!

```python
nev = input("Mi a neved? ")
print("Szia,", nev)
```

### 🧠 Részletes Magyarázat

**input("szöveg")**  
A zárójelben lévő szöveg a kérdés, ami megjelenik a felhasználónak. A program megáll és vár, amíg a felhasználó beír valamit és Entert nyom. Az eredmény **mindig `str`** (szöveg), még ha számot írt is be!

```python
nev = input("Mi a neved? ")
# A program megáll → a felhasználó beírja: Anna → Enter
# nev = "Anna" (str típus!)
```

⚠️ Fontos: ha szám kell, konvertálni kell! Erről a következő részben tanulunk.

---

## 🔄 Típuskonverzió

Az `input()` mindig szöveget ad. Számokká kell alakítani:

```python
szam_szoveg = input("Adj meg egy számot: ")
szam = int(szam_szoveg)         # egész számmá alakítás
print("A duplája:", szam * 2)

ar = float(input("Ár: "))      # közvetlenül is lehet
print("ÁFA-val:", ar * 1.27)
```

### 🧠 Részletes Magyarázat

**int()** – Szöveget egész számmá alakít.
```python
szoveg = "42"
szam = int(szoveg)    # szam = 42 (int típus)
```
Csak akkor működik, ha a szöveg valóban egész szám! `int("alma")` → **HIBA!**

**float()** – Szöveget tizedes számmá alakít.
```python
szoveg = "3.14"
szam = float(szoveg)  # szam = 3.14 (float típus)
```

**str()** – Számot szöveggé alakít.
```python
szam = 42
szoveg = str(szam)    # szoveg = "42" (str típus)
```

**Miért kell konvertálni?**  
Mert az `input()` mindig `str`-t ad, és szöveggel nem lehet matematikai műveletet végezni:
```python
szam = input("Szám: ")   # A felhasználó beírja: 5
print(szam * 2)           # "55" – a szöveget megkettőzi, nem összeadja!

szam = int(input("Szám: "))
print(szam * 2)           # 10 – most már számként működik!
```

**Rövidített forma** – Az `int()` és `input()` egymásba ágyazható:
```python
# Hosszú forma:
szoveg = input("Kor: ")
kor = int(szoveg)

# Rövid forma (ugyanaz):
kor = int(input("Kor: "))
```

---

## ✏️ Gyakorlat: Egyszerű számológép

```python
a = int(input("Első szám: "))
b = int(input("Második szám: "))

print("Összeg:", a + b)
print("Különbség:", a - b)
print("Szorzat:", a * b)
```

### 🧠 Részletes Magyarázat

Ez egy tipikus **bemenet → feldolgozás → kimenet** program:
1. **Bemenet**: bekérjük a két számot `input()`-tal és `int()`-tel konvertáljuk
2. **Feldolgozás**: elvégezzük a műveleteket (`+`, `-`, `*`)
3. **Kimenet**: kiírjuk az eredményeket `print()`-tel

Ez a minta szinte minden programban visszaköszön!

---

# 4. óra: Szövegműveletek

## 🔗 Szöveg összefűzés (konkatenáció)

```python
vezeteknev = "Kiss"
keresztnev = "Anna"
teljes_nev = vezeteknev + " " + keresztnev
print(teljes_nev)  # Kiss Anna
```

### 🧠 Részletes Magyarázat

**+ operátor szövegeknél**  
Amikor két `str` típusú értéket `+`-szal kapcsolsz össze, a Python összefűzi őket:
```python
"Hello" + "Világ"       # "HelloVilág" (nincs szóköz!)
"Hello" + " " + "Világ" # "Hello Világ" (szóközt nekünk kell hozzáadni)
```

⚠️ Szöveget és számot nem lehet `+`-szal összefűzni:
```python
"Kor: " + 16            # HIBA! TypeError
"Kor: " + str(16)       # "Kor: 16" – először konvertálni kell str()-rel
```

**Szöveg ismétlése `*`-gal:**
```python
print("-" * 30)          # ------------------------------ (30 kötőjel)
print("Ha" * 3)          # HaHaHa
```

---

## 🔢 Szöveg indexelés

Minden karakter sorszámot kap, 0-tól kezdve:

```
K  i  s  s     A  n  n  a
0  1  2  3  4  5  6  7  8
```

```python
nev = "Kiss Anna"
print(nev[0])    # K (első karakter)
print(nev[5])    # A
print(nev[-1])   # a (utolsó karakter)
print(nev[-2])   # n (utolsó előtti)
```

### 🧠 Részletes Magyarázat

**Pozitív index** – Balról jobbra számol, 0-tól kezdve.  
**Negatív index** – Jobbról balra számol, -1-től kezdve (az utolsó karakter).

```python
szoveg = "Python"
#         P  y  t  h  o  n
# index:  0  1  2  3  4  5
# negatív:-6 -5 -4 -3 -2 -1
```

**Szeletelés (slicing)** – Egy részszöveget kivágsz:
```python
szoveg = "Python"
print(szoveg[0:3])    # "Pyt" – 0. indextől a 3. előttig
print(szoveg[2:])     # "thon" – a 2. indextől a végéig
print(szoveg[:3])     # "Pyt" – az elejétől a 3. előttig
```

**len()** – Megadja a szöveg hosszát (karakterek száma):
```python
nev = "Kiss Anna"
print(len(nev))       # 9 (a szóköz is karakter!)
```

---

## 🛠️ Szöveg metódusok

```python
nev = "Kiss Anna"
print(nev.lower())       # kiss anna
print(nev.upper())       # KISS ANNA
print(nev.title())       # Kiss Anna
print(nev.strip())       # szóközök eltávolítása az elejéről/végéről
print(nev.replace("Kiss", "Nagy"))  # Nagy Anna
print(nev.count("a"))    # 1 (kisbetű "a" egyszer van)
print(nev.startswith("Ki"))  # True
print(nev.find("Anna"))  # 5 (az 5. indextől kezdődik)
```

### 🧠 Részletes Magyarázat

**metódus** = egy függvény, ami a szöveghez tartozik. A pont `.` operátorral hívjuk meg.

**lower() / upper()** – Kisbetűssé / nagybetűssé alakítja a teljes szöveget. Az eredeti változó nem módosul!
```python
nev = "Kiss Anna"
kicsi = nev.lower()      # kicsi = "kiss anna"
print(nev)               # "Kiss Anna" – az eredeti változatlan!
```

**strip()** – Eltávolítja a felesleges szóközöket (és sortöréseket) a szöveg elejéről és végéről. Nagyon hasznos `input()` utáni tisztításra:
```python
bemenet = "   hello   "
print(bemenet.strip())   # "hello"
```

**replace(régi, új)** – Kicserél egy részt a szövegben:
```python
mondat = "Ma szép az idő"
print(mondat.replace("szép", "rossz"))  # "Ma rossz az idő"
```

**find(keresett)** – Megadja, hányadik indextől kezdődik a keresett szöveg. Ha nem találja: `-1`.

---

## ✨ f-string formázás

A legkényelmesebb módja szöveg és változók kombinálásának:

```python
nev = "Anna"
kor = 16
print(f"Szia, {nev}! Te {kor} éves vagy.")
# Szia, Anna! Te 16 éves vagy.
```

### 🧠 Részletes Magyarázat

**f-string** – Az idézőjel elé tett `f` betű jelzi, hogy a kapcsos zárójelek `{}` között változókat (vagy kifejezéseket) használsz:
```python
ar = 1500
print(f"Az ár: {ar} Ft")           # Az ár: 1500 Ft
print(f"ÁFA-val: {ar * 1.27} Ft")  # ÁFA-val: 1905.0 Ft (kifejezés is lehet!)
```

**Formázási lehetőségek:**
```python
atlag = 4.56789
print(f"Átlag: {atlag:.2f}")       # Átlag: 4.57 (2 tizedesre kerekítve)

szam = 42
print(f"Szám: {szam:05d}")         # Szám: 00042 (5 jegyű, nullákkal feltöltve)
```

A `.2f` = 2 tizedes jegy (`f` = float formátum). Ez nagyon hasznos átlagszámításnál!

---

## ✏️ Gyakorlat: Névkártya generátor

```python
vezeteknev = input("Vezetéknév: ")
keresztnev = input("Keresztnév: ")

print(f"Névkártya: {vezeteknev.upper()} {keresztnev}")
print(f"Monogram: {vezeteknev[0]}.{keresztnev[0]}.")
print(f"Email: {keresztnev.lower()}.{vezeteknev.lower()}@iskola.hu")
```

### 🧠 Részletes Magyarázat

Ez a program jól mutatja, hogyan kombinálható az `input()`, a szöveg metódusok és az f-string:
- `vezeteknev.upper()` – nagybetűssé alakítja a vezetéknevet a névkártyán
- `vezeteknev[0]` – kiveszi az első betűt (a monogramhoz)
- `keresztnev.lower()` – kisbetűssé alakítja az email-címhez

Figyeld meg, hogy a metódusokat közvetlenül az f-string-en belül is használhatod – nem kell külön változóba menteni!
