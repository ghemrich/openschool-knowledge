# Python kurzus tanterv – 10. évfolyam

## Kurzus áttekintés

**Cél:** A diákok elsajátítsák a Python programozás és a Git/GitHub alapjait, és felkészüljenek a szintfelmérő vizsgára.
**Időtartam:** 13 hét (heti 2 óra = 26 tanóra)
**Vizsga:** 40 pontos szintfelmérő (90 perc, GitHub Classroom-on keresztül)

---

## Szükséges Python ismeretek (vizsgakövetelmények alapján)

| Témakör | Vizsga feladat |
|---------|---------------|
| `print()`, `input()`, változók | 1., 2., 3. feladat |
| Típuskonverzió (`int()`, `float()`, `str()`) | 1., 2., 3. feladat |
| Szövegműveletek (indexelés, `.lower()`, összefűzés, f-string) | 1. feladat |
| Feltételes elágazás (`if/elif/else`) | 2. feladat |
| `while` ciklus | 2. feladat |
| Listák (létrehozás, bejárás, `append`, `sum()`) | 2., 3. feladat |
| `import random`, `random.randint()` | 2. feladat |
| Függvények (`def`, paraméterek, `return`) | 1., 2., 3. feladat |
| Fájlkezelés (olvasás, írás, UTF-8) | 3. feladat |
| `.split()`, `.strip()` | 3. feladat |
| Összetett adatszerkezetek (lista listája, szótárak listája) | 3. feladat |
| Szűrés, számlálás, min/max keresés | 3. feladat |
| Saját modul készítése és importálása | 3. feladat |
| Git alapok, GitHub Classroom | vizsga beadás, házi feladatok |

---

## Heti bontás

### 0. hét – Git és GitHub alapok
**0. óra: Git bevezetés**
- Mi a Git? Mi a GitHub?
- Git telepítés és beállítás (`git config`)
- Alapfogalmak: repository, commit, push, clone
- Alapparancsok: `git add`, `git commit`, `git push`, `git status`
- GitHub Classroom: feladat elfogadása, klónozás, beadás
- Gyakorlat: első repo létrehozása és commit

---

### 1. hét – Bevezetés és alapok
**1. óra: A Python világa**
- Mi a programozás? Mi a Python?
- Fejlesztői környezet beállítása
- Első program: `print("Hello, világ!")`
- Megjegyzések (`#`)

**2. óra: Változók és típusok**
- Változók létrehozása, elnevezési szabályok
- Alaptípusok: `int`, `float`, `str`, `bool`
- `type()` függvény
- Gyakorlat: saját bemutatkozó program

---

### 2. hét – Bevitel és szövegkezelés
**3. óra: Billentyűzetes bevitel**
- `input()` függvény
- Típuskonverzió: `int()`, `float()`, `str()`
- Gyakorlat: egyszerű számológép (két szám összeadása)

**4. óra: Szövegműveletek**
- Szöveg összefűzés (`+`)
- Szöveg indexelés (`[0]`, `[-1]`)
- Szöveg metódusok: `.lower()`, `.upper()`, `.strip()`
- f-string formázás: `f"Szia, {nev}!"`
- Gyakorlat: névkártya generátor

---

### 3. hét – Feltételes elágazások
**5. óra: Az `if` utasítás**
- `if`, `else` szerkezet
- Összehasonlító operátorok (`==`, `!=`, `<`, `>`, `<=`, `>=`)
- Logikai operátorok (`and`, `or`, `not`)
- Gyakorlat: páros/páratlan eldöntése

**6. óra: Többágú elágazás**
- `elif` használata
- Összetett feltételek
- Beágyazott elágazások
- Gyakorlat: jegybesorolás (1–5 skála szövegesen)

---

### 4. hét – Ciklusok
**7. óra: A `while` ciklus**
- `while` ciklus felépítése
- Számláló változó
- Végtelen ciklus és kilépés
- Gyakorlat: visszaszámlálás, számkitalálós játék

**8. óra: A `for` ciklus és `range()`**
- `for` ciklus szövegen és `range()`-en
- `range(start, stop, step)`
- `break` és `continue`
- Gyakorlat: szorzótábla kiírása

---

### 5. hét – Listák
**9. óra: Listák alapjai**
- Lista létrehozása, indexelés
- `append()`, `len()`, `sum()`
- Lista bejárása `for` ciklussal
- Gyakorlat: bevásárlólista kezelő

**10. óra: Listműveletek**
- Lista szeletelés (`[1:3]`)
- `in` operátor
- Lista rendezés (`.sort()`, `sorted()`)
- Lista comprehension (alapok)
- Gyakorlat: osztályzatok átlaga, min, max

---

### 6. hét – Függvények I.
**11. óra: Függvények alapjai**
- Miért kellenek függvények?
- `def`, paraméterek, `return`
- Függvény hívása
- Gyakorlat: köszöntő függvény, területszámítók

**12. óra: Függvények gyakorlat**
- Több paraméter, több visszatérési érték
- Függvények egymás hívása
- Program struktúrálása függvényekkel
- **Gyakorlat: 1. vizsga feladat típusú program** (névgenerátor függvényekkel)

---

### 7. hét – Random modul és játéklogika
**13. óra: A `random` modul**
- `import random`
- `random.randint(a, b)`
- `random.choice()`, `random.shuffle()`
- Gyakorlat: dobókocka szimulátor

**14. óra: Játékprogram építése**
- `while` ciklus + feltételek + számláló kombinálása
- Hibajelzés érvénytelen bemenetre
- **Gyakorlat: 2. vizsga feladat típusú program** (tippelős játék)

---

### 8. hét – Fájlkezelés I.
**15. óra: Fájlból olvasás**
- `open()` függvény, `encoding="utf-8"`
- Fájl soronkénti olvasása (`for sor in f`)
- `.strip()` és `.split(";")`
- `with` blokk
- Gyakorlat: egyszerű szövegfájl beolvasása és kiírása

**16. óra: Fájlba írás**
- Fájl megnyitása írásra (`"w"`)
- `f.write()` használata
- Gyakorlat: lista mentése fájlba, majd visszaolvasása

---

### 9. hét – Összetett adatszerkezetek
**17. óra: Lista listája**
- Lista, amelynek elemei listák
- Beolvasás fájlból lista listába
- Típuskonverzió beolvasáskor (`int()`, `float()`)
- Gyakorlat: tanulók adatainak tárolása és kiírása

**18. óra: Szótárak és szótárak listája**
- Szótár (`dict`) alapok: kulcs-érték párok
- Szótárak listája mint adatszerkezet
- Hozzáférés: `film["cim"]` vs `film[0]`
- Gyakorlat: ugyanaz az adat kétféle szerkezetben

---

### 10. hét – Adatfeldolgozás
**19. óra: Számlálás, szűrés**
- Elemek számlálása feltétel alapján
- Szűrés kategória/típus szerint
- `.get()` szótár metódus számláláshoz
- Gyakorlat: filmek/könyvek számlálása kategóriánként

**20. óra: Keresés, min/max**
- Lineáris keresés listában
- Minimum és maximum keresés
- Keresés eredményének kiírása
- **Gyakorlat: 3. vizsga feladat részfeladatai** (egyenként)

---

### 11. hét – Modulok és összefoglaló projekt
**21. óra: Saját modul készítése**
- Mi a modul? Miért hasznos?
- `fgv.py` létrehozása függvényekkel
- `import fgv` használata a főprogramban
- `fgv.fuggvenynev()` hívása
- Gyakorlat: adatfeldolgozó program modulokra bontása

**22. óra: Komplex feladat – teljes 3. vizsga feladat**
- Fájl beolvasás → adatszerkezet → feldolgozás → fájlba írás
- Minden részfeladat összekötése
- **Gyakorlat: teljes 3. feladat megoldása lépésről lépésre**

---

### 12. hét – Vizsgafelkészítés
**23. óra: Próbavizsga**
- Teljes vizsga szimulálása (90 perc, 40 pont)
- Vizsga körülmények között dolgozás
- Önellenőrzés az értékelési rubrika alapján

**24. óra: Próbavizsga megbeszélése és kérdések**
- Közös megoldás áttekintése
- Tipikus hibák megbeszélése
- Utolsó kérdések, hiánypótlás

---

## Értékelés

| Elem | Arány |
|------|-------|
| Órai munka, gyakorlatok | 30% |
| Házi feladatok | 20% |
| Próbavizsga | 10% |
| Szintfelmérő vizsga (40 pont) | 40% |

---

## Ajánlott eszközök

- **IDE:** VS Code vagy Thonny
- **Python verzió:** 3.10+
- **Git:** 2.x+
- **GitHub fiók:** minden diáknak kell (ingyenes)
- **Segédanyagok:** órai kódpéldák a `doksik/diakok/` mappában
