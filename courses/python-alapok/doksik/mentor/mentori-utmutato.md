# Mentori útmutató – Python Alapok

## Kurzus felépítése

A kurzus 13 hétre van bontva (0–12. hét, heti 2 óra), és fokozatosan építi fel a vizsgához szükséges tudást. A vizsga beadása **GitHub Classroom**-on keresztül történik.

**Kapcsolódó dokumentumok:**
- Tanterv: [`doksik/tanterv/tanterv.md`](../tanterv/tanterv.md)
- Tanuló leckék: [`doksik/tanulok/leckek/`](../tanulok/leckek/)
- Tanuló feladatok: [`doksik/tanulok/feladatok/`](../tanulok/feladatok/)
- GitHub Classroom útmutató: [`github-classroom-utmutato.md`](github-classroom-utmutato.md)
- Értékelési módszertan: [`ertekeles-modszertan.md`](ertekeles-modszertan.md)

---

## Heti ütemterv és javaslatok

### 0. hét: Git és GitHub Classroom
- **Cél:** A tanulók beállítják a Git-et, létrehoznak GitHub fiókot, és megtanulják az alapokat
- **Tipp:** Előre készíts egy GitHub Classroom szervezetet és egy próba-feladatot. Az órán segítsd a tanulókat a fióklétrehozásban.
- **Beállítás:** Lásd [`github-classroom-utmutato.md`](github-classroom-utmutato.md)
- **Házi feladat:** Próba repo: klónozás, `hello.py` létrehozása, commit, push

### 1–2. hét: Alapok (print, input, változók, szövegkezelés)
- **Cél:** A tanulók kényelmesen írjanak egyszerű programokat
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
- **Tipp:** A szótárak listája olvashatóbb – ezt ajánlom a tanulóknak
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

> **Részletes értékelési módszertan:** lásd `doksik/mentor/ertekeles-modszertan.md`

---

## Értékelés

Részletes értékelési rendszer, szinthatárok, code review szempontok és szóbeli kérdések: lásd [`ertekeles-modszertan.md`](ertekeles-modszertan.md).

Vizsga és házi feladat kezelése GitHub Classroom-ban: lásd [`github-classroom-utmutato.md`](github-classroom-utmutato.md).

---

## Gyakori tanulói problémák és megoldásuk

A kurzus-specifikus hibák és megoldásaik részletes listáját lásd a központi hibaelhárítási útmutatóban:

- [Hibaelhárítás és GYIK — Python Alapok kurzus](../../../../guides/hibaelharitas.md#python-alapok-kurzus)
- [Hibaelhárítás és GYIK — Git és GitHub](../../../../guides/hibaelharitas.md#git-és-github)
- [Hibaelhárítás és GYIK — GitHub Classroom](../../../../guides/hibaelharitas.md#github-classroom)
