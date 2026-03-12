# GitHub Classroom — Tanuló útmutató

Ez az útmutató elmagyarázza, hogyan működik a GitHub Classroom a feladatok beadásához, hogyan ellenőrizheted az eredményeidet, és mit tegyél, ha valami nem működik.

---

## Mi az a GitHub Classroom?

A GitHub Classroom egy rendszer, amely:
- Minden feladathoz **saját GitHub repót** hoz létre neked
- A beadás = **`git push`** a repódba
- Az értékelés **automatikus** — a GitHub Actions lefuttatja a teszteket

Nem kell semmit sem feltölteni manuálisan. A kódod a saját GitHub repódban él, és minden push után azonnal látod az eredményt.

---

## Feladat elfogadása

1. **Kattints a feladat linkjére** — a mentortól/kurzusoldalról kapod meg (pl. `https://classroom.github.com/a/abc123`)
2. **Jelentkezz be** a GitHub fiókoddal (ha még nem vagy bejelentkezve)
3. Ha névjegyzék van, **válaszd ki a nevedet** a listából (első alkalomnál)
4. Kattints az **„Accept this assignment"** gombra
5. Várj néhány másodpercet — a GitHub létrehozza a **saját repódat**
6. Kattints a megjelenő linkre — ez a te repód, ide fogod a kódodat pusholni

> A repó neve a feladat nevéből és a GitHub felhasználónevedből áll össze (pl. `het01-alapok-felhasznalonev`).

---

## Munkafolyamat

### 1. Klónozd le a repót

```bash
git clone https://github.com/SZERVEZET/FELADAT-NEVED.git
cd FELADAT-NEVED
```

### 2. Dolgozz a feladaton

Nyisd meg VS Code-ban és írd meg a kódot:

```bash
code .
```

### 3. Commitold és pushold

```bash
git add .
git commit -m "1. feladat kész"
git push
```

### 4. Ellenőrizd az eredményt

A `git push` után a GitHub Actions automatikusan lefuttatja a teszteket. Az eredményt kétféleképpen nézheted meg:

**A) GitHub felületen:**
1. Nyisd meg a repódat a böngészőben
2. Nézd meg a commit mellett a jelölést:
   - ✅ Zöld pipa = minden teszt átment
   - ❌ Piros X = egy vagy több teszt bukott
   - 🟡 Sárga kör = a tesztek még futnak

**B) Actions fül:**
1. Kattints a repódban az **Actions** fülre
2. Válaszd ki a legutóbbi futást
3. A részleteknél látod, melyik teszt ment át és melyik nem

---

## Hogyan értelmezd a teszt eredményeket?

### Sikeres tesztek (✅)

```
✅ test_1_feladat PASSED
✅ test_2_feladat PASSED
✅ test_3_feladat PASSED
```

Minden kész — a feladatod teljesítve.

### Sikertelen tesztek (❌)

```
✅ test_1_feladat PASSED
❌ test_2_feladat FAILED
✅ test_3_feladat PASSED
```

A 2. feladat tesztje nem ment át. Kattints a sikertelen tesztre a részletekért — a hibaüzenet megmutatja, mi volt a probléma:

```
AssertionError: assert "Helló, Anna!" == program_kimenete
# A programod "Hello, Anna!"-t adott vissza (hiányzó ékezet)
```

### A tesztek még futnak (🟡)

Várj 1-2 percet és frissítsd az oldalt.

---

## Többszöri beadás

Nincs korlátozva, hányszor pusholhatsz. Minden push után újra lefutnak a tesztek:

```bash
# Javítás után:
git add .
git commit -m "2. feladat javítva"
git push
```

Az utolsó push eredménye számít.

---

## Gyakori problémák

| Probléma | Megoldás |
|----------|----------|
| A Classroom link „404 Not Found" | Nem vagy bejelentkezve GitHubra. Jelentkezz be, majd próbáld újra. |
| „You don't have access" | Nem vagy tagja a GitHub szervezetnek. Kérd a mentorod, hogy hívjon meg. |
| A tesztek nem futnak le | Ellenőrizd, hogy a fájljaid a **gyökérmappában** vannak-e (nem egy almappában). |
| Lokálisan működik, Actions-ben nem | A tesztek más környezetben futnak. Ellenőrizd: nem használsz-e abszolút fájlutat? Az `encoding="utf-8"` megvan? |
| `git push` hiba: „rejected" | Valaki (vagy a GitHub) módosította a repót. Futtasd: `git pull --rebase` majd `git push`. |
| Nem látom az Actions fület | Ellenőrizd, hogy a `.github/workflows/` mappa és a CI fájl benne van-e a repóban. Ha nem, klónozd újra. |

---

## Tippek

- **Commitolj gyakran** — ne csak a végén egyszer. Több kis commit jobb, mint egy nagy.
- **Olvasd el a README-t** — a feladat repóban a `README.md` tartalmazza a pontos leírást.
- **Nézd meg a tesztfájlt** — a `.github/` mappában vagy a gyökérben lévő tesztfájl megmutatja, pontosan mit ellenőriz a rendszer.
- **Ne módosítsd a tesztfájlokat** — ha átírod a teszteket, az nem számít megoldásnak.

---

**Következő lépés:** [Kezdő útmutató — Hogyan kezdj hozzá?](kezdo-utmutato.md)
