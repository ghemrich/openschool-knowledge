# Feladatok – 12. hét: Vizsgafelkészítés

> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz
> A megoldásokat commitold és pushold a GitHub repódba.

---

### 12.1 – Próbavizsga ⭐⭐⭐
Oldd meg a teljes vizsgát (mindhárom feladat) 90 perc alatt, vizsga körülmények között:
1. Fogadd el a GitHub Classroom próbavizsga linket
2. Klónozd le, dolgozz, commitolj rendszeresen
3. Az utolsó push a beadás

### 12.2 – Hibakeresés ⭐⭐
Az alábbi kódrészletekben hibák vannak. Keresd meg és javítsd ki őket!

**a)**
```python
nev = input("Neved: ")
print("Szia, " + nev + "! Te " + 16 + " éves vagy.")
```

**b)**
```python
import random
szam = random.randint(1, 10)
tipp = input("Tippelj: ")
if tipp == szam:
    print("Talált!")
```

**c)**
```python
with open("adatok.txt", "r") as f:
    for sor in f:
        adatok = sor.split(";")
        ev = adatok[2]
        print(ev + 1)
```

**d)**
```python
def beolvas(fajl):
    lista = []
    with open(fajl) as f:
        for sor in f:
            adat = sor.split(";")
            lista.append(adat)
    return lista

adatok = beolvas("adatok.txt")
print(adatok[0]["nev"])
```

### 12.3 – Git gyakorlás ⭐
Készíts egy `hello.py` fájlt. Végezd el az alábbi lépéseket, és minden lépés után futtasd a `git log --oneline` parancsot:
1. Hozd létre a fájlt egy `print("Hello")` sorral → commit
2. Adj hozzá egy második `print()` sort → commit
3. Adj hozzá egy `input()` bekérést → commit
4. Pushold az egészet
