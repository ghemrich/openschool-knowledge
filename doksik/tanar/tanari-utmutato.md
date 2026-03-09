# Tanári útmutató – Python kurzus 10. évfolyam

## Kurzus felépítése

A kurzus 13 hétre van bontva (0–12. hét, heti 2 óra), és fokozatosan építi fel a vizsgához szükséges tudást. A vizsga beadása **GitHub Classroom**-on keresztül történik. A diákok anyagai a `doksik/diakok/` mappában találhatók, heti bontásban.

---

## Heti ütemterv és javaslatok

### 0. hét: Git és GitHub Classroom
- **Cél:** A diákok beállítják a Git-et, létrehoznak GitHub fiókot, és megtanulják az alapokat
- **Tipp:** Előre készíts egy GitHub Classroom szervezetet és egy próba-feladatot. Az órán segítsd a diákokat a fióklétrehozásban.
- **GitHub Classroom beállítás:**
  1. Hozz létre egy GitHub Organizationt az iskola/osztály részére
  2. A [classroom.github.com](https://classroom.github.com) oldalon hozz létre egy Classroom-ot
  3. Készíts template repokat a feladatokhoz (a `vizsgak/filmek/forras/` és `vizsgak/konyvek/forras/` mappákból)
  4. Hozz létre Assignment-eket a házi feladatokhoz és a vizsgához
- **Házi feladat:** Próba repo: klónozás, `hello.py` létrehozása, commit, push

### 1–2. hét: Alapok (print, input, változók, szövegkezelés)
- **Cél:** A diákok kényelmesen írjanak egyszerű programokat
- **Tipp:** Sok kis gyakorlat, ne hosszú magyarázat
- **Házi feladat:** Mini programok (pl. bemutatkozó, egyszerű számológép)

### 3–4. hét: Vezérlési szerkezetek (if, while, for)
- **Cél:** Feltételes logika és ismétlés megértése
- **Tipp:** A `while` fontosabb a vizsgán, mint a `for` – több időt érdemes rá szánni
- **Házi feladat:** Számkitalálós játék (egyszerű verzió, függvények nélkül)

### 5. hét: Listák
- **Cél:** Adatgyűjtemények kezelése
- **Tipp:** Az `append()`, `len()`, `sum()` és a `for` ciklussal bejárás a legfontosabb
- **Házi feladat:** Jegyek átlagszámítása

### 6. hét: Függvények
- **Cél:** Az 1. vizsgafeladat típusú program megírása
- **Tipp:** Ez kulcsfontosságú hét – a vizsgán minden feladatnál elvárás a függvényekre bontás
- **Házi feladat:** Az 1. vizsgafeladat megoldása önállóan

### 7. hét: Random és játéklogika
- **Cél:** A 2. vizsgafeladat típusú program megírása
- **Tipp:** Érdemes lépésről lépésre építeni: először a random, aztán a ciklus, aztán a kiértékelés
- **Házi feladat:** A 2. vizsgafeladat megoldása önállóan

### 8–9. hét: Fájlkezelés és összetett adatszerkezetek
- **Cél:** Fájlból olvasás, szótárak listája
- **Tipp:** A szótárak listája olvashatóbb – ezt ajánlom a diákoknak
- **Házi feladat:** Egyszerű fájl beolvasás és feldolgozás

### 10–11. hét: Adatfeldolgozás és modulok
- **Cél:** A 3. vizsgafeladat típusú program megírása
- **Tipp:** A 3. feladat a legnehezebb (18 pont) – érdemes részfeladatonként haladni
- **Házi feladat:** A 3. vizsgafeladat megoldása

### 12. hét: Vizsgafelkészítés
- **Cél:** Próbavizsga, hibaelemzés
- **Tipp:** Valódi vizsgakörülmények között dolgozzanak – a próbavizsga is GitHub Classroom-on keresztül történjen

---

## Vizsgavariánsok

Két vizsga variáns áll rendelkezésre az A/B csoportos dolgozatíráshoz:

| | A variáns (filmek) | B variáns (konyvek) |
|---|---|---|
| **Feladatlap** | `vizsgak/filmek/feladat/vizsga.md` | `vizsgak/konyvek/feladat/vizsga.md` |
| **Értékelés** | `vizsgak/filmek/feladat/ertekeles.md` | `vizsgak/konyvek/feladat/ertekeles.md` |
| **Forrásfájlok** | `vizsgak/filmek/forras/` | `vizsgak/konyvek/forras/` |
| **Megoldás** | `vizsgak/filmek/megoldas/` | `vizsgak/konyvek/megoldas/` |

**Különbségek:**
- 1. feladat: felhasználónév generátor vs. email generátor
- 2. feladat: kártyahúzás (1–13, max 39) vs. kockadobás (1–6, max 18)
- 3. feladat: filmek (értékelés, kategória) vs. könyvek (bevétel, nyelv/műfaj)

---

## Értékelési javaslat

| Elem | Arány | Megjegyzés |
|------|-------|------------|
| Órai munka | 30% | Aktív részvétel, gyakorlatok |
| Házi feladatok | 20% | Heti kis feladatok |
| Próbavizsga | 10% | 12. héten |
| Szintfelmérő vizsga | 40% | 40 pont, 90 perc |

**Elégséges határ:** 50% (20 pont)

---

## Mappaszerkezet a diákoknak (GitHub Classroom)

A vizsgán a diákok a GitHub Classroom által létrehozott repot használják. A repo már tartalmazza a forrásfájlokat:

```
vizsga-kissanna/          ← GitHub Classroom hozza létre
  filmek.txt              ← a template-ből
  filmek.py               ← a template-ből (tartalék)
  feladat1.py             ← diák írja
  feladat2.py             ← diák írja
  feladat3.py             ← diák írja
  fgv.py                  ← diák írja
```

### GitHub Classroom vizsga létrehozása

1. Készíts egy **template repository**-t a szervezetben:
   - Tartalma: `filmek.txt` + `filmek.py` (A variáns) vagy `konyvek.txt` + `konyvek.py` (B variáns)
   - Adj hozzá egy `README.md`-t a feladatleírással (a `vizsga.md` tartalmával)
2. Hozz létre egy **Assignment**-et a Classroom-ban:
   - Individual assignment
   - Template: a fenti repo
   - Deadline: a vizsga vége
3. Oszd ki a meghívó linket a diákoknak

---

## Gyakori diákproblémák és megoldásuk

| Probléma | Megoldás |
|----------|----------|
| `SyntaxError` ékezetes változóneveknél | Kerüljék az ékezetes változóneveket, vagy használjanak ASCII neveket |
| `FileNotFoundError` | A `.txt` fájl nem ugyanabban a mappában van, mint a `.py` |
| `UnicodeDecodeError` | Hiányzik az `encoding="utf-8"` paraméter |
| `ModuleNotFoundError: fgv` | A `fgv.py` és a főprogram nem ugyanabban a mappában van |
| `TypeError: can't concat str to int` | Elfelejtett `int()` vagy `str()` konverzió |
| `git push` sikertelen | Ellenőrizd: van-e commit? A megfelelő mappában vagy-e? |
| GitHub Classroom link nem működik | A diák nincs bejelentkezve GitHubra, vagy nem tagja a szervezetnek |
