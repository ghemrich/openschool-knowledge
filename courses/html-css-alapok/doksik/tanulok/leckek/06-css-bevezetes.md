# 6. hét – CSS bevezetés

> **Dokumentáció:** [W3Schools – CSS bevezető](https://www.w3schools.com/css/css_intro.asp) | [CSS szelektorok](https://www.w3schools.com/css/css_selectors.asp) | [CSS színek](https://www.w3schools.com/css/css_colors.asp)

## Mi a CSS?

A **CSS** (Cascading Style Sheets) a weboldal **megjelenését** formázza. A HTML a szerkezetet, a CSS a stílust adja.

---

## CSS hozzáadásának módjai

### 1. Inline stílus (elemen belül)

```html
<p style="color: red; font-size: 20px;">Piros szöveg</p>
```

### 2. Belső stíluslap (`<style>` elemben)

```html
<head>
    <style>
        p { color: blue; }
    </style>
</head>
```

### 3. Külső stíluslap (ajánlott!)

```html
<head>
    <link rel="stylesheet" href="style.css">
</head>
```

```css
/* style.css */
p {
    color: green;
    font-size: 16px;
}
```

> **Ajánlás:** Mindig külső stíluslapot használj – ez a legtisztább és legkarbantarthatóbb megoldás.

---

## CSS szelektorok

A szelektorok meghatározzák, melyik elemekre vonatkozik a stílus:

```css
/* Elem szelektor */
h1 { color: navy; }

/* Osztály szelektor (.) */
.kiemelt { background-color: yellow; }

/* ID szelektor (#) */
#fejlec { font-size: 24px; }

/* Csoport szelektor */
h1, h2, h3 { font-family: Arial; }
```

```html
<h1>Elem szelektor</h1>
<p class="kiemelt">Osztály szelektor</p>
<div id="fejlec">ID szelektor</div>
```

---

## Szín megadási módok

```css
p { color: red; }               /* Névvel */
p { color: #FF0000; }           /* Hexadecimális */
p { color: rgb(255, 0, 0); }    /* RGB */
```

## Alapvető tulajdonságok

| Tulajdonság | Leírás | Példa |
|------------|--------|-------|
| `color` | Szöveg színe | `color: #333;` |
| `background-color` | Háttérszín | `background-color: #f0f0f0;` |
| `font-size` | Betűméret | `font-size: 18px;` |
| `font-family` | Betűtípus | `font-family: Arial, sans-serif;` |
| `text-align` | Szöveg igazítás | `text-align: center;` |
| `font-weight` | Betűvastagság | `font-weight: bold;` |
