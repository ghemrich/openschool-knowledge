# Feladatok – 7. hét: Random modul és játéklogika

> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz
> A megoldásokat commitold és pushold a GitHub repódba.

---

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
