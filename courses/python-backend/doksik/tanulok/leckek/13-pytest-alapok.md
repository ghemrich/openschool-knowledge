# Lecke 13 – pytest alapok

> **Dokumentáció:** [pytest](https://docs.pytest.org/) · [pytest fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html) · [assert](https://docs.pytest.org/en/stable/how-to/assert.html)

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

```bash
pytest
pytest -v          # részletes kimenet
pytest -v -s       # print() is látszik
```

### assert részletesen

```python
def test_assert_peldak():
    assert 1 + 1 == 2                     # egyenlőség
    assert "alma" in ["alma", "körte"]     # tartalmazás
    assert len([1, 2, 3]) == 3            # hossz
    assert isinstance(42, int)             # típus
    assert not False                       # negáció
```

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

### Fixture scope

```python
@pytest.fixture(scope="module")    # egyszer fut le a modul összes tesztjéhez
def db_connection():
    conn = create_connection()
    yield conn                      # yield után: cleanup
    conn.close()
```

| Scope | Életciklus |
|-------|-----------|
| `function` | Minden teszthez újra (alapértelmezett) |
| `class` | Osztályonként egyszer |
| `module` | Fájlonként egyszer |
| `session` | Teljes teszt futáshoz egyszer |

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

### Tesztek csoportosítása osztályokkal

```python
class TestOsszead:
    def test_pozitiv(self):
        assert osszead(2, 3) == 5

    def test_negativ(self):
        assert osszead(-1, -2) == -3
```

### Tesztek futtatása szelektíven

```bash
pytest tests/test_matek.py              # egy fájl
pytest tests/test_matek.py::test_dupla  # egy teszt
pytest -k "negativ"                      # név alapján szűrés
pytest --tb=short                        # rövid traceback
```

---

## Gyakorlat

1. Hozz létre egy `tests/` mappát és írj 5 egyszerű tesztet
2. Használj fixture-t minta adatok előkészítéséhez
3. Írj `@pytest.mark.parametrize` tesztet legalább 4 bemenettel
4. Teszteld egy kivétel dobását `pytest.raises`-zel
5. Commitold és pushold
