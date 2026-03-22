# 0. hét – Git, GitHub, parancssor

> **Beadás:** commitold és pushold a megoldásaidat ebbe a repóba!
> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz

Ezen a héten a parancssort, a Git haladóbb funkcióit és a GitHub munkafolyamatot sajátítod el. Ha már ismered a Git alapokat az előző kurzusról, most mélyebbre merülsz!

---

## 0.1 – Parancssor navigáció ⭐
Készíts egy `parancsok.txt` fájlt, amely tartalmazza a következő parancsok kimenetét:
- `pwd` (aktuális könyvtár)
- `ls -la` (fájlok listázása)
- `mkdir`, `cd`, `rmdir` használata

## 0.2 – Git alapok ⭐
Készíts egy `git-naplo.txt` fájlt, amely tartalmazza a `git log` kimenetedet. A repóban legyen legalább 3 commit értelmes üzenetekkel.

## 0.3 – Branch műveletek ⭐⭐
Hozz létre egy `fejlesztes` branch-et. Készíts benne egy `branch-teszt.py` fájlt, ami kiírja: "Ez a fejlesztés ágon készült". Merge-eld a `main`-be.

## 0.4 – .gitignore ⭐⭐
Hozz létre egy `.gitignore` fájlt, amely kizárja: `__pycache__/`, `*.pyc`, `.env`, `venv/`. Készíts egy `teszt.pyc` fájlt és ellenőrizd, hogy a git ignorálja.

## 0.5 – Merge konfliktus ⭐⭐⭐
Hozz létre két branch-et, mindkettőben módosítsd ugyanazt a fájlt. Merge-eld és old meg a konfliktust. Készíts `konfliktus-megoldas.txt`-t, amelyben leírod a lépéseket.

---

## Dokumentáció

- [Git alapok](https://git-scm.com/book/en/v2/Getting-Started-Git-Basics)
- [Parancssor alapok](https://ubuntu.com/tutorials/command-line-for-beginners)
- [.gitignore](https://www.w3schools.com/git/git_ignore.asp)

## 📚 Kapcsolódó anyagok

Az ehhez a héthez tartozó elméleti anyagot és további gyakorlófeladatokat itt találod:

- 📖 [Lecke: Git, GitHub, Linux](https://github.com/ghemrich/openschool-knowledge/blob/master/courses/python-backend/doksik/tanulok/leckek/00-git-github-linux.md)
- 📝 [Gyakorlófeladatok: Git, GitHub, Linux](../../doksik/tanulok/feladatok/00-git-github-linux.md)

## Beadás

1. Minden feladatot a megfelelő fájlba írd
2. Commitolj értelmes üzenetekkel
3. `git push` – ez a beadás!
