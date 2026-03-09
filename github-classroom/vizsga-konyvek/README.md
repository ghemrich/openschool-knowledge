# Python szintfelmérő – Könyvek (B variáns)

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

## 1. feladat – Emailgeneráló program (8 pont)

Készíts programot (`feladat1.py`), amely bekéri a felhasználó **vezetéknevét**, **keresztnevét** és **születési évét**, majd három ajánlott email címet állít össze `mail.com` végződéssel.

### Működés:

1. Kérd be a vezetéknevet, a keresztnevet és a születési évet.
2. A bekért adatokból állíts össze három email címet csupa kisbetűvel:
   - **1. cím:** teljes keresztnév + vezetéknév első betűje + `@mail.com` (pl. `annak@mail.com`)
   - **2. cím:** keresztnév első betűje + teljes vezetéknév + születési év + `@mail.com` (pl. `akiss2004@mail.com`)
   - **3. cím:** teljes keresztnév + `.` + teljes vezetéknév + `@mail.com` (pl. `anna.kiss@mail.com`)
3. Jelenítsd meg a három email címet a képernyőn.

### Technikai elvárások:

- A program **legalább 3 függvényt** tartalmazzon (bekérés, feldolgozás, megjelenítés).

---

## 2. feladat – Kockadobós tippelős játék (14 pont)

Készíts programot (`feladat2.py`), amely három kockadobást generál (1–6 értékűt), és a játékosnak ki kell találnia az összegüket.

### Működés:

1. A program generáljon három véletlenszerű számot 1 és 6 között, és tárolja listában.
2. A játékos tippelhet, mennyi a három kocka összege.
3. A program értékelje ki a tippet:
   - Ha a tipp kisebb, mint 3 vagy nagyobb, mint 18: **„HIBA: nem lehetséges érték!"**
   - Ha a tipp kisebb, mint az összeg: **„Ennél több"**
   - Ha a tipp nagyobb, mint az összeg: **„Ennél kevesebb"**
   - Ha a tipp megegyezik az összeggel: **„Talált!"**
4. A játék addig folytatódik, amíg a játékos el nem találja az összeget.
5. Tartsa nyilván a tippek számát.
6. A játék végén írja ki a dobásokat, a tippek számát, és köszönje meg a játékot: **„Köszönjük a játékot!"**

### Technikai elvárások:

- A `random` modul használata szükséges.
- A program `while` ciklust használjon.
- A program **legalább 2 függvényt** tartalmazzon.

---

## 3. feladat – Könyvek feldolgozása (18 pont)

Az UTF-8 kódolású `konyvek.txt` állomány könyvek adatait tartalmazza pontosvesszővel elválasztva:

**cím;nyelv;műfaj;év;bevétel**

A nyelvek: angol, német, francia. A műfajok: fantasy, krimi, sci-fi, történelmi.

### Feladatok:

1. Olvasd be az állomány tartalmát szótárak listájába. Az évet és a bevételt alakítsd egész számmá. Ha nem tudod a fájlt beolvasni, használhatod a `konyvek.py` modult.
2. Írd ki, hány könyv található a listában.
3. Írd ki, hogy hány angol, német és francia nyelven íródott könyv található.
4. Írd ki a legnagyobb és a legkisebb bevételt hozó könyv címét és bevételét.
5. Kérd be egy könyv címét! Ha megtalálható a listában, írd az adatait egy `valasztott_konyv.txt` fájlba pontosvesszővel elválasztva. Ha nem létezik, írd ki: „Nincs ilyen cím a listában".
6. Kérd be egy műfaj nevét! Írd ki az adott műfajba tartozó könyvek címét és kiadási évét.

### Technikai elvárások:

- A segédfüggvényeket a `fgv.py` fájlba írd!
- A `fgv.py` modult importáld a `feladat3.py` fájlban!
- A `fgv.py` fájlban az alábbi függvényneveket használd:

| Függvény | Leírás |
|----------|--------|
| `beolvasas(fajlnev)` | Beolvassa a fájlt, visszaadja szótárak listáját |
| `darabszam(konyvek)` | Visszaadja az elemek számát |
| `nyelvek_szama(konyvek)` | Visszaad egy szótárat a nyelvek darabszámával |
| `legtobb_legkevesebb_bevetel(konyvek)` | Visszaadja a legtöbb és legkevesebb bevételű könyvet |
| `konyv_keresese(konyvek, cim)` | Visszaadja a könyvet cím alapján, vagy `None`-t |
| `konyv_fajlba_iras(konyv, fajlnev)` | Kiírja a könyv adatait fájlba pontosvesszővel |
| `mufajhoz_tartozo_konyvek(konyvek, mufaj)` | Visszaadja az adott műfaj könyveinek címét és évét |

---

## Beadás

1. `git add .`
2. `git commit -m "vizsga megoldás"`
3. `git push`

Az utolsó push az óra végén = beadás!
