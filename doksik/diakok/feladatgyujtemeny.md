# Feladatgyűjtemény – Házi feladatok és gyakorlófeladatok

> Minden héten oldd meg a hozzád tartozó feladatokat! A megoldásokat commitold és pushold a GitHub repódba.
> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz

---

## 0. hét – Git és GitHub alapok

### 0.1 – Első repo ⭐
Hozz létre egy `bemutatkozas.py` fájlt, amely kiírja a neved. Commitold és pushold GitHubra.

### 0.2 – Több commit ⭐
Módosítsd a `bemutatkozas.py` fájlt háromszor, és mindegyik módosítás után készíts egy külön commitot értelmes üzenettel. Pushold az eredményt.

### 0.3 – Git napló ⭐⭐
Futtasd a `git log --oneline` parancsot, és készíts egy képernyőképet vagy másold be a terminál kimenetét egy `git_naplo.txt` fájlba. Commitold és pushold.

---

## 1. hét – Bevezetés és alapok

### 1.1 – Bemutatkozás ⭐
Írj programot, amely kiírja a neved, a korod, a lakóhelyedet és a kedvenc hobbid külön-külön sorokban. Használj változókat!

### 1.2 – Számológép ⭐
Hozz létre két változót (`a = 15`, `b = 4`), és írd ki az összegüket, különbségüket, szorzatukat, hányadosukat és a maradékos osztás eredményét.

### 1.3 – Névjegykártya ⭐⭐
Tárold változókban a következő adatokat: név, életkor, osztály, iskola neve. Írd ki az adatokat egy szép formázott névjegykártya formájában a `print()` segítségével.

### 1.4 – Típusok felfedezése ⭐⭐
Hozz létre legalább 6 változót (2 `int`, 2 `float`, 1 `str`, 1 `bool`), és mindegyikről írd ki a `type()` függvénnyel a típusát is.

### 1.5 – Személyi igazolvány ⭐⭐⭐
Készíts programot, amely változókban tárolja egy személy adatait (név, születési év, személyi szám, lakcím), majd kiírja ezeket formázottan. A kiírás így nézzen ki:
```
=========================
     SZEMÉLYI IGAZOLVÁNY
=========================
Név:    Kiss Anna
Szül.:  2010
Szem.:  123456AB
Cím:    Budapest, Fő u. 1.
=========================
```

---

## 2. hét – Bevitel és szövegkezelés

### 2.1 – Köszöntő ⭐
Kérd be a felhasználó nevét, majd írd ki: „Üdvözöllek, [név]!"

### 2.2 – Életkor számítás ⭐
Kérd be a felhasználó születési évét (szám), és számold ki, hány éves lesz idén. Írd ki az eredményt.

### 2.3 – Téglalap kerülete ⭐⭐
Kérd be egy téglalap két oldalának hosszát, és számold ki a kerületét és a területét. Írd ki az eredményt 2 tizedesjegy pontossággal f-string segítségével.

### 2.4 – Monogram ⭐⭐
Kérd be a felhasználó vezeték- és keresztnevét! Írd ki:
- A teljes nevet nagybetűsítve
- A monogramot (pl. „K.A.")
- A nevet fordítva (keresztnév + vezetéknév)

### 2.5 – Jelszó generátor ⭐⭐
Kérd be a felhasználó nevét és kedvenc számát! Állíts elő egy „jelszót" az alábbi képlettel: a név első 3 betűje kisbetűvel + a kedvenc szám + a név utolsó 2 betűje nagybetűvel. Például: név = „Kovács", szám = „42" → „kov42CS"

### 2.6 – Egységátváltó ⭐⭐⭐
Kérd be egy távolságot kilométerben (tizedestört is lehet)! Váltsd át mérföldre (1 km = 0.621371 mérföld), méterre, és centiméterbe. Írd ki mindhárom eredményt 2 tizedesjegyre kerekítve.

---

## 3. hét – Feltételes elágazások

### 3.1 – Pozitív/negatív ⭐
Kérj be egy számot, és írd ki, hogy pozitív, negatív, vagy nulla.

### 3.2 – Belépőjegy ⭐
Kérd be a látogató életkorát! 6 év alatt ingyenes, 6–14 között 500 Ft, 14–65 között 1000 Ft, 65 felett 600 Ft. Írd ki az árat.

### 3.3 – Osztályzat szövegesen ⭐⭐
Kérd be egy dolgozat százalékos eredményét! Írd ki az osztályzatot:
- 90–100%: Jeles (5)
- 75–89%: Jó (4)
- 60–74%: Közepes (3)
- 40–59%: Elégséges (2)
- 0–39%: Elégtelen (1)

### 3.4 – Háromszög ⭐⭐
Kérd be egy háromszög három oldalát! Döntsd el, hogy a háromszög egyenlő oldalú, egyenlő szárú, vagy általános háromszög.

### 3.5 – Szökőév ⭐⭐
Kérd be egy évszámot! Döntsd el, hogy szökőév-e! (Szökőév: osztható 4-gyel, DE nem osztható 100-zal, KIVÉVE ha osztható 400-zal.)

### 3.6 – Távolsági vonat ⭐⭐⭐
Kérd be a jegy típusát („teljes" vagy „kedvezményes"), az utazás távolságát km-ben, és hogy első vagy másodosztályú helyet kér! Árak:
- Alapár: 20 Ft/km
- Kedvezményes: 50% kedvezmény
- Első osztály: +40% felár
Számold ki és írd ki a jegy végső árát.

---

## 4. hét – Ciklusok

### 4.1 – Visszaszámlálás ⭐
Írj programot, amely 10-től 1-ig visszaszámol, majd kiírja: „Start!"

### 4.2 – Páros számok ⭐
Írd ki az összes páros számot 1 és 50 között!

### 4.3 – Szorzótábla ⭐⭐
Kérd be egy számot, és írd ki a szorzótábláját 1-től 10-ig szép formázásban (pl. „5 x 3 = 15").

### 4.4 – Összegző ⭐⭐
A program kérjen be számokat a felhasználótól, amíg 0-t nem ír be. A végén írja ki az összeget és az átlagot.

### 4.5 – Jelszóellenőrző ⭐⭐
A program kérjen be egy jelszót. Ha a jelszó nem „titok123", kérje be újra. Maximum 3 próbálkozás legyen! Ha 3-nál több próba után sem sikerül, írja ki: „Fiók zárolva."

### 4.6 – Piramis rajzoló ⭐⭐⭐
Kérd be a sorok számát (n), majd rajzolj csillagokból piramist:
```
    *
   ***
  *****
 *******
*********
```

### 4.7 – Tökéletes számok ⭐⭐⭐
Írd ki az összes tökéletes számot 1 és 1000 között! (Egy szám tökéletes, ha egyenlő az osztóinak összegével, önmagát nem számítva. Pl. 6 = 1 + 2 + 3.)

---

## 5. hét – Listák

### 5.1 – Kedvencek ⭐
Hozz létre egy listát 5 kedvenc ételeddel! Írd ki az elemeket sorszámozva (`enumerate`).

### 5.2 – Páros szűrő ⭐
Adott a lista: `[3, 8, 12, 5, 22, 7, 18, 1, 30, 11]`. Írd ki belőle csak a páros számokat!

### 5.3 – Statisztika ⭐⭐
Kérj be 5 számot a felhasználótól, tárold listában! Írd ki az összegüket, átlagukat, a legkisebbet és a legnagyobbat.

### 5.4 – Bevásárlólista ⭐⭐
Készíts programot, ahol a felhasználó hozzáadhat elemeket egy bevásárlólistához, törölhet elemet, és ki tudja íratni a listát. A program addig fusson, amíg a felhasználó ki nem lép.

### 5.5 – Név rendezés ⭐⭐
Kérj be neveket a felhasználótól (üres sor = vége)! Rendezd ABC sorrendbe, és írd ki a rendezett listát sorszámozva.

### 5.6 – Lista comprehension gyakorlat ⭐⭐⭐
Az alábbi feladatokat oldd meg lista comprehension-nel:
1. Az 1–20 közötti számok négyzetei
2. Az 1–50 közötti 3-mal osztható számok
3. Egy bekért mondat szavainak hosszai (pl. „Szia világ" → [4, 5])

---

## 6. hét – Függvények

### 6.1 – Köszöntő függvény ⭐
Írj egy `koszont(nev)` függvényt, amely kiírja: „Szia, [név]! Üdv a programban!" Hívd meg 3 különböző névvel.

### 6.2 – Területszámítók ⭐
Írj függvényeket a következő alakzatok területének kiszámítására:
- `teglalap_terulet(a, b)`
- `kor_terulet(r)`
- `haromszog_terulet(a, m)`

Teszteld mindegyiket!

### 6.3 – Hőmérséklet átváltó ⭐⭐
Írj két függvényt:
- `celsius_fahrenheit(c)` → átváltás Fahrenheitre
- `fahrenheit_celsius(f)` → átváltás Celsiusra

A főprogramban kérd be az értéket és az irányt, majd hívd meg a megfelelő függvényt.

### 6.4 – Legkisebb keresés ⭐⭐
Írj egy `legkisebb(szamok)` függvényt, amely egy számlistából visszaadja a legkisebb elemet (ne használj `min()`-t!). A főprogramban kérj be 5 számot, és hívd meg a függvényt.

### 6.5 – Névgenerátor ⭐⭐⭐
Írj programot **három függvénnyel** (pont mint a vizsga 1. feladatában):
1. `bekeres()` – bekéri a vezetéknevet, keresztnevet, kedvenc állatot
2. `generalas(vnev, knev, allat)` – előállít 3 felhasználónevet (legyél kreatív a formátumokkal!)
3. `kiiras(nev1, nev2, nev3)` – kiírja a neveket

A főprogram hívja meg a három függvényt a megfelelő sorrendben.

### 6.6 – Prímszám ellenőrző ⭐⭐⭐
Írj egy `prim_e(szam)` függvényt, amely `True`-t ad vissza, ha a szám prím, `False`-t ha nem. A főprogramban írd ki az összes prímet 1 és 100 között!

---

## 7. hét – Random modul és játéklogika

### 7.1 – Dobókocka ⭐
Írj programot, amely dob egy kockával (1–6), és kiírja az eredményt.

### 7.2 – Többszöri dobás ⭐
Kérd be, hányszor akar a felhasználó dobni! Dobd meg annyiszor a kockát, és írd ki a dobások listáját, összegét és átlagát.

### 7.3 – Kő-papír-olló ⭐⭐
Készíts kő-papír-olló játékot! A gép véletlenszerűen választ, a játékos billentyűzetről. Írd ki, ki nyert.

### 7.4 – Lottóhúzás ⭐⭐
Generálj 5 különböző véletlenszámot 1 és 90 között! (Ügyelj rá, hogy ne ismétlődjenek!) Rendezd sorba és írd ki.

### 7.5 – Tippelős játék ⭐⭐⭐
Írj tippelős játékot (mint a vizsga 2. feladata), **de** adjál hozzá egy nehézségi szintet:
- Könnyű: 1–10 közötti szám, korlátlan tipp
- Közepes: 1–50 közötti szám, max 10 tipp
- Nehéz: 1–100 közötti szám, max 7 tipp

A program a végén írja ki, hány tippből találta el.

### 7.6 – Memóriajáték ⭐⭐⭐
A program generál egy véletlenszerű számsorozatot (pl. 3 szám 1–9 között), megmutatja 3 másodpercig, majd kitörli a képernyőt. A játékosnak vissza kell gépelnie a számokat. Minden körben eggyel több szám legyen! A játék addig tart, amíg a játékos hibázik.

> Tipp: `import time` és `time.sleep(3)` a várakozáshoz, `import os` és `os.system("clear")` a képernyő törléséhez.

---

## 8. hét – Fájlkezelés

### 8.1 – Fájl létrehozás ⭐
Írj programot, amely létrehoz egy `naplo.txt` fájlt, és beleír 3 sort (pl. a mai nap eseményei).

### 8.2 – Fájl olvasás ⭐
Írj programot, amely beolvassa a `naplo.txt` fájlt és kiírja a tartalmát sorszámozva.

### 8.3 – Szó számláló ⭐⭐
Írj programot, amely beolvas egy szövegfájlt, és kiírja:
- A sorok számát
- A szavak számát
- A karakterek számát (szóközök nélkül)

### 8.4 – Tanulói adatok ⭐⭐
Hozz létre egy `tanulok.txt` fájlt az alábbi tartalommal:
```
Kiss Anna;16;Budapest;4.5
Nagy Béla;17;Debrecen;3.8
Tóth Csaba;16;Szeged;4.2
```
Írj programot, amely beolvassa és kiírja az adatokat formázottan.

### 8.5 – Jegyzetfüzet alkalmazás ⭐⭐⭐
Készíts programot, amely:
1. Bekér egy sort a felhasználótól
2. Hozzáfűzi (`"a"` mód) a `jegyzetek.txt` fájlhoz dátummal (pl. „2026-03-09: szöveg")
3. Ki tudja listázni az összes korábbi jegyzetet
4. A program menüből vezérelve fusson (1 = új jegyzet, 2 = listázás, 3 = kilépés)

---

## 9. hét – Összetett adatszerkezetek

### 9.1 – Lista listája ⭐
Hozz létre egy 3×3-as „mátrixot" (lista listája számokkal), és írd ki formázottan.

### 9.2 – Szótár alapok ⭐
Hozz létre egy szótárat 5 magyar-angol szópárral. Kérd be egy magyar szót, és írd ki az angol megfelelőjét, vagy „Nem található", ha nincs benne.

### 9.3 – Diákok szótárban ⭐⭐
Hozz létre egy szótárak listáját 3 diák adataival (név, kor, jegyek listája). Írd ki mindegyik diák nevét és jegyeinek átlagát.

### 9.4 – Mini adatbázis ⭐⭐
Írj programot, amely `input()`-tal kéri be termékek adatait (név, ár, mennyiség), szótárak listájában tárolja, és a végén kiírja:
- Az összes terméket
- A legdrágább terméket
- Az összes termék értékét (ár × mennyiség összege)

### 9.5 – Fájlból szótárba ⭐⭐⭐
Olvasd be a tanulók adatait egy pontosvesszővel tagolt fájlból szótárak listájába! A fájl formátuma:
```
név;kor;város;átlag
```
Írd ki az adatokat táblázatszerűen, és keresd meg a legjobb átlagú diákot.

---

## 10. hét – Adatfeldolgozás

### 10.1 – Számlálás ⭐
Adott egy szavakat tartalmazó lista: `["alma", "körte", "alma", "szilva", "körte", "alma"]`. Számold meg, melyik szó hányszor fordul elő! Használj szótárat.

### 10.2 – Szűrés ⭐⭐
Adott szótárak listája (termékek: név, ár, kategória). Kérd be egy kategóriát, és írd ki a hozzá tartozó termékeket.

### 10.3 – Min/max keresés ⭐⭐
Adott szótárak listája (diákok: név, pontszám). Keresd meg és írd ki a legjobb és legrosszabb pontszámú diákot (ne használj `min()`/`max()` beépített függvényt!).

### 10.4 – Statisztika fájlból ⭐⭐
Olvasd be a `filmek.txt` (vagy `konyvek.txt`) fájlt, és írd ki:
- Hány elem van összesen
- A kategóriák/nyelvek szerinti darabszámot
- A legjobb/legrosszabb értékelésű/bevételű elemet

### 10.5 – Top 5 lista ⭐⭐⭐
Olvasd be a `filmek.txt` fájlt! Kérd be egy kategóriát, és írd ki az adott kategória **5 legjobb értékelésű** filmjét csökkenő sorrendben.

### 10.6 – Összesítő riport ⭐⭐⭐
Olvasd be a `filmek.txt` fájlt! Készíts egy összesítő riportot, amelyet egy `riport.txt` fájlba írsz:
- Összesen hány film van
- Kategóriánként: db, átlagos értékelés, legjobb film címe
- A 3 legjobb és 3 legrosszabb film

---

## 11. hét – Modulok és összefoglaló projekt

### 11.1 – Első modul ⭐
Hozz létre egy `matek.py` modult az alábbi függvényekkel:
- `osszeg(a, b)`
- `szorzat(a, b)`
- `hatvany(alap, kitevo)`

A főprogramban (`foprogram.py`) importáld és teszteld mindhárom függvényt.

### 11.2 – Szöveg modul ⭐⭐
Hozz létre egy `szoveg_eszkozok.py` modult:
- `nagybetus(szoveg)` – nagybetűsre alakít
- `szavak_szama(szoveg)` – visszaadja a szavak számát
- `forditott(szoveg)` – megfordítja a szöveget

A főprogramban kérj be egy mondatot és teszteld mindhárom függvényt!

### 11.3 – Teljes vizsgafeladat gyakorlás ⭐⭐⭐
Oldd meg a teljes 3. vizsga feladatot (a `filmek.txt` VAGY `konyvek.txt` alapján):
1. Beolvasás összetett adatszerkezetbe
2. Darabszám kiírása
3. Kategória/nyelv szerinti számlálás
4. Legjobb/legrosszabb keresése
5. Cím szerinti keresés + fájlba írás
6. Kategória/műfaj szerinti szűrés

A függvényeket `fgv.py` modulban helyezd el, a főprogramot `feladat3.py`-ban. Commitold és pushold!

### 11.4 – Saját projekt ⭐⭐⭐
Válassz egy témát (pl. zenék, sportolók, receptek), és készíts hozzá:
1. Egy `.txt` adatfájlt legalább 15 rekorddal
2. Egy `fgv.py` modult legalább 4 függvénnyel (beolvasás, számlálás, keresés, szűrés)
3. Egy főprogramot, amely használja a modult
4. Commitold és pushold a repódba!

---

## 12. hét – Vizsgafelkészítés

### 12.1 – Próbavizsga ⭐⭐⭐
Oldd meg a teljes vizsgát (mindhárom feladat) 90 perc alatt, vizsga körülmények között:
1. Fogadd el a GitHub Classroom próbavizsga linket
2. Klónozd le, dolgozz, commitolj rendszeresen
3. Az utolsó push a beadás

### 12.2 – Hibakeresés ⭐⭐
Az alábbi kódrészletekben hibák vannak. Keresd meg és javítsd ki őket!

**a)**
```python
nev = input("Neved: ")
print("Szia, " + nev + "! Te " + 16 + " éves vagy.")
```

**b)**
```python
import random
szam = random.randint(1, 10)
tipp = input("Tippelj: ")
if tipp == szam:
    print("Talált!")
```

**c)**
```python
with open("adatok.txt", "r") as f:
    for sor in f:
        adatok = sor.split(";")
        ev = adatok[2]
        print(ev + 1)
```

**d)**
```python
def beolvas(fajl):
    lista = []
    with open(fajl) as f:
        for sor in f:
            adat = sor.split(";")
            lista.append(adat)
    return lista

adatok = beolvas("adatok.txt")
print(adatok[0]["nev"])
```

### 12.3 – Git gyakorlás ⭐
Készíts egy `hello.py` fájlt. Végezd el az alábbi lépéseket, és minden lépés után futtasd a `git log --oneline` parancsot:
1. Hozd létre a fájlt egy `print("Hello")` sorral → commit
2. Adj hozzá egy második `print()` sort → commit
3. Adj hozzá egy `input()` bekérést → commit
4. Pushold az egészet
