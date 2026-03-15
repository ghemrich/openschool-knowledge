# Vizsga – C variáns: Webshop weboldal

**Időtartam:** 90 perc
**Összpontszám:** 40 pont
**Beadás:** GitHub Classroom (commit + push)

---

## 1. feladat – Terméklista oldal (8 pont)

Készíts egy weboldalt (`feladat1.html`), amely egy webshop termékeit mutatja be.

### Követelmények:
- `<h1>` – a webshop neve
- `<h2>` – legalább 3 termék kategória (pl. Elektronika, Ruházat, Könyvek)
- Minden kategória alatt rendezetlen lista (`<ul>`, `<li>`) a termékekkel (név és ár)
- Egy táblázat (`<table>`) a legkelendőbb termékekkel:
  - Oszlopok: Termék neve, Kategória, Ár, Értékelés
  - Fejléc sor (`<th>`)
  - Legalább 3 termék
- Legalább 1 kép (`<img>`) `alt` attribútummal
- Érvényes HTML5 dokumentum szerkezet

---

## 2. feladat – Rendelési oldal (14 pont)

Készíts egy weboldalt (`feladat2.html`) és stílusfájlt (`feladat2.css`).

### HTML követelmények:
- Szemantikus szerkezet: `<header>`, `<nav>`, `<main>`, `<footer>`
- Navigáció legalább 3 menüponttal (Főoldal, Termékek, Rendelés)
- Rendelési űrlap (`<form>`):
  - Név (`<input type="text">`, `required`)
  - Email (`<input type="email">`, `required`)
  - Termék kiválasztása (`<select>` legalább 5 opcióval)
  - Darabszám (`<input type="number" min="1" max="10">`)
  - Szállítási cím (`<textarea>`)
  - Rendelés gomb (`<button>`)
  - Minden mezőhöz `<label>`

### CSS követelmények:
- Külső CSS fájl (`<link rel="stylesheet">`)
- Háttérszín a fejlécen és láblécen
- Betűtípus beállítás az egész oldalon
- Az űrlap elemei formázva (padding, border, szín)
- Navigáció stílusozva (szín, hover effekt)
- Szöveg igazítás és sortávolság

---

## 3. feladat – Teljes webshop weboldal (18 pont)

Készíts egy teljes reszponzív weboldalt (`feladat3.html`) és stílusfájlt (`feladat3.css`).

### HTML követelmények:
- Fejléc (`<header>`) a webshop nevével és navigációval (`<nav>`)
- Hős szekció (`<section>`) nagy akciós szöveggel és „Vásárolj most!" gombbal
- Termék szekció: legalább 4 termék kártya, mindegyikben kép, név, leírás, ár
- Lábléc (`<footer>`) 3 oszloppal: Ügyfélszolgálat, Információk, Fizetési módok

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
