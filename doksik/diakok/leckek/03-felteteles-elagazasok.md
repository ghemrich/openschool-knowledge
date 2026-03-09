# 3. hét – Feltételes elágazások

> **Dokumentáció:** [W3Schools – If...Else](https://www.w3schools.com/python/python_conditions.asp)

## 5. óra: Az `if` utasítás

### Alapszerkezet

```python
kor = int(input("Hány éves vagy? "))

if kor >= 18:
    print("Felnőtt vagy.")
else:
    print("Kiskorú vagy.")
```

### Összehasonlító operátorok

| Operátor | Jelentés |
|----------|----------|
| `==` | egyenlő |
| `!=` | nem egyenlő |
| `<` | kisebb |
| `>` | nagyobb |
| `<=` | kisebb vagy egyenlő |
| `>=` | nagyobb vagy egyenlő |

### Logikai operátorok

```python
kor = 16
diak = True

if kor >= 14 and diak:
    print("Diákigazolvány jár!")

szam = 15
if szam < 10 or szam > 20:
    print("A szám a tartományon kívül van")
```

### Gyakorlat: Páros/páratlan

```python
szam = int(input("Adj meg egy számot: "))

if szam % 2 == 0:
    print(f"{szam} páros szám.")
else:
    print(f"{szam} páratlan szám.")
```

---

## 6. óra: Többágú elágazás

### `elif` használata

```python
pontszam = int(input("Pontszám: "))

if pontszam >= 90:
    print("Jeles (5)")
elif pontszam >= 75:
    print("Jó (4)")
elif pontszam >= 60:
    print("Közepes (3)")
elif pontszam >= 40:
    print("Elégséges (2)")
else:
    print("Elégtelen (1)")
```

### Összetett feltételek

```python
ho = int(input("Hónap (1-12): "))

if ho >= 3 and ho <= 5:
    print("Tavasz")
elif ho >= 6 and ho <= 8:
    print("Nyár")
elif ho >= 9 and ho <= 11:
    print("Ősz")
else:
    print("Tél")
```

### Gyakorlat: Belépőjegy árazás

```python
kor = int(input("Életkor: "))
diak = input("Diák vagy? (igen/nem): ")

if kor < 6:
    print("Ingyenes")
elif kor < 18 or diak == "igen":
    print("Kedvezményes: 500 Ft")
elif kor >= 65:
    print("Nyugdíjas: 800 Ft")
else:
    print("Teljes ár: 1500 Ft")
```
