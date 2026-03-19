# 5. hét – Szemantikus HTML és haladó űrlapok

> **Határidő:** a következő óra előtt
> **Beadás:** commitold és pushold a megoldásaidat ebbe a repoba!
> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz

---

Ezen a héten megtanulod a szemantikus HTML használatát. A szemantikus elemek (pl. `<header>`, `<nav>`, `<main>`, `<footer>`) nem csak a megjelenést, hanem a tartalom *jelentését* is leírják – ez javítja az akadálymentességet és a keresőoptimalizálást (SEO).

---

## 5.1 – Szemantikus szerkezet ⭐
Készíts egy weboldalt (`feladat1.html`) az alábbi szemantikus elemekkel:
- `<header>` – oldal fejléc, címmel
- `<main>` – fő tartalom, legalább 2 bekezdéssel
- `<footer>` – lábléc, szerzői jog szöveggel

## 5.2 – Navigáció és szekciók ⭐
Készíts egy weboldalt (`feladat2.html`), amely tartalmaz:
- `<nav>` elemet legalább 3 menüponttal
- Legalább 2 `<section>` elemet, mindegyik saját `<h2>` címsorral
- `<header>` és `<footer>` elemet

## 5.3 – Blog oldal ⭐⭐
Készíts egy weboldalt (`feladat3.html`) blog szerkezettel:
- `<header>` – blog neve és navigáció (`<nav>`)
- `<main>` – legalább 2 `<article>` elem, mindegyikben:
  - `<h2>` cím
  - `<p>` szöveg
  - Dátum vagy szerző
- `<aside>` – oldalsáv, „Legutóbbi bejegyzések" listával
- `<footer>` – szerzői jog

## 5.4 – Haladó űrlap ⭐⭐
Készíts egy weboldalt (`feladat4.html`) egy regisztrációs űrlappal:
- `<input type="text">` – Teljes név (`required`, `placeholder`)
- `<input type="email">` – Email (`required`)
- `<input type="password">` – Jelszó (`required`)
- `<input type="date">` – Születési dátum
- `<select>` – Ország kiválasztása (legalább 5 opció)
- `<input type="radio">` – Nem választása (Férfi/Nő/Egyéb)
- `<input type="checkbox">` – Felhasználási feltételek elfogadása
- `<button>` – Regisztráció gomb

## 5.5 – Teljes szemantikus oldal ⭐⭐⭐
Készíts egy teljes szemantikus weboldalt (`feladat5.html`) egy képzeletbeli újság számára:
- `<header>` – újság neve (`<h1>`), alcím, navigáció (`<nav>`)
- `<main>`:
  - `<section>` – „Kiemelt hírek" legalább 2 `<article>` elemmel
  - `<section>` – „Vélemények" legalább 1 `<article>` elemmel
- `<aside>` – „Időjárás" és „Hirdetés" szekciók
- `<footer>` – kapcsolat, szerzői jog
- Használj `<figure>`, `<figcaption>`, `<time>` elemeket is

---

## 📚 Kapcsolódó anyagok

Az ehhez a héthez tartozó elméleti anyagot és további gyakorlófeladatokat a kurzus dokumentációjában találod:

- [Heti tananyagok és gyakorlófeladatok](../../doksik/tanulok/README.md)

## Dokumentáció

- [HTML szemantikus elemek](https://www.w3schools.com/html/html5_semantic_elements.asp)
- [HTML article](https://www.w3schools.com/tags/tag_article.asp)
- [HTML section](https://www.w3schools.com/tags/tag_section.asp)
- [HTML form elemek](https://www.w3schools.com/html/html_form_elements.asp)

## Beadás

1. Minden feladatot külön `.html` fájlba írj
2. Commitolj értelmes üzenetekkel
3. `git push` – ez a beadás!
