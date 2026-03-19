# 7. hét – CSS box modell

> **Dokumentáció:** [W3Schools – CSS box modell](https://www.w3schools.com/css/css_boxmodel.asp) | [CSS margin](https://www.w3schools.com/css/css_margin.asp) | [CSS padding](https://www.w3schools.com/css/css_padding.asp)

## A box modell

Minden HTML elem egy „doboz", ami 4 rétegből áll (belülről kifelé):

1. **Content** – a tényleges tartalom (szöveg, kép)
2. **Padding** – belső margó (tartalom és szegély között)
3. **Border** – szegély
4. **Margin** – külső margó (elemek közötti távolság)

```
┌──────────────────────── margin ─────────────────────────┐
│  ┌───────────────────── border ──────────────────────┐  │
│  │  ┌────────────────── padding ─────────────────┐   │  │
│  │  │                                            │   │  │
│  │  │              TARTALOM                      │   │  │
│  │  │                                            │   │  │
│  │  └────────────────────────────────────────────┘   │  │
│  └───────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────┘
```

---

## Margin és padding

```css
.doboz {
    margin: 20px;           /* mind a 4 oldalon */
    margin: 10px 20px;      /* fent-lent | jobb-bal */
    margin: 10px 20px 30px 40px; /* fent | jobb | lent | bal */

    padding: 15px;
    padding-top: 10px;
    padding-left: 20px;
}
```

> **Tipp:** `margin: 0 auto;` vízszintesen középre igazítja az elemet (ha van megadott szélessége).

## Border

```css
.doboz {
    border: 2px solid black;
    border-radius: 10px;     /* lekerekített sarkok */
}
```

## Width és height

```css
.doboz {
    width: 300px;
    height: 200px;
}
```

---

## Box-sizing

Alapértelmezetten a `width` csak a tartalomra vonatkozik. A `border-box` beállítással a padding és border beleszámít:

```css
* {
    box-sizing: border-box;
}
```

> **Ajánlás:** Mindig használd a `box-sizing: border-box` beállítást – sokkal kiszámíthatóbb elrendezést ad.
