# Kiegészítő gyakorlatok – 0. hét: Git és GitHub alapok

> Ezek a feladatok a heti házi feladat melletti **extra gyakorlást** szolgálják.
> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz

---

### 0.1 – .gitignore ⭐
Hozz létre egy `.gitignore` fájlt a repódban, amely kizárja a `__pycache__/` mappát és a `.pyc` fájlokat. Hozz létre egy `teszt.pyc` fájlt, és ellenőrizd `git status`-szal, hogy a Git nem követi.

### 0.2 – Commit üzenetek ⭐
Hozz létre egy `jegyzetek.txt` fájlt és módosítsd 5 alkalommal. Minden commit üzenete kövesse az alábbi mintát: `típus: rövid leírás` (pl. `feat: jegyzetek fájl létrehozása`, `fix: elírás javítása`). Futtasd a `git log --oneline`-t és mentsd egy `log.txt` fájlba.

### 0.3 – Git diff ⭐⭐
Módosíts egy fájlt anélkül, hogy commitolnád. Futtasd a `git diff` parancsot és másold a kimenetét egy `diff_kimenet.txt` fájlba. Írd fölé kommentben, hogy mit jelentenek a `+` és `-` jelek. Commitold az egészet.
