# 12. hét – Vizsgafelkészítés

> **Határidő:** a vizsga előtt
> **Beadás:** commitold és pushold a megoldásaidat ebbe a repoba!
> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz

---

## Próbavizsga

A próbavizsga 3 feladatból áll, összesen 40 pont. A valódi vizsgán is hasonló feladatokat fogsz kapni.

### 12.1 – Statikus HTML oldal (8 pont) ⭐
Készíts egy weboldalt (`feladat1.html`) egy étlap oldalnak:
- `<h1>` – az étterem neve
- `<h2>` – legalább 3 kategória (pl. Előételek, Főételek, Desszertek)
- Minden kategória alatt rendezetlen lista (`<ul>`) az ételekkel (név + ár)
- Egy táblázat a napi menüvel (oszlopok: Étel, Ár, Kalória)
- `<img>` legalább 1 képpel, `alt` attribútummal

### 12.2 – CSS stílusozás és űrlap (14 pont) ⭐⭐
Készíts egy weboldalt (`feladat2.html`) és stílusfájlt (`feladat2.css`):
- Szemantikus szerkezet: `<header>`, `<nav>`, `<main>`, `<footer>`
- Navigáció legalább 3 menüponttal
- Egy foglalási űrlap: név, email, dátum, vendégek száma, üzenet, küldés gomb
- CSS stílusozás:
  - Külső CSS fájl (bekötve `<link>`-kel)
  - Színek, betűtípusok, igazítás
  - Szegély és padding az űrlap elemeken
  - Háttérszín a fejlécen és láblécen

### 12.3 – Reszponzív weboldal (18 pont) ⭐⭐⭐
Készíts egy teljes reszponzív weboldalt (`feladat3.html`) és stílusfájlt (`feladat3.css`) egy étteremnek:
- Fejléc navigációval (Flexbox)
- Hős szekció nagy címsorral és CTA gombbal
- Menü szekció kártyákkal (legalább 4 étel kártya, Flexbox)
- Lábléc 3 oszloppal
- Reszponzív design:
  - Viewport meta tag
  - Legalább 1 `@media` töréspont
  - Mobilon: navigáció függőlegesen, kártyák 1 oszlopban, lábléc 1 oszlopban
- CSS változók (legalább `--szin-elsodleges`)
- Hover effekt a kártyákon vagy gombokon (`transition`)

---

## Emlékeztető – vizsgán elvárt ismeretek

- HTML5 dokumentum szerkezet
- Szemantikus elemek (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`)
- Listák, táblázatok, képek, linkek, űrlapok
- Külső CSS fájl
- CSS szelektorok (elem, osztály, azonosító)
- CSS box modell (margin, padding, border)
- Flexbox elrendezés
- Reszponzív design (`@media`)

## Dokumentáció

- [HTML referencia](https://www.w3schools.com/tags/)
- [CSS referencia](https://www.w3schools.com/cssref/)

## Beadás

1. Minden feladatot külön fájlba/fájlpárba írj
2. Commitolj értelmes üzenetekkel
3. `git push` – ez a beadás!
