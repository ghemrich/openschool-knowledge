# 10. hét – Adatfeldolgozás

> **Dokumentáció:** [W3Schools – Szótár metódusok](https://www.w3schools.com/python/python_dictionaries_methods.asp) | [Lista bejárás](https://www.w3schools.com/python/python_lists_loop.asp)

## 19. óra: Számlálás, szűrés

### Elemek számlálása

```python
filmek = [
    {"cim": "Film A", "kategoria": "akció", "ertekeles": 7.5},
    {"cim": "Film B", "kategoria": "dráma", "ertekeles": 8.2},
    {"cim": "Film C", "kategoria": "akció", "ertekeles": 6.1},
    {"cim": "Film D", "kategoria": "horror", "ertekeles": 7.0}
]

# Hány darab van összesen?
print(f"Összesen {len(filmek)} film van.")
```

### Számlálás kategóriánként

```python
# 1. módszer: kézi számlálás
akcio = 0
drama = 0
for film in filmek:
    if film["kategoria"] == "akció":
        akcio += 1
    elif film["kategoria"] == "dráma":
        drama += 1

# 2. módszer: szótár alapú (rugalmasabb!)
szamlalo = {}
for film in filmek:
    kat = film["kategoria"]
    szamlalo[kat] = szamlalo.get(kat, 0) + 1

for kat, db in szamlalo.items():
    print(f"{kat}: {db} db")
```

> **A `.get(kulcs, alap)` trükk:** Ha a kulcs nem létezik, az alapértéket adja vissza (itt `0`).

### Szűrés kategória szerint

```python
kategoria = input("Kategória: ")

for film in filmek:
    if film["kategoria"] == kategoria:
        print(f"  {film['cim']} ({film['ev']})")
```

---

## 20. óra: Keresés, min/max

### Lineáris keresés

```python
def film_keresese(filmek, keresett_cim):
    for film in filmek:
        if film["cim"] == keresett_cim:
            return film
    return None

cim = input("Film címe: ")
talalat = film_keresese(filmek, cim)

if talalat:
    print(f"Megtalálva: {talalat}")
else:
    print("Nincs ilyen cím a listában")
```

### Minimum és maximum keresés

```python
def legjobb_legrosszabb(filmek):
    legjobb = filmek[0]
    legrosszabb = filmek[0]

    for film in filmek:
        if film["ertekeles"] > legjobb["ertekeles"]:
            legjobb = film
        if film["ertekeles"] < legrosszabb["ertekeles"]:
            legrosszabb = film

    return legjobb, legrosszabb

legjobb, legrosszabb = legjobb_legrosszabb(filmek)
print(f"Legjobb: {legjobb['cim']} ({legjobb['ertekeles']})")
print(f"Legrosszabb: {legrosszabb['cim']} ({legrosszabb['ertekeles']})")
```

### Teljes munkafolyamat (3. feladat előkészítés)

```python
# 1. Beolvasás
filmek = beolvasas("filmek.txt")

# 2. Darabszám
print(f"Összesen: {len(filmek)} film")

# 3. Kategóriánként
szamlalo = kategoriak_szama(filmek)

# 4. Min/max
legjobb, legrosszabb = legjobb_legrosszabb(filmek)

# 5. Keresés + fájlba írás
# 6. Szűrés kategóriára
```
