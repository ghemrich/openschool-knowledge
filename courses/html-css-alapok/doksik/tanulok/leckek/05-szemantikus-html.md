# 5. hét – Szemantikus HTML és haladó űrlapok

> **Dokumentáció:** [W3Schools – Szemantikus elemek](https://www.w3schools.com/html/html5_semantic_elements.asp) | [MDN – HTML elemek referencia](https://developer.mozilla.org/hu/docs/Web/HTML/Element)

## Miért fontos a szemantikus HTML?

A szemantikus elemek nem csak megjelenítik, hanem **jelentéssel** látják el a tartalmat:
- **Akadálymentesség**: A képernyőolvasók jobban értelmezik az oldalt
- **SEO**: A keresőmotorok jobban indexelik a tartalmat
- **Karbantarthatóság**: A kód olvashatóbb fejlesztők számára

---

## Szemantikus elemek

```html
<header>
    <nav>
        <a href="/">Főoldal</a>
        <a href="/rolunk">Rólunk</a>
    </nav>
</header>

<main>
    <article>
        <h2>Cikk címe</h2>
        <p>Cikk tartalma...</p>
    </article>

    <aside>
        <h3>Kapcsolódó linkek</h3>
        <ul>
            <li><a href="#">Link 1</a></li>
        </ul>
    </aside>
</main>

<footer>
    <p>&copy; 2026 Iskola neve</p>
</footer>
```

| Elem | Szerepe |
|------|---------|
| `<header>` | Oldal vagy szekció fejléce |
| `<nav>` | Navigációs linkek |
| `<main>` | Az oldal fő tartalma (egyszer szerepel) |
| `<article>` | Önálló tartalom (cikk, bejegyzés) |
| `<section>` | Tematikus szekció |
| `<aside>` | Kiegészítő tartalom (oldalsáv) |
| `<footer>` | Lábléc |
| `<figure>` / `<figcaption>` | Kép és képaláírás |

---

## Haladó űrlap elemek

### Validáció attribútumok

```html
<input type="text" required minlength="3" maxlength="50">
<input type="number" min="1" max="100" step="1">
<input type="email" placeholder="pelda@email.hu">
<input type="text" pattern="[A-Za-z]{3,}" title="Legalább 3 betű">
```

| Attribútum | Hatás |
|-----------|-------|
| `required` | Kötelező mező |
| `placeholder` | Halvány útmutató szöveg |
| `minlength` / `maxlength` | Szöveg hossz korlát |
| `min` / `max` | Szám korlát |
| `pattern` | Regex minta validáció |

### Fieldset és legend

```html
<fieldset>
    <legend>Személyes adatok</legend>
    <label for="nev">Név:</label>
    <input type="text" id="nev" name="nev">
</fieldset>
```
