# Python szintfelmérő – 10. évfolyam

**Időtartam:** 90 perc
**Összpontszám:** 40 pont

---

## 1. feladat – Jelszógeneráló program (8 pont)

Készíts programot, amely bekéri a felhasználó **vezetéknevét**, **keresztnevét** és **kedvenc számát**, majd három erős jelszójavaslatot állít össze.

### Működés:

1. A program kérje be a vezetéknevet, a keresztnevet és a kedvenc számot.
2. A beírt neveket alakítsa nagybetűsre.
3. Állítson össze három jelszót az alábbi formátumokban:
   - **1. jelszó:** keresztnév utolsó 3 betűje + `_` + kedvenc szám + vezetéknév első betűje (pl. `NNA_42K`)
   - **2. jelszó:** vezetéknév fordítva + kedvenc szám (pl. `SSIK42`)
   - **3. jelszó:** keresztnév első betűje + kedvenc szám + `#` + teljes vezetéknév (pl. `A42#KISS`)
4. Jelenítse meg a három jelszót a képernyőn.

### Technikai elvárások:

- A program függvényekre bontva legyen megírva.
- Az adatbekérés, az összefűzés és a megjelenítés külön függvényben legyen.

---

## 2. feladat – Nyerőgépes tippelős játék (14 pont)

Készíts programot, amely három véletlenszerű nyerőgép szimbólumot generál (1–10 értékűt), és a játékosnak ki kell találnia a szimbólumok összegét.

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
6. A játék végén írja ki a húzott szimbólumokat, a tippek számát, és köszönje meg a játékot.

### Technikai elvárások:

- A `random` modul használata szükséges.
- A program függvényekre bontva és `while` ciklussal legyen megírva.

---

## 3. feladat – Zenék feldolgozása (18 pont)

Az UTF-8 kódolású `zenek.txt` fájl zenék adatait tartalmazza pontosvesszővel elválasztva:

**cím;műfaj;év;hossz_mp;értékelés**

A műfajok: pop, rock, elektronikus, hiphop.

### Feladatok:

1. Olvasd be az állomány tartalmát, és tárold összetett adatszerkezetű listában (lista listája vagy szótárak listája). Az évet és a hosszt alakítsd egész számmá, az értékelést valós számmá (float). Ha nem tudod a fájlt beolvasni, használhatod a `zenek.py` modult.
2. Írd ki, hány zene található a listában.
3. Írd ki, hogy hány pop, rock, elektronikus és hiphop zene van.
4. Keresd meg és írd ki a legjobb és a legrosszabb értékelésű zene címét és értékelését.
5. Kérd be egy zene címét! Ha megtalálható a listában, írd ki az adatait egy `valasztott_zene.txt` fájlba pontosvesszővel elválasztva. Ha nem létezik, írd ki: „Nincs ilyen cím a listában".
6. Kérd be egy műfaj nevét! Írd ki az adott műfajba tartozó zenék címét és megjelenési évét.

### Technikai elvárások:

- A segédfüggvényeket külön modulban (`fgv.py`) kell megírni.
- A `fgv.py` modult importálni kell a `feladat3.py`-ban.
- Minden alfeladathoz külön függvény tartozzon.
