# Kiegészítő gyakorlatok – 1. hét: Python ismétlés, venv

> Ezek a feladatok a heti házi feladat melletti **extra gyakorlást** szolgálják.
> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz

---

### 1.1 – pip kezelés ⭐
Aktiváld a venv-et, és telepíts 3 csomagot: `httpx`, `python-dotenv`, `rich`. Futtasd a `pip list`-et és `pip freeze > requirements.txt`-t. Távolítsd el a `rich`-et (`pip uninstall`), és generáld újra a `requirements.txt`-t.

### 1.2 – Type hints ⭐
Írj programot, amely demonstrálja a típusjegyzeteket (type hints):
```python
def osszead(a: int, b: int) -> int:
    ...
def koszont(nev: str, formalis: bool = False) -> str:
    ...
def atlag(szamok: list[float]) -> float:
    ...
```
Hívd meg mindegyik függvényt és írd ki az eredményeket.

### 1.3 – List/dict comprehension ⭐⭐
Oldd meg egyetlen sorban (comprehension-nel):
1. A páros számok négyzetei 1-50 között
2. Egy szótár, ahol a kulcs egy szó, az érték a szó hossza: `{"alma": 4, "körte": 5, ...}`
3. Egy szűrt szótár: az eredeti szótárból csak a 4-nél hosszabb kulcsúak

### 1.4 – Dekorátor ⭐⭐
Írj egy `idozit` dekorátort, amely méri és kiírja egy függvény futási idejét. Teszteld egy lassabb függvénnyel (pl. `time.sleep(0.5)` vagy nagy lista rendezése).

### 1.5 – Csomagstruktúra ⭐⭐⭐
Hozd létre a következő csomagstruktúrát:
```
myapp/
├── __init__.py
├── math_utils.py    (osszead, kivon, szoroz)
└── string_utils.py  (fordit, nagybetus, szamol_szavak)
main.py              (importálja és teszteli mindkét modult)
```
A `__init__.py`-ban exportáld a legfontosabb függvényeket, hogy `from myapp import osszead` működjön.
