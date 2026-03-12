# Lecke 01 – Python ismétlés, virtuális környezet

> **Dokumentáció:** [Python venv](https://docs.python.org/3/library/venv.html) · [pip](https://pip.pypa.io/en/stable/) · [Python tutorial](https://docs.python.org/3/tutorial/)

---

## 7–8. óra: Python ismétlés

### Változók és típusok

```python
nev = "Anna"           # str
kor = 25               # int
atlag = 4.5            # float
aktiv = True           # bool
```

### Vezérlési szerkezetek

```python
# Feltétel
if kor >= 18:
    print("Felnőtt")
elif kor >= 14:
    print("Tinédzser")
else:
    print("Gyerek")

# Ciklus
for i in range(5):
    print(i)

szamok = [1, 2, 3, 4, 5]
for szam in szamok:
    print(szam * 2)
```

### Függvények

```python
def koszontes(nev: str) -> str:
    return f"Szia, {nev}!"

eredmeny = koszontes("Anna")
print(eredmeny)  # Szia, Anna!
```

### Szótárak

```python
felhasznalo = {
    "nev": "Kiss Anna",
    "kor": 25,
    "email": "anna@example.com"
}

print(felhasznalo["nev"])          # Kiss Anna
felhasznalo["telefon"] = "06301234567"

for kulcs, ertek in felhasznalo.items():
    print(f"{kulcs}: {ertek}")
```

### Fájlkezelés gyorsismétlés

```python
# Olvasás
with open("adat.txt", "r", encoding="utf-8") as f:
    for sor in f:
        print(sor.strip())

# Írás
with open("kimenet.txt", "w", encoding="utf-8") as f:
    f.write("Helló, világ!\n")
```

---

## 9–10. óra: Virtuális környezetek

### Mi a virtuális környezet?

Minden Python projektnek lehetnek különböző csomagfüggőségei. A virtuális környezet egy **elszigetelt Python telepítés**, ami csak az adott projekthez tartozik.

| Fogalom | Leírás |
|---------|--------|
| `venv` | Python beépített virtuális környezet kezelő |
| `pip` | Python csomagkezelő |
| `requirements.txt` | Projekt függőségek listája |

### Létrehozás és aktiválás

```bash
# Virtuális környezet létrehozása
python3 -m venv venv          # Linux/Mac
python -m venv venv           # Windows

# Aktiválás
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows (PowerShell / cmd)

# Deaktiválás
deactivate
```

Aktiválás után a prompt elejére kikerül a `(venv)` felirat:

```
(venv) user@gep:~/projekt$
```

### Csomagok telepítése

```bash
# Csomag telepítése
pip install fastapi

# Telepített csomagok listája
pip list

# Függőségek mentése fájlba
pip freeze > requirements.txt

# Függőségek telepítése fájlból
pip install -r requirements.txt
```

### .gitignore beállítása

A `venv/` mappát **soha ne commitold**! Add hozzá a `.gitignore`-hoz:

```
venv/
__pycache__/
*.pyc
.env
```

---

## 11–12. óra: Projektstruktúra

### Python csomagok és modulok

```
projekt/
├── app/
│   ├── __init__.py      # Csomag jelölő (üres fájl)
│   ├── main.py          # Fő alkalmazás
│   └── utils.py         # Segédfüggvények
├── requirements.txt
├── .gitignore
└── README.md
```

Az `__init__.py` fájl jelöli, hogy a mappa Python csomag:

```python
# app/utils.py
def koszontes(nev: str) -> str:
    return f"Szia, {nev}!"

# app/main.py
from app.utils import koszontes
print(koszontes("Anna"))
```

---

## Gyakorlat

1. Hozz létre egy `het01` mappát
2. Készíts virtuális környezetet: `python3 -m venv venv` (Windows: `python -m venv venv`)
3. Aktiváld: `source venv/bin/activate` (Windows: `venv\Scripts\activate`)
4. Telepíts egy csomagot: `pip install requests`
5. Mentsd a függőségeket: `pip freeze > requirements.txt`
6. Hozd létre a `.gitignore` fájlt a megfelelő bejegyzésekkel
7. Commitold és pushold
