# 9. hét – Flexbox

> **Határidő:** a következő óra előtt
> **Beadás:** commitold és pushold a megoldásaidat ebbe a repoba!
> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz

---

Ezen a héten megismerkedsz a Flexbox elrendezési rendszerrel, ami jelentősen megkönnyíti az elemek sorba vagy oszlopba rendezését. A Flexbox a modern webdesign egyik legfontosabb eszköze.

---

## 9.1 – Flexbox alapok ⭐
Készíts egy weboldalt (`feladat1.html`) és stílusfájlt (`feladat1.css`):
- Egy szülő `<div>` (`display: flex`), benne 4 színes doboz
- `justify-content: space-between` beállítás
- Minden doboznak legyen `padding`, `border`, és szín

## 9.2 – Flex irány ⭐
Készíts egy weboldalt (`feladat2.html`) és stílusfájlt (`feladat2.css`):
- 4 példa konténer, mindegyikben 3 doboz:
  1. `flex-direction: row` (alapértelmezett)
  2. `flex-direction: row-reverse`
  3. `flex-direction: column`
  4. `flex-direction: column-reverse`
- Írd minden konténer fölé szövegként, melyik irány van beállítva

## 9.3 – Navigációs sáv ⭐⭐
Készíts egy weboldalt (`feladat3.html`) és stílusfájlt (`feladat3.css`) navigációs sávval:
- `<nav>` elem `display: flex` beállítással
- A logó balra, a menüpontok jobbra (`justify-content: space-between`)
- A menüpontok listából (`<ul>`, `<li>`) legyenek, Flexbox-szal vízszintesen
- `gap` használata a menüpontok közötti térhez

## 9.4 – Kártya elrendezés ⭐⭐
Készíts egy weboldalt (`feladat4.html`) és stílusfájlt (`feladat4.css`):
- Legalább 6 kártya `display: flex` és `flex-wrap: wrap` használatával
- Minden kártya fix szélesség (`flex-basis: 300px`) vagy `flex: 1 1 300px`
- `gap` a kártyák között
- Minden kártya tartalmazzon képet (placeholdert), címet és leírást

## 9.5 – Középre igazítás ⭐⭐
Készíts egy weboldalt (`feladat5.html`) és stílusfájlt (`feladat5.css`):
- Egy teljes képernyős konténer (`min-height: 100vh`)
- Benne egy tartalom doboz, ami vízszintesen ÉS függőlegesen is középre van igazítva (`justify-content: center; align-items: center`)
- A doboz tartalmazzon címsort, bekezdést és gombot

## 9.6 – Teljes oldal Flexbox-szal ⭐⭐⭐
Készíts egy weboldalt (`feladat6.html`) és stílusfájlt (`feladat6.css`) teljes oldal elrendezéssel, kizárólag Flexbox használatával:
- Fejléc logóval és navigációval (Flexbox egy sorban)
- Fő tartalom terület két oszloppal: tartalom (70%) és oldalsáv (30%) – Flexbox-szal
- A fő tartalom 3 kártyát tartalmaz (Flexbox, `flex-wrap`)
- Lábléc 3 oszloppal (Flexbox)
- Az egész oldal `min-height: 100vh`, a lábléc mindig alul (`flex-grow` a fő tartalmon)

---

## 📚 Kapcsolódó anyagok

Az ehhez a héthez tartozó elméleti anyagot és további gyakorlófeladatokat a kurzus dokumentációjában találod:

- [Heti tananyagok és gyakorlófeladatok](../../doksik/tanulok/README.md)

## Dokumentáció

- [CSS Flexbox](https://www.w3schools.com/css/css3_flexbox.asp)
- [Flexbox konténer](https://www.w3schools.com/css/css3_flexbox_container.asp)
- [Flexbox elemek](https://www.w3schools.com/css/css3_flexbox_items.asp)
- [Flexbox Froggy játék](https://flexboxfroggy.com/) – interaktív gyakorlás

## Beadás

1. Minden feladatot külön `.html` + `.css` fájlpárba írj
2. Commitolj értelmes üzenetekkel
3. `git push` – ez a beadás!
