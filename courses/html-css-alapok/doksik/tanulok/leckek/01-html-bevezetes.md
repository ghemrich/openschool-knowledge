# 1. hét – HTML bevezetés és dokumentum szerkezet

> **Dokumentáció:** [W3Schools – HTML bevezető](https://www.w3schools.com/html/html_intro.asp) | [HTML elemek](https://www.w3schools.com/html/html_elements.asp) | [HTML attribútumok](https://www.w3schools.com/html/html_attributes.asp)

## Mi a HTML?

A **HTML** (HyperText Markup Language) a weboldalak alapja. Meghatározza a weboldal **szerkezetét** és **tartalmát**. A HTML nem programozási nyelv, hanem jelölőnyelv (markup language).

---

## HTML dokumentum felépítése

Minden HTML fájl ezzel a szerkezettel kezdődik:

```html
<!DOCTYPE html>
<html lang="hu">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Az oldal címe</title>
</head>
<body>
    <h1>Üdvözöllek!</h1>
    <p>Ez az első weboldalam.</p>
</body>
</html>
```

| Elem | Szerepe |
|------|---------|
| `<!DOCTYPE html>` | HTML5 dokumentum jelölése |
| `<html>` | A dokumentum gyökéreleme |
| `<head>` | Metaadatok (cím, kódolás) |
| `<body>` | A látható tartalom |

---

## Címsorok

A HTML 6 szintű címsort biztosít:

```html
<h1>Főcím</h1>
<h2>Alcím</h2>
<h3>Al-alcím</h3>
```

> Az `<h1>` a legfontosabb, az `<h6>` a legkisebb. Egy oldalon általában egyetlen `<h1>` van.

## Bekezdések és formázás

```html
<p>Ez egy bekezdés.</p>
<p>Ez egy <strong>félkövér</strong> és egy <em>dőlt</em> szöveg.</p>
<p>Ez egy <mark>kiemelt</mark> szöveg.</p>
<hr>
<p>Elválasztó vonal fölött és <br> sortörés után.</p>
```

| Elem | Hatás |
|------|-------|
| `<strong>` | **Félkövér** (fontos) |
| `<em>` | *Dőlt* (hangsúlyos) |
| `<mark>` | Kiemelt háttér |
| `<hr>` | Vízszintes elválasztó vonal |
| `<br>` | Sortörés |

---

## Hogyan próbáld ki?

1. Nyiss egy szövegszerkesztőt (VS Code ajánlott)
2. Mentsd el a fájlt `.html` kiterjesztéssel (pl. `index.html`)
3. Nyisd meg a fájlt böngészőben (dupla kattintás)
