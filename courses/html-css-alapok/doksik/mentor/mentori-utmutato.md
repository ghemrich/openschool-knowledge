# Mentori útmutató – HTML & CSS Alapok

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
- **Házi feladat:** Próba repo: klónozás, `index.html` létrehozása, commit, push

### 1–2. hét: HTML alapok (dokumentum szerkezet, szöveges elemek, listák)
- **Cél:** A tanulók kényelmesen hoznak létre alapvető HTML oldalakat
- **Tipp:** Sok kis gyakorlat, ne hosszú magyarázat. Mutasd meg a böngésző fejlesztői eszközeit (F12) az elejétől
- **Házi feladat:** Bemutatkozó weboldal, kedvenc dolgok listája

### 3. hét: Linkek és képek
- **Cél:** Oldalak összekötése, képek beágyazása
- **Tipp:** A relatív és abszolút útvonalak közötti különbség nehéz lehet – rajzolj mappaszerkezetet a táblára
- **Házi feladat:** Képgaléria navigációs linkekkel

### 4–5. hét: Táblázatok, űrlapok és szemantikus HTML
- **Cél:** Komplex HTML elemek megismerése, szemantikus gondolkodás
- **Tipp:** A szemantikus HTML-nél mutasd meg a különbséget: `<div>` vs `<header>`, `<nav>`, stb. – a screen reader szimulátort is érdemes bemutatni
- **Házi feladat:** Regisztrációs űrlap, szemantikus blog oldal

### 6. hét: CSS bevezetés
- **Cél:** A HTML és CSS kapcsolatának megértése, alapvető stílusozás
- **Tipp:** Ez kulcsfontosságú hét – a tanulók itt értik meg, hogy az oldal kinézetét külön kezeljük. Mindig külső CSS fájlt használjunk, ne inline stílust
- **Házi feladat:** Meglévő HTML oldalak formázása CSS-sel

### 7. hét: CSS box modell
- **Cél:** A doboz modell megértése – ez az alap minden CSS elrendezéshez
- **Tipp:** A Chrome DevTools „box model" paneljét használd szemléltetéshez. A `box-sizing: border-box` bevezetése itt fontos
- **Házi feladat:** Kártya komponensek készítése

### 8. hét: CSS elrendezés és pozícionálás
- **Cél:** Pozícionálás és float megértése
- **Tipp:** A `position` nehéz téma – érdemes lépésről lépésre mutatni, DevTools-ban módosítgatva az értékeket. A float-ot csak röviden érintsd, a Flexbox a fontosabb
- **Házi feladat:** Rögzített navigáció, egyszerű oldal elrendezés

### 9. hét: Flexbox
- **Cél:** Modern elrendezés Flexbox-szal
- **Tipp:** Ez a legfontosabb elrendezési módszer a kurzusban – több időt érdemes rá szánni. A [Flexbox Froggy](https://flexboxfroggy.com/) játék remek gyakorláshoz
- **Házi feladat:** Kártya elrendezés, navigáció Flexbox-szal

### 10. hét: Reszponzív design
- **Cél:** Mobilbarát weboldalak készítése
- **Tipp:** A DevTools eszköztár mobilnézet gombjával mutasd meg a különbséget. Mobile-first megközelítést taníts
- **Házi feladat:** Korábban készített oldal reszponzívvá tétele

### 11. hét: CSS haladó témák és projekt
- **Cél:** Teljes vizsgafeladat típusú weboldal megírása
- **Tipp:** A 3. feladat a legnehezebb (18 pont) – érdemes részfeladatonként haladni. A CSS változók egyszerűsítik a stílusok kezelését
- **Házi feladat:** Teljes weboldal projekt

### 12. hét: Vizsgafelkészítés
- **Cél:** Próbavizsga, hibaelemzés
- **Tipp:** Valódi vizsgakörülmények között dolgozzanak – a próbavizsga is GitHub Classroom-on keresztül történjen

---

## Vizsgavariánsok

Négy vizsga variáns áll rendelkezésre:

| | A – étterem | B – portfólió | C – webshop | D – blog |
|---|---|---|---|---|
| **Feladatlap** | `vizsgak/etterem/feladat/vizsga.md` | `vizsgak/portfolio/feladat/vizsga.md` | `vizsgak/webshop/feladat/vizsga.md` | `vizsgak/blog/feladat/vizsga.md` |
| **Értékelés** | `vizsgak/etterem/feladat/ertekeles.md` | `vizsgak/portfolio/feladat/ertekeles.md` | `vizsgak/webshop/feladat/ertekeles.md` | `vizsgak/blog/feladat/ertekeles.md` |
| **Forrásfájlok** | `vizsgak/etterem/forras/` | `vizsgak/portfolio/forras/` | `vizsgak/webshop/forras/` | `vizsgak/blog/forras/` |
| **Megoldás** | `vizsgak/etterem/megoldas/` | `vizsgak/portfolio/megoldas/` | `vizsgak/webshop/megoldas/` | `vizsgak/blog/megoldas/` |
| **GitHub Classroom** | `github-classroom/vizsga-etterem/` | `github-classroom/vizsga-portfolio/` | `github-classroom/vizsga-webshop/` | `github-classroom/vizsga-blog/` |

**Különbségek:**
- 1. feladat: étlap / projektek / terméklista / cikk – statikus HTML oldal táblázattal és listával
- 2. feladat: foglalás / kapcsolat / rendelés / hozzászólás – űrlap és CSS stílusozás
- 3. feladat: étterem / portfólió / webshop / blog – teljes reszponzív weboldal

> **Részletes értékelési módszertan:** lásd `doksik/mentor/ertekeles-modszertan.md`

---

## Értékelés

Részletes értékelési rendszer, szinthatárok, code review szempontok és szóbeli kérdések: lásd [`ertekeles-modszertan.md`](ertekeles-modszertan.md).

Vizsga és házi feladat kezelése GitHub Classroom-ban: lásd [`github-classroom-utmutato.md`](github-classroom-utmutato.md).

---

## Gyakori tanulói problémák és megoldásuk

### HTML hibák
- **Hiányzó záró tag:** Mutasd meg a HTML validátor használatát (VS Code kiegészítő vagy W3C Validator)
- **Hiányzó `alt` attribútum képeknél:** Hangsúlyozd, hogy ez kötelező – akadálymentesség
- **Rosszul beágyazott elemek:** A `<p>` belsejében nem lehet `<div>`, az `<a>` belsejében nem lehet `<a>`
- **Fájlnév szóközzel:** A fájlnevekben ne használjunk szóközt, ékezetet – `index.html`, nem `Kezdo Oldal.html`

### CSS hibák
- **A CSS nem töltődik be:** Ellenőrizd a `<link>` tag `href` útvonalát – relatív útvonal a `.html` fájlhoz képest
- **A szelektor nem működik:** Gyakori hiba: `.osztaly` helyett `osztaly` (pont nélkül) vagy `#id` helyett `id` (kettős kereszt nélkül)
- **Flexbox nem működik:** A `display: flex` a szülő elemre kell, nem a gyermekekre
- **A stílus nem érvényesül:** CSS specificitás – az `id` szelektor erősebb, mint az `osztály`, ami erősebb, mint az elem

### Git hibák
- A központi hibaelhárítási útmutatóban: [Hibaelhárítás és GYIK — Git és GitHub](../../../../guides/hibaelharitas.md#git-és-github)
- [GitHub Classroom hibák](../../../../guides/hibaelharitas.md#github-classroom)
