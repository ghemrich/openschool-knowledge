# Python szintfelmérő – Filmek (A variáns)

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

## 1. feladat – Felhasználónév generáló program (8 pont)

Készíts programot (`feladat1.py`), amely bekéri a felhasználó **vezetéknevét**, **keresztnevét** és **kedvenc számát**, majd három ajánlott felhasználónevet állít össze.

### Működés:

1. A program kérje be a vezetéknevet, a keresztnevet és a kedvenc számot.
2. A beírt neveket alakítsa kisbetűsre.
3. Állítson össze három felhasználónevet az alábbi formátumokban:
   - **1. név:** teljes keresztnév + vezetéknév első betűje + kedvenc szám (pl. `annak42`)
   - **2. név:** keresztnév első betűje + `_` + teljes vezetéknév + kedvenc szám (pl. `a_kiss42`)
   - **3. név:** teljes vezetéknév + `.` + teljes keresztnév + kedvenc szám (pl. `kiss.anna42`)
4. Jelenítse meg a három felhasználónevet a képernyőn.

### Technikai elvárások:

- A program **legalább 3 függvényt** tartalmazzon (bekérés, feldolgozás, megjelenítés).

---

## 2. feladat – Kártyahúzós tippelős játék (14 pont)

Készíts programot (`feladat2.py`), amely három véletlenszerű kártyát húz (1–13 értékűt), és a játékosnak ki kell találnia a kártyák összegét.

### Működés:

1. A program generáljon három véletlenszerű számot 1 és 13 között, és tárolja listában.
2. A játékos tippelhet, mennyi a három kártya összege.
3. A program értékelje ki a tippet:
   - Ha a tipp kisebb, mint 3 vagy nagyobb, mint 39: **„HIBA: nem lehetséges érték!"**
   - Ha a tipp kisebb, mint az összeg: **„Ennél több"**
   - Ha a tipp nagyobb, mint az összeg: **„Ennél kevesebb"**
   - Ha a tipp megegyezik az összeggel: **„Talált!"**
4. A játék addig folytatódik, amíg a játékos el nem találja az összeget.
5. Tartsa nyilván a tippek számát.
6. A játék végén írja ki a húzott kártyákat, a tippek számát, és köszönje meg a játékot: **„Köszönjük a játékot!"**

### Technikai elvárások:

- A `random` modul használata szükséges.
- A program `while` ciklust használjon.
- A program **legalább 2 függvényt** tartalmazzon.

---

## 3. feladat – Filmek feldolgozása (18 pont)

Az UTF-8 kódolású `filmek.txt` fájl filmek adatait tartalmazza pontosvesszővel elválasztva:

**cím;kategória;év;hossz_perc;értékelés**

A kategóriák: akció, vígjáték, dráma, horror.

### Feladatok:

1. Olvasd be az állomány tartalmát szótárak listájába. Az évet és a hosszt alakítsd egész számmá, az értékelést valós számmá (float). Ha nem tudod a fájlt beolvasni, használhatod a `filmek.py` modult.
2. Írd ki, hány film található a listában.
3. Írd ki, hogy hány akció, vígjáték, dráma és horror film van.
4. Keresd meg és írd ki a legjobb és a legrosszabb értékelésű film címét és értékelését.
5. Kérd be egy film címét! Ha megtalálható a listában, írd ki az adatait egy `valasztott_film.txt` fájlba pontosvesszővel elválasztva. Ha nem létezik, írd ki: „Nincs ilyen cím a listában".
6. Kérd be egy kategória nevét! Írd ki az adott kategóriába tartozó filmek címét és megjelenési évét.

### Technikai elvárások:

- A segédfüggvényeket a `fgv.py` fájlba írd!
- A `fgv.py` modult importáld a `feladat3.py` fájlban!
- A `fgv.py` fájlban az alábbi függvényneveket használd:

| Függvény | Leírás |
|----------|--------|
| `beolvasas(fajlnev)` | Beolvassa a fájlt, visszaadja szótárak listáját |
| `darabszam(filmek)` | Visszaadja az elemek számát |
| `kategoriak_szama(filmek)` | Visszaad egy szótárat a kategóriák darabszámával |
| `legjobb_legrosszabb(filmek)` | Visszaadja a legjobb és legrosszabb értékelésű filmet |
| `film_keresese(filmek, cim)` | Visszaadja a filmet cím alapján, vagy `None`-t |
| `film_fajlba_iras(film, fajlnev)` | Kiírja a film adatait fájlba pontosvesszővel |
| `kategoriahoz_tartozo_filmek(filmek, kategoria)` | Visszaadja az adott kategória filmjeinek címét és évét |

---

## Beadás

1. `git add .`
2. `git commit -m "vizsga megoldás"`
3. `git push`

Az utolsó push az óra végén = beadás!
