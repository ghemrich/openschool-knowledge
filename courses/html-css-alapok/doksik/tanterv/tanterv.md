# HTML & CSS Alapok – tanterv

## Kurzus áttekintés

**Cél:** A tanulók elsajátítsák a HTML és CSS webfejlesztés és a Git/GitHub alapjait, és felkészüljenek a szintfelmérő vizsgára.
**Időtartam:** 13 hét (heti 2 óra = 26 óra)
**Vizsga:** 40 pontos szintfelmérő (90 perc, GitHub Classroom-on keresztül)

---

## Szükséges HTML/CSS ismeretek (vizsgakövetelmények alapján)

| Témakör | Vizsga feladat |
|---------|---------------|
| HTML dokumentum szerkezet (`<!DOCTYPE>`, `<html>`, `<head>`, `<body>`) | 1., 2., 3. feladat |
| Szöveges elemek (`<h1>`–`<h6>`, `<p>`, `<span>`, `<strong>`, `<em>`) | 1., 2., 3. feladat |
| Listák (`<ul>`, `<ol>`, `<li>`) | 1., 3. feladat |
| Linkek és képek (`<a>`, `<img>`) | 1., 2., 3. feladat |
| Táblázatok (`<table>`, `<tr>`, `<th>`, `<td>`) | 1. feladat |
| Űrlapok (`<form>`, `<input>`, `<textarea>`, `<select>`, `<button>`) | 2. feladat |
| Szemantikus elemek (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) | 2., 3. feladat |
| CSS szelektorok (elem, osztály, azonosító) | 2., 3. feladat |
| CSS box model (`margin`, `padding`, `border`) | 2., 3. feladat |
| CSS szövegformázás (`color`, `font-family`, `font-size`, `text-align`) | 2., 3. feladat |
| CSS háttér (`background-color`, `background-image`) | 2., 3. feladat |
| Flexbox (`display: flex`, `justify-content`, `align-items`, `gap`) | 3. feladat |
| Reszponzív design (`@media` lekérdezések) | 3. feladat |
| CSS külső fájl (`<link rel="stylesheet">`) | 2., 3. feladat |
| Git alapok, GitHub Classroom | vizsga beadás, házi feladatok |

---

## Heti bontás

### 0. hét – Git és GitHub alapok
**0. óra: Git bevezetés**
- Mi a Git? Mi a GitHub?
- Git telepítés és beállítás (`git config`)
- Alapfogalmak: repository, commit, push, clone
- Alapparancsok: `git add`, `git commit`, `git push`, `git status`
- GitHub Classroom: feladat elfogadása, klónozás, beadás
- Gyakorlat: első repo létrehozása és commit

---

### 1. hét – HTML bevezetés és dokumentum szerkezet
**1. óra: Mi a HTML?**
- A web működése: böngésző, szerver, HTML
- HTML fájl létrehozása VS Code-ban
- Első weboldal: `<!DOCTYPE html>`, `<html>`, `<head>`, `<body>`
- `<title>` és az oldal címe a böngészőben
- Megjegyzések (`<!-- komment -->`)

**2. óra: Alapvető szöveges elemek**
- Címsorok: `<h1>` – `<h6>`
- Bekezdések: `<p>`
- Sortörés: `<br>`, vízszintes vonal: `<hr>`
- Szöveg kiemelés: `<strong>`, `<em>`, `<mark>`
- Gyakorlat: bemutatkozó weboldal készítése

---

### 2. hét – Szöveg és listák
**3. óra: Listák**
- Rendezetlen lista: `<ul>`, `<li>`
- Rendezett lista: `<ol>`, `<li>`
- Beágyazott listák
- Gyakorlat: kedvenc filmek/zenék listája

**4. óra: Szöveg finomítás**
- `<span>` és `<div>` elemek
- Speciális karakterek (`&amp;`, `&lt;`, `&gt;`, `&nbsp;`)
- `<blockquote>` és `<cite>`
- `<code>` és `<pre>` kódblokkok
- Gyakorlat: idézetes, formázott weboldal

---

### 3. hét – Linkek és képek
**5. óra: Linkek**
- `<a href="">` elem
- Abszolút és relatív URL-ek
- Új ablakban megnyitás: `target="_blank"`
- Oldal belső link: `id` és `#`
- Gyakorlat: navigációs menü készítése

**6. óra: Képek**
- `<img src="" alt="">` elem
- Képformátumok: JPG, PNG, SVG, WebP
- Képméretezés: `width`, `height` attribútumok
- `<figure>` és `<figcaption>`
- Gyakorlat: képgaléria oldal

---

### 4. hét – Táblázatok és űrlapok I.
**7. óra: Táblázatok**
- `<table>`, `<tr>`, `<th>`, `<td>`
- Táblázat címe: `<caption>`
- Cellaösszevonás: `colspan`, `rowspan`
- Gyakorlat: órarend vagy árlista táblázat

**8. óra: Űrlapok alapjai**
- `<form>` elem
- `<input>` típusok: `text`, `email`, `password`, `number`
- `<label>` és `for` attribútum
- `<textarea>`, `<button>`
- Gyakorlat: egyszerű kapcsolatfelvételi űrlap

---

### 5. hét – Űrlapok II. és szemantikus HTML
**9. óra: Haladó űrlapelemek**
- `<select>` és `<option>` legördülő lista
- `<input type="checkbox">` és `<input type="radio">`
- `<input type="date">`, `<input type="range">`
- `required`, `placeholder`, `value` attribútumok
- Gyakorlat: regisztrációs űrlap

**10. óra: Szemantikus HTML**
- Mi a szemantikus HTML és miért fontos?
- `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<aside>`, `<footer>`
- Az oldal felépítése szemantikus elemekkel
- Gyakorlat: blog oldal szemantikus szerkezettel

---

### 6. hét – CSS bevezetés
**11. óra: CSS alapok**
- Mi a CSS? Hogyan kapcsolódik a HTML-hez?
- CSS beágyazás módjai: inline, belső (`<style>`), külső (`<link>`)
- CSS szintaxis: szelektor, tulajdonság, érték
- Elem szelektor, osztály szelektor (`.`), azonosító szelektor (`#`)
- Gyakorlat: meglévő HTML oldal színezése

**12. óra: Színek és szövegformázás**
- Színek: névvel, hex (`#FF5733`), RGB (`rgb()`), HSL
- `color`, `background-color`
- `font-family`, `font-size`, `font-weight`, `font-style`
- `text-align`, `text-decoration`, `text-transform`
- `line-height`, `letter-spacing`
- Gyakorlat: tipográfiai stíluslap készítése

---

### 7. hét – CSS box modell
**13. óra: A box modell**
- Minden elem egy doboz: content, padding, border, margin
- `width`, `height`, `max-width`
- `padding` (rövidített és egyedi oldalak)
- `border` (szín, vastagság, stílus, lekerekítés: `border-radius`)
- Gyakorlat: kártyák készítése szegéllyel és paddingal

**14. óra: Margin és elrendezés alapok**
- `margin` (rövidített és egyedi oldalak)
- Margin összeomlás (collapse)
- `box-sizing: border-box` és miért fontos
- `display: block`, `display: inline`, `display: inline-block`
- Gyakorlat: fejléc és lábléc formázása

---

### 8. hét – CSS elrendezés és pozícionálás
**15. óra: Pozícionálás**
- `position: static`, `relative`, `absolute`, `fixed`, `sticky`
- `top`, `right`, `bottom`, `left`
- `z-index`
- Gyakorlat: rögzített navigáció és vissza-a-tetejére gomb

**16. óra: Float és clearfix**
- `float: left`, `float: right`
- `clear: both`
- `overflow` tulajdonság
- Mikor használjunk float-ot (és mikor ne)
- Gyakorlat: kép körüli szöveg tördelése

---

### 9. hét – Flexbox
**17. óra: Flexbox alapok**
- `display: flex`
- Főtengely és kereszttengely
- `flex-direction`, `justify-content`, `align-items`
- `gap`
- Gyakorlat: navigációs sáv Flexbox-szal

**18. óra: Flexbox haladó**
- `flex-wrap`
- `flex-grow`, `flex-shrink`, `flex-basis`
- `align-self`, `order`
- Gyakorlat: kártya elrendezés (termék kártyák egymás mellett)

---

### 10. hét – Reszponzív design
**19. óra: Media query-k**
- Mi a reszponzív design?
- `<meta name="viewport">`
- `@media` lekérdezések: `min-width`, `max-width`
- Mobile-first megközelítés
- Gyakorlat: navigáció átalakítása mobilra

**20. óra: Reszponzív minták**
- Relatív egységek: `%`, `em`, `rem`, `vw`, `vh`
- Reszponzív képek: `max-width: 100%`
- Reszponzív tipográfia
- Gyakorlat: korábban készített oldal reszponzívvá tétele

---

### 11. hét – CSS haladó témák és projekt
**21. óra: Dekoráció és vizuális effektek**
- `box-shadow`, `text-shadow`
- `opacity` és `rgba()`/`hsla()` átlátszóság
- `transition` (egyszerű animáció hover-re)
- CSS változók (`--szin-elsodleges`, `var()`)
- Gyakorlat: interaktív gombok és kártyák hover effektekkel

**22. óra: Komplex feladat – teljes weboldal**
- Fejléc navigációval
- Fő tartalom szekciókkal
- Kártya elrendezés Flexbox-szal
- Lábléc
- Reszponzív design
- **Gyakorlat: teljes vizsgafeladat megoldása lépésről lépésre**

---

### 12. hét – Vizsgafelkészítés
**23. óra: Próbavizsga**
- Teljes vizsga szimulálása (90 perc, 40 pont)
- Vizsga körülmények között dolgozás
- Önellenőrzés az értékelési rubrika alapján

**24. óra: Próbavizsga megbeszélése és kérdések**
- Közös megoldás áttekintése
- Tipikus hibák megbeszélése
- Utolsó kérdések, hiánypótlás

---

## Értékelés

| Elem | Arány |
|------|-------|
| Házi feladatok | 25% |
| Órai munka, gyakorlatok | 15% |
| Próbavizsga | 10% |
| Szintfelmérő vizsga (40 pont) | 50% |

---

## Ajánlott eszközök

- **Szerkesztő:** VS Code (Live Server kiegészítővel)
- **Böngésző:** Google Chrome vagy Firefox (Fejlesztői eszközök: F12)
- **Git:** 2.x+ (Windows: [git-scm.com](https://git-scm.com))
- **Operációs rendszer:** Windows 10+, Linux vagy macOS
- **GitHub fiók:** minden tanulónak kell (ingyenes)
- **Segédanyagok:** órai kódpéldák a `doksik/tanulok/` mappában

> **VS Code tipp:** A Live Server kiegészítő telepítése után jobb klikk az `index.html`-re → „Open with Live Server" – automatikus frissítés minden mentésnél.
