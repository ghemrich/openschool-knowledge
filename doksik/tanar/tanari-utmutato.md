# Tanári útmutató – Python kurzus 10. évfolyam

## Kurzus felépítése

A kurzus 13 hétre van bontva (0–12. hét, heti 2 óra), és fokozatosan építi fel a vizsgához szükséges tudást. A vizsga beadása **GitHub Classroom**-on keresztül történik.

**Kapcsolódó dokumentumok:**
- Tanterv: [`doksik/tanterv/tanterv.md`](../tanterv/tanterv.md)
- Diák leckék: [`doksik/diakok/leckek/`](../diakok/leckek/)
- Diák feladatok: [`doksik/diakok/feladatok/`](../diakok/feladatok/)
- GitHub Classroom útmutató: [`github-classroom-utmutato.md`](github-classroom-utmutato.md)
- Értékelési módszertan: [`ertekeles-modszertan.md`](ertekeles-modszertan.md)

---

## Heti ütemterv és javaslatok

### 0. hét: Git és GitHub Classroom
- **Cél:** A diákok beállítják a Git-et, létrehoznak GitHub fiókot, és megtanulják az alapokat
- **Tipp:** Előre készíts egy GitHub Classroom szervezetet és egy próba-feladatot. Az órán segítsd a diákokat a fióklétrehozásban.
- **Beállítás:** Lásd [`github-classroom-utmutato.md`](github-classroom-utmutato.md)
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

Négy vizsga variáns áll rendelkezésre:

| | A – filmek | B – konyvek | C – zenek | D – sportolok |
|---|---|---|---|---|
| **Feladatlap** | `vizsgak/filmek/feladat/vizsga.md` | `vizsgak/konyvek/feladat/vizsga.md` | `vizsgak/zenek/feladat/vizsga.md` | `vizsgak/sportolok/feladat/vizsga.md` |
| **Értékelés** | `vizsgak/filmek/feladat/ertekeles.md` | `vizsgak/konyvek/feladat/ertekeles.md` | `vizsgak/zenek/feladat/ertekeles.md` | `vizsgak/sportolok/feladat/ertekeles.md` |
| **Forrásfájlok** | `vizsgak/filmek/forras/` | `vizsgak/konyvek/forras/` | `vizsgak/zenek/forras/` | `vizsgak/sportolok/forras/` |
| **Megoldás** | `vizsgak/filmek/megoldas/` | `vizsgak/konyvek/megoldas/` | `vizsgak/zenek/megoldas/` | `vizsgak/sportolok/megoldas/` |
| **GitHub Classroom** | `github-classroom/vizsga-filmek/` | `github-classroom/vizsga-konyvek/` | `github-classroom/vizsga-zenek/` | `github-classroom/vizsga-sportolok/` |

**Különbségek:**
- 1. feladat: felhasználónév / email / jelszó / becenév generátor
- 2. feladat: kártyahúzás (3–39) / kockadobás (3–18) / nyerőgép (3–30) / golyóhúzás (4–20)
- 3. feladat: filmek / könyvek / zenék / sportolók feldolgozása

> **Részletes értékelési módszertan:** lásd `doksik/tanar/ertekeles-modszertan.md`

---

## Értékelés

Részletes értékelési rendszer, jegyhatárok, code review szempontok és szóbeli kérdések: lásd [`ertekeles-modszertan.md`](ertekeles-modszertan.md).

Vizsga és házi feladat kezelése GitHub Classroom-ban: lásd [`github-classroom-utmutato.md`](github-classroom-utmutato.md).

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
