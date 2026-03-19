# Feladatok – 9. hét: Flexbox

> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz
> A megoldásokat commitold és pushold a GitHub repódba.

---

### 9.1 – Flexbox alapok ⭐
Készíts egy konténert 4 dobozzal, amelyek vízszintesen egymás mellett helyezkednek el `display: flex` segítségével. Próbáld ki a `justify-content` különböző értékeit (`flex-start`, `center`, `space-between`, `space-around`).

### 9.2 – Navigáció Flexbox-szal ⭐
Készíts egy vízszintes navigációs sávot Flexbox-szal. A logó legyen bal oldalon, a menüpontok jobb oldalon (`justify-content: space-between`).

### 9.3 – Kártya rács ⭐⭐
Készíts egy kártya rácsot Flexbox-szal, ahol:
- A kártyák sorba rendeződnek
- Automatikusan törnek új sorba (`flex-wrap: wrap`)
- Egyforma szélességűek (`flex-basis`)
- Egyenletes a térköz (`gap`)

### 9.4 – Középre igazítás ⭐⭐
Készíts egy oldalt, ahol a tartalom vízszintesen és függőlegesen is középre van igazítva a képernyőn (`justify-content: center` + `align-items: center` + `min-height: 100vh`).

### 9.5 – Dashboard elrendezés ⭐⭐⭐
Készíts egy dashboard (vezérlőpult) oldalt Flexbox-szal:
- Fejléc teljes szélességben
- Bal oldali sidebar fix szélességgel
- Fő tartalmi terület, ami kitölti a maradék helyet (`flex: 1`)
- A fő területen kártya rácsban jelennek meg statisztikák
- Lábléc teljes szélességben
