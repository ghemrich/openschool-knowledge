# Kiegészítő gyakorlatok – 13. hét: pytest alapok

> Ezek a feladatok a heti házi feladat melletti **extra gyakorlást** szolgálják.
> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz

---

### 13.1 – Szöveges tesztek ⭐
Írj teszteket egy `szoveg_utils.py` modulhoz: `nagybetus(s)`, `szamol_maganhangzo(s)`, `palindrom_e(s)`. Mindegyikhez legalább 3 teszt eset (normál, üres string, speciális karakterek).

### 13.2 – Lista tesztek ⭐
Készíts `lista_utils.py` modult: `egyedi(lista)`, `laposit(lista_lista)`, `csoportosit(lista, meret)`. Például `csoportosit([1,2,3,4,5], 2)` → `[[1,2],[3,4],[5]]`. Írj teszteket mindegyikhez.

### 13.3 – Fixture öröklődés ⭐⭐
Készíts `conftest.py`-t fixture-ökkel: `minta_konyvek` (lista 5 könyvvel), `ures_lista`, `temp_fajl` (tmp_path-ot használ). Használd őket különböző tesztfájlokban anélkül, hogy importálnád.

### 13.4 – Boundary tesztelés ⭐⭐
Készíts `kor_kategoria(kor: int) -> str` függvényt (gyerek: 0-13, tinédzser: 14-17, felnőtt: 18-64, idős: 65+; negatív → ValueError). Írj `parametrize` teszteket a határértékekre: -1, 0, 13, 14, 17, 18, 64, 65, 100.

### 13.5 – Fixture scope ⭐⭐⭐
Készíts fixture-öket különböző scope-okkal:
- `scope="function"` – minden tesztnél új
- `scope="module"` – modulonként egyszer
- `scope="session"` – a teljes tesztfutásban egyszer

Adj `print()` hívást mindegyik fixture-be és futtasd `pytest -s`-sel. Figyeld meg, hányszor hívódnak meg.
