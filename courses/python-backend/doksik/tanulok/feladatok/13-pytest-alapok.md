# Feladatok – 13. hét: pytest alapok

> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz
> A megoldásokat commitold és pushold a GitHub repódba.

---

### 13.1 – Első tesztek ⭐
Hozz létre `tests/test_alapok.py` fájlt. Írj 5 egyszerű tesztet `assert`-tel: egyenlőség, tartalmazás, típus, hossz, negáció.

### 13.2 – Függvény tesztelés ⭐
Írj egy `utils.py` modult `osszead`, `kivon`, `szoroz` függvényekkel. Írj mindegyikhez 2-2 tesztet (pozitív és negatív számokkal).

### 13.3 – Fixture ⭐⭐
Készíts fixture-t (`minta_adatok`), amely egy dictionary-t ad vissza (nev, kor, email). Használd 3 különböző tesztben.

### 13.4 – Kivétel tesztelés ⭐⭐
Írj `osztas(a, b)` függvényt, amely `ValueError`-t dob nullával osztásnál. Teszteld `pytest.raises`-zel, és ellenőrizd a hibaüzenetet is (`match=`).

### 13.5 – Parametrize ⭐⭐
Írj `@pytest.mark.parametrize` tesztet egy `faktoriális(n)` függvényhez legalább 5 bemenettel (0!, 1!, 5!, 10!, negatív szám → ValueError).

### 13.6 – conftest.py ⭐⭐⭐
Hozz létre `tests/conftest.py`-t legalább 3 fixture-rel. Használd őket különböző tesztfájlokban. Ellenőrizd, hogy a fixture-ök automatikusan elérhetők.
