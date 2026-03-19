# HTML & CSS szintfelmérő – Étterem (A variáns)

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

## 1. feladat – Étlap oldal (8 pont)

Készíts egy weboldalt (`feladat1.html`), amely egy étterem étlapját mutatja be.

### Követelmények:
- `<h1>` – az étterem neve
- `<h2>` – legalább 3 étlap kategória (pl. Előételek, Főételek, Desszertek)
- Minden kategória alatt rendezetlen lista (`<ul>`, `<li>`) az ételekkel (név és ár)
- Egy táblázat (`<table>`) a napi menüvel:
  - Oszlopok: Étel neve, Ár, Kalória
  - Fejléc sor (`<th>`)
  - Legalább 3 étel
- Legalább 1 kép (`<img>`) `alt` attribútummal
- Érvényes HTML5 dokumentum szerkezet (`<!DOCTYPE html>`, `<html>`, `<head>`, `<body>`, `<title>`)

---

## 2. feladat – Asztalfoglalás oldal (14 pont)

Készíts egy weboldalt (`feladat2.html`) és stílusfájlt (`feladat2.css`).

### HTML követelmények:
- Szemantikus szerkezet: `<header>`, `<nav>`, `<main>`, `<footer>`
- Navigáció legalább 3 menüponttal (Főoldal, Étlap, Foglalás)
- Asztalfoglalási űrlap (`<form>`):
  - Név (`<input type="text">`, `required`)
  - Email (`<input type="email">`, `required`)
  - Dátum (`<input type="date">`)
  - Vendégek száma (`<input type="number" min="1" max="20">`)
  - Megjegyzés (`<textarea>`)
  - Foglalás gomb (`<button>`)
  - Minden mezőhöz `<label>`

### CSS követelmények:
- Külső CSS fájl (`<link rel="stylesheet">`)
- Háttérszín a fejlécen és láblécen
- Betűtípus beállítás az egész oldalon
- Az űrlap elemei formázva (padding, border, szín)
- Navigáció stílusozva (szín, hover effekt)
- Szöveg igazítás és sortávolság

---

## 3. feladat – Teljes étterem weboldal (18 pont)

Készíts egy teljes reszponzív weboldalt (`feladat3.html`) és stílusfájlt (`feladat3.css`).

### HTML követelmények:
- Fejléc (`<header>`) az étterem nevével és navigációval (`<nav>`)
- Hős szekció (`<section>`) nagy üdvözlő szöveggel és „Foglalj asztalt!" gombbal
- Menü szekció: legalább 4 étel kártya (`<div>` vagy `<article>`), mindegyikben kép, név, leírás, ár
- Lábléc (`<footer>`) 3 oszloppal: Nyitvatartás, Cím, Közösségi média linkek

### CSS követelmények:
- Viewport meta tag (`<meta name="viewport">`)
- CSS változók: legalább `--szin-elsodleges`, `--szin-hatter`
- Flexbox elrendezés a navigációhoz, kártyákhoz és lábléchez
- Hover effekt a kártyákon vagy gombokon (`transition`)
- `@media` lekérdezés legalább 1 törésponttal:
  - Mobilon: navigáció függőlegesen, kártyák 1 oszlopban, lábléc 1 oszlopban
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
