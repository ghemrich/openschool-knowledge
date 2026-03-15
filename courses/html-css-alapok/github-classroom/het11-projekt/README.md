# 11. hét – Haladó CSS és projekt

> **Határidő:** a következő óra előtt
> **Beadás:** commitold és pushold a megoldásaidat ebbe a repoba!
> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz

---

## 11.1 – Hover effektek ⭐
Készíts egy weboldalt (`feladat1.html`) és stílusfájlt (`feladat1.css`):
- 3 gomb (link vagy button), mindegyik más hover effekttel:
  1. Háttérszín változás hover-re
  2. Szövegszín és aláhúzás változás hover-re
  3. Szegélyszín változás hover-re
- Használj `transition` tulajdonságot a sima animációhoz

## 11.2 – Box shadow és text shadow ⭐
Készíts egy weboldalt (`feladat2.html`) és stílusfájlt (`feladat2.css`):
- 3 kártya, mindegyik más `box-shadow` stílussal (enyhe, közepes, erős)
- Egy nagy címsor `text-shadow` effekttel
- Az árnyékok hover-re változzanak (`transition`)

## 11.3 – CSS változók ⭐⭐
Készíts egy weboldalt (`feladat3.html`) és stílusfájlt (`feladat3.css`):
- Definiálj legalább 4 CSS változót a `:root`-ban:
  - `--szin-elsodleges`, `--szin-masodlagos`, `--szin-hatter`, `--betucsalad`
- Használd a változókat `var()` segítségével az egész oldalon
- Demonstráld, hogy 1 helyen változtatva az egész oldal színvilága megváltozik

## 11.4 – Átlátszóság és átmenetek ⭐⭐
Készíts egy weboldalt (`feladat4.html`) és stílusfájlt (`feladat4.css`):
- Egy képgaléria (legalább 4 kép), ahol hover-re:
  - A kép `opacity` változik (0.7 → 1)
  - Egy szöveg overlay jelenik meg a képen (átlátszó háttérrel: `rgba()`)
- `transition: all 0.3s ease` használata a sima animációkhoz

## 11.5 – Teljes weboldal projekt ⭐⭐⭐
Készíts egy teljes weboldalt (`index.html`) és stílusfájlt (`style.css`) egy képzeletbeli cégnek. Az oldal tartalmazzon:
- **Fejléc:** logó (szöveg) + navigáció (Flexbox)
- **Hős szekció:** nagy háttérszín, nagy címsor, alcím, CTA gomb
- **Szolgáltatások szekció:** 3 kártya Flexbox-szal, ikonokkal (emoji is elfogadott)
- **Rólunk szekció:** szöveg és kép egymás mellett (Flexbox)
- **Kapcsolat szekció:** egyszerű űrlap (név, email, üzenet)
- **Lábléc:** 3 oszlop (Flexbox), szerzői jog
- **CSS követelmények:**
  - Külső CSS fájl
  - CSS változók (`--szin-elsodleges`, stb.)
  - Flexbox elrendezés
  - Hover effektek `transition`-nel
  - Reszponzív design legalább 1 `@media` törésponttal
  - `box-shadow` legalább egy elemen

---

## Dokumentáció

- [CSS shadow](https://www.w3schools.com/css/css3_shadows.asp)
- [CSS transition](https://www.w3schools.com/css/css3_transitions.asp)
- [CSS opacity](https://www.w3schools.com/css/css_image_transparency.asp)
- [CSS változók](https://www.w3schools.com/css/css3_variables.asp)
- [CSS hover](https://www.w3schools.com/css/css_pseudo_classes.asp)

## Beadás

1. Minden feladatot külön fájlba/fájlpárba írj
2. Commitolj értelmes üzenetekkel
3. `git push` – ez a beadás!
