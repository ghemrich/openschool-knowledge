# HTML & CSS szintfelmérő – Blog (D variáns)

> **Időtartam:** 90 perc
> **Összpontszám:** 40 pont
> **Beadás:** az utolsó `git push` az óra végén = beadás!

---

## Vizsga szabályok

- **Idő:** 90 perc
- **Internet használható** (dokumentáció, MDN, W3Schools stb.)
- Egymásnak NEM segíthettek!
- Rendszeresen commitolj! (`git add . && git commit -m "üzenet" && git push`)

---

## 1. feladat – Cikkek oldal (8 pont)

Készíts egy weboldalt (`feladat1.html`), amely egy blog cikkeit mutatja be.

### Követelmények:
- `<h1>` – a blog neve
- `<h2>` – legalább 3 cikk kategória (pl. Technológia, Utazás, Egészség)
- Minden kategória alatt rendezetlen lista (`<ul>`, `<li>`) a cikkekkel (cím és dátum)
- Egy táblázat (`<table>`) a legnépszerűbb cikkekkel:
  - Oszlopok: Cím, Szerző, Dátum, Olvasások száma
  - Fejléc sor (`<th>`)
  - Legalább 3 cikk
- Legalább 1 kép (`<img>`) `alt` attribútummal
- Érvényes HTML5 dokumentum szerkezet

---

## 2. feladat – Hozzászólás oldal (14 pont)

Készíts egy weboldalt (`feladat2.html`) és stílusfájlt (`feladat2.css`).

### HTML követelmények:
- Szemantikus szerkezet: `<header>`, `<nav>`, `<main>`, `<footer>`
- Navigáció legalább 3 menüponttal (Főoldal, Cikkek, Hozzászólás)
- Hozzászólás űrlap (`<form>`):
  - Név (`<input type="text">`, `required`)
  - Email (`<input type="email">`, `required`)
  - Téma kiválasztása (`<select>` legalább 3 opcióval)
  - Hozzászólás (`<textarea>`)
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

## 3. feladat – Teljes blog weboldal (18 pont)

Készíts egy teljes reszponzív weboldalt (`feladat3.html`) és stílusfájlt (`feladat3.css`).

### HTML követelmények:
- Fejléc (`<header>`) a blog nevével és navigációval (`<nav>`)
- Hős szekció (`<section>`) nagy üdvözlő szöveggel és „Olvasd a legújabb cikket!" gombbal
- Cikkek szekció: legalább 4 cikk kártya (`<article>`), mindegyikben kép, cím, kivonat, dátum
- Lábléc (`<footer>`) 3 oszloppal: Kategóriák, Közösségi média, Szerzői jog

### CSS követelmények:
- Viewport meta tag
- CSS változók: legalább `--szin-elsodleges`, `--szin-hatter`
- Flexbox elrendezés a navigációhoz, kártyákhoz és lábléchez
- Hover effekt a kártyákon vagy gombokon (`transition`)
- `@media` lekérdezés legalább 1 törésponttal
- `box-shadow` legalább egy elemen
- `border-radius` lekerekítés

---

## 📚 Segédanyagok

- [Kurzus tananyagok és leckék](../../doksik/tanulok/README.md)
- [HTML referencia (W3Schools)](https://www.w3schools.com/tags/)
- [CSS referencia (W3Schools)](https://www.w3schools.com/cssref/)

## Beadás

1. `git add .`
2. `git commit -m "vizsga kész"`
3. `git push`
