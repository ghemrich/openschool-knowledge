# Vizsga – B variáns: Portfólió weboldal

**Időtartam:** 90 perc
**Összpontszám:** 40 pont
**Beadás:** GitHub Classroom (commit + push)

---

## 1. feladat – Projektek oldal (8 pont)

Készíts egy weboldalt (`feladat1.html`), amely a projektjeidet mutatja be.

### Követelmények:
- `<h1>` – a neved
- `<h2>` – legalább 3 projekt kategória (pl. Weboldalak, Alkalmazások, Egyéb)
- Minden kategória alatt rendezetlen lista (`<ul>`, `<li>`) a projektekkel (név és rövid leírás)
- Egy táblázat (`<table>`) a technológiáiddal:
  - Oszlopok: Technológia, Szint, Tapasztalat (év)
  - Fejléc sor (`<th>`)
  - Legalább 3 technológia
- Legalább 1 kép (`<img>`) `alt` attribútummal
- Érvényes HTML5 dokumentum szerkezet

---

## 2. feladat – Kapcsolat oldal (14 pont)

Készíts egy weboldalt (`feladat2.html`) és stílusfájlt (`feladat2.css`).

### HTML követelmények:
- Szemantikus szerkezet: `<header>`, `<nav>`, `<main>`, `<footer>`
- Navigáció legalább 3 menüponttal (Főoldal, Projektek, Kapcsolat)
- Kapcsolatfelvételi űrlap (`<form>`):
  - Név (`<input type="text">`, `required`)
  - Email (`<input type="email">`, `required`)
  - Tárgy (`<select>` legalább 3 opcióval)
  - Üzenet (`<textarea>`)
  - Küldés gomb (`<button>`)
  - Minden mezőhöz `<label>`

### CSS követelmények:
- Külső CSS fájl (`<link rel="stylesheet">`)
- Háttérszín a fejlécen és láblécen
- Betűtípus beállítás az egész oldalon
- Az űrlap elemei formázva (padding, border, szín)
- Navigáció stílusozva (szín, hover effekt)
- Szöveg igazítás és sortávolság

---

## 3. feladat – Teljes portfólió weboldal (18 pont)

Készíts egy teljes reszponzív weboldalt (`feladat3.html`) és stílusfájlt (`feladat3.css`).

### HTML követelmények:
- Fejléc (`<header>`) a neveddel és navigációval (`<nav>`)
- Hős szekció (`<section>`) nagy bemutatkozó szöveggel és „Vedd fel a kapcsolatot!" gombbal
- Projektek szekció: legalább 4 projekt kártya, mindegyikben kép, cím, leírás, link
- Lábléc (`<footer>`) 3 oszloppal: Közösségi média, Elérhetőség, Szerzői jog

### CSS követelmények:
- Viewport meta tag
- CSS változók: legalább `--szin-elsodleges`, `--szin-hatter`
- Flexbox elrendezés a navigációhoz, kártyákhoz és lábléchez
- Hover effekt a kártyákon vagy gombokon (`transition`)
- `@media` lekérdezés legalább 1 törésponttal
- `box-shadow` legalább egy elemen
- `border-radius` lekerekítés

---

## Beadás

1. Minden feladatot a megadott fájlnevekkel készíts el
2. Commitolj legalább 3 alkalommal, értelmes üzenetekkel
3. `git push` – ez a beadás!
