# 8. hét – Elrendezés és pozícionálás

> **Dokumentáció:** [W3Schools – CSS display](https://www.w3schools.com/css/css_display_visibility.asp) | [CSS position](https://www.w3schools.com/css/css_positioning.asp) | [CSS float](https://www.w3schools.com/css/css_float.asp)

## Display tulajdonság

Meghatározza, hogyan jelenik meg egy elem:

```css
.blokk { display: block; }      /* Teljes sor, új sorban kezdődik */
.inline { display: inline; }     /* Sorban marad, nem tördel */
.ib { display: inline-block; }   /* Sorban marad, DE van szélesség/magasság */
.rejtett { display: none; }      /* Teljesen eltűnik */
```

| Típus | Viselkedés | Példa elemek |
|-------|-----------|-------------|
| `block` | Új sor, teljes szélesség | `<div>`, `<p>`, `<h1>` |
| `inline` | Sorban marad, méret nem állítható | `<span>`, `<a>`, `<strong>` |
| `inline-block` | Sorban marad, méret állítható | Navigációs elemek |

---

## Position

```css
.elem {
    position: static;    /* Alapértelmezett, normál folyam */
    position: relative;  /* A normál helyéhez képest mozgatható */
    position: absolute;  /* A legközelebbi pozícionált szülőhöz képest */
    position: fixed;     /* Az ablakhoz képest rögzített */
    position: sticky;    /* Görgetésig normál, utána rögzített */
}
```

### Relative + absolute példa

```css
.szulo {
    position: relative;
}
.gyerek {
    position: absolute;
    top: 10px;
    right: 10px;
}
```

A gyerek a szülő jobb felső sarkába kerül.

---

## Float

```css
img {
    float: left;
    margin-right: 15px;
}
```

A `float` kiemeli az elemet a normál folyamból – a szöveg körbefolyja.

### Clearfix

Ha egy konténer nem veszi körül a float elemeit:

```css
.clearfix::after {
    content: "";
    display: table;
    clear: both;
}
```

---

## Z-index

Átfedő elemek sorrendjét szabályozza (csak pozícionált elemeken működik):

```css
.elso { z-index: 1; }
.masodik { z-index: 2; }  /* Ez lesz felül */
```
