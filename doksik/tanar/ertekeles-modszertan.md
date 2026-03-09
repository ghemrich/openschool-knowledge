# Értékelési módszertan – Python kurzus 10. évfolyam

## 1. Értékelési filozófia

### Alapelvek

- **Formatív értékelés elsőbbsége:** A félév során a cél a tanulás támogatása, nem a szűrés. A heti házi feladatok pontszámai visszajelzésként szolgálnak, nem büntetésként.
- **Fokozatos nehezítés:** A heti feladatok pontértéke tükrözi a komplexitást (13–19 pont), a vizsga pedig az összesített tudást méri (40 pont).
- **Automatizált + emberi értékelés:** A GitHub Classroom autograding ad egy objektív alappontszámot, de a tanári kód-átnézés (code review) is része az értékelésnek.
- **Növekedési szemlélet (growth mindset):** 10. évfolyamos diákoknál a programozás új — az előrehaladás fontosabb, mint az abszolút szint.

### Mit mérünk?

| Szint | Leírás | Példa |
|-------|--------|-------|
| **Működik** | A kód lefut, helyes eredményt ad | Autograding: PASS |
| **Strukturált** | Függvényeket használ, logikusan szervezett | Code review: van-e `def`, van-e modul |
| **Érthető** | Olvasható változónevek, logikus felépítés | Code review: elnevezések, tagolás |
| **Önálló** | Nem másolt, a diák el tudja magyarázni | Szóbeli kérdés vagy Git history |

---

## 2. Értékelési összetevők

### Összesített jegy

| Összetevő | Súly | Mérés módja |
|-----------|------|-------------|
| Heti házi feladatok (het00–het11) | 25% | GitHub Classroom autograding |
| Órai munka és aktivitás | 15% | Tanári megfigyelés |
| Próbavizsga (het12) | 10% | GitHub Classroom autograding + code review |
| Szintfelmérő vizsga | 50% | GitHub Classroom autograding + code review |

### Jegyhatárok (szintfelmérő)

| Pontszám | Százalék | Jegy |
|----------|----------|------|
| 36–40 | 90–100% | 5 (jeles) |
| 28–35 | 70–89% | 4 (jó) |
| 20–27 | 50–69% | 3 (közepes) |
| 12–19 | 30–49% | 2 (elégséges) |
| 0–11 | 0–29% | 1 (elégtelen) |

---

## 3. Automatizált értékelés (GitHub Classroom)

### Hogyan működik?

1. A diák pushol a GitHub repójába
2. A GitHub Actions workflow automatikusan lefut
3. Az `autograding.json` tesztjei ellenőrzik a kódot
4. A pontszám megjelenik a GitHub Classroom felületen

### A tesztek három szintje

**Szint 1 – Létezés és struktúra (shell tesztek)**
- Létezik-e a fájl? (`test -f feladat1.py`)
- Van-e benne függvény? (`grep -c '^def '`)
- Importálja-e a modult? (`grep 'import fgv'`)
- Használ-e kulcsszavakat? (`grep 'while'`, `grep 'import random'`)

**Szint 2 – Futtathatóság (shell tesztek stdin-nel)**
- Lefut-e bemenettel? (`python3 feladat1.py` + stdin)
- A kimenet tartalmazza-e az elvárt szöveget? (`"comparison": "included"`)

**Szint 3 – Funkcionális helyesség (Python tesztek)**
- Az egyes függvények helyes eredményt adnak? (`test_fgv.py`)
- Helyes adatszerkezet? Helyes darabszám? Helyes szűrés?
- Fájlba írás működik?

### Automatizált pontszámok értelmezése

| Autograding pontszám | Értelmezés |
|---------------------|------------|
| 90–100% | A kód jól működik, kis javításokra lehet szükség |
| 60–89% | Az alapok megvannak, de hiányzik néhány funkció |
| 30–59% | Próbálkozott, de a megvalósítás hiányos |
| 0–29% | Nem készült el, vagy nem működik |

### Fontos: az autograding nem elég

Az autograding **szükséges, de nem elégséges** feltétele a jó jegynek:
- Egy diák másolhatott (→ Git history ellenőrzés)
- A kód működik, de olvashatatlan (→ code review)
- A kód túl egyszerű megoldást használ (→ struktúra ellenőrzés)
- A diák nem érti a saját kódját (→ szóbeli kérdés)

---

## 4. Tanári kód-átnézés (Code Review)

### Mikor szükséges?

- **Heti házi feladatok:** Szúrópróbaszerűen (heti 3-5 diák repóját)
- **Próbavizsga:** Minden diák kódját
- **Szintfelmérő vizsga:** Minden diák kódját részletesen

### Code review szempontok

**Ellenőrzőlista (vizsga):**

```
□ feladat1.py – Függvényekre bontva? Nem egyben van az egész?
□ feladat2.py – Van ciklus? Van kilépési feltétel? Nem végtelen?
□ feladat3.py – Importálja a fgv.py-t? Hívja a függvényeket?
□ fgv.py     – Minden függvény paraméterrel dolgozik?
                Nem használ globális változókat?
                Van return érték?
□ Kódminőség – Értelmse változónevek? (nem a, b, x, y)
                Nincs felesleges kód? Nincs kikommentált szemét?
□ Git history – Legalább 3 commit? Értelmes commit üzenetek?
                Az időbélyegek a vizsga idejére esnek?
```

### Pontmódosítás code review alapján

| Eset | Módosítás |
|------|----------|
| Autograding PASS + jó kódminőség | Teljes pontszám |
| Autograding PASS + gyenge kódminőség | –10% a részfeladaton |
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
git blame feladat3.py
```

### Piros zászlók

- **1 commit az egész vizsgára** → valószínű másolás
- **Commitok a vizsga időablakán kívül** → otthoni előkészítés (megengedett-e?)
- **Más felhasználónév a commitban** → másolás másik diáktól
- **Hatalmas commit diff** → nem fokozatosan dolgozott

---

## 6. Szóbeli ellenőrzés

### Mikor alkalmazzuk?

- Gyanús Git history esetén
- Kiemelkedően jó vagy gyenge autograding eredménynél az elvárthoz képest
- A diák kérésére (javítási lehetőség)

### Kérdések szintenként

**Alapszint (2-es jegyhez):**
- Mit csinál az `input()` függvény?
- Mi a különbség az `int` és a `str` típus között?
- Mit jelent a `while` ciklus?

**Középszint (3-4-es jegyhez):**
- Magyarázd el, mit csinál a `beolvasas()` függvényed!
- Miért kellett `split(";")` -et használni?
- Hogyan működik a szűrés a programodban?

**Haladó szint (5-ös jegyhez):**
- Milyen adatszerkezetet választottál és miért?
- Hogyan oldottad meg a maximum/minimum keresést?
- Mi történne, ha a fájl üres lenne?

### Szóbeli értékelés hatása

| Eredmény | Hatás a jegyre |
|----------|----------------|
| A diák magabiztosan elmagyarázza a kódját | Megerősíti az autograding jegyet |
| A diák részben érti, de vannak hiányosságok | Az autograding jegyet max 1 jeggyel csökkenti |
| A diák nem tudja elmagyarázni a saját kódját | A feladatra 0 pont (másolásgyanú) |

---

## 7. Házi feladatok értékelése

### Heti házi feladatok (het00–het11)

- **Automatikus:** GitHub Classroom pontszám (azonnal látható a diáknak)
- **Határidő:** A következő óra előtt 1 nappal
- **Késés:** Heti 1 nap késés megengedett, utána 50% levonás
- **Minimumkövetelmény:** A félév végéig legalább 8 házi feladat beadva

### Összesítés

A 12 heti házi feladat összpontszáma **223 pont**. Ebből számított százalék:

| Százalék | Házi feladat jegy |
|----------|-------------------|
| 80–100% | 5 |
| 60–79% | 4 |
| 40–59% | 3 |
| 20–39% | 2 |
| 0–19% | 1 |

---

## 8. Vizsgavariánsok kezelése

### 4 variáns rendszer

| Variáns | Téma | Adat | Fő különbség |
|---------|------|------|-------------|
| A (filmek) | Felhasználónév + kártyahúzás (3–39) + filmek | 100 sor | Kategória szerinti szűrés, értékelés |
| B (konyvek) | Email + kockadobás (3–18) + könyvek | 104 sor | Nyelv/műfaj szerinti szűrés, bevétel |
| C (zenek) | Jelszó + nyerőgép (3–30) + zenék | 100 sor | Műfaj szerinti szűrés, hossz/értékelés |
| D (sportolok) | Becenév + golyóhúzás (4–20) + sportolók | 97 sor | Nemzetiség/sportág, érmek/pontszám |

### Kiosztási javaslat

- **2 csoport:** A+B vagy C+D variáns
- **4 csoport:** Minden variáns más sorrendben (A, B, C, D)
- **Véletlenszerű:** GitHub Classroom-ban 4 assignment, a diákok random kapják

A variánsok **azonos nehézségűek** — mindegyik azonos struktúrájú (3 feladat: 8+14+18 pont), és az autograding tesztek pontról pontra megfelelnek egymásnak.

---

## 9. Különleges esetek

### Hiányzó diák a vizsgán
- Pótvizsga: másik variánssal (C vagy D, ha az órákon A és B volt)
- Határidő: 1 héten belül

### Technikai probléma a vizsgán
- A diák jelezze azonnal
- A tanár ellenőrizze a Git history-t (volt-e push?)
- Szükség esetén a helyi fájlok manuális begyűjtése (USB)

### Plágiumgyanú
1. Git history összehasonlítás két diáknál (`git log`, `git blame`)
2. Kód hasonlóság vizsgálat (változónevek, struktúra, kommentek)
3. Szóbeli ellenőrzés mindkét diákkal
4. Ha bizonyított: mindkét diák 0 pontot kap a feladatra

### Kimagasló teljesítmény
- 40/40 pont + kiváló kódminőség: dicséret, mentor szerep lehetőség
- A diák segíthet a gyengébb társaiknak (pair programming)

---

## 10. Összefoglalás

```
Értékelési piramis:

    ┌──────────────┐
    │  SZÓBELI (?)  │  ← csak gyanú esetén
    ├──────────────┤
    │  CODE REVIEW  │  ← tanári átnézés
    ├──────────────┤
    │  GIT HISTORY  │  ← munkafolyamat ellenőrzés
    ├──────────────┤
    │  AUTOGRADING  │  ← objektív alappontszám
    └──────────────┘
```

**Az autograding az alap, nem a plafon.** A számítógép megmondja, hogy működik-e a kód — a tanár dönti el, hogy a diák érti-e és önállóan készítette-e.
