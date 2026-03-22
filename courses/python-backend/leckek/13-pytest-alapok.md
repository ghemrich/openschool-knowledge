# 📘 Lecke 13 – pytest alapok

> 📚 Dokumentáció:
> https://docs.pytest.org/
> https://docs.pytest.org/en/stable/how-to/fixtures.html
> https://docs.pytest.org/en/stable/how-to/assert.html

---

## 79–80. óra: Tesztelés alapjai

### Miért tesztelünk?

- A kód **helyességét** bizonyítjuk automatikusan
- Megvéd a **regressziótól** (ami működött, az ne romoljon el)
- GitHub Classroom is **pytest**-tel ellenőrzi a beadott feladatokat

### pytest telepítése

```bash
pip install pytest
pip freeze > requirements.txt
```

### 🧠 Részletes Magyarázat

- **pytest** – A Python legnépszerűbb tesztelési keretrendszere. Egyszerűbb, mint a beépített `unittest`: nem kell osztályokat írni, elég sima függvényeket. Automatikusan megtalálja a `test_` prefixű fájlokat és függvényeket.
- **Miért nem `unittest`?** – A pytest rövídebb, olvashatóbb szintaxist ad. Az `assert` egy sor, míg az `unittest`-ben `self.assertEqual(a, b)` kell. A pytest fixture rendszere is rugalmasabb.

### Első teszt

```python
# tests/test_matek.py

def osszead(a, b):
    return a + b

def test_osszead():
    assert osszead(2, 3) == 5

def test_osszead_negativ():
    assert osszead(-1, 1) == 0

def test_osszead_nulla():
    assert osszead(0, 0) == 0
```

### 🧠 Részletes Magyarázat

- **`test_` prefix** – A pytest konvenciója: minden tesztfüggvény neve `test_`-tel kezdődik. A tesztfájlok neve `test_`-tel kezdődik vagy `_test`-re végződik. Ha nem tartod be, a pytest nem találja meg.
- **`assert`** – Python beépített kulcsszó. Ha az utána lévő kifejezés `False`, `AssertionError` keletkezik és a teszt elbukik. A pytest kibővíti az `assert`-et: hiba esetén részletes összehasonlítást mutat (melyik érték mit volt).
- **Elnevezés fontossága** – A tesztfüggvény neve leírja, mit tesztelünk: `test_osszead_negativ` egyértelműen jelzi, hogy negatív számokkal tesztelünk. Bukásnál a név azonnal mutatja a problémát.

```bash
pytest
pytest -v          # részletes kimenet
pytest -v -s       # print() is látszik
```

### 🧠 Részletes Magyarázat

| Flag | Jelentés |
|------|----------|
| (nincs) | Tömör eredmény: `.` = sikeres, `F` = bukott |
| `-v` | **V**erbose: minden teszt neve és eredménye kiírva |
| `-s` | A `print()` kimenetet is mutatja (alapból elnyomja) |
| `-v -s` | Kombinálható: részletes + print |

### assert részletesen

```python
def test_assert_peldak():
    assert 1 + 1 == 2                     # egyenlőség
    assert "alma" in ["alma", "körte"]     # tartalmazás
    assert len([1, 2, 3]) == 3            # hossz
    assert isinstance(42, int)             # típus
    assert not False                       # negáció
```

### 🧠 Részletes Magyarázat

Az `assert` után bármilyen Python kifejezés állhat, ami `True` vagy `False` értékű:

| Assert típus | Mit ellenőriz | Bukás üzenet példa |
|-------------|---------------|-------------------|
| `assert a == b` | Egyenlőség | `assert 3 == 5` → `3 != 5` |
| `assert x in lista` | Elem benne van | `assert "banán" in ["alma"]` |
| `assert len(x) == n` | Méret/hossz | `assert 2 == 3` |
| `assert isinstance(x, T)` | Típus ellenőrzés | `False` |
| `assert not x` | Hamis-e | `assert not True` |

A pytest az `assert` hiba esetén automatikusan megmutatja a bal és jobb oldal értékét – nem kell kézzel hibaüzenetet írni.

### Kivétel tesztelése

```python
import pytest

def osztas(a, b):
    if b == 0:
        raise ValueError("Nullával nem lehet osztani")
    return a / b

def test_osztas_nullaval():
    with pytest.raises(ValueError, match="Nullával"):
        osztas(10, 0)
```

### 🧠 Részletes Magyarázat

- **`pytest.raises(ValueError)`** – Kontextuskezelő, ami ellenőrzi, hogy a blokkon belül a megadott típusú kivétel keletkezik. Ha **nem** dob kivételt, a teszt **elbukik** (mert azt vártuk, hogy hibázik).
- **`match="Nullával"`** – Opcionális: a hibaüzenet szövegét is ellenőrzi (regex mintával). Ha a kivétel szövege nem tartalmazza a „Nullával" szót, a teszt bukik.
- **Mikor használjuk?** – Amikor azt akarjuk bizonyítani, hogy a kód **helyesen hibázik**. Pl. érvénytelen input esetén a megfelelő kivételt dobja-e?

---

## 81–82. óra: Fixtures és struktúra

### Mi a fixture?

A **fixture** egy előkészítő függvény, amit a tesztek automatikusan megkapnak paraméterként:

```python
import pytest

@pytest.fixture
def minta_lista():
    return [1, 2, 3, 4, 5]

def test_lista_hossz(minta_lista):
    assert len(minta_lista) == 5

def test_lista_osszeg(minta_lista):
    assert sum(minta_lista) == 15
```

### 🧠 Részletes Magyarázat

- **Fixture** – Tesztadatot vagy erőforrást előkészítő függvény. A `@pytest.fixture` dekorátor jelöli. A tesztfüggvény **paraméterében** a fixture nevét adja meg, és a pytest automatikusan meghívja és átadja az értéket.
- **Miért jó?** – (1) Nem kell minden tesztben copy-paste-elni az előkészítő kódot. (2) Ha változik a minta adat, csak egy helyen kell módosítani. (3) A fixture-ök láncolhatók (`fixture_a` használhat `fixture_b`-t).
- **Automatikus injection** – A pytest a paraméter **neve** alapján találja meg a fixture-t. Ha a teszt paramétere `minta_lista`, a pytest megkeresi a `minta_lista` nevű fixture-t és meghívja.

### Fixture scope

```python
@pytest.fixture(scope="module")    # egyszer fut le a modul összes tesztjéhez
def db_connection():
    conn = create_connection()
    yield conn                      # yield után: cleanup
    conn.close()
```

### 🧠 Részletes Magyarázat

- **`yield` a fixture-ben** – A `yield` előtti rész az **előkészítés** (setup), a `yield` utáni rész a **takarítás** (teardown). A `yield conn` átadja a `conn`-t a tesztnek, a teszt lefut, majd a `conn.close()` végrehajtódik. Ez analóg a `try...finally` mintával.

| Scope | Életciklus | Mikor használjuk |
|-------|-----------|-----------------|
| `function` | Minden teszthez újra (alapértelmezett) | Minta adatok |
| `class` | Osztályonként egyszer | Közös setup egy tesztosztályhoz |
| `module` | Fájlonként egyszer | Drága erőforrás (pl. DB kapcsolat) |
| `session` | Teljes teszt futáshoz egyszer | Alkalmazás szintű inicializáció |

- **Scope választás** – Minél szűkebb a scope, annál jobban izoláltak a tesztek (kevesebb mellékhatás). De drága műveleteknél (adatbázis kapcsolat) érdemes `module` vagy `session` scope-ot használni a sebesség érdekében.

### conftest.py

A `conftest.py` fájlban definiált fixture-ök **automatikusan** elérhetők minden tesztfájlban:

```python
# tests/conftest.py
import pytest

@pytest.fixture
def minta_felhasznalo():
    return {
        "nev": "Teszt Elek",
        "email": "teszt@example.com",
        "jelszo": "titkosjelszo123"
    }
```

```python
# tests/test_users.py
def test_felhasznalo_nev(minta_felhasznalo):
    assert minta_felhasznalo["nev"] == "Teszt Elek"
```

### 🧠 Részletes Magyarázat

- **`conftest.py`** – Speciális pytest fájl (a név rögzített, nem változtatható). A benne lévő fixture-öket **nem kell importálni** – a pytest automatikusan megtalálja és elérhetővé teszi az összes tesztfájlban, ami ugyanabban a mappában (vagy almappákban) van.
- **Hierarchia** – Több `conftest.py` is lehet: a `tests/conftest.py` az összes tesztre hat, de egy `tests/api/conftest.py` csak az `api/` almappára. A szűkebb felülírhatja a tágabbat.
- **Tipikus tartalom** – Minta adatok, adatbázis beállítás, TestClient létrehozás, autentikáció fixture.

---

## 83–84. óra: Tesztszervezés és paraméterezés

### Projekt struktúra tesztekkel

```
projekt/
├── app/
│   ├── __init__.py
│   ├── main.py
│   └── ...
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_matek.py
│   └── test_users.py
├── requirements.txt
└── pytest.ini
```

### pytest.ini

```ini
[pytest]
testpaths = tests
python_files = test_*.py
python_functions = test_*
```

### 🧠 Részletes Magyarázat

- **`pytest.ini`** – A pytest konfigurációs fájlja a projekt gyökerében. Beállítja, hol keresse a teszteket és milyen nevű fájlokat/függvényeket tekintsen tesztnek.
- **`testpaths = tests`** – Csak a `tests/` mappában keres teszteket (nem az egész projektben).
- **`python_files = test_*.py`** – Csak a `test_`-tel kezdődő fájlokat tekinti tesztfájlnak.
- **`python_functions = test_*`** – Csak a `test_`-tel kezdődő függvényeket tekinti tesztnek.

### Parametrize – egy teszt, több adat

```python
import pytest

def dupla(n):
    return n * 2

@pytest.mark.parametrize("bemenet, vart", [
    (1, 2),
    (3, 6),
    (0, 0),
    (-5, -10),
])
def test_dupla(bemenet, vart):
    assert dupla(bemenet) == vart
```

### 🧠 Részletes Magyarázat

- **`@pytest.mark.parametrize`** – Dekorátor, ami egyetlen tesztfüggvényt **többször** futtat különböző adatokkal. Az eredmény 4 külön teszt a kimenetben (mindegyik saját név+adatpárral).
- **Szintaxis:** `parametrize("param1, param2", [(val1, val2), (val3, val4)])` – az első string a paraméternevek vesszővel elválasztva, a második a lista az értékpárokkal.
- **Előny** – Egyetlen tesztfüggvénnyel 4 (vagy 100) esetet tesztelünk. Ha egy eset bukik, pontosan látjuk melyik (pl. `test_dupla[-5--10] FAILED`). Sokkal jobb, mint 4 különálló tesztfüggvény.

### Tesztek csoportosítása osztályokkal

```python
class TestOsszead:
    def test_pozitiv(self):
        assert osszead(2, 3) == 5

    def test_negativ(self):
        assert osszead(-1, -2) == -3
```

### 🧠 Részletes Magyarázat

- **`class Test*`** – A pytest az osztályneveket is automatikusan felismeri, ha `Test`-tel kezdődnek. Az osztályon belüli `test_*` metódusok lesznek a tesztek.
- **`self`** – Kötelező első paraméter (Python osztálymetódus), de a pytest nem használja – nem kell semmit beállítani rajta.
- **Mikor használjunk osztályt?** – Ha logikailag összetartozó teszteket akarunk csoportosítani. A `-v` kimenetben `TestOsszead::test_pozitiv` formában jelennek meg.

### Tesztek futtatása szelektíven

```bash
pytest tests/test_matek.py              # egy fájl
pytest tests/test_matek.py::test_dupla  # egy teszt
pytest -k "negativ"                      # név alapján szűrés
pytest --tb=short                        # rövid traceback
```

### 🧠 Részletes Magyarázat

| Parancs | Mit csinál |
|---------|-----------|
| `pytest tests/test_matek.py` | Csak egy fájl tesztjei futnak |
| `pytest ...::test_dupla` | Egyetlen konkrét teszt futtatása |
| `pytest -k "negativ"` | Minden teszt, aminek a neve tartalmazza a „negativ" szót |
| `pytest --tb=short` | Rövid traceback: csak a hiba helye, nem a teljes stack |
| `pytest -x` | Első hiba után megáll (hasznos hibakeresésnél) |
| `pytest --lf` | Csak a **l**ast **f**ailed teszteket futtatja újra |

---

## Gyakorlat

1. Hozz létre egy `tests/` mappát és írj 5 egyszerű tesztet
2. Használj fixture-t minta adatok előkészítéséhez
3. Írj `@pytest.mark.parametrize` tesztet legalább 4 bemenettel
4. Teszteld egy kivétel dobását `pytest.raises`-zel
5. Commitold és pushold
