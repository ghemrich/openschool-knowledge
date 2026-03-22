# 16. hét – Haladó tesztelési minták

> **Beadás:** commitold és pushold a megoldásaidat ebbe a repóba!
> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz

---

Ezen a héten haladó tesztelési mintákat tanulsz: fixture-ök, parametrizált tesztek, és teszt lefedettség mérése. Ezek segítségével átfogóbb és hatékonyabb teszteket írhatsz.

---

## Feladat

Készíts egy **Felhasználó + Termék API**-t auth-tal, és írj hozzá haladó teszteket.

### Struktúra:
Az előző hét struktúráját bővítsd ki auth-tal (`auth.py`, `dependencies.py`).

### Végpontok:
- `POST /auth/regisztracio` → regisztráció (201) ⭐
- `POST /auth/login` → JWT token (200) ⭐
- `POST /termekek` → védett, létrehozás (201) ⭐⭐
- `DELETE /termekek/{id}` → védett, törlés ⭐⭐

### Te írod a teszteket! Legalább:
- 3 parametrizált teszt (`@pytest.mark.parametrize`) ⭐⭐
- 3 negatív teszt (rossz jelszó, dupla email, jogosultsági hiba) ⭐⭐
- AAA (Arrange-Act-Assert) minta használata ⭐⭐⭐
- Coverage >70% ⭐⭐⭐

---

## Automatikus tesztelés

```bash
pip install -r requirements.txt
pytest tests/ -v --cov=app
```

## Dokumentáció

- [pytest parametrize](https://docs.pytest.org/en/stable/how-to/parametrize.html)
- [pytest-cov](https://pytest-cov.readthedocs.io/)

## 📚 Kapcsolódó anyagok

Az ehhez a héthez tartozó elméleti anyagot és további gyakorlófeladatokat itt találod:

- 📖 [Lecke: Haladó tesztelés](https://github.com/ghemrich/openschool-knowledge/blob/master/courses/python-backend/leckek/16-halado-teszteles.md)

## Beadás

1. `app/` csomag + `tests/` mappa legyen a repóban
2. Legalább 10 teszt, mind zöld
3. Commitolj értelmes üzenetekkel
4. `git push` – ez a beadás!
