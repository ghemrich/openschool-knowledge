# Python szintfelmérő – 10. évfolyam

**Időtartam:** 90 perc
**Összpontszám:** 40 pont

---

## 1. feladat – Becenévgeneráló program (8 pont)

Készíts programot, amely bekéri a felhasználó **vezetéknevét**, **keresztnevét** és **születési évét**, majd három ajánlott becenevet állít össze.

### Működés:

1. A program kérje be a vezetéknevet, a keresztnevet és a születési évet.
2. A beírt neveket alakítsa kisbetűsre.
3. Állítson össze három becenevet az alábbi formátumokban:
   - **1. becenév:** keresztnév első 3 betűje + születési év utolsó 2 jegye (pl. `ann04`)
   - **2. becenév:** teljes vezetéknév + `_` + keresztnév utolsó betűje + születési év utolsó 2 jegye (pl. `kiss_a04`)
   - **3. becenév:** teljes keresztnév + születési év utolsó 2 jegye + `.` + vezetéknév fordítva (pl. `anna04.ssik`)
4. Jelenítse meg a három becenevet a képernyőn.

### Technikai elvárások:

- A program függvényekre bontva legyen megírva.
- Az adatbekérés, az összefűzés és a megjelenítés külön függvényben legyen.

---

## 2. feladat – Golyóhúzásos tippelős játék (14 pont)

Készíts programot, amely négy véletlenszerű golyót húz (1–5 értékűt), és a játékosnak ki kell találnia a golyók összegét.

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
6. A játék végén írja ki a húzott golyókat, a tippek számát, és köszönje meg a játékot.

### Technikai elvárások:

- A `random` modul használata szükséges.
- A program függvényekre bontva és `while` ciklussal legyen megírva.

---

## 3. feladat – Sportolók feldolgozása (18 pont)

Az UTF-8 kódolású `sportolok.txt` állomány sportolók adatainak listáját tartalmazza. Az állomány sorai azonos szerkezetűek, az adattagok pontosvesszővel tagoltak. Az állomány egy sora például:

**Tóth Gábor;futás;magyar;2008;5;88.5**

Az adattagok jelentése rendre a következők: sportoló neve, sportága, nemzetisége, első versenyének éve, érmek száma, pontszáma.

### Feladatok:

1. Olvasd be az állomány tartalmát, és tárold le a megfelelő összetett adatszerkezetű listában! Ha nem tudod a fájlt beolvasni, használhatod a `sportolok.py` modult.
2. Írd ki, hogy hány sportoló található a listában!
3. Írd ki, hogy hány magyar, német, francia és angol nemzetiségű sportoló található a listában!
4. Írd ki a legtöbb és a legkevesebb éremmel rendelkező sportoló nevét és érmei számát!
5. Kérd be a felhasználótól egy sportoló nevét! Ha van ilyen név a listában, akkor annak az összes adatát írd ki egy fájlba (`valasztott_sportolo.txt`), és erről tájékoztasd a felhasználót! Ha nincs a listában ilyen nevű sportoló, akkor a „Nincs ilyen név a listában" szöveget jelenítsd meg!
6. Kérd be a felhasználótól egy sportág nevét! A képernyőre írd ki az összes sportoló nevét és érmei számát, aki a megadott sportághoz tartozik!

### Technikai elvárások:

- A segédfüggvényeket külön modulban (`fgv.py`) kell megírni.
- A `fgv.py` modult importálni kell a `feladat3.py`-ban.
- Minden alfeladathoz külön függvény tartozzon.
