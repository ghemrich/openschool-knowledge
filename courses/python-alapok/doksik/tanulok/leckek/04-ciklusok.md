# 4. hét – Ciklusok

> **Dokumentáció:** [W3Schools – While ciklus](https://www.w3schools.com/python/python_while_loops.asp) | [For ciklus](https://www.w3schools.com/python/python_for_loops.asp)

## 7. óra: A `while` ciklus

### Alapszerkezet
A `while` ciklus addig ismétel, amíg a feltétel igaz.

```python
szam = 5
while szam > 0:
    print(szam)
    szam -= 1
print("Start!")
```

### Számláló változó

```python
i = 1
while i <= 10:
    print(i)
    i += 1
```

### Felhasználói bemenet ciklusban

```python
jelszo = ""
while jelszo != "titok":
    jelszo = input("Add meg a jelszót: ")
print("Helyes jelszó!")
```

### Gyakorlat: Számkitalálós játék

```python
import random

gondolt = random.randint(1, 20)
tipp = 0

while tipp != gondolt:
    tipp = int(input("Tippelj (1-20): "))
    if tipp < gondolt:
        print("Nagyobbra gondoltam!")
    elif tipp > gondolt:
        print("Kisebbre gondoltam!")

print(f"Eltaláltad! A szám: {gondolt}")
```

---

## 8. óra: A `for` ciklus és `range()`

### `for` ciklus szövegen

```python
szo = "Python"
for betu in szo:
    print(betu)
```

### `range()` függvény

```python
# 0-tól 4-ig (5 nem tartozik bele)
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# 1-től 10-ig
for i in range(1, 11):
    print(i)

# Páros számok 2-től 20-ig
for i in range(2, 21, 2):
    print(i)
```

### `break` és `continue`

```python
# break – kilépés a ciklusból
for i in range(1, 100):
    if i == 5:
        break
    print(i)  # 1, 2, 3, 4

# continue – ugrás a következő ismétlésre
for i in range(1, 6):
    if i == 3:
        continue
    print(i)  # 1, 2, 4, 5
```

### Gyakorlat: Szorzótábla

```python
szam = int(input("Melyik szorzótáblát írassam ki? "))

for i in range(1, 11):
    print(f"{szam} x {i} = {szam * i}")
```
