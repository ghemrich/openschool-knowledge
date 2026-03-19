# 2. hét – Szöveg és listák

> **Dokumentáció:** [W3Schools – HTML szövegformázás](https://www.w3schools.com/html/html_formatting.asp) | [HTML listák](https://www.w3schools.com/html/html_lists.asp)

## Szövegformázás

### Idézetek

```html
<blockquote>Ez egy blokk idézet.</blockquote>
<p>Ahogy <q>Einstein</q> mondta...</p>
```

### Egyéb szövegelemek

| Elem | Jelentés | Példa |
|------|----------|-------|
| `<abbr>` | Rövidítés | `<abbr title="HyperText Markup Language">HTML</abbr>` |
| `<code>` | Kódrészlet | `<code>console.log()</code>` |
| `<pre>` | Előformázott szöveg | Megőrzi a szóközöket és sortöréseket |
| `<sub>` | Alsó index | H`<sub>`2`</sub>`O |
| `<sup>` | Felső index | x`<sup>`2`</sup>` |

---

## Listák

### Rendezetlen lista (felsorolás)

```html
<ul>
    <li>Első elem</li>
    <li>Második elem</li>
    <li>Harmadik elem</li>
</ul>
```

### Rendezett lista (számozott)

```html
<ol>
    <li>Első lépés</li>
    <li>Második lépés</li>
    <li>Harmadik lépés</li>
</ol>
```

### Leíró lista

```html
<dl>
    <dt>HTML</dt>
    <dd>Jelölőnyelv weboldalak készítéséhez</dd>
    <dt>CSS</dt>
    <dd>Stílusleíró nyelv a megjelenés formázásához</dd>
</dl>
```

### Beágyazott listák

Listákon belül további listákat is elhelyezhetsz:

```html
<ul>
    <li>Gyümölcsök
        <ul>
            <li>Alma</li>
            <li>Körte</li>
        </ul>
    </li>
    <li>Zöldségek
        <ul>
            <li>Répa</li>
            <li>Brokkoli</li>
        </ul>
    </li>
</ul>
```
