# 📘 Lecke 01 – Python ismétlés, virtuális környezet

> 📚 Dokumentáció:  
> https://docs.python.org/3/library/venv.html ·  
> https://pip.pypa.io/en/stable/ ·  
> https://docs.python.org/3/tutorial/

---

# 7–8. óra: Python ismétlés

## 📝 Változók és típusok

```python
nev = "Anna"           # str
kor = 25               # int
atlag = 4.5            # float
aktiv = True           # bool
```

### 🧠 Részletes Magyarázat

**Típusok emlékeztető:**
| Típus | Leírás | Példa |
|-------|--------|-------|
| `str` | Szöveg | `"Helló"`, `'Anna'` |
| `int` | Egész szám | `42`, `-5`, `0` |
| `float` | Tizedes szám | `3.14`, `-2.5` |
| `bool` | Logikai érték | `True`, `False` |

A backend fejlesztésben a **type hint** (típusmegjelölés) nagyon fontos lesz – a FastAPI erre épül.

---

## 🔀 Vezérlési szerkezetek

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

### 🧠 Részletes Magyarázat

Ezek az alapok a Python-alapok kurzusból. A backend fejlesztésben leggyakrabban a `for` ciklusokat és `if` elágazásokat fogjuk használni – adatok szűrésére, validálására és feldolgozására.

---

## 🔧 Függvények

```python
def koszontes(nev: str) -> str:
    return f"Szia, {nev}!"

eredmeny = koszontes("Anna")
print(eredmeny)  # Szia, Anna!
```

### 🧠 Részletes Magyarázat

**Type hints** – A Python-alapok kurzusban nem volt kötelező, de a backend fejlesztésben IGEN:
- `nev: str` → a `nev` paraméter szöveg típusú
- `-> str` → a függvény szöveget ad vissza

```python
def osszead(a: int, b: int) -> int:
    return a + b
```

A type hint NEM kényszeríti ki a típust futáskor, de a **FastAPI használja** a validációhoz és a dokumentáció generáláshoz.

---

## 📕 Szótárak

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

### 🧠 Részletes Magyarázat

A szótár a backend fejlesztés LEGFONTOSABB adatszerkezete, mert a **JSON formátum** (amit az API-k használnak) pontosan megfelel a Python szótárnak:

```python
# Python szótár:
{"nev": "Anna", "kor": 25}

# JSON (amit az API küld/fogad):
{"nev": "Anna", "kor": 25}
```

Szinte teljesen ugyanaz a szintaxis – ez teszi a Pythont ideálissá API fejlesztésre.

---

## 📂 Fájlkezelés gyorsismétlés

```python
# Olvasás
with open("adat.txt", "r", encoding="utf-8") as f:
    for sor in f:
        print(sor.strip())

# Írás
with open("kimenet.txt", "w", encoding="utf-8") as f:
    f.write("Helló, világ!\n")
```

### 🧠 Részletes Magyarázat

A `with open()` minta ismerős a Python-alapok kurzusból. A backend fejlesztésben is használjuk majd – konfigurációs fájlok olvasásánál, logolásánál, és fájlfeltöltéseknél.

---

# 9–10. óra: Virtuális környezetek

## 🏠 Mi a virtuális környezet?

Minden Python projektnek lehetnek különböző csomagfüggőségei. A virtuális környezet egy **elszigetelt Python telepítés**, ami csak az adott projekthez tartozik.

| Fogalom | Leírás |
|---------|--------|
| `venv` | Python beépített virtuális környezet kezelő |
| `pip` | Python csomagkezelő |
| `requirements.txt` | Projekt függőségek listája |

### 🧠 Részletes Magyarázat

**Miért kell virtuális környezet?**

Képzeld el: az A projekted FastAPI 0.100-at használ, a B projekted FastAPI 0.110-et. Ha globálisan telepíted, az egyik mindig összeomlik! A virtuális környezet megoldja:

```
📁 A projekt/
  └── venv/ → FastAPI 0.100 (csak ide telepítve)

📁 B projekt/
  └── venv/ → FastAPI 0.110 (csak ide telepítve)
```

Mindkét projekt a saját csomagjait használja, nincs ütközés.

---

## ⚙️ Létrehozás és aktiválás

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

### 🧠 Részletes Magyarázat

**python3 -m venv venv** – A `python3 -m venv` a parancs, a második `venv` a mappa neve. Konvenció szerint `venv`-nek nevezzük, de bármi lehetne.

**Aktiválás után** a prompt elejére kikerül a `(venv)` felirat:
```
(venv) user@gep:~/projekt$
```

Ez jelzi, hogy az elszigetelt környezetben dolgozol. Minden `pip install` ide telepít, nem a globális Pythonba.

**deactivate** – Kilép a virtuális környezetből. Ezután a globális Python-t használod megint.

---

## 📦 Csomagok telepítése

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

### 🧠 Részletes Magyarázat

**pip install** – Letölti és telepíti a csomagot a PyPI (Python Package Index) adatbázisból.

**pip freeze > requirements.txt** – Kilistázza az összes telepített csomagot a verziószámokkal, és egy fájlba menti:
```
fastapi==0.110.0
uvicorn==0.29.0
pydantic==2.6.3
```

**pip install -r requirements.txt** – Telepíti az összes csomagot a fájlból. Ezt használja a csapatod (vagy a szerver), amikor klónozzák a projektet:
```bash
git clone <repo>
cd projekt
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt  # Minden csomag települ!
```

---

## 🚫 .gitignore beállítása

A `venv/` mappát **soha ne commitold**! Add hozzá a `.gitignore`-hoz:

```
venv/
__pycache__/
*.pyc
.env
```

### 🧠 Részletes Magyarázat

**Miért ne commitoljuk a venv/-t?**
- Több száz MB méretű lehet
- Operációs-rendszertől függ (Linux/Mac/Windows más binárisokat tartalmaz)
- A `requirements.txt` elegendő – bárki újra tudja telepíteni

**__pycache__/** – Python automatikusan létrehozza a `.pyc` (compiled) fájlokat. Ezek feleslegesek a Git-ben.

**.env** – Titkos beállításokat (jelszavak, API kulcsok) tartalmaz. SOHA ne kerüljön a repóba!

---

# 11–12. óra: Projektstruktúra

## 📁 Python csomagok és modulok

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

### 🧠 Részletes Magyarázat

**__init__.py** – Ez az üres fájl jelöli, hogy az `app/` mappa egy Python **csomag** (package). Nélküle nem tudnánk importálni belőle.

**Importálás csomagból:**
```python
# app/utils.py
def koszontes(nev: str) -> str:
    return f"Szia, {nev}!"

# app/main.py
from app.utils import koszontes
print(koszontes("Anna"))
```

**from app.utils import koszontes** – A `from` kulcsszóval a csomag egy konkrét függvényét importáljuk. Ez olvashatóbb, mint az `import fgv` + `fgv.koszontes()` minta, amit a Python-alapok kurzusban tanultunk.

---

## ✏️ Gyakorlat

1. Hozz létre egy `het01` mappát
2. Készíts virtuális környezetet: `python3 -m venv venv` (Windows: `python -m venv venv`)
3. Aktiváld: `source venv/bin/activate` (Windows: `venv\Scripts\activate`)
4. Telepíts egy csomagot: `pip install requests`
5. Mentsd a függőségeket: `pip freeze > requirements.txt`
6. Hozd létre a `.gitignore` fájlt a megfelelő bejegyzésekkel
7. Commitold és pushold
