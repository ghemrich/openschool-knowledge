# 📘 Lecke 06 – Függvények

> 📚 Dokumentáció:  
> https://www.w3schools.com/python/python_functions.asp

---

# 11. óra: Függvények alapjai

## ❓ Miért kellenek függvények?

- **Átláthatóbb kód** – Kisebb, érthető egységekre bontjuk a programot
- **Újrafelhasználhatóság** – Egyszer megírjuk, többször használjuk
- **Könnyebb tesztelés** – Külön-külön tesztelhetők
- **A vizsgán elvárás!**

---

## 🔧 Függvény létrehozása

```python
def koszont():
    print("Szia! Üdvözöllek a programban!")

# Függvény hívása
koszont()
```

### 🧠 Részletes Magyarázat

**def** – „Define" (definiálni). Ezzel hozunk létre új függvényt. A szintaxis:
```python
def fuggveny_neve():
    # A függvény törzse (behúzva!)
    ...
```

**Függvény hívása** – A függvényt a nevével és `()`-vel hívjuk meg. Ha nem hívjuk meg, a kód nem fut le!

```python
def koszont():
    print("Szia!")

# Ez CSAK definiál, nem futtat semmit.
# A Python megjegyzi, hogy van egy koszont nevű függvény.

koszont()   # ITT fut le! A () a hívás operátora.
koszont()   # Többször is hívható!
```

**Elnevezési konvenció** – Kisbetűs, szavak között aláhúzás: `beolvas_adatot()`, `szamol_atlagot()`.

---

## 📥 Paraméterek

```python
def koszont(nev):
    print(f"Szia, {nev}!")

koszont("Anna")
koszont("Béla")
```

### 🧠 Részletes Magyarázat

**Paraméter** – A zárójelben megadott változó, amit a függvény „kap" a hívástól. A `nev` paraméter értéke minden híváskor más lehet.

**Több paraméter:**
```python
def bemutatkozas(nev, kor):
    print(f"Nevem {nev}, {kor} éves vagyok.")

bemutatkozas("Anna", 20)    # Nevem Anna, 20 éves vagyok.
bemutatkozas("Béla", 25)    # Nevem Béla, 25 éves vagyok.
```

**Paraméterek sorrendje** – A híváskor a paramétereket UGYANABBAN a sorrendben kell megadni, mint a definiáláskor! Kivéve, ha nevesített paramétereket használunk:
```python
bemutatkozas(kor=25, nev="Béla")  # Ez is működik!
```

---

## ↩️ Visszatérési érték: `return`

```python
def osszeg(a, b):
    return a + b

eredmeny = osszeg(3, 5)
print(eredmeny)  # 8
```

### 🧠 Részletes Magyarázat

**return** – A függvény „visszaad" egy értéket a hívónak. A `return` után a függvény azonnal véget ér.

```python
def dupla(szam):
    return szam * 2
    print("Ez soha nem fut le!")  # A return UTÁN semmi nem hajtódik végre!

eredmeny = dupla(5)   # eredmeny = 10
```

**print() vs return:**
```python
# Ez KIÍRJA az eredményt, de nem adja vissza:
def osszeg_print(a, b):
    print(a + b)

# Ez VISSZAADJA az eredményt, amit eltárolhatunk:
def osszeg_return(a, b):
    return a + b

x = osszeg_print(3, 5)   # Kiír: 8, de x = None!
y = osszeg_return(3, 5)   # Nem ír ki semmit, de y = 8
```

**A vizsgán mindig `return`-t használj**, mert így a függvény eredményét tovább tudod használni!

---

## ✏️ Gyakorlat: Területszámítók

```python
def teglalap_terulet(a, b):
    return a * b

def kor_terulet(r):
    return r * r * 3.14159

print(f"Téglalap: {teglalap_terulet(5, 3)} cm²")
print(f"Kör: {kor_terulet(4):.2f} cm²")
```

### 🧠 Részletes Magyarázat

Minden függvénynek egy jól meghatározott feladata van:
- `teglalap_terulet(a, b)` → két oldal alapján kiszámolja a területet
- `kor_terulet(r)` → sugár alapján kiszámolja a kör területét

A `:.2f` formázás két tizedesjegyre kerekíti az eredményt (a kör terület nem egész szám lesz).

---

# 12. óra: Függvények gyakorlat

## 📦 Több visszatérési érték

```python
def beolvas():
    vezeteknev = input("Vezetéknév: ")
    keresztnev = input("Keresztnév: ")
    szam = input("Kedvenc szám: ")
    return vezeteknev, keresztnev, szam

# Több értéket kapunk vissza
vnev, knev, szam = beolvas()
```

### 🧠 Részletes Magyarázat

**Több return érték** – A `return` után vesszővel elválasztva több értéket adhatunk vissza. Technikailag ez egy **tuple**-t (rendezett n-es) ad vissza, amit szétbonthatunk (unpacking):

```python
def min_max(szamok):
    return min(szamok), max(szamok)

legkisebb, legnagyobb = min_max([5, 2, 8, 1, 9])
print(legkisebb)   # 1
print(legnagyobb)  # 9
```

---

## 🏗️ Program strukturálása függvényekkel

A vizsgán elvárás, hogy a program függvényekre legyen bontva:
- Egy függvény a **bekérésre**
- Egy függvény az **összefűzésre/előállításra**
- Egy függvény a **megjelenítésre**

### 🧠 Részletes Magyarázat

Ez az úgynevezett **MVC-szerű struktúra** (egyszerűsített):
1. **Bemenet (Input)** – Felhasználóval kommunikál, adatot gyűjt
2. **Feldolgozás (Logic)** – Számol, átalakít, létrehoz
3. **Kimenet (Output)** – Eredményt jelenít meg

```python
# ❌ ROSSZ: Mindent egy helyre ömlesztve
nev = input("Név: ")
kor = int(input("Kor: "))
if kor >= 18:
    print(f"{nev} felnőtt")
else:
    print(f"{nev} kiskorú")

# ✅ JÓ: Függvényekre bontva
def bekeres():
    nev = input("Név: ")
    kor = int(input("Kor: "))
    return nev, kor

def ellenorzes(kor):
    return "felnőtt" if kor >= 18 else "kiskorú"

def kiiras(nev, kategoria):
    print(f"{nev} {kategoria}")

# Főprogram
nev, kor = bekeres()
kat = ellenorzes(kor)
kiiras(nev, kat)
```

---

## ✏️ Gyakorlat: Felhasználónév generátor (vizsgafeladat típus!)

```python
def bekeres():
    vezeteknev = input("Vezetéknév: ")
    keresztnev = input("Keresztnév: ")
    kedvenc_szam = input("Kedvenc szám: ")
    return vezeteknev, keresztnev, kedvenc_szam


def nevek_osszeallitasa(vezeteknev, keresztnev, kedvenc_szam):
    vezeteknev = vezeteknev.lower()
    keresztnev = keresztnev.lower()
    nev1 = keresztnev + vezeteknev[0] + kedvenc_szam
    nev2 = keresztnev[0] + "_" + vezeteknev + kedvenc_szam
    nev3 = vezeteknev + "." + keresztnev + kedvenc_szam
    return nev1, nev2, nev3


def megjelenites(nev1, nev2, nev3):
    print(f"1. felhasználónév: {nev1}")
    print(f"2. felhasználónév: {nev2}")
    print(f"3. felhasználónév: {nev3}")


# Főprogram
vnev, knev, szam = bekeres()
n1, n2, n3 = nevek_osszeallitasa(vnev, knev, szam)
megjelenites(n1, n2, n3)
```

### 🧠 Részletes Magyarázat

Ez egy tipikus vizsgafeladat-struktúra. Három, jól elkülönülő függvény:

**bekeres()** – Összegyűjti a felhasználói adatokat és visszaadja tuple-ként. Az `input()` hívások CSAK itt vannak.

**nevek_osszeallitasa()** – A feldolgozás: kisbetűsít, összefűz, három variációt generál. Nincs benne `print()` és `input()`.

**megjelenites()** – Csak kiírja az eredményt. Nincs benne logika vagy számolás.

**A főprogram** – Három sor, ami összefűzi a függvényeket. Ez teszi olvashatóvá a kódot: a program logikája egy pillanat alatt átlátható.
