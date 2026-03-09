# 2. hét – Bevitel és szövegkezelés

> **Dokumentáció:** [W3Schools – Input](https://www.w3schools.com/python/python_user_input.asp) | [Szövegek (Strings)](https://www.w3schools.com/python/python_strings.asp) | [Szöveg metódusok](https://www.w3schools.com/python/python_strings_methods.asp) | [String formázás](https://www.w3schools.com/python/python_string_formatting.asp)

## 3. óra: Billentyűzetes bevitel

### Az `input()` függvény
A felhasználótól kér be adatot. Mindig szöveget (`str`) ad vissza!

```python
nev = input("Mi a neved? ")
print("Szia,", nev)
```

### Típuskonverzió
Az `input()` mindig szöveget ad. Számokká kell alakítani:

```python
szam_szoveg = input("Adj meg egy számot: ")
szam = int(szam_szoveg)         # egész számmá alakítás
print("A duplája:", szam * 2)

ar = float(input("Ár: "))      # közvetlenül is lehet
print("ÁFA-val:", ar * 1.27)
```

### Gyakorlat: Egyszerű számológép

```python
a = int(input("Első szám: "))
b = int(input("Második szám: "))

print("Összeg:", a + b)
print("Különbség:", a - b)
print("Szorzat:", a * b)
```

---

## 4. óra: Szövegműveletek

### Szöveg összefűzés

```python
vezeteknev = "Kiss"
keresztnev = "Anna"
teljes_nev = vezeteknev + " " + keresztnev
print(teljes_nev)  # Kiss Anna
```

### Szöveg indexelés
Minden karakter sorszámot kap, 0-tól kezdve:

```
K  i  s  s
0  1  2  3
```

```python
nev = "Kiss"
print(nev[0])   # K (első karakter)
print(nev[-1])  # s (utolsó karakter)
```

### Szöveg metódusok

```python
nev = "Kiss Anna"
print(nev.lower())   # kiss anna
print(nev.upper())   # KISS ANNA
print(nev.strip())   # szóközök eltávolítása az elejéről/végéről
```

### f-string formázás
A legkényelmesebb módja szöveg és változók kombinálásának:

```python
nev = "Anna"
kor = 16
print(f"Szia, {nev}! Te {kor} éves vagy.")
# Szia, Anna! Te 16 éves vagy.
```

### Gyakorlat: Névkártya generátor

```python
vezeteknev = input("Vezetéknév: ")
keresztnev = input("Keresztnév: ")

print(f"Névkártya: {vezeteknev.upper()} {keresztnev}")
print(f"Monogram: {vezeteknev[0]}.{keresztnev[0]}.")
print(f"Email: {keresztnev.lower()}.{vezeteknev.lower()}@iskola.hu")
```
