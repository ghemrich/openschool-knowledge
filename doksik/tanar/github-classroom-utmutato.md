# GitHub Classroom – Tanári útmutató a házi feladatokhoz

Ez a dokumentum lépésről lépésre elmagyarázza, hogyan kell a GitHub Classroom rendszert használni a heti házi feladatok kiosztásához és értékeléséhez.

---

## 1. Előkészületek (egyszer kell megcsinálni)

### 1.1 GitHub Organization létrehozása

1. Lépj be a [github.com](https://github.com) oldalra a saját GitHub fiókoddal
2. Kattints a jobb felső sarokban a **+** gombra → **New organization**
3. Válaszd a **Free** tervet
4. Adj nevet (pl. `iskola-10b-python-2026`)
5. Add meg az email címedet, majd kattints a **Create** gombra

### 1.2 GitHub Classroom létrehozása

1. Nyisd meg: [classroom.github.com](https://classroom.github.com)
2. Kattints: **New Classroom**
3. Válaszd ki az imént létrehozott Organization-t
4. Adj nevet a Classroom-nak (pl. „Python 10.B – 2026")
5. Készen is van!

### 1.3 Diákok meghívása

1. A Classroom oldalán kattints a **Students** fülre
2. Itt két lehetőséged van:
   - **Meghívó link** küldése (a diákok magukat adják hozzá)
   - **Névsor feltöltése** (CSV fájl, hogy a diákok nevüket kiválaszthassák)
3. **Ajánlás:** Töltsd fel a névjegyzéket, hogy a diákok a saját nevüket válasszák ki az első assignment elfogadásakor — így a GitHub felhasználónevük össze lesz rendelve a valódi nevükkel

---

## 2. Template repok feltöltése GitHubra

A `github-classroom/` mappában 13 kész template repo van, hetente egy. Mindegyiket külön GitHub repóként kell feltölteni az Organization-be.

### Lépések (minden hétre ismételd):

```bash
# Példa a 0. hétre:
cd github-classroom/het00-git-alapok

git init
git add .
git commit -m "template"
git branch -M main
git remote add origin https://github.com/ORGANIZATION_NEVE/het00-git-alapok.git
git push -u origin main
```

> **FONTOS:** A repot a GitHub weboldalon is létre kell hozni az Organization alatt, mielőtt pusholsz!

### Gyors módszer (mind a 13 repo):

1. A GitHub weboldalon, az Organization alatt hozd létre a repokat:
   - `het00-git-alapok`
   - `het01-alapok`
   - `het02-bevitel-szoveg`
   - `het03-feltetelek`
   - `het04-ciklusok`
   - `het05-listak`
   - `het06-fuggvenyek`
   - `het07-random-jatek`
   - `het08-fajlkezeles`
   - `het09-adatszerkezetek`
   - `het10-adatfeldolgozas`
   - `het11-modulok-projekt`
   - `het12-vizsga`

2. Mindegyik repot **Template repository**-nak kell jelölni:
   - Repo → **Settings** → **General** → ✅ **Template repository** jelölőnégyzet

3. Pushold fel a tartalmat a `github-classroom/` mappából

---

## 3. Heti házi feladat kiosztása

Minden héten egy új **Assignment**-et kell létrehozni. Ezt kell tenned:

### 3.1 Assignment létrehozása

1. Nyisd meg a Classroom-ot: [classroom.github.com](https://classroom.github.com)
2. Kattints: **New Assignment**
3. Töltsd ki:

| Mező | Érték | Példa |
|------|-------|-------|
| **Title** | A hét neve | `Het 03 - Felteteles elagazasok` |
| **Deadline** | A következő óra dátuma + időpont | `2026-03-16 08:00` |
| **Individual or Group** | **Individual** | - |
| **Repository visibility** | **Private** | (ne másolhassák egymástól) |
| **Template repository** | Az adott heti template | `het03-feltetelek` |

4. Kattints: **Create Assignment**
5. Megkapod a **meghívó linket** (pl. `https://classroom.github.com/a/AbCdEf`)

### 3.2 Link kiosztása

- Küldd el a meghívó linket a diákoknak (Teams, email, Kréta üzenet, stb.)
- A diák rákattint → elfogadja → automatikusan létrejön a saját privát repoja
  (pl. `het03-feltetelek-kissanna`)

---

## 4. Automatikus tesztelés (Autograding)

Minden template repo tartalmaz automatikus teszteket (`.github/classroom/autograding.json`), amelyek **automatikusan lefutnak**, amikor a diák pushol. Nem kell ehhez semmit beállítanod — a tesztek a template repo részeként kerülnek a diákok repójába.

### 4.1 Hogyan működik?

1. A diák pushol → a GitHub Actions automatikusan lefuttatja a teszteket
2. A Classroom felületén megjelenik az eredmény (pl. „7/10 pont")
3. A diák is látja a saját eredményét a repojában (Actions fül → zöld ✅ vagy piros ❌)

### 4.2 Mit tesztelnek?

A tesztek feladatonként ellenőrzik:

| Teszt típus | Példa | Mit ellenőriz |
|-------------|-------|---------------|
| **Fájl létezik** | `test -f feladat1.py` | A diák létrehozta-e a fájlt |
| **Kód lefut** | `python3 feladat1.py` | A program hiba nélkül fut-e |
| **Kimenet helyes** | output: `"500"` | A kimenet tartalmazza-e az elvárt értéket |
| **Struktúra helyes** | `grep -q 'def koszont'` | A kód tartalmaz-e függvényt/importot/stb. |
| **Git használat** | `git log` commit számlálás | Rendszeresen commitolt-e |

### 4.3 Pontszámok

Minden héten feladatonként vannak elosztva a pontok. A Classroom felületén látod az összesítést:
- **Zöld pipa ✅** = minden teszt sikeres
- **Piros X ❌** = valamelyik teszt sikertelen
- A pontos pontszám az Assignment áttekintésben látható

### 4.4 Fontos tudnivalók

- A tesztek **nem tökéletesek** — nem helyettesítik a tanári ellenőrzést, de jó első szűrőt adnak
- Ha egy diák „átmegy" a teszteken, az nem jelenti, hogy a kód szép vagy jól strukturált
- A tesztek inkább **ösztönzőként** működnek: a diák azonnal látja, hogy helyes-e a megoldása
- **Ne változtasd meg** az autograding fájlokat a template repóban, mert az elronthatja a tesztelést

---

## 5. Házi feladatok ellenőrzése

### 5.1 Áttekintés a Classroom-ban

1. Nyisd meg az Assignment-et a Classroom-ban
2. Látod az összes diák státuszát:
   - ✅ Elfogadta a feladatot
   - 🔄 Commitolt (utolsó commit időpontja)
   - 📊 Autograding pontszám (pl. „7/10")
   - A repojára kattintva megnézheted a kódot

### 5.2 Kód megtekintése

- Kattints egy diák repojára → a GitHub oldalon megnyílik
- A **Commits** fülön látod, mikor és mit commitolt
- Az **Actions** fülön látod a tesztek eredményeit
- A fájlokra kattintva megnézheted a kódot

### 5.3 Gyors ellenőrzés – klónozás

Ha a gépen is le akarod tölteni az összes megoldást:

```bash
# GitHub Classroom Assistant alkalmazás használata (ajánlott):
# https://classroom.github.com/assistant

# VAGY manuálisan, egyenként:
git clone https://github.com/ORGANIZATION/het03-feltetelek-kissanna.git
```

---

## 6. Heti teendők összefoglalása

Minden héten ezeket kell megtenned:

| # | Teendő | Mikor |
|---|--------|-------|
| 1 | Hozd létre az Assignment-et a Classroom-ban | Az óra előtt |
| 2 | Oszd ki a meghívó linket a diákoknak | Az órán |
| 3 | A deadline után nézd meg a beadásokat | A következő óra előtt |
| 4 | Adj visszajelzést (GitHub komment vagy szóban) | A következő órán |

---

## 7. Template repok tartalma

| Mappa | Tartalom | Adatfájlok | Tesztek |
|-------|----------|------------|---------|
| `het00-git-alapok/` | README.md | – | 4 teszt (13 pont) |
| `het01-alapok/` | README.md | – | 8 teszt (18 pont) |
| `het02-bevitel-szoveg/` | README.md | – | 9 teszt (18 pont) |
| `het03-feltetelek/` | README.md | – | 10 teszt (16 pont) |
| `het04-ciklusok/` | README.md | – | 9 teszt (18 pont) |
| `het05-listak/` | README.md | – | 10 teszt (15 pont) |
| `het06-fuggvenyek/` | README.md | – | 12 teszt (19 pont) |
| `het07-random-jatek/` | README.md | – | 8 teszt (17 pont) |
| `het08-fajlkezeles/` | README.md | tanulok.txt, minta.txt | 9 teszt (16 pont) |
| `het09-adatszerkezetek/` | README.md | tanulok.txt | 8 teszt (15 pont) |
| `het10-adatfeldolgozas/` | README.md | filmek.txt | 10 teszt (19 pont) |
| `het11-modulok-projekt/` | README.md | filmek.txt | 11 teszt (19 pont) |
| `het12-vizsga/` | README.md | filmek.txt, filmek.py | 14 teszt (40 pont) |

> Minden template repo tartalmazza az autograding konfigurációt (`.github/classroom/autograding.json`) és a GitHub Actions workflow-t (`.github/workflows/classroom.yml`).

---

## 8. Értékelési javaslat a házi feladatokhoz

| Szempont | Leírás |
|----------|--------|
| **Beadta-e?** | Van-e commit a deadline előtt? |
| **Működik-e?** | A kód lefut hiba nélkül? |
| **Helyes-e?** | A kimenet megfelel a feladatnak? |
| **Git használat** | Értelmes commit üzenetek, rendszeres commitolás? |

### Egyszerű értékelési skála:

| Jegy | Feltétel |
|------|----------|
| ⭐⭐⭐⭐⭐ (5) | Minden feladat kész, helyes, szép kód |
| ⭐⭐⭐⭐ (4) | A ⭐ és ⭐⭐ feladatok készen vannak és helyesek |
| ⭐⭐⭐ (3) | A ⭐ feladatok készen vannak és helyesek |
| ⭐⭐ (2) | Legalább 2 feladat beadva, de hibás |
| ⭐ (1) | Nem adott be semmit, vagy nem commitolt |

---

## 9. Gyakori problémák és megoldásaik

| Probléma | Megoldás |
|----------|---------|
| „A diák nem tudja elfogadni a linket" | Ellenőrizd, hogy van-e GitHub fiókja. Segítsd a regisztrációban. |
| „Nem lát semmit a repo-ban" | Valószínűleg nem klónozta le. Segíts a `git clone` paranccsal. |
| „Commitolt, de nem pusholt" | Mutasd meg neki a `git push` parancsot. Ellenőrizd a GitHub oldalon. |
| „Deadline után pusholt" | A GitHub Classroom mutatja az utolsó commit időpontját. Te döntöd el, elfogadod-e. |
| „A kód más gépen nem fut" | Valószínűleg fájlútvonal probléma. Mutasd meg a relatív útvonalat. |
| „Nem tudja, mit commitoljon" | Mutasd meg: `git add .` → `git commit -m "üzenet"` → `git push` |

---

## 10. Tippek

- **Első órán** (0. hét): szánj rá időt, hogy mindenki beállítsa a Git-et és a GitHub fiókot. Ez a legfontosabb lépés!
- **Névsor feltöltése** a Classroom-ba: így a diákok nevéhez rendelheted a GitHub felhasználónevüket
- **Privát repok** használata: a diákok nem látják egymás megoldásait
- **GitHub Classroom Assistant** alkalmazás: egyszerre le tudod tölteni az összes diák repóját → [classroom.github.com/assistant](https://classroom.github.com/assistant)
- **Nem kell minden héten minden feladatot részletesen ellenőrizni** — a fontos az, hogy a diák rendszeresen gyakoroljon és commitoljon
