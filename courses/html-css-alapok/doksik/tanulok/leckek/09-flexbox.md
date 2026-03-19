# 9. hét – Flexbox

> **Dokumentáció:** [W3Schools – CSS Flexbox](https://www.w3schools.com/css/css3_flexbox.asp) | [MDN – Flexbox útmutató](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_flexible_box_layout/Basic_concepts_of_flexbox)

## Mi a Flexbox?

A Flexbox egy modern elrendezési rendszer, ami megkönnyíti az elemek sorba vagy oszlopba rendezését. Különösen hasznos navigációk, kártyaelrendezések és központozás megvalósításához.

---

## Alapfogalmak

A Flexbox két szereplővel dolgozik:
- **Flex container** – a szülő elem (`display: flex`)
- **Flex items** – a gyerek elemek

```css
.kontener {
    display: flex;
}
```

---

## Fő tengely irány (flex-direction)

```css
.kontener {
    flex-direction: row;            /* Vízszintes (alapértelmezett) */
    flex-direction: row-reverse;    /* Vízszintes, fordított */
    flex-direction: column;         /* Függőleges */
    flex-direction: column-reverse; /* Függőleges, fordított */
}
```

## Igazítás a fő tengelyen (justify-content)

```css
.kontener {
    justify-content: flex-start;    /* Balra (alapértelmezett) */
    justify-content: flex-end;      /* Jobbra */
    justify-content: center;        /* Középre */
    justify-content: space-between; /* Egyenlő távolság elemek között */
    justify-content: space-around;  /* Egyenlő margó elemek körül */
    justify-content: space-evenly;  /* Teljesen egyenlő elosztás */
}
```

## Igazítás a kereszt tengelyen (align-items)

```css
.kontener {
    align-items: stretch;     /* Kitöltés (alapértelmezett) */
    align-items: flex-start;  /* Felülre */
    align-items: flex-end;    /* Alulra */
    align-items: center;      /* Középre */
}
```

---

## Flex items tulajdonságai

```css
.elem {
    flex-grow: 1;     /* Arányos növekedés */
    flex-shrink: 0;   /* Ne zsugorodjon */
    flex-basis: 200px; /* Alap méret */
    flex: 1;          /* Rövidítés: grow 1, shrink 1, basis 0 */
}
```

## Sortörés (flex-wrap)

```css
.kontener {
    flex-wrap: wrap;    /* Új sorba tördel, ha nem fér el */
    flex-wrap: nowrap;  /* Egy sorban marad (alapértelmezett) */
}
```

## Gap

```css
.kontener {
    gap: 20px;         /* Elemek közötti távolság */
    gap: 10px 20px;    /* Sor- és oszlopköz külön */
}
```

---

## Gyakori minták

### Vízszintes és függőleges középre igazítás

```css
.kontener {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
}
```

### Navigációs sáv

```css
nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px 20px;
}
```
