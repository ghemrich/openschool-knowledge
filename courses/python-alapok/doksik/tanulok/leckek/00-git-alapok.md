# 0. hét – Git és GitHub alapok

> **Dokumentáció:** [W3Schools – Git bevezető](https://www.w3schools.com/git/git_intro.asp) | [Git parancsok](https://www.w3schools.com/git/git_staging_environment.asp) | [GitHub bevezető](https://www.w3schools.com/git/git_remote_getstarted.asp)

## Miért tanuljuk a Gitet?

A vizsgát **GitHub Classroom**-on keresztül fogjátok megírni. Ehhez ismernetek kell a Git alapjait:
- Fájlok verziókezelése (mentés, visszaállítás)
- Munka feltöltése GitHubra
- Feladatok elfogadása és beadása GitHub Classroom-ban

---

## Mi a Git?

A Git egy **verziókezelő rendszer**. Nyomon követi a fájlok változásait, és lehetővé teszi, hogy:
- Visszatérj egy korábbi állapothoz
- Lásd, mit változtattál és mikor
- Feltöltsd a munkádat egy távoli szerverre (GitHub)

## Mi a GitHub?

A GitHub egy **online platform**, ahol a Git tárhelyeket (repository-kat) tároljuk. A GitHub Classroom erre épül: a mentor kioszt egy feladatot, a tanuló elfogadja, megoldja, és feltölti.

---

## Git telepítés és beállítás

### 1. Git telepítése

Ellenőrizd, hogy telepítve van-e:

```bash
git --version
```

Ha nincs telepítve:
- **Windows:** letöltés a [git-scm.com](https://git-scm.com) oldalról (a telepítő tartalmaz egy Git Bash terminált is)
- **Linux:** `sudo apt install git`
- **Mac:** `brew install git`

### 2. Git beállítása (egyszer kell megcsinálni)

```bash
git config --global user.name "Kiss Anna"
git config --global user.email "kiss.anna@iskola.hu"
```

---

## Alapfogalmak

| Fogalom | Jelentés |
|---------|----------|
| **Repository (repo)** | Egy projekt mappája, amit a Git követ |
| **Commit** | Egy mentési pont – pillanatkép a fájlokról |
| **Stage (add)** | Fájlok kijelölése a következő commithoz |
| **Push** | Commitok feltöltése GitHubra |
| **Clone** | Egy távoli repo letöltése a gépedre |

---

## Alapparancsok

### Projekt letöltése (clone)

Amikor elfogadod a GitHub Classroom feladatot, kapsz egy linket. Azt így töltöd le:

```bash
git clone https://github.com/iskolam/feladat-kissanna.git
cd feladat-kissanna
```

### Munka mentése és feltöltése

Ez a három parancs a legfontosabb – ezt fogod a legtöbbet használni:

```bash
git add .                    # Minden módosított fájl kijelölése
git commit -m "feladat1 kész"  # Mentési pont létrehozása üzenettel
git push                     # Feltöltés GitHubra
```

### Állapot ellenőrzése

```bash
git status                   # Mi változott?
git log --oneline            # Eddigi commitok listája
```

> **Teljes parancsreferencia:** [Git puskalap](../../../../../guides/git-puskalap.md)

---

## Tipikus munkafolyamat (minden óra/házi feladat)

```
1. Megnyitod a projektet VS Code-ban
2. Megírod/módosítod a Python fájlokat
3. Terminálban:
   git add .
   git commit -m "rövid leírás, mit csináltál"
   git push
4. Kész – a mentor látja a munkádat GitHubon!
```

---

## GitHub Classroom – lépésről lépésre

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
- A határidő után a mentor értékeli a repóban lévő fájlokat

> **Részletes útmutató:** [GitHub Classroom — Tanuló útmutató](../../../../../guides/github-classroom-tanulo-utmutato.md)

---

## Gyakorlat

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

## Gyakori hibák és megoldásuk

Ha hibába ütközöl, nézd meg a részletes hibaelhárítási útmutatót:

- [Hibaelhárítás és GYIK — Git és GitHub](../../../../../guides/hibaelharitas.md#git-és-github)
- [Hibaelhárítás és GYIK — GitHub Classroom](../../../../../guides/hibaelharitas.md#github-classroom)
- [Git puskalap — Gyors parancskereső](../../../../../guides/git-puskalap.md)
