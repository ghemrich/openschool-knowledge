# 11. hét – Modulok és összefoglaló projekt

> **Dokumentáció:** [W3Schools – Modulok](https://www.w3schools.com/python/python_modules.asp)

## 21. óra: Saját modul készítése

### Mi a modul?
Egy Python fájl (`.py`), amelyben függvényeket tárolunk. Más programból importálhatjuk és használhatjuk.

### Miért használunk modult?
- Átláthatóbb kód
- Újrafelhasználhatóság
- **A vizsgán kötelező a 3. feladatnál!**

### Modul létrehozása

Hozzunk létre egy `fgv.py` nevű fájlt:

```python
# fgv.py

def beolvasas(fajlnev):
    filmek = []
    with open(fajlnev, "r", encoding="utf-8") as f:
        for sor in f:
            adatok = sor.strip().split(";")
            film = {
                "cim": adatok[0],
                "kategoria": adatok[1],
                "ev": int(adatok[2]),
                "hossz": int(adatok[3]),
                "ertekeles": float(adatok[4])
            }
            filmek.append(film)
    return filmek


def darabszam(filmek):
    return len(filmek)


def kategoriak_szama(filmek):
    szamlalo = {}
    for film in filmek:
        kat = film["kategoria"]
        szamlalo[kat] = szamlalo.get(kat, 0) + 1
    return szamlalo
```

### Modul importálása és használata

A főprogramban (`feladat3.py`):

```python
# feladat3.py
import fgv

filmek = fgv.beolvasas("filmek.txt")
print(f"Összesen {fgv.darabszam(filmek)} film.")

szamlalo = fgv.kategoriak_szama(filmek)
for kat, db in szamlalo.items():
    print(f"{kat}: {db} db")
```

> **Fontos:** A `fgv.py` és a `feladat3.py` fájl **ugyanabban a mappában** legyen!

---

## 22. óra: Komplex feladat – teljes 3. vizsga feladat

### A teljes modul (`fgv.py`)

```python
def beolvasas(fajlnev):
    filmek = []
    with open(fajlnev, "r", encoding="utf-8") as f:
        for sor in f:
            adatok = sor.strip().split(";")
            film = {
                "cim": adatok[0],
                "kategoria": adatok[1],
                "ev": int(adatok[2]),
                "hossz": int(adatok[3]),
                "ertekeles": float(adatok[4])
            }
            filmek.append(film)
    return filmek


def darabszam(filmek):
    return len(filmek)


def kategoriak_szama(filmek):
    szamlalo = {}
    for film in filmek:
        kat = film["kategoria"]
        szamlalo[kat] = szamlalo.get(kat, 0) + 1
    return szamlalo


def legjobb_legrosszabb(filmek):
    legjobb = filmek[0]
    legrosszabb = filmek[0]
    for film in filmek:
        if film["ertekeles"] > legjobb["ertekeles"]:
            legjobb = film
        if film["ertekeles"] < legrosszabb["ertekeles"]:
            legrosszabb = film
    return legjobb, legrosszabb


def film_keresese(filmek, cim):
    for film in filmek:
        if film["cim"] == cim:
            return film
    return None


def film_fajlba_iras(film, fajlnev):
    with open(fajlnev, "w", encoding="utf-8") as f:
        sor = f"{film['cim']};{film['kategoria']};{film['ev']};{film['hossz']};{film['ertekeles']}"
        f.write(sor)


def kategoriahoz_tartozo(filmek, kategoria):
    talalatok = []
    for film in filmek:
        if film["kategoria"] == kategoria:
            talalatok.append((film["cim"], film["ev"]))
    return talalatok
```

### A főprogram (`feladat3.py`)

```python
import fgv

# 1. Beolvasás
filmek = fgv.beolvasas("filmek.txt")

# 2. Darabszám
print(f"A listában {fgv.darabszam(filmek)} film található.")

# 3. Kategóriánként
szamlalo = fgv.kategoriak_szama(filmek)
for kat, db in szamlalo.items():
    print(f"{kat}: {db} db")

# 4. Legjobb és legrosszabb
legjobb, legrosszabb = fgv.legjobb_legrosszabb(filmek)
print(f"Legjobb: {legjobb['cim']} ({legjobb['ertekeles']})")
print(f"Legrosszabb: {legrosszabb['cim']} ({legrosszabb['ertekeles']})")

# 5. Film keresése
cim = input("Add meg egy film címét: ")
film = fgv.film_keresese(filmek, cim)
if film:
    fgv.film_fajlba_iras(film, "valasztott_film.txt")
    print("A film adatai kiírva a valasztott_film.txt fájlba.")
else:
    print("Nincs ilyen cím a listában")

# 6. Kategória szűrés
kategoria = input("Add meg a kategória nevét: ")
talalatok = fgv.kategoriahoz_tartozo(filmek, kategoria)
for cim, ev in talalatok:
    print(f"{cim} ({ev})")
```
