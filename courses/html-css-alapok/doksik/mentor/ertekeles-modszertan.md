# Értékelési módszertan – HTML & CSS Alapok

## 1. Értékelési filozófia

### Alapelvek

- **Formatív értékelés elsőbbsége:** A félév során a cél a tanulás támogatása, nem a szűrés. A heti házi feladatok pontszámai visszajelzésként szolgálnak, nem büntetésként.
- **Fokozatos nehezítés:** A heti feladatok pontértéke tükrözi a komplexitást (10–20 pont), a vizsga pedig az összesített tudást méri (40 pont).
- **Automatizált + emberi értékelés:** A GitHub Classroom autograding ad egy objektív alappontszámot, de a mentori kód-átnézés (code review) is része az értékelésnek. A HTML/CSS-nél a **vizuális megjelenés** értékelése különösen fontos.
- **Növekedési szemlélet (growth mindset):** Kezdő webfejlesztőknél a vizuális gondolkodás új – az előrehaladás fontosabb, mint az abszolút szint.

### Mit mérünk?

| Szint | Leírás | Példa |
|-------|--------|-------|
| **Érvényes** | A HTML érvényes, a CSS betöltődik | Autograding: fájlok léteznek, alapelemek megvannak |
| **Strukturált** | Szemantikus elemeket használ, CSS jól szervezett | Code review: `<header>` vs `<div>`, osztályok használata |
| **Vizuális** | Az oldal jól néz ki, reszponzív, letisztult | Böngészőben megnézve: olvasható, konzisztens |
| **Önálló** | Nem másolt, a tanuló el tudja magyarázni | Szóbeli kérdés vagy Git history |

---

## 2. Értékelési összetevők

### Összesített értékelés

| Összetevő | Súly | Mérés módja |
|-----------|------|-------------|
| Heti házi feladatok (het00–het11) | 25% | GitHub Classroom autograding |
| Órai munka és aktivitás | 15% | Mentori megfigyelés |
| Próbavizsga (het12) | 10% | GitHub Classroom autograding + code review |
| Szintfelmérő vizsga | 50% | GitHub Classroom autograding + code review |

### Szinthatárok (szintfelmérő)

| Pontszám | Százalék | Szint |
|----------|----------|-------|
| 36–40 | 90–100% | Kiváló |
| 28–35 | 70–89% | Haladó |
| 20–27 | 50–69% | Megfelelő |
| 12–19 | 30–49% | Kezdő |
| 0–11 | 0–29% | Nem teljesített |

---

## 3. Automatizált értékelés (GitHub Classroom)

### Hogyan működik?

1. A tanuló pushol a GitHub repójába
2. A GitHub Actions workflow automatikusan lefut
3. Az `autograding.json` tesztjei ellenőrzik a kódot
4. A pontszám megjelenik a GitHub Classroom felületen

### A tesztek három szintje

**Szint 1 – Létezés és struktúra (shell tesztek)**
- Létezik-e a fájl? (`test -f index.html`)
- Van-e benne HTML elem? (`grep -qi '<h1' index.html`)
- Létezik-e CSS fájl? (`test -f style.css`)
- Be van-e kötve a CSS? (`grep -qi 'stylesheet' index.html`)

**Szint 2 – Elemek és attribútumok (shell tesztek)**
- Tartalmaz-e szemantikus elemeket? (`grep -qi '<header' index.html`)
- Van-e `alt` attribútum a képeknél? (`grep -qi 'alt=' index.html`)
- Van-e `viewport` meta tag? (`grep -qi 'viewport' index.html`)
- Van-e `@media` query? (`grep -qi '@media' style.css`)

**Szint 3 – Vizuális és funkcionális (mentori review)**
- Az oldal jól néz ki böngészőben?
- Reszponzív-e mobilon?
- Konzisztens-e a színvilág és tipográfia?
- A kód olvasható és jól szervezett?

### Automatizált pontszámok értelmezése

| Autograding pontszám | Értelmezés |
|---------------------|------------|
| 90–100% | Minden szükséges elem és struktúra megvan |
| 60–89% | Az alapok megvannak, de hiányzik néhány elem |
| 30–59% | Próbálkozott, de a megvalósítás hiányos |
| 0–29% | Nem készült el, vagy nem működik |

### Fontos: az autograding nem elég

Az autograding **szükséges, de nem elégséges** feltétele a jó eredménynek:
- A HTML elem megvan, de nincs benne tartalom (→ vizuális review)
- A CSS fájl létezik, de üres vagy minimális (→ code review)
- Az oldal strukturálisan helyes, de vizuálisan elfogadhatatlan (→ böngésző review)
- Egy tanuló másolhatott (→ Git history ellenőrzés)

---

## 4. Mentori kód-átnézés (Code Review)

### Mikor szükséges?

- **Heti házi feladatok:** Szúrópróbaszerűen (heti 3-5 tanuló repóját)
- **Próbavizsga:** Minden tanuló kódját
- **Szintfelmérő vizsga:** Minden tanuló kódját részletesen + böngészőben megnézve

### Code review szempontok

**Ellenőrzőlista (vizsga):**

```
□ index.html – Érvényes HTML5 dokumentum szerkezet?
□ index.html – Szemantikus elemek használata? (<header>, <nav>, <main>, <footer>)
□ index.html – Minden kép rendelkezik alt attribútummal?
□ style.css  – Külső CSS fájl, megfelelően bekötve?
□ style.css  – Osztály szelektorok használata (nem csak elem szelektorok)?
□ style.css  – Flexbox használata az elrendezéshez?
□ style.css  – Van media query reszponzív designhoz?
□ Vizuális   – Az oldal böngészőben rendesen megjelenik?
                Mobilon is jól néz ki?
                Konzisztens színvilág és tipográfia?
□ Kódminőség – Értelmes osztálynevek? (nem .a, .b, .x, .y)
                Nincs felesleges kód? Nincs kikommentált szemét?
□ Git history – Legalább 3 commit? Értelmes commit üzenetek?
                Az időbélyegek a vizsga idejére esnek?
```

### Pontmódosítás code review alapján

| Eset | Módosítás |
|------|----------|
| Autograding PASS + jó vizuális megjelenés + jó kódminőség | Teljes pontszám |
| Autograding PASS + gyenge vizuális megjelenés | –10–20% a részfeladaton |
| Autograding FAIL + jó megközelítés, apró hiba | +1–2 pont részpontként |
| Autograding PASS + gyanús Git history (1 commit, copy-paste) | Szóbeli ellenőrzés szükséges |

---

## 5. Git history elemzés

A Git history a leghatékonyabb eszköz a másolás kiszűrésére és a munkafolyamat megértésére.

### Ellenőrizendő

```bash
# Commitok száma és időzítése
git log --oneline --format="%h %ai %s"

# Ki írta a kódot?
git log --format="%an <%ae>" | sort -u

# Mikor történtek a commitok?
git log --format="%ai" | head -20

# Soronkénti szerzőség
git blame index.html
```

### Piros zászlók

- **1 commit az egész vizsgára** → valószínű másolás
- **Commitok a vizsga időablakán kívül** → otthoni előkészítés (megengedett-e?)
- **Más felhasználónév a commitban** → másolás másik tanulótól
- **Hatalmas commit diff** → nem fokozatosan dolgozott

---

## 6. Szóbeli ellenőrzés

### Mikor alkalmazzuk?

- Gyanús Git history esetén
- Kiemelkedően jó vagy gyenge autograding eredménynél az elvárthoz képest
- A tanuló kérésére (javítási lehetőség)

### Kérdések szintenként

**Alapszint:**
- Mi a különbség a `<div>` és a `<span>` között?
- Mi a `<head>` és a `<body>` feladata?
- Hogyan kötjük be a CSS fájlt az HTML-be?

**Középszint:**
- Mire jó a szemantikus HTML? Mondj 3 szemantikus elemet!
- Magyarázd el a CSS box modellt!
- Mi a különbség a `class` és az `id` szelektor között?

**Haladó szint:**
- Hogyan működik a Flexbox? Mi a `justify-content` és `align-items` különbsége?
- Hogyan csináltad reszponzívvá az oldalad? Milyen töréspontokat használtál?
- Mi a `box-sizing: border-box` és miért hasznos?

### Szóbeli értékelés hatása

| Eredmény | Hatás az értékelésre |
|----------|----------------------|
| A tanuló magabiztosan elmagyarázza a kódját | Megerősíti az autograding eredményt |
| A tanuló részben érti, de vannak hiányosságok | Az autograding eredményt max 1 szinttel csökkenti |
| A tanuló nem tudja elmagyarázni a saját kódját | A feladatra 0 pont (másolásgyanú) |

---

## 7. Házi feladatok értékelése

### Heti házi feladatok (het00–het11)

- **Automatikus:** GitHub Classroom pontszám (azonnal látható a tanulónak)
- **Határidő:** A következő óra előtt 1 nappal
- **Késés:** Heti 1 nap késés megengedett, utána 50% levonás
- **Minimumkövetelmény:** A félév végéig legalább 8 házi feladat beadva

### Összesítés

A házi feladatok összesített pontszáma a félév végén kerül kiszámításra, a legjobb 10 hét eredménye alapján (a leggyengébb 2 hét kiesik).
