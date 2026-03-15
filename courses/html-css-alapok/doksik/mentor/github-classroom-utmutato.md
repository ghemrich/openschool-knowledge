# GitHub Classroom útmutató – HTML & CSS Alapok

## 1. Szervezet és kurzus létrehozása

### GitHub szervezet (Organization)
1. GitHub → Settings → Organizations → New organization
2. Név: pl. `openschool-html-css-alapok-2026`
3. Terv: Free (oktatási célokra elegendő)

### GitHub Classroom kurzus
1. [classroom.github.com](https://classroom.github.com) → New classroom
2. Válaszd ki a szervezetet
3. Adj nevet a kurzusnak: pl. „HTML CSS Alapok – 2026 tavasz"
4. Hívd meg a tanulókat (roster)

---

## 2. Template repók

A template repók a `github-classroom/` mappában találhatók. Minden héthez és vizsgavariánshoz van egy.

### Heti házi feladatok

| Hét | Template mappa | Téma |
|-----|---------------|------|
| 0 | `het00-git-alapok/` | Git alapok |
| 1 | `het01-html-bevezetes/` | HTML bevezetés |
| 2 | `het02-szoveg-listak/` | Szöveg és listák |
| 3 | `het03-linkek-kepek/` | Linkek és képek |
| 4 | `het04-tablazatok-urlapok/` | Táblázatok és űrlapok |
| 5 | `het05-szemantikus-html/` | Szemantikus HTML és haladó űrlapok |
| 6 | `het06-css-bevezetes/` | CSS bevezetés |
| 7 | `het07-box-modell/` | CSS box modell |
| 8 | `het08-elrendezes/` | Elrendezés és pozícionálás |
| 9 | `het09-flexbox/` | Flexbox |
| 10 | `het10-reszponziv/` | Reszponzív design |
| 11 | `het11-projekt/` | Haladó CSS és projekt |
| 12 | `het12-vizsga/` | Vizsgafelkészítés |

### Template repó feltöltése
1. Hozz létre egy új GitHub repót (pl. `het01-html-bevezetes`)
2. Másold be a `github-classroom/het01-html-bevezetes/` tartalmát
3. A repó beállításaiban jelöld be: **Template repository** ✓
4. A `.github/` mappa tartalmazza az autograding konfigurációt

### Vizsga template-ek

| Variáns | Template mappa |
|---------|---------------|
| A – Étterem | `vizsga-etterem/` |
| B – Portfólió | `vizsga-portfolio/` |
| C – Webshop | `vizsga-webshop/` |
| D – Blog | `vizsga-blog/` |

---

## 3. Feladat (Assignment) létrehozása

1. GitHub Classroom → New assignment
2. **Title:** pl. „1. hét – HTML bevezetés"
3. **Deadline:** a következő óra előtt 1 nappal
4. **Repository visibility:** Private
5. **Template repository:** a megfelelő template repó
6. **Add autograding:** Importálva az `autograding.json`-ból

---

## 4. Autograding

### Hogyan működik?
- A `.github/workflows/classroom.yml` fájl egy GitHub Actions workflow-t definiál
- Minden push után automatikusan lefut
- Az `autograding.json` tartalmazza a teszteket
- A pontszám megjelenik a GitHub Classroom felületen

### Teszttípusok HTML/CSS kurzushoz

**Fájl létezés:**
```json
{
  "name": "index.html létezik",
  "run": "test -f index.html",
  "timeout": 10,
  "points": 1
}
```

**HTML elem keresés:**
```json
{
  "name": "Van h1 címsor",
  "run": "grep -qi '<h1' index.html",
  "timeout": 10,
  "points": 1
}
```

**CSS fájl létezés és hivatkozás:**
```json
{
  "name": "style.css létezik és be van kötve",
  "run": "test -f style.css && grep -qi 'stylesheet' index.html",
  "timeout": 10,
  "points": 2
}
```

**Szemantikus elemek ellenőrzése:**
```json
{
  "name": "Szemantikus elemek használata",
  "run": "grep -qi '<header' index.html && grep -qi '<footer' index.html && grep -qi '<nav' index.html",
  "timeout": 10,
  "points": 2
}
```

**Reszponzív meta tag:**
```json
{
  "name": "Viewport meta tag megvan",
  "run": "grep -qi 'viewport' index.html",
  "timeout": 10,
  "points": 1
}
```

**Media query ellenőrzése:**
```json
{
  "name": "Van media query a CSS-ben",
  "run": "grep -qi '@media' style.css",
  "timeout": 10,
  "points": 2
}
```

---

## 5. Hibaelhárítás

### Gyakori problémák

| Probléma | Megoldás |
|----------|---------|
| A teszt nem találja a fájlt | Ellenőrizd, hogy a fájl a gyökérmappában van, nem almappában |
| A `grep` nem talál elemet | A HTML elem több sorba is tördelve lehet – használj `-z` flaget |
| A tanuló nem lát pontszámot | GitHub Actions tab → kattints a workflow-ra → részletek |
| Az autograding nem fut le | Ellenőrizd, hogy a `.github/` mappa megvan-e a push után |

### Fontos megjegyzés

A HTML/CSS autograding korlátozott – a `grep` alapú tesztek csak a struktúrát és az elemek meglétét ellenőrzik, a vizuális megjelenést nem. Ezért a **mentori code review** különösen fontos ennél a kurzusnál.
