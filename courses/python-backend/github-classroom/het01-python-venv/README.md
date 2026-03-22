# 1. hét – Python ismétlés, virtuális környezet

> **Beadás:** commitold és pushold a megoldásaidat ebbe a repóba!
> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz

---

Ezen a héten átismétled a Python alapokat és megismerkedsz a virtuális környezetekkel (`venv`). A venv biztosítja, hogy minden projekt a saját függőségeivel dolgozzon – ez professzionális fejlesztésben alapvető.

---

## 1.1 – Virtuális környezet ⭐
Hozz létre virtuális környezetet (`venv`), aktiváld, telepítsd a `requests` csomagot. Készíts `requirements.txt` fájlt (`pip freeze`). A `venv/` mappa **ne** kerüljön a repóba (`.gitignore`).

## 1.2 – Típusok és változók ⭐
Írj programot (`feladat2.py`), amely létrehoz 8 különböző típusú változót (int, float, str, bool, list, dict, tuple, set) és kiírja mindegyik értékét és típusát.

## 1.3 – Szótár feldolgozás ⭐⭐
Írj programot (`feladat3.py`), amely egy szótárban 5 tanuló nevét és jegyét tárolja. Írja ki az átlagot, a legjobb tanulót és rendezze a neveket ábécé sorrendben.

## 1.4 – Fájl feldolgozás ⭐⭐
Írj programot (`feladat4.py`), amely beolvassa az `input.txt` fájlt, megszámolja a sorok, szavak és karakterek számát, és kiírja az eredményt. Hozd létre az `input.txt` fájlt is legalább 5 sorral.

## 1.5 – Modul készítés ⭐⭐⭐
Készíts egy `utils.py` modult `atlag(lista)`, `maximum(lista)`, `minimum(lista)` függvényekkel. A `main.py` importálja és hívja meg mindhárom függvényt tesztadatokkal.

---

## Dokumentáció

- [Python venv](https://docs.python.org/3/library/venv.html)
- [Python dict](https://www.w3schools.com/python/python_dictionaries.asp)
- [Python file handling](https://www.w3schools.com/python/python_file_handling.asp)

## 📚 Kapcsolódó anyagok

Az ehhez a héthez tartozó elméleti anyagot és további gyakorlófeladatokat itt találod:

- 📖 [Lecke: Python, venv, pip](https://github.com/ghemrich/openschool-knowledge/blob/master/courses/python-backend/leckek/01-python-venv.md)

## Beadás

1. Minden feladatot külön `.py` fájlba írj
2. A `requirements.txt` legyen benne a repóban
3. Commitolj értelmes üzenetekkel
4. `git push` – ez a beadás!
