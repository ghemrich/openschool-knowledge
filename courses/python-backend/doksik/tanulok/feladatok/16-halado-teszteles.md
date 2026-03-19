# Kiegészítő gyakorlatok – 16. hét: Haladó tesztelési minták

> Ezek a feladatok a heti házi feladat melletti **extra gyakorlást** szolgálják.
> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz

---

### 16.1 – Teszt szervezés osztályokkal ⭐⭐
Írj teszteket `class`-okba szervezve:
```python
class TestFelhasznaloLetrehozas:
    def test_sikeres_regisztracio(self, client): ...
    def test_dupla_email(self, client): ...
    def test_gyenge_jelszo(self, client): ...

class TestFelhasznaloLogin:
    def test_sikeres_login(self, client): ...
    def test_rossz_jelszo(self, client): ...
```
Futtasd: `pytest -v` és figyeld a csoportosítást.

### 16.2 – Mark-ok használata ⭐⭐
Jelöld meg a teszteket mark-okkal:
- `@pytest.mark.slow` – lassabb tesztek
- `@pytest.mark.auth` – auth-hoz kötődő tesztek
- `@pytest.mark.crud` – CRUD tesztek

Regisztráld a mark-okat a `pytest.ini`-ben. Futtasd: `pytest -m auth`, `pytest -m "not slow"`.

### 16.3 – monkeypatch ⭐⭐
Használd a `monkeypatch` fixture-t:
1. Állítsd be a `SECRET_KEY` környezeti változót teszteléshez
2. Cseréld ki a `datetime.now()` visszatérési értékét egy fix időpontra
3. Mockolj egy fájlolvasó függvényt, hogy ne valós fájlból olvasson

### 16.4 – Snapshot tesztelés ⭐⭐
Írj teszteket, amelyek mentik a válasz JSON-t fájlba ("gold file" minta). Az első futáskor mentsék el a várt kimenetet, a következő futásokon hasonlítsák össze. Ha eltérés van, a teszt elbukik.

### 16.5 – Coverage és hiányzó sorok ⭐⭐⭐
Futtasd: `pytest --cov=app --cov-report=html`. Nyisd meg a HTML riportot és keresd meg a lefedetlen sorokat. Írj célzott teszteket a 3 legkevesebb lefedettségű fájlhoz, amíg eléred a 90%-os összlefedettséget.
