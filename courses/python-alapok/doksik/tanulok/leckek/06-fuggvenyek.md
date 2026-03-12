# 6. hét – Függvények I.

> **Dokumentáció:** [W3Schools – Függvények](https://www.w3schools.com/python/python_functions.asp)

## 11. óra: Függvények alapjai

### Miért kellenek függvények?
- Átláthatóbb kód
- Újrafelhasználhatóság
- Könnyebb tesztelés
- **A vizsgán elvárás!**

### Függvény létrehozása

```python
def koszont():
    print("Szia! Üdvözöllek a programban!")

# Függvény hívása
koszont()
```

### Paraméterek

```python
def koszont(nev):
    print(f"Szia, {nev}!")

koszont("Anna")
koszont("Béla")
```

### Visszatérési érték: `return`

```python
def osszeg(a, b):
    return a + b

eredmeny = osszeg(3, 5)
print(eredmeny)  # 8
```

### Gyakorlat: Területszámítók

```python
def teglalap_terulet(a, b):
    return a * b

def kor_terulet(r):
    return r * r * 3.14159

print(f"Téglalap: {teglalap_terulet(5, 3)} cm²")
print(f"Kör: {kor_terulet(4):.2f} cm²")
```

---

## 12. óra: Függvények gyakorlat

### Több visszatérési érték

```python
def beolvas():
    vezeteknev = input("Vezetéknév: ")
    keresztnev = input("Keresztnév: ")
    szam = input("Kedvenc szám: ")
    return vezeteknev, keresztnev, szam

# Több értéket kapunk vissza
vnev, knev, szam = beolvas()
```

### Program strukturálása függvényekkel

A vizsgán elvárás, hogy a program függvényekre legyen bontva. Például az 1. feladatban:
- Egy függvény a **bekérésre**
- Egy függvény az **összefűzésre/előállításra**
- Egy függvény a **megjelenítésre**

### Gyakorlat: Felhasználónév generátor (vizsgafeladat típus!)

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
