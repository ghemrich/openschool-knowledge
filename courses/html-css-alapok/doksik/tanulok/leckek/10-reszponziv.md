# 10. hét – Reszponzív design

> **Dokumentáció:** [W3Schools – Reszponzív design](https://www.w3schools.com/css/css_rwd_intro.asp) | [CSS media queries](https://www.w3schools.com/css/css_rwd_mediaqueries.asp) | [Viewport](https://www.w3schools.com/css/css_rwd_viewport.asp)

## Mi a reszponzív design?

A reszponzív (responsive) design azt jelenti, hogy a weboldal **minden képernyőméreten** jól néz ki és jól használható – mobilon, tableten és asztali gépen egyaránt.

---

## Viewport meta tag

Minden reszponzív oldal `<head>`-jében kell:

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

Ez biztosítja, hogy a böngésző a készülék szélességéhez igazítsa az oldalt.

---

## Media queries

A `@media` lekérdezések feltételes stílusokat alkalmaznak:

```css
/* Alapértelmezett (minden méret) */
.kontener {
    width: 100%;
    padding: 20px;
}

/* Tablet (768px felett) */
@media (min-width: 768px) {
    .kontener {
        width: 750px;
        margin: 0 auto;
    }
}

/* Asztali (1024px felett) */
@media (min-width: 1024px) {
    .kontener {
        width: 960px;
    }
}
```

### Gyakori töréspontok

| Méret | Eszköz | Töréspont |
|-------|--------|-----------|
| < 576px | Mobil | Alapértelmezett |
| ≥ 768px | Tablet | `@media (min-width: 768px)` |
| ≥ 1024px | Asztali | `@media (min-width: 1024px)` |

---

## Mobile-first megközelítés

Először a mobil stílusokat írd meg, majd `min-width` media query-kkel bővítsd nagyobb méretekre:

```css
/* Mobil (alapértelmezett) */
.grid {
    display: flex;
    flex-direction: column;
}

/* Tablet: 2 oszlop */
@media (min-width: 768px) {
    .grid {
        flex-direction: row;
        flex-wrap: wrap;
    }
    .grid > * {
        width: 50%;
    }
}

/* Asztali: 3 oszlop */
@media (min-width: 1024px) {
    .grid > * {
        width: 33.33%;
    }
}
```

---

## Reszponzív képek

```css
img {
    max-width: 100%;
    height: auto;
}
```

## Reszponzív betűméret

```css
h1 {
    font-size: 1.5rem;  /* Mobil */
}

@media (min-width: 768px) {
    h1 {
        font-size: 2.5rem;  /* Tablet és asztali */
    }
}
```
