# 10. hét – Reszponzív design

> **Határidő:** a következő óra előtt
> **Beadás:** commitold és pushold a megoldásaidat ebbe a repoba!
> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz

---

## 10.1 – Viewport meta tag ⭐
Készíts egy weboldalt (`feladat1.html`) és stílusfájlt (`feladat1.css`):
- Viewport meta tag a `<head>`-ben: `<meta name="viewport" content="width=device-width, initial-scale=1.0">`
- Használj relatív egységeket (`%`, `em`, `rem`) a fix méretezés (`px`) helyett
- Egy kép `max-width: 100%` beállítással (reszponzív kép)
- Szöveg `rem` egységben méretezve

## 10.2 – Első media query ⭐
Készíts egy weboldalt (`feladat2.html`) és stílusfájlt (`feladat2.css`):
- Alapértelmezett háttérszín: kék
- 768px alatt: háttérszín piros, betűméret nagyobb
- 480px alatt: háttérszín zöld, szöveg középre igazítva
- Írd ki szövegben is, melyik töréspontnál mit kellene látni

## 10.3 – Reszponzív navigáció ⭐⭐
Készíts egy weboldalt (`feladat3.html`) és stílusfájlt (`feladat3.css`):
- Asztali nézetben: vízszintes navigáció (Flexbox, `row`)
- Mobil nézetben (768px alatt): függőleges navigáció (`flex-direction: column`)
- A menüpontok háttere és mérete változzon a töréspontnál

## 10.4 – Reszponzív kártyák ⭐⭐
Készíts egy weboldalt (`feladat4.html`) és stílusfájlt (`feladat4.css`):
- 4 kártya Flexbox-szal
- Asztali nézetben: 4 kártya egymás mellett
- Tablet nézetben (768px): 2 kártya egy sorban
- Mobil nézetben (480px): 1 kártya egy sorban
- Használj `flex-wrap` és `flex-basis` kombinációt

## 10.5 – Reszponzív tipográfia ⭐⭐
Készíts egy weboldalt (`feladat5.html`) és stílusfájlt (`feladat5.css`):
- `<h1>` betűmérete: 3rem asztali, 2rem tablet, 1.5rem mobil
- `<p>` betűmérete: 1.1rem asztali, 1rem tablet, 0.9rem mobil
- Sortávolság (`line-height`) is változzon a töréspontnál
- Demonstráld a `vw` egységet is egy nagy címsorhoz

## 10.6 – Teljes reszponzív oldal ⭐⭐⭐
Készíts egy weboldalt (`feladat6.html`) és stílusfájlt (`feladat6.css`) teljes reszponzív oldallal:
- Fejléc navigációval (vízszintesből függőlegesre vált)
- Fő tartalom terület: asztali 2 oszlop → mobil 1 oszlop
- Kártyák: asztali 3 → tablet 2 → mobil 1 oszlop
- Képek reszponzívak (`max-width: 100%`)
- Lábléc: asztali 3 oszlop → mobil 1 oszlop
- Legalább 2 töréspontot használj (`@media`)

---

## Dokumentáció

- [CSS reszponzív design](https://www.w3schools.com/css/css_rwd_intro.asp)
- [CSS media query-k](https://www.w3schools.com/css/css_rwd_mediaqueries.asp)
- [CSS viewport](https://www.w3schools.com/css/css_rwd_viewport.asp)
- [CSS egységek](https://www.w3schools.com/css/css_units.asp)

## Beadás

1. Minden feladatot külön `.html` + `.css` fájlpárba írj
2. Commitolj értelmes üzenetekkel
3. `git push` – ez a beadás!
