# 13. hét – pytest alapok

> **Beadás:** commitold és pushold a megoldásaidat ebbe a repóba!
> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz

---

Ezen a héten megismerkedsz a pytest keretrendszerrel és megírod az első tesztjeidet. Az automatikus tesztelés biztosítja, hogy a kódod a várt módon működik, és a változtatások nem törnek el meglévő funkciókat.

---

## 13.1 – Alap tesztek ⭐
Hozz létre `utils.py` fájlt a következő függvényekkel:
- `osszead(a, b)` → a + b
- `kivon(a, b)` → a - b
- `szoroz(a, b)` → a * b

Az automatikus tesztelés ellenőrzi a függvényeidet (rejtett tesztek).

## 13.2 – Osztás és kivétel ⭐⭐
Adj hozzá `osztas(a, b)` függvényt a `utils.py`-hoz. Ha `b == 0`, dobj `ValueError`-t "Nullával nem lehet osztani" üzenettel. A tesztek ellenőrzik.

## 13.3 – Lista műveletek ⭐⭐
Adj hozzá a `utils.py`-hoz:
- `atlag(lista)` → lista átlaga (üres lista → ValueError)
- `egyedi(lista)` → egyedi elemek listája

## 13.4 – Szótár műveletek ⭐⭐⭐
Adj hozzá:
- `leggyakoribb(lista)` → a leggyakoribb elem
- `szavak_szama(szoveg)` → szótár, ahol a kulcs a szó, az érték az előfordulás

---

## Automatikus tesztelés

A megoldásodat rejtett tesztek ellenőrzik automatikusan a push után (GitHub Classroom Autograding). Helyi teszteléshez írj saját teszteket:
```bash
pip install pytest
pytest -v
```

## Dokumentáció

- [pytest](https://docs.pytest.org/)
- [pytest assert](https://docs.pytest.org/en/stable/how-to/assert.html)
- [pytest.raises](https://docs.pytest.org/en/stable/how-to/assert.html#assertions-about-expected-exceptions)

## 📚 Kapcsolódó anyagok

Az ehhez a héthez tartozó elméleti anyagot és további gyakorlófeladatokat itt találod:

- 📖 [Lecke: pytest alapok](https://github.com/ghemrich/openschool-knowledge/blob/master/courses/python-backend/leckek/13-pytest-alapok.md)

## Beadás

1. `utils.py` legyen a repó gyökerében
2. A push után a rejtett tesztek automatikusan futnak
3. Commitolj értelmes üzenetekkel
4. `git push` – ez a beadás!
