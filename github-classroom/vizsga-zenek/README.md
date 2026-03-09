# Python szintfelmérő – Zenék (C variáns)

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

## 1. feladat – Jelszógeneráló program (8 pont)

Készíts programot (`feladat1.py`), amely bekéri a felhasználó **vezetéknevét**, **keresztnevét** és **kedvenc számát**, majd három erős jelszójavaslatot állít össze.

### Működés:

1. Kérd be a vezetéknevet, a keresztnevet és a kedvenc számot.
2. A beírt neveket alakítsd nagybetűsre.
3. Állíts össze három jelszót az alábbi formátumokban:
   - **1. jelszó:** keresztnév utolsó 3 betűje + `_` + kedvenc szám + vezetéknév első betűje (pl. `NNA_42K`)
   - **2. jelszó:** vezetéknév fordítva + kedvenc szám (pl. `SSIK42`)
   - **3. jelszó:** keresztnév első betűje + kedvenc szám + `#` + teljes vezetéknév (pl. `A42#KISS`)
4. Jelenítsd meg a három jelszót a képernyőn.

### Technikai elvárások:

- A program **legalább 3 függvényt** tartalmazzon (bekérés, feldolgozás, megjelenítés).

---

## 2. feladat – Nyerőgépes tippelős játék (14 pont)

Készíts programot (`feladat2.py`), amely három véletlenszerű nyerőgép szimbólumot generál (1–10 értékűt), és a játékosnak ki kell találnia a szimbólumok összegét.

### Működés:

1. A program generáljon három véletlenszerű számot 1 és 10 között, és tárolja listában.
2. A játékos tippelhet, mennyi a három szimbólum összege.
3. A program értékelje ki a tippet:
   - Ha a tipp kisebb, mint 3 vagy nagyobb, mint 30: **„HIBA: nem lehetséges érték!"**
   - Ha a tipp kisebb, mint az összeg: **„Ennél több"**
   - Ha a tipp nagyobb, mint az összeg: **„Ennél kevesebb"**
   - Ha a tipp megegyezik az összeggel: **„Talált!"**
4. A játék addig folytatódik, amíg a játékos el nem találja az összeget.
5. Tartsa nyilván a tippek számát.
6. A játék végén írja ki a húzott szimbólumokat, a tippek számát, és köszönje meg a játékot: **„Köszönjük a játékot!"**

### Technikai elvárások:

- A `random` modul használata szükséges.
- A program `while` ciklust használjon.
- A program **legalább 2 függvényt** tartalmazzon.

---

## 3. feladat – Zenék feldolgozása (18 pont)

Az UTF-8 kódolású `zenek.txt` fájl zenék adatait tartalmazza pontosvesszővel elválasztva:

**cím;műfaj;év;hossz_mp;értékelés**

A műfajok: pop, rock, elektronikus, hiphop.

### Feladatok:

1. Olvasd be az állomány tartalmát szótárak listájába. Az évet és a hosszt alakítsd egész számmá, az értékelést valós számmá (float). Ha nem tudod a fájlt beolvasni, használhatod a `zenek.py` modult.
2. Írd ki, hány zene található a listában.
3. Írd ki, hogy hány pop, rock, elektronikus és hiphop zene van.
4. Keresd meg és írd ki a legjobb és a legrosszabb értékelésű zene címét és értékelését.
5. Kérd be egy zene címét! Ha megtalálható a listában, írd az adatait egy `valasztott_zene.txt` fájlba pontosvesszővel elválasztva. Ha nem létezik, írd ki: „Nincs ilyen cím a listában".
6. Kérd be egy műfaj nevét! Írd ki az adott műfajba tartozó zenék címét és megjelenési évét.

### Technikai elvárások:

- A segédfüggvényeket a `fgv.py` fájlba írd!
- A `fgv.py` modult importáld a `feladat3.py` fájlban!
- A `fgv.py` fájlban az alábbi függvényneveket használd:

| Függvény | Leírás |
|----------|--------|
| `beolvasas(fajlnev)` | Beolvassa a fájlt, visszaadja szótárak listáját |
| `darabszam(zenek)` | Visszaadja az elemek számát |
| `mufajok_szama(zenek)` | Visszaad egy szótárat a műfajok darabszámával |
| `legjobb_legrosszabb(zenek)` | Visszaadja a legjobb és legrosszabb értékelésű zenét |
| `zene_keresese(zenek, cim)` | Visszaadja a zenét cím alapján, vagy `None`-t |
| `zene_fajlba_iras(zene, fajlnev)` | Kiírja a zene adatait fájlba pontosvesszővel |
| `mufajhoz_tartozo_zenek(zenek, mufaj)` | Visszaadja az adott műfaj zenéinek címét és évét |

---

## Beadás

1. `git add .`
2. `git commit -m "vizsga megoldás"`
3. `git push`

Az utolsó push az óra végén = beadás!
