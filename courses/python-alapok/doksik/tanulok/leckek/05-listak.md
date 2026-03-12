# 5. hét – Listák

> **Dokumentáció:** [W3Schools – Listák](https://www.w3schools.com/python/python_lists.asp) | [Lista metódusok](https://www.w3schools.com/python/python_lists_methods.asp) | [Lista comprehension](https://www.w3schools.com/python/python_lists_comprehension.asp)

## 9. óra: Listák alapjai

### Lista létrehozása

```python
gyumolcsok = ["alma", "körte", "szilva"]
szamok = [10, 20, 30, 40, 50]
ures_lista = []
```

### Indexelés és hossz

```python
gyumolcsok = ["alma", "körte", "szilva"]
print(gyumolcsok[0])    # alma
print(gyumolcsok[-1])   # szilva
print(len(gyumolcsok))  # 3
```

### Elem hozzáadása: `append()`

```python
szamok = [1, 2, 3]
szamok.append(4)
print(szamok)  # [1, 2, 3, 4]
```

### Lista bejárása

```python
nevek = ["Anna", "Béla", "Csaba"]

for nev in nevek:
    print(f"Szia, {nev}!")
```

### Hasznos függvények

```python
szamok = [5, 2, 8, 1, 9]

print(len(szamok))  # 5 (elemek száma)
print(sum(szamok))  # 25 (összeg)
print(min(szamok))  # 1 (legkisebb)
print(max(szamok))  # 9 (legnagyobb)
```

### Gyakorlat: Bevásárlólista

```python
lista = []

while True:
    elem = input("Mit vegyek? (kilépés: 'vége'): ")
    if elem == "vége":
        break
    lista.append(elem)

print(f"\nBevásárlólista ({len(lista)} tétel):")
for i, elem in enumerate(lista, 1):
    print(f"  {i}. {elem}")
```

---

## 10. óra: Listaműveletek

### Szeletelés

```python
szamok = [10, 20, 30, 40, 50]
print(szamok[1:3])   # [20, 30]
print(szamok[:3])    # [10, 20, 30]
print(szamok[2:])    # [30, 40, 50]
```

### Az `in` operátor

```python
gyumolcsok = ["alma", "körte", "szilva"]

if "alma" in gyumolcsok:
    print("Van alma!")

if "banán" not in gyumolcsok:
    print("Nincs banán.")
```

### Rendezés

```python
szamok = [5, 2, 8, 1, 9]

# Helyben rendezés
szamok.sort()
print(szamok)  # [1, 2, 5, 8, 9]

# Csökkenő sorrend
szamok.sort(reverse=True)
print(szamok)  # [9, 8, 5, 2, 1]

# Új listát ad vissza
rendezett = sorted([5, 2, 8])
print(rendezett)  # [2, 5, 8]
```

### Lista comprehension

```python
# Hagyományos módszer
parosak = []
for i in range(1, 11):
    if i % 2 == 0:
        parosak.append(i)

# Ugyanaz tömörebben
parosak = [i for i in range(1, 11) if i % 2 == 0]
print(parosak)  # [2, 4, 6, 8, 10]
```

### Gyakorlat: Osztályzatok elemzése

```python
jegyek = []

while True:
    bemenet = input("Jegy (1-5, vagy 'vége'): ")
    if bemenet == "vége":
        break
    jegyek.append(int(bemenet))

print(f"Jegyek száma: {len(jegyek)}")
print(f"Átlag: {sum(jegyek) / len(jegyek):.2f}")
print(f"Legjobb: {max(jegyek)}")
print(f"Legrosszabb: {min(jegyek)}")
```
