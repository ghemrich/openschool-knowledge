# 4. hét – Táblázatok és űrlapok

> **Dokumentáció:** [W3Schools – HTML táblázatok](https://www.w3schools.com/html/html_tables.asp) | [HTML űrlapok](https://www.w3schools.com/html/html_forms.asp)

## Táblázatok

### Alap táblázat

```html
<table>
    <tr>
        <th>Név</th>
        <th>Kor</th>
        <th>Város</th>
    </tr>
    <tr>
        <td>Anna</td>
        <td>17</td>
        <td>Budapest</td>
    </tr>
    <tr>
        <td>Péter</td>
        <td>16</td>
        <td>Debrecen</td>
    </tr>
</table>
```

| Elem | Jelentés |
|------|---------|
| `<table>` | Táblázat konténer |
| `<tr>` | Sor (table row) |
| `<th>` | Fejléc cella (félkövér, középre zárt) |
| `<td>` | Adat cella |

### Cella összevonás

```html
<td colspan="2">Két oszlopot foglal el</td>
<td rowspan="3">Három sort foglal el</td>
```

---

## Űrlapok

Az űrlapok segítségével a felhasználó adatokat küldhet:

```html
<form action="/feldolgozas" method="POST">
    <label for="nev">Név:</label>
    <input type="text" id="nev" name="nev" required>

    <label for="email">Email:</label>
    <input type="email" id="email" name="email">

    <button type="submit">Küldés</button>
</form>
```

### Input típusok

| Típus | Megjelenés |
|-------|-----------|
| `text` | Egysoros szöveges mező |
| `email` | Email cím (validációval) |
| `password` | Jelszó mező (rejtett karakterek) |
| `number` | Szám bevitel |
| `date` | Dátumválasztó |
| `checkbox` | Jelölőnégyzet |
| `radio` | Rádiógomb (egy választható) |
| `submit` | Küldés gomb |

### Textarea és select

```html
<textarea name="uzenet" rows="4" cols="50" placeholder="Írd ide az üzeneted..."></textarea>

<select name="varos">
    <option value="bp">Budapest</option>
    <option value="db">Debrecen</option>
    <option value="sz">Szeged</option>
</select>
```
