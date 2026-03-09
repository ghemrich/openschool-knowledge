# 8. hét – Fájlkezelés

> **Dokumentáció:** [W3Schools – Fájlkezelés](https://www.w3schools.com/python/python_file_handling.asp) | [Fájl olvasás](https://www.w3schools.com/python/python_file_open.asp) | [Fájl írás](https://www.w3schools.com/python/python_file_write.asp)

## 15. óra: Fájlból olvasás

### A `with open()` szerkezet

```python
with open("adatok.txt", "r", encoding="utf-8") as f:
    tartalom = f.read()
    print(tartalom)
```

### Soronkénti olvasás

```python
with open("adatok.txt", "r", encoding="utf-8") as f:
    for sor in f:
        print(sor.strip())  # .strip() eltávolítja a sortörést
```

### `.split()` – sor darabolása

Ha a fájl pontosvesszővel tagolt:
```
Kiss Anna;16;Budapest
Nagy Béla;17;Debrecen
```

```python
with open("tanulok.txt", "r", encoding="utf-8") as f:
    for sor in f:
        adatok = sor.strip().split(";")
        nev = adatok[0]
        kor = int(adatok[1])
        varos = adatok[2]
        print(f"{nev} ({kor} éves) – {varos}")
```

### Gyakorlat: Szövegfájl beolvasása

```python
# Olvassuk be a fájlt, és számoljuk meg a sorokat
sorok_szama = 0

with open("szoveg.txt", "r", encoding="utf-8") as f:
    for sor in f:
        sorok_szama += 1
        print(f"{sorok_szama}. sor: {sor.strip()}")

print(f"\nÖsszesen {sorok_szama} sor.")
```

---

## 16. óra: Fájlba írás

### Fájl megnyitása írásra

```python
with open("kimenet.txt", "w", encoding="utf-8") as f:
    f.write("Ez az első sor.\n")
    f.write("Ez a második sor.\n")
```

> **Figyelem:** `"w"` mód felülírja a fájlt! Ha hozzáfűzni akarunk: `"a"`

### Lista mentése fájlba

```python
nevek = ["Anna", "Béla", "Csaba"]

with open("nevek.txt", "w", encoding="utf-8") as f:
    for nev in nevek:
        f.write(nev + "\n")

print("Fájl sikeresen létrehozva!")
```

### Gyakorlat: Beolvasás és visszaírás

```python
# 1. Beolvasás listába
tanulok = []
with open("tanulok.txt", "r", encoding="utf-8") as f:
    for sor in f:
        adatok = sor.strip().split(";")
        tanulok.append(adatok)

# 2. Egy kiválasztott tanuló fájlba írása
keresett = input("Kit keresünk? ")
with open("eredmeny.txt", "w", encoding="utf-8") as f:
    for tanulo in tanulok:
        if tanulo[0] == keresett:
            f.write(";".join(tanulo))
            print("Adat kiírva a fájlba!")
```
