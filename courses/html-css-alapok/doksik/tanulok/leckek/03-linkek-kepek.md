# 3. hét – Linkek és képek

> **Dokumentáció:** [W3Schools – HTML linkek](https://www.w3schools.com/html/html_links.asp) | [HTML képek](https://www.w3schools.com/html/html_images.asp)

## Linkek (hiperhivatkozások)

Az `<a>` elem hivatkozásokat hoz létre:

```html
<a href="https://www.w3schools.com">W3Schools</a>
<a href="masik-oldal.html">Másik oldal</a>
<a href="#szekció">Ugrás a szekcióra</a>
```

### Link attribútumok

| Attribútum | Jelentés |
|-----------|----------|
| `href` | A link célja (URL vagy fájlnév) |
| `target="_blank"` | Új lapon nyílik meg |
| `title` | Tooltip szöveg (rámutatáskor jelenik meg) |

### Belső linkek (horgonyok)

```html
<h2 id="rolam">Rólam</h2>
<!-- ... tartalom ... -->
<a href="#rolam">Vissza a Rólam részhez</a>
```

---

## Képek

Az `<img>` elem képeket jelenít meg:

```html
<img src="kep.jpg" alt="Leírás a képről" width="300">
```

| Attribútum | Jelentés |
|-----------|----------|
| `src` | A kép elérési útja |
| `alt` | Alternatív szöveg (ha a kép nem tölt be, vagy képernyőolvasónak) |
| `width` / `height` | Méret pixelben |

> **Fontos:** Mindig adj `alt` szöveget! Ez segíti a látássérült felhasználókat és javítja a SEO-t.

### Relatív és abszolút útvonalak

```html
<!-- Relatív: ugyanabban a mappában -->
<img src="logo.png" alt="Logo">

<!-- Relatív: almappában -->
<img src="kepek/foto.jpg" alt="Fotó">

<!-- Abszolút: teljes URL -->
<img src="https://example.com/kep.jpg" alt="Külső kép">
```

---

## Kép mint link

```html
<a href="https://example.com">
    <img src="logo.png" alt="Kattints ide">
</a>
```
