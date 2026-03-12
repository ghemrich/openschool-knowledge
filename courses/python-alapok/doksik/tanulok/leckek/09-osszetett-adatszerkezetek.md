# 9. hét – Összetett adatszerkezetek

> **Dokumentáció:** [W3Schools – Szótárak](https://www.w3schools.com/python/python_dictionaries.asp) | [Beágyazott listák](https://www.w3schools.com/python/python_lists_access.asp)

## 17. óra: Lista listája

### Mi az a lista listája?
Olyan lista, amelynek minden eleme szintén egy lista.

```python
tanulok = [
    ["Kiss Anna", 16, "Budapest"],
    ["Nagy Béla", 17, "Debrecen"],
    ["Tóth Csaba", 16, "Szeged"]
]
```

### Hozzáférés

```python
print(tanulok[0])       # ["Kiss Anna", 16, "Budapest"]
print(tanulok[0][0])    # Kiss Anna
print(tanulok[1][2])    # Debrecen
```

### Fájlból beolvasás lista listába

```python
filmek = []

with open("filmek.txt", "r", encoding="utf-8") as f:
    for sor in f:
        adatok = sor.strip().split(";")
        # Típuskonverzió!
        adatok[2] = int(adatok[2])    # év
        adatok[3] = int(adatok[3])    # hossz
        adatok[4] = float(adatok[4])  # értékelés
        filmek.append(adatok)

# Használat
print(filmek[0][0])  # Első film címe
print(filmek[0][4])  # Első film értékelése
```

---

## 18. óra: Szótárak és szótárak listája

### Szótár (`dict`) alapok

```python
tanulo = {
    "nev": "Kiss Anna",
    "kor": 16,
    "varos": "Budapest"
}

print(tanulo["nev"])    # Kiss Anna
print(tanulo["kor"])    # 16
```

### Szótárak listája
Sokkal olvashatóbb, mint a lista listája!

```python
filmek = [
    {"cim": "Film A", "kategoria": "akció", "ev": 2020, "ertekeles": 7.5},
    {"cim": "Film B", "kategoria": "dráma", "ev": 2019, "ertekeles": 8.2}
]

# Hozzáférés
print(filmek[0]["cim"])       # Film A
print(filmek[1]["ertekeles"]) # 8.2
```

### Beolvasás szótárak listájába

```python
filmek = []

with open("filmek.txt", "r", encoding="utf-8") as f:
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

# Sokkal olvashatóbb!
for film in filmek:
    print(f"{film['cim']} ({film['ev']}) - {film['ertekeles']}")
```

### Összehasonlítás

| | Lista listája | Szótárak listája |
|---|---|---|
| Hozzáférés | `film[0]` | `film["cim"]` |
| Olvashatóság | Nehezebb | Könnyebb |
| Memória | Kevesebb | Több |
| Vizsgán | Elfogadott | Elfogadott |
