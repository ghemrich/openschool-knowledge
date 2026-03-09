# Python szintfelmérő – Sportolók (D variáns)

> **Időtartam:** 90 perc
> **Összpontszám:** 40 pont
> **Beadás:** az utolsó `git push` az óra végén = beadás!

---

## Vizsga szabályok

- **Idő:** 90 perc
- **Internet használható** (dokumentáció, W3Schools stb.)
- Egymásnak NEM segíthettek!
- Rendszeresen commitolj! (`git add . && git commit -m "üzenet" && git push`)

---

## 1. feladat – Becenévgeneráló program (8 pont)

Készíts programot (`feladat1.py`), amely bekéri a felhasználó **vezetéknevét**, **keresztnevét** és **születési évét**, majd három ajánlott becenevet állít össze.

### Működés:

1. Kérd be a vezetéknevet, a keresztnevet és a születési évet.
2. A beírt neveket alakítsd kisbetűsre.
3. Állíts össze három becenevet az alábbi formátumokban:
   - **1. becenév:** keresztnév első 3 betűje + születési év utolsó 2 jegye (pl. `ann04`)
   - **2. becenév:** teljes vezetéknév + `_` + keresztnév utolsó betűje + születési év utolsó 2 jegye (pl. `kiss_a04`)
   - **3. becenév:** teljes keresztnév + születési év utolsó 2 jegye + `.` + vezetéknév fordítva (pl. `anna04.ssik`)
4. Jelenítsd meg a három becenevet a képernyőn.

### Technikai elvárások:

- A program **legalább 3 függvényt** tartalmazzon (bekérés, feldolgozás, megjelenítés).

---

## 2. feladat – Golyóhúzásos tippelős játék (14 pont)

Készíts programot (`feladat2.py`), amely négy véletlenszerű golyót húz (1–5 értékűt), és a játékosnak ki kell találnia a golyók összegét.

### Működés:

1. A program generáljon négy véletlenszerű számot 1 és 5 között, és tárolja listában.
2. A játékos tippelhet, mennyi a négy golyó összege.
3. A program értékelje ki a tippet:
   - Ha a tipp kisebb, mint 4 vagy nagyobb, mint 20: **„HIBA: nem lehetséges érték!"**
   - Ha a tipp kisebb, mint az összeg: **„Ennél több"**
   - Ha a tipp nagyobb, mint az összeg: **„Ennél kevesebb"**
   - Ha a tipp megegyezik az összeggel: **„Talált!"**
4. A játék addig folytatódik, amíg a játékos el nem találja az összeget.
5. Tartsa nyilván a tippek számát.
6. A játék végén írja ki a húzott golyókat, a tippek számát, és köszönje meg a játékot: **„Köszönjük a játékot!"**

### Technikai elvárások:

- A `random` modul használata szükséges.
- A program `while` ciklust használjon.
- A program **legalább 2 függvényt** tartalmazzon.

---

## 3. feladat – Sportolók feldolgozása (18 pont)

Az UTF-8 kódolású `sportolok.txt` állomány sportolók adatait tartalmazza pontosvesszővel elválasztva:

**név;sportág;nemzetiség;év;érmek;pontszám**

A nemzetiségek: magyar, német, francia, angol. A sportágak: futás, úszás, kerékpár, labdarúgás.

### Feladatok:

1. Olvasd be az állomány tartalmát szótárak listájába. Az évet és az érmek számát alakítsd egész számmá, a pontszámot valós számmá (float). Ha nem tudod a fájlt beolvasni, használhatod a `sportolok.py` modult.
2. Írd ki, hány sportoló található a listában.
3. Írd ki, hogy hány magyar, német, francia és angol nemzetiségű sportoló található.
4. Írd ki a legtöbb és a legkevesebb éremmel rendelkező sportoló nevét és érmei számát.
5. Kérd be egy sportoló nevét! Ha megtalálható a listában, írd az adatait egy `valasztott_sportolo.txt` fájlba pontosvesszővel elválasztva. Ha nem létezik, írd ki: „Nincs ilyen név a listában".
6. Kérd be egy sportág nevét! Írd ki az adott sportághoz tartozó sportolók nevét és érmei számát.

### Technikai elvárások:

- A segédfüggvényeket a `fgv.py` fájlba írd!
- A `fgv.py` modult importáld a `feladat3.py` fájlban!
- A `fgv.py` fájlban az alábbi függvényneveket használd:

| Függvény | Leírás |
|----------|--------|
| `beolvasas(fajlnev)` | Beolvassa a fájlt, visszaadja szótárak listáját |
| `darabszam(sportolok)` | Visszaadja az elemek számát |
| `nemzetisegek_szama(sportolok)` | Visszaad egy szótárat a nemzetiségek darabszámával |
| `legtobb_legkevesebb_erem(sportolok)` | Visszaadja a legtöbb és legkevesebb éremmel rendelkező sportolót |
| `sportolo_keresese(sportolok, nev)` | Visszaadja a sportolót név alapján, vagy `None`-t |
| `sportolo_fajlba_iras(sportolo, fajlnev)` | Kiírja a sportoló adatait fájlba pontosvesszővel |
| `sportaghoz_tartozo_sportolok(sportolok, sportag)` | Visszaadja az adott sportág sportolóinak nevét és érmeit |

---

## Beadás

1. `git add .`
2. `git commit -m "vizsga megoldás"`
3. `git push`

Az utolsó push az óra végén = beadás!
