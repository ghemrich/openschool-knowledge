# Feladatok – 0. hét: Git, GitHub, parancssor

> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz
> A megoldásokat commitold és pushold a GitHub repódba.

---

### 0.1 – Linux navigáció ⭐
Hozz létre a `/home` könyvtáradban egy `projektek` mappát, azon belül három almappát: `elso`, `masodik`, `harmadik`. Listázd ki a mappákat az `ls -la` paranccsal, készíts képernyőképet.

### 0.2 – Fájlkezelés terminálban ⭐
Hozz létre a `projektek/elso` mappában 3 fájlt: `hello.py`, `notes.txt`, `README.md`. Írd bele mindegyikbe a `echo` vagy `cat` paranccsal valamilyen szöveget. Listázd ki a fájlok tartalmát.

### 0.3 – Git alapok ⭐⭐
Inicializálj egy Git repót a `projektek/elso` mappában. Hozz létre egy Python fájlt, add hozzá a staging area-hoz, és commitold "Első commit" üzenettel. Írd ki a `git log` kimenetét.

### 0.4 – Branch-ek ⭐⭐
Az előző repóban hozz létre egy `fejlesztes` nevű branch-et. Válts rá, módosítsd a Python fájlt, commitold. Válts vissza `main`-re és merge-eld a `fejlesztes` ágat. Töröld a `fejlesztes` ágat.

### 0.5 – .gitignore ⭐⭐
Hozz létre egy `.gitignore` fájlt, amely kizárja a következőket: `__pycache__/`, `*.pyc`, `.env`, `venv/`. Ellenőrizd a `git status` paranccsal, hogy a kizárt fájlok nem jelennek meg.

### 0.6 – GitHub Classroom ⭐⭐⭐
Fogadd el a mentor által küldött GitHub Classroom meghívó linket. Klónozd le a repót, oldd meg a benne lévő feladatot, commitold és pushold. Ellenőrizd a GitHub weboldalon, hogy a push sikeres volt.

### 0.7 – Merge konfliktus ⭐⭐⭐
Hozz létre egy repóban két branch-et. Mindkettőben módosítsd **ugyanazt a sort** ugyanabban a fájlban. Merge-eld az egyiket a `main`-be, majd a másikat is – old meg a keletkező konfliktust manuálisan.
