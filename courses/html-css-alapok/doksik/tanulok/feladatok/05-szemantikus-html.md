# Feladatok – 5. hét: Szemantikus HTML

> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz
> A megoldásokat commitold és pushold a GitHub repódba.

---

### 5.1 – Szemantikus szerkezet ⭐
Készíts egy oldalt, amely tartalmazza az összes fő szemantikus elemet: `<header>`, `<nav>`, `<main>`, `<article>`, `<section>`, `<aside>`, `<footer>`. Mindegyikbe írj rövid szöveget, ami elmagyarázza a funkciójukat.

### 5.2 – Blog oldal ⭐
Készíts egy blog oldalt, ahol:
- A `<header>`-ben van a blog neve és navigáció
- A `<main>`-ben legalább 2 bejegyzés van `<article>`-ként
- Az `<aside>` tartalmaz egy „Népszerű bejegyzések" listát
- A `<footer>`-ben van szerzői jogi szöveg

### 5.3 – Validált űrlap ⭐⭐
Készíts egy rendelési űrlapot HTML5 validációval:
- Kötelező mezők (`required`)
- E-mail mező (`type="email"`)
- Szám mező min-max értékkel (`type="number"`, `min`, `max`)
- Minta illeszkedés (`pattern`) telefonszámra
- `placeholder` szöveg minden mezőn

### 5.4 – Híroldal ⭐⭐
Készíts egy híroldal főoldalt, ahol:
- Minden hír egy `<article>` elemben van
- Mindegyiknek van `<header>` (cím, szerző, dátum) és `<footer>` (kategória) része
- Van egy `<aside>` szekció legfrissebb hírekkel

### 5.5 – Akadálymentes űrlap ⭐⭐⭐
Készíts egy komplex űrlapot, amely minden beviteli elemhez `<label>`-t használ (`for` attribútummal), a mezők `<fieldset>` és `<legend>` elemekkel vannak csoportosítva, és a validáció HTML5 attribútumokkal működik.
