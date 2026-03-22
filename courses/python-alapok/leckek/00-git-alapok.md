# 📘 Lecke 00 – Git és GitHub alapok

> 📚 Dokumentáció:  
> https://git-scm.com/book/en/v2 ·  
> https://www.w3schools.com/git/ ·  
> https://docs.github.com

---

# 1. óra: Miért Git? Mi a verziókezelés?

## ❓ Miért tanuljuk a Gitet?

A vizsgát **GitHub Classroom**-on keresztül fogjátok megírni. Ehhez ismernetek kell a Git alapjait:
- Fájlok verziókezelése (mentés, visszaállítás)
- Munka feltöltése GitHubra
- Feladatok elfogadása és beadása GitHub Classroom-ban

👉 A programozók világában a Git annyira alap, mint a Word a szövegszerkesztésben!

---

## 📦 Mi a Git?

A Git egy **verziókezelő rendszer**. Nyomon követi a fájlok változásait, és lehetővé teszi, hogy:
- Visszatérj egy korábbi állapothoz
- Lásd, mit változtattál és mikor
- Feltöltsd a munkádat egy távoli szerverre (GitHub)

### 🧠 Részletes Magyarázat

**Verziókezelés** azt jelenti, hogy a fájljaid minden mentési pontja megmarad. Képzeld el úgy, mint egy „visszavonás" gombot, ami örökre megjegyez mindent.

Példa: ha a kedden írt kódod működött, de szerdán elrontottad, simán visszamehetsz a keddi állapotra. Nem kell manuálisan másolgatni a fájlokat `feladat_v1.py`, `feladat_v2.py` stílusban – a Git ezt automatikusan kezeli.

**A Git helyi rendszer** – a saját gépeden fut, nem kell hozzá internet. A GitHub viszont egy online platform, ahová feltöltöd a Git-tel kezelt projektjeidet.

---

## 🌐 Mi a GitHub?

A GitHub egy **online platform**, ahol a Git tárhelyeket (repository-kat) tároljuk. A GitHub Classroom erre épül: a mentor kioszt egy feladatot, a tanuló elfogadja, megoldja, és feltölti.

### 🧠 Részletes Magyarázat

**Repository (repo)** = egy projekt mappája, amit a Git követ. Olyan, mint egy mappa a gépeden, de a Git mindenről naplót vezet benne.

**GitHub** = egy webes szolgáltatás, ahol a repo-kat online tároljuk.  
**GitHub Classroom** = a GitHub egy speciális funkciója oktatáshoz: a tanár feladatot ad ki linken, a diák elfogadja, és automatikusan kap egy saját repo-t a megoldáshoz.

---

# 2. óra: Git telepítés, beállítás és alapparancsok

## 🔧 Git telepítése

Ellenőrizd, hogy telepítve van-e:

```bash
git --version
```

Ha nincs telepítve:
- **Windows:** letöltés a [git-scm.com](https://git-scm.com) oldalról (a telepítő tartalmaz egy Git Bash terminált is)
- **Linux:** `sudo apt install git`
- **Mac:** `brew install git`

### 🧠 Részletes Magyarázat

**git --version**  
Kiírja a telepített Git verzióját. Ha hibát kapsz ("command not found"), akkor nincs telepítve a gépeden. Windows-on a telepítő egy **Git Bash** nevű terminált is ad – ezt használd a parancsok futtatásához, ha nem VS Code terminált használsz.

---

## ⚙️ Git beállítása (egyszer kell megcsinálni)

```bash
git config --global user.name "Kiss Anna"
git config --global user.email "kiss.anna@iskola.hu"
```

### 🧠 Részletes Magyarázat

**git config --global user.name**  
Beállítja a nevedet, ami minden commit-nál megjelenik. A `--global` azt jelenti, hogy az egész gépre érvényes, nem csak egy projektre.

**git config --global user.email**  
Beállítja az email címedet. Fontos, hogy **ugyanaz** legyen, mint amivel a GitHub fiókodba regisztráltál, különben nem fogja összekapcsolni a commit-jaidat a profildaddal.

Ha ellenőrizni akarod a beállításokat:
```bash
git config --list
```

---

## 📋 Alapfogalmak

| Fogalom | Jelentés |
|---------|----------|
| **Repository (repo)** | Egy projekt mappája, amit a Git követ |
| **Commit** | Egy mentési pont – pillanatkép a fájlokról |
| **Stage (add)** | Fájlok kijelölése a következő commithoz |
| **Push** | Commitok feltöltése GitHubra |
| **Pull** | Változások letöltése GitHubról |
| **Clone** | Egy távoli repo letöltése a gépedre |

### 🧠 Részletes Magyarázat

**Commit** – Gondolj rá úgy, mint egy „mentési pontra" egy játékban. Bármikor visszatérhetsz ide. Minden commithoz tartozik egy üzenet, ami leírja, mit csináltál.

**Stage (add)** – Mielőtt commit-olnál, ki kell jelölnöd, melyik fájlokat akarod beletenni. Ez azért jó, mert nem kell mindig mindent mentened – kiválogathatod.

**Push** – A commitjaidat feltolod a GitHub-ra, hogy a mentor (vagy bárki) lássa.

**Clone** – Letöltöd egy GitHub repo teljes tartalmát a gépedre, beleértve a teljes verziótörténetet.

---

## 📥 Projekt letöltése (clone)

Amikor elfogadod a GitHub Classroom feladatot, kapsz egy linket. Azt így töltöd le:

```bash
git clone https://github.com/iskolam/feladat-kissanna.git
cd feladat-kissanna
```

### 🧠 Részletes Magyarázat

**git clone <URL>**  
Letölti a teljes repository-t a gépedre. A parancs automatikusan létrehozza a mappát (a repo nevével), abban az összes fájlt és a teljes verziótörténetet.

**cd feladat-kissanna**  
Belép a letöltött mappába. A `cd` = "change directory" = könyvtárváltás. Fontos, hogy a Git parancsok csak akkor működnek, ha benne vagy a projekt mappájában!

---

## 💾 Munka mentése és feltöltése

Ez a három parancs a legfontosabb – ezt fogod a legtöbbet használni:

```bash
git add .                    # Minden módosított fájl kijelölése
git commit -m "feladat1 kész"  # Mentési pont létrehozása üzenettel
git push                     # Feltöltés GitHubra
```

### 🧠 Részletes Magyarázat

**git add .** (add pont)  
A `.` (pont) azt jelenti: „az összes módosított és új fájl". Ez kijelöli őket a következő commithoz. Ha csak egy fájlt akarsz:
```bash
git add feladat1.py          # Csak ez az egy fájl
```

**git commit -m "üzenet"**  
Létrehoz egy mentési pontot az összes kijelölt (staged) fájlból. A `-m` utáni szöveg a commit üzenet – röviden írd le, mit csináltál! Példa jó üzenetek:
- `"feladat1 kész"`
- `"javítottam a számológépet"`
- `"hozzáadtam a köszöntő funkciót"`

**git push**  
Feltölti az összes helyi commitot a GitHub-ra. Amíg nem pusholsz, a munkád csak a saját gépeden van!

---

## 🔍 Állapot ellenőrzése

```bash
git status                   # Mi változott?
git log --oneline            # Eddigi commitok listája
```

### 🧠 Részletes Magyarázat

**git status**  
Megmutatja az aktuális állapotot:
- 🔴 Piros fájlok = módosítottad, de még nem adtad hozzá (`git add` kell)
- 🟢 Zöld fájlok = hozzáadtad (staged), készen áll commit-ra
- Ha minden tiszta: „nothing to commit, working tree clean"

**git log --oneline**  
Kilistázza az eddigi commit-okat röviden. Minden sorban egy commit: hash + üzenet.
```
a1b2c3d feladat1 kész
e4f5g6h első commitom
```

---

## 🔄 Tipikus munkafolyamat (minden óra/házi feladat)

```
1. Megnyitod a projektet VS Code-ban
2. Megírod/módosítod a Python fájlokat
3. Terminálban:
   git add .
   git commit -m "rövid leírás, mit csináltál"
   git push
4. Kész – a mentor látja a munkádat GitHubon!
```

### 🧠 Részletes Magyarázat

Ez a munkafolyamat mindig ugyanaz, akár házi feladatot csinálsz, akár vizsgázol:
1. **Nyisd meg a VS Code-ot** → File → Open Folder → válaszd ki a klónozott mappát
2. **Írj kódot** a megfelelő `.py` fájlokba
3. **Nyisd meg a terminált** (VS Code-ban: Ctrl+ö vagy Terminal → New Terminal)
4. **Írd be a 3 parancsot**: `git add .` → `git commit -m "..."` → `git push`
5. **Ellenőrizd** a GitHub weboldalon, hogy feltöltődtek-e a fájlok

💡 Tipp: commitolj gyakran, ne csak a végén! Ha elakadsz, a mentor a félkész munkádat is látja és tud segíteni.

---

# 3. óra: GitHub Classroom használata

## 🎓 GitHub Classroom – lépésről lépésre

### Feladat elfogadása
1. A mentortól kapsz egy **meghívó linket**
2. Rákattintasz → a GitHub létrehoz neked egy saját repository-t
3. Leklónozod a gépedre: `git clone <link>`

### Munka közben
- Dolgozol a fájlokon a saját gépeden
- Rendszeresen commitolsz és pusholsz
- A mentor bármikor láthatja az aktuális állapotot

### Beadás
- Az utolsó `git push` a beadás
- A mentor értékeli a repóban lévő fájlokat

### 🧠 Részletes Magyarázat

**Miért GitHub Classroom?**  
A hagyományos email-es beadás helyett a GitHub Classroom automatizálja a folyamatot:
- Minden diák saját repo-t kap (nem tudtok egymás munkájába belenyúlni)
- A mentor egy helyen látja mindenki munkáját
- Automatikus tesztek futhatnak a beadott kódra (a zöld pipa = minden teszt sikerült)

**A meghívó link** általában így néz ki:  
`https://classroom.github.com/a/AbCdEfGh`  
Rákattintasz → "Accept this assignment" → pár másodperc után kapsz egy saját repo URL-t.

**Fontos:** az első alkalommal össze kell kapcsolnod a GitHub fiókodat a neveddel a classroom-ban. Válaszd ki a saját neved a listából!

---

## ✏️ Gyakorlat

1. Állítsd be a Git nevet és email címet a gépeden
2. Fogadd el a mentor által kiadott gyakorló feladatot (GitHub Classroom link)
3. Klónozd le a repót
4. Hozz létre egy `hello.py` fájlt, ami kiírja a neved
5. Add hozzá, commitold, és pushold:

```bash
git add .
git commit -m "Első commitom"
git push
```

6. Ellenőrizd a GitHubon, hogy megjelent-e a fájlod!

---

## ⚠️ Gyakori hibák és megoldásuk

| Hiba | Ok | Megoldás |
|------|------|----------|
| `fatal: not a git repository` | Nem vagy a projekt mappában | `cd <mappa neve>` paranccsal lépj be a repo mappába |
| `error: failed to push` | Nincs internet, vagy a remote nem létezik | Ellenőrizd a netet, és próbáld `git push origin main` |
| `nothing to commit` | Nem módosítottál semmit, vagy már commitoltad | Módosíts egy fájlt, majd `git add .` + `git commit` |
| Üres repo a GitHubon push után | Elfelejtettél `git add`-ot | Mindig: `git add .` → `git commit` → `git push` sorrendben |

### 🧠 Részletes Magyarázat

**„not a git repository"**  
Ez a leggyakoribb hiba. Azt jelenti, hogy a terminálban nem a klónozott projekt mappájában vagy. Használd a `cd` parancsot a belépéshez, vagy a VS Code-ban nyisd meg a megfelelő mappát.

**„failed to push"**  
Általában azért van, mert:
1. Nincs internetkapcsolatod
2. Rossz URL-re próbálsz push-olni
3. Nincs jogosultságod (nem te vagy a repo tulajdonosa)

**„nothing to commit"**  
Két eset:
1. Nem módosítottál fájlt → írd meg a feladatot, aztán próbáld újra
2. Már hozzáadtad és commit-oltad → a `git status` mutatja, hogy „clean" – nincs mit menteni, mert minden naprakész
