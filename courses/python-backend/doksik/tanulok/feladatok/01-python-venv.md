# Feladatok – 1. hét: Python ismétlés, venv

> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz
> A megoldásokat commitold és pushold a GitHub repódba.

---

### 1.1 – Venv létrehozás ⭐
Hozz létre egy új projektet `het01` néven. Készíts benne virtuális környezetet, aktiváld, és telepíts egy csomagot (pl. `requests`). Generálj `requirements.txt` fájlt.

### 1.2 – Python alaptípusok ⭐
Írj programot, amely létrehoz legalább 8 változót (int, float, str, bool, list, dict, tuple, set), és kiírja mindegyik típusát a `type()` függvénnyel.

### 1.3 – Szótár műveletek ⭐⭐
Hozz létre egy szótárat, amely 5 tanuló nevét és jegyét tartalmazza. Írd ki az átlagot, a legjobb és legrosszabb jegyet, és a tanulók nevét ábécé sorrendben.

### 1.4 – Fájl feldolgozás ⭐⭐
Írj programot, amely beolvas egy szöveges fájlt (soronként), megszámolja a sorokat, szavakat és karaktereket, majd kiírja az eredményt. Hozd létre a bemeneti fájlt is.

### 1.5 – Projekt struktúra ⭐⭐
Hozd létre a következő struktúrát: `app/` mappa `__init__.py`-vel, `main.py` a gyökérben ami importál az `app` csomagból. A `requirements.txt` tartalmazza a függőségeket. Adj hozzá `.gitignore`-t.

### 1.6 – Függvények és listák ⭐⭐⭐
Írj egy modult (`utils.py`) amely tartalmazza a következő függvényeket: `atlag(lista)`, `medián(lista)`, `leggyakoribb(lista)`. Teszteld mindhárom függvényt a `main.py`-ból különböző listákkal.
