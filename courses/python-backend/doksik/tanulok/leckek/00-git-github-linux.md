# 📘 Lecke 00 – Git, GitHub, parancssor alapok

> 📚 Dokumentáció:  
> https://git-scm.com/book/en/v2 ·  
> https://ubuntu.com/tutorials/command-line-for-beginners ·  
> https://docs.github.com

---

# 1–2. óra: Parancssor alapok

## ❓ Miért tanuljuk a parancssort?

Backend fejlesztőként minden nap használod a terminált:
- szerveren futtatsz programokat
- fájlokat kezelsz
- konténereket indítasz

👉 A grafikus felület nem mindig elérhető!

---

## 📍 Navigáció

```bash
pwd         # Aktuális könyvtár kiírása
ls          # Fájlok listázása
ls -la      # Részletes lista (tartalmazza az elrejtett fájlokat is -a, és részleteket -l)
cd mappa    # Belépés egy mappába
cd ..       # Egy szinttel vissza (a szülő mappába)
cd ~        # A home könyvtárba lépés (pl. /home/felhasználó)
cd /        # A gyökér könyvtárba lépés
```

### 🧠 Részletes Magyarázat

**pwd** (print working directory)  
Kiírja, hogy jelenleg melyik könyvtárban vagy. Nagyon hasznos, ha elvesztél a fájlrendszerben. 
Kimenet például: `/home/felhasználo/projektek/app`

**ls** (list)  
Felsorolja az aktuális könyvtárban lévő fájlokat és mappákat.
- `ls` = alapvető lista
- `ls -la` = részletes lista (a = all = elrejtett fájlok is, l = long format = jogosultságok, méret, dátum)
- `ls -lh` = "human readable" formátum (legible méretteL: 5.2M, 3.4K)

**cd** (change directory)  
Navigálás a fájlrendszerben.
- `cd projektom` = belépés a projektom mappába
- `cd ..` = egy szinttel vissza
- `cd ~/Documents` = közvetlenül a Documents mappába
- `cd -` = az előző könyvtárra lépés vissza

---

## 📁 Fájlműveletek

```bash
mkdir projekt              # Új mappa létrehozása
mkdir -p a/b/c           # Több szint mély mappa (ha nem létezik, feldatja)
touch fajl.txt           # Üres fájl létrehozása (vagy az aktuális idő frissítése)
cp fajl.txt masolat.txt  # Fájl másolása
cp -r mappa/ masolat_m/  # Mappa másolása (rekurzív: -r)
mv fajl.txt ujnev.txt    # Fájl átnevezése vagy mozgatása
mv fajl.txt ../masik_m/ # Fájl másik mappába mozgatása
rm fajl.txt              # Fájl törlése (VÉGLEGES! nincs papirkosár)
rm -r mappa/             # Mappa teljes tartalmának törlése
cat fajl.txt             # Fájl tartalmának kiírása
nano fajl.txt            # Fájl szerkesztése nano szerkesztővel
```

### 🧠 Részletes Magyarázat

**mkdir** (make directory)  
Új mappákat hoz létre. Egyetlen mappát vagy egy teljes útvonalat is létrehozhatsz.
```bash
mkdir projekt           # Egyetlen mappa: projekt/
mkdir -p a/b/c/d       # Teljes útvonal: a/b/c/d/
```

**touch**  
Létrehoz egy üres fájlt, vagy ha már létezik, frissíti az utolsó módosítás dátumát. Gyors módja a fájl létrehozásának.

**cp** (copy)  
Fájl vagy mappa másolása. Az eredeti megmarad, létrejön egy másolat.
- `cp fajl.txt masolat.txt` = egy fájl másolása
- `cp -r mappa/ masolat_mappa/` = mappa másolása a benne lévő összes fájllal (-r = rekurzív)

**mv** (move)  
Fájl vagy mappa mozgatása vagy átnevezése. Az eredeti helyről eltűnik.
```bash
mv fajl.txt ujnev.txt     # Átnevezés
mv fajl.txt ./mappa/      # Mozgatás másik mappába
```

**rm** (remove)  
Fájl vagy mappa törlése. ⚠️ FIGYELEM: Végleges törlés! Nincs Papírkosár!
- `rm fajl.txt` = fájl törlése
- `rm -r mappa/` = mappa és tartalmának törlése (-r = rekurzív)
- `rm -i fajl.txt` = mielőtt törlés: "biztos vagy-e?" kérdés

**cat** (concatenate)  
Fájl tartalmának kiírása a terminálra. Rövid fájlokhoz ideális, hogy megnézd a tartalmát.
```bash
cat tananyag.md         # A fájl teljes kiírása
cat tananyag.md | head -10  # Csak az első 10 sor
```

**nano** (szövegszerkesztő)  
Egyszerű beépített szerkesztő a terminálban.
- Ctrl+X: Kilépés (majd Y=igen, N=nem mentéshez)
- Ctrl+O: Mentés
- Ctrl+W: Keresés

---

## 🔐 Jogosultságok (Permissions)

```bash
ls -la                      # Jogosultságok megtekintése
chmod +x script.sh          # Fájl futtathatóvá tétele
chmod -x script.sh          # Futtathatóság eltávolítása
chmod 644 fajl.txt          # Számokkal: tulajdonos olvashat/írhat, mások csak olvashatnak
chmod 755 script.sh         # Számokkal: tulajdonos teljes hozzáférés, mások futtathatnak
chmod 700 titkos.txt        # Csak a tulajdonos hozzáférhet
chown felhasználo fajl.txt  # Fájl tulajdonosának megváltoztatása
```

### 🧠 Részletes Magyarázat

**ls -la kimenet értelmezése:**
```
-rw-r--r--  1  janosi  staff  4096  mar 20 10:30  fajl.txt
^ ^ ^ ^ ^
| | | | |
1 2 3 4 5
```

1. **Fájltípus és jogosultságok:**
   - `-` = reguláris fájl (d = mappa, l = link)
   - `rw-` = tulajdonos jogai (read, write, no execute)
   - `r--` = csoport jogai (csak olvasás)
   - `r--` = mások jogai (csak olvasás)

2. **Jogosultságok szimbólumokkal:**
   - `r` (read) = 4 = olvasás
   - `w` (write) = 2 = írás
   - `x` (execute) = 1 = futtatás

**chmod parancsok:**
```bash
chmod +x script.sh          # Futtathatóvá tesz (+ = hozzáad)
chmod -x script.sh          # Futtathatóság elvét (- = eltávolít)
chmod u+rw fajl.txt         # Tulajdonosnak írás és olvasás
chmod g+r fajl.txt          # Csoport csak olvasás
chmod o-rwx fajl.txt        # Mások nem hozzáférhetnek
```

**Számokkal:**
- `chmod 644` = rw- r-- r-- (típikus fájlokhoz)
- `chmod 755` = rwx r-x r-x (típikus scriptekhez és mappákhoz)
- `chmod 700` = rwx --- --- (csak a tulajdonos, biztonságos fájlok)

---

# 3–4. óra: Git

## 🔧 Git Alapparancsok

```bash
git init                    # Új Git repository inicializálása
git add .                   # Összes módosított fájl "stage" területre (staging area)
git add fajl.txt            # Adott fájl hozzáadása
git commit -m "üzenet"      # Staged fájlok mentése a verziókezelésbe azzal az üzenettel
git push origin main        # Helyi commits feltöltése a remote repository főágára
git pull origin main        # Remote változások letöltése és merge-elése a helyi ágba
git status                  # Az aktuális állapot megtekintése (módosított, új fájlok, stb.)
git log --oneline           # Commit történet rövidített formában
git diff                    # Megjelenít az utolsó commit óta megváltoztatott kódot
git restore fajl.txt        # Fájl visszaállítása az utolsó commit állapotára
```

### 🧠 Részletes Magyarázat – A Git Workflow

**1. git init**  
Új Git repository létrehozása a mappamban. Ez egy `.git` rejtett mappában tároli az összes verziókezelési információt.
```bash
cd my_project
git init        # Most már verziókezelés alatt van a mappa
```

**2. git add**  
Fájlok hozzáadása a "staging area"-hoz (felkészülési zóna). Csak a stage-elendő fájlok kerülnek majd a commitba.
```bash
git add .               # MINDEN módosított fájl
git add src/app.js      # Csak egy adott fájl
git add *.py            # Mintázat alapján (minden Python fájl)
```

**3. git commit**  
A staged fájlok véglegesítése egy verzióként. Ez létrehozza a verziókezelési történet egy új pontját.
```bash
git commit -m "Felhasználó belépés funkció hozzáadva"
# Jó commit üzenetek: rövid (50 kar), leíró, imperatívus hangnem
```

**4. git push**  
Helyi commits feltöltése a GitHub-ra (vagy más remote repository-ba).
```bash
git push origin main       # A main ágat feltölteni az 'origin'-nek nevezett remote-ra
git push origin feature    # Egy feature ágat feltölteni
```

**5. git pull**  
A remote repository legújabb verziójának letöltése és zusammeolvasztása a helyi ágba.
```bash
git pull origin main       # A remote main ágat beolvasztani a helyi main-be
```

**6. git status**  
Gyakorlatilag: "Mi történt azóta, hogy voltam itt?" Megjeleníti:
- Módosított, de nem stage-elt fájlok (vörös)
- Stage-elt, de nem committed fájlok (zöld)
- Untracked fájlok (új fájlok, melyeket Git még nem követ)

**7. git log**  
A commit történet megtekintése. `--oneline` = kompakt format.
```bash
git log                     # Teljes commit információ
git log --oneline           # Rövid format (commit hash + üzenet)
git log -n 5                # Az utolsó 5 commit
```

**8. git diff**  
Az utolsó commit óta megváltoztatott kódot mutatja.
```bash
git diff                    # AZ ÖSSZES módosítás
git diff fajl.txt           # Egy adott fájl módosításai
git diff --staged           # A staged (hozzáadott) módosítások
```

---

## 🚫 .gitignore – Mit ne követjünk verziókezelésben?

```
# Python
venv/                   # Python virtuális környezet mappája
__pycache__/            # Lefordított Python fájlok
*.pyc                   # Compiled Python fájlok
*.pyo

# Node.js
node_modules/           # NPM csomagok (nem küldünk fel!)
npm-debug.log

# Környezeti változók (titkosak!)
.env                    # Jelszavak, API kulcsok – SOHA ne github-ra!
.env.local
.env.*.local

# IDE szerkesztők
.vscode/                # Visual Studio Code beállítások
.idea/                  # IntelliJ IDEA beállítások
*.swp                   # Vim backup fájlok
*.sublime-project

# OS
.DS_Store               # macOS mappa info
Thumbs.db               # Windows kép cache

# Build output
dist/
build/
*.o
*.so
```

### 🧠 Részletes Magyarázat

**Mi a .gitignore?**  
Ez egy speciális fájl, amely azt mondja Git-nek: "ezek a fájlok/mappák-ok ne kerüljenek be a verziókezelésbe".

**Miért szükséges?**
1. **venv/, node_modules/** - Ezeket generálható (npm install, pip install), nem szükséges bizálkodni rá. Hatalmas méret spórlás!
2. **.env** - Tartalmaz jelszavakat, API kulcsokat. Biztonsági риск a GitHub-ra feltölteni!
3. **.idea/, .vscode/** - IDE beállítások, amelyek személyesek. Másnak más keggel szükséges.
4. **.pyc, __pycache__/** - Python automatikusan legenerál. Spórolj feltöltésben!
5. **.DS_Store** - macOS rendszerfájl. Windows/Linux felhasználók nem szükséges.

**Hogyan működik?**
```
# Megjegyzés
*.log           # Összes .log fájl figyelmen kívül hagyása
data/           # A teljes data/ mappa figyelmen kívül hagyása
!data/keep.txt  # KIVÉTEL: szálltsd fel ezt a fájlt, még ha data/ ki van hagyva
```

**Példa projekt .gitignore-ja:**
```
# Backend
venv/
.env
*.pyc

# Frontend
node_modules/
.next/
dist/

# IDE
.vscode/
.idea/

# OS
.DS_Store
Thumbs.db
```

---

## 🌿 Branch-ek (Ágak) – Párhuzamos fejlesztés

```bash
git branch                      # Az összes ág listázása (* = aktuális ág)
git branch feature/login        # Új ág létrehozása
git checkout feature/login      # Ágra váltás
git checkout -b feature/login   # Ág létrehozása és rá váltás (1 parancsban)
git push origin feature/login   # Ág feltöltése GitHub-ra
git merge feature/login         # Ág beolvasztása az aktuális ágba
git branch -d feature/login     # Ág törlése (helyi)
git push origin -d feature/login # Ág törlése a remote-on (GitHub)
```

### 🧠 Részletes Magyarázat

**Mi az a branch?**  
Egy branch a project egy párhuzamos verziója. Lehetővé teszi, hogy különböző funkciók fejlesztésén dolgozz egymást nem zavaráva.

**Tipikus workflow:**
```
main (stabil, éles verzió)
  ├─ feature/login (felhasználó belépés)
  ├─ feature/database (adatbázis szerkezet)
  └─ bugfix/fix-typo (kis hiba javítás)
```

**git branch**  
Felsorolja az összes ágat. Az `*` jelöli, melyiken vagy.
```bash
git branch                  # Lokális ágak
git branch -a               # Összes ág (helyi + remote)
git branch -r               # Csak remote ágak
```

**Ág létrehozása:**
```bash
git branch feature/login        # Csak létrehozás
git checkout -b feature/login   # Létrehozás + váltás (ajánlott)
```

**Ág váltása:**
```bash
git checkout main               # Vissza a main ágra
git checkout feature/login      # A feature/login ágra váltás
git switch feature/login        # Újabb szintaxis (git 2.23+)
```

**"Upstream" beállítása:**
```bash
git push -u origin feature/login    # -u = GitHub-ra feltölt és "megjegyzi" ezt a remote-ot
# Utána már elég: git push / git pull
```

**Ág beolvasztása (merge):**
```bash
git checkout main               # Váltás a cél ágra (main-re)
git merge feature/login         # A feature/login beolvasztása a main-be
# Most a feature/login kódja a main-ben is van
```

**Ág törlése:**
```bash
git branch -d feature/login             # Helyi törlés
git push origin -d feature/login        # Remote törlés (GitHub-ról)
```

**Jó branch nevek:**
- `feature/user-auth` - új funkció
- `bugfix/login-error` - hiba javítás
- `refactor/clean-code` - kód tisztázás
- `chore/update-deps` - függőségek frissítése

---

## 💥 Ütközések (Conflicts) – Mi történik, ha két munka nem fér össze?

### Ütközés kialakulása

Ha ketten ugyanazon a helyen módosítják a kódot, és beolvasztasz (merge), Git nem tudja automatikusan dönteni melyik verzió a helyes:

```
<<<<<<< HEAD
egyik verzió (az ágod)
=======
másik verzió (a merge-elendő ág)
>>>>>>> feature/uj
```

### 🧠 Részletes Magyarázat

**Hogyan történik egy conflict?**

1. A `feature/uj` ágon módosított funkcióval dolgoztál
2. Közben a `main` ágon mások is módosították ugyanazt a fájlt
3. `git merge feature/uj` után Git jelzi: "Nem tudom ezt összeolvasztani, mivel ellentmondó módosítások vannak"

**Conflict jelölés:**
```python
def login_user(username):
<<<<<<< HEAD
    # A main ágon ez van (az agyad)
    user = find_user(username)
    return user.hashed_password == provided_pass
=======
    # A feature ágon ez van
    user = database.query(User).filter(User.name == username).first()
    return bcrypt.verify(provided_pass, user.password_hash)
>>>>>>> feature/login
```

**Konfliktus megoldása:**

1. **Fájl szerkesztése:** Kézzel döntsd el melyik verzió a helyes, vagy kombin-álj mindkettőt
2. **Szerkesztés után:** Távolítsd el a konfliktus jelöléseket (`<<<<<<<`, `=======`, `>>>>>>>`)
3. **Véglegesítés:**
```bash
git add .
git commit -m "konfliktus megoldva: login-funkció"
```

**Konfliktus megoldási stratégiák:**

```bash
# 1. Saját verzió megtartása
git checkout --ours fajl.txt

# 2. Másik verzió megtartása
git checkout --theirs fajl.txt

# 3. Merge abortálása (vissza az eredeti állapotba)
git merge --abort
```

**Konfliktus megelőzése (Best Practices):**
1. **Gyakori pull** - a remote változásokat naponta lehozz
2. **Szűk ágak** - egy feature egy ágon, ha lehet pár napig
3. **Kommunikáció** - munkatársadnak mondd el mit módosítasz
4. **Gyakori push** - ne maradjon soká a module unpushed kód
5. **Jó kitalálás** - fájlok más helyeit szerkeszd, ha lehet

**Visual Studio Code-ban conflict resolution:**
- Jelzi: `Incoming Change` (remote verzió) vs `Current Change` (a te verziód)
- Gombokkal: "Accept Current Change", "Accept Incoming Change", "Accept Both Changes"

---

# 5–6. óra: GitHub

## 🔄 GitHub integráció – Teljes workflow egy projekthez

```bash
# 1. Repository klónozása (GitHub-ról letöltés)
git clone <repo>

# 2. Módosítások végzése
# ... szerkeszteszz fájlokat ...

# 3. Módosítások stage-elése
git add .

# 4. Commit létrehozása
git commit -m "leírás"

# 5. Push GitHub-ra
git push

# 6. (Csapatmmunka) Mások változásainak lehozása
git pull
```

### 🧠 Részletes Magyarázat – Lépésről Lépésre

**1. git clone - Az első lépés**  
Letöltöd a GitHub-on lévő teljes repository-t a gépedre.
```bash
git clone https://github.com/username/repository.git
cd repository   # Belépés a mappába
```
Ez letölti az ÖSSZES verziókezelési történetet + az összes fájlt.

**2. Módosítások végzése**  
Most szerkesztesz fájlokat, új funktciókat adol hozz, stb.
```bash
# VŐ: módosítasz pár fájlt
nano app.py
# Módosítás: hozzáadtál egy új funkciót
```

**3. git add - "Felkészülés"**  
Megmondod Git-nek: "ezt a módosítást szeretném feltölteni".
```bash
git add .                   # ÖSSZES módosított fájl
git add app.py main.py      # Csak ezek a fájlok
# Most a módosítások a "staging area"-ban vannak
```

**4. git commit - "Versiókezelésbe rögzítés"**  
A staged módosítások egy verzióként mentésre kerülnek egy üzenettel.
```bash
git commit -m "Új felhasználó autentifikáció hozzáadva"
# Most helyi történetben van, de még nem a GitHub-on
```

**5. git push - "Feltöltés"**  
A helyi commits feltöltésre kerülnek a GitHub-ra, így mások is látják.
```bash
git push                    # Az aktuális ágat
git push origin main        # Explicit: main ág az 'origin' remote-ra
# Most az összes munka a GitHub-on is van
```

**6. git pull - "Mások munkájának lehozása"**  
Ha munkatársaid commitok leszálítanak, lehozod az ő módosításaikat.
```bash
git pull                    # Az aktuális ág remote verziójából
# Git: automatikusan beolvasztja az új kódot a te munkádba
```

### Teljes napi workflow:

```bash
# Reggel: mások munkájának lehozása
git pull origin main

# Nap közben: fejlesztés, committal
git add .
git commit -m "feature megjegyzés"
git push

# Este: szinkron az összes munkatárssal
git pull origin main  # Esetleges új commitok lehozása
```

### Pull Request (PR) a csapatmunkához:

```bash
# 1. Feature ágon dolgozol
git checkout -b feature/new-api

# 2. Fejlesztés + push
git add .
git commit -m "API endpoint hozzáadva"
git push origin feature/new-api

# 3. GitHub felületen: "Create Pull Request" gomb
# 4. Csapattársak review-zzák, megjegyzéseket hagynak
# 5. Módosítást végez + push
# 6. Merge: "Squash and merge" vagy "Create a merge commit"
```

**Tippek:**
- **Gyakori commit** - minden 30-60 percnél
- **Értelmes üzenetek** - ne csak "fix" vagy "update"
- **Pull mielőtt push** - `git pull` → munkád → `git push`
- **Szűk ágak** - egy feature egy ágon, ne keverd össze
- **Branch neve** - pl. `feature/user-auth`, `bugfix/login-email`

---

# 🏁 Összegzés

✔ **Parancssor alapok** - Navigáció, fájlműveletek, jogosultságok  
✔ **Git alapok** - Verziókézelés, commitok  
✔ **GitHub workflow** - Csapatmunka, pull requests, merge-ek  

---

# 💡 Fontos tippek kezdőknek

## Napi szokások:
```bash
# Munkany kezdeténél
git status          # Mi módosult?
git pull origin main # Mások munkájának lehozása

# Munkanynassá során (30 percenként)
git add .
git commit -m "Opisateľný üzenet"
git push origin <ag-neved>

# Munkány végén
git pull origin main # Szinkronizálás csapattal
```

## Gyakori hibák és megoldások:

### "Hoppá, azt nem akartam commitolni!"
```bash
git revert HEAD     # Utolsó commit visszavonása (új commit-ot hoz létre)
# VAGY
git reset HEAD~1    # Utolsó commit eltávolítása (kódja marad)
```

### "Rossz üzenetet írtam a commitba"
```bash
git commit --amend -m "Helyes üzenet"  # Utolsó commit javítása
```

### "Véletlenül törltem egy fájlt"
```bash
git restore fajl.txt    # Visszaállítás az utolsó commit-ből
```

### "Összekevertem az ágakat"
```bash
git branch -M main                  # Aktuális ág átnevezése main-re
git reset --hard origin/main        # Vissza az eredeti állapotba
```

## Git parancsok "cheat sheet":
| Parancs | Mit csinál |
|---------|-----------|
| `git init` | Új projekt inicializálása |
| `git clone` | GitHub-ról projekt letöltése |
| `git status` | Aktuális állapot megtekintése |
| `git add .` | Összes módosítás hozzáadása |
| `git commit -m "msg"` | Verziókezelébe mentés |
| `git push` | Feltöltés GitHub-ra |
| `git pull` | Letöltés GitHub-ról |
| `git branch` | Ágak listrezése |
| `git checkout -b ág` | Új ág létrehozása |
| `git merge ág` | Ág beolvasztása |
| `git log --oneline` | Verzióelőzmények |

---

# 📚 Segítségül:
- **Git dokumentáció:** https://git-scm.com/book/en/v2
- **Oh My Git:** https://ohmygit.org/ (interaktív tanulás)
- **GitHub Learning Lab:** https://lab.github.com/
- **Atlassian Git Tutorial:** https://www.atlassian.com/git/tutorials


