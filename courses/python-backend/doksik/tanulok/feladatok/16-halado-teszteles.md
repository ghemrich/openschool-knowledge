# Feladatok – 16. hét: Haladó tesztelési minták

> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz
> A megoldásokat commitold és pushold a GitHub repódba.

---

### 16.1 – Parametrizált API tesztek ⭐⭐
Írj `@pytest.mark.parametrize` tesztet a `POST` végpontra: legalább 4 eset (érvényes adat, üres név, negatív ár, hiányzó mező). Ellenőrizd a várt status kódokat.

### 16.2 – Negatív tesztek ⭐⭐
Írj legalább 5 negatív tesztet: rossz jelszavú login, nem létező user login, dupla regisztráció, más user itemjének törlése, lejárt token.

### 16.3 – AAA minta ⭐⭐
Írj 3 tesztet az AAA (Arrange-Act-Assert) minta szerint, jól elkülönítve a három részt kommentekkel.

### 16.4 – Coverage riport ⭐⭐
Telepítsd a `pytest-cov` csomagot, futtasd a teszteket coverage-dzsel. Érj el legalább 80%-os lefedettséget az `app/` mappában.

### 16.5 – Factory fixture ⭐⭐⭐
Készíts factory fixture-öket: `create_user(nev, email)` és `create_item(nev, ar)`. Használd őket legalább 3 tesztben, ahol különböző felhasználók és elemek kellenek.
