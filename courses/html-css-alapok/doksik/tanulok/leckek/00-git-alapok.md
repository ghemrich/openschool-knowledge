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
- **Windows:** letöltés a [git-scm.com](https://git-scm.com) oldalról
- **Linux:** `sudo apt install git`
- **Mac:** `brew install git`

### 2. Git beállítása (egyszer kell megcsinálni)

```bash
git config --global user.name "Neved"
git config --global user.email "email@cimed.hu"
```

---

## Alapvető Git parancsok

| Parancs | Mit csinál |
|---------|-----------|
| `git init` | Új Git repó létrehozása |
| `git clone <url>` | Meglévő repó letöltése |
| `git status` | Változások listázása |
| `git add .` | Összes változás hozzáadása |
| `git commit -m "üzenet"` | Mentés (commit) készítése |
| `git push` | Feltöltés GitHubra |
| `git pull` | Letöltés GitHubról |
| `git log --oneline` | Commit előzmények |

---

## GitHub Classroom munkafolyamat

1. Kattints a mentortól kapott **meghívó linkre**
2. Fogadd el a feladatot → létrejön a saját repód
3. **Klónozd** a repót: `git clone <url>`
4. Dolgozz a feladatokon
5. `git add .` → `git commit -m "megoldás"` → `git push`
6. Ellenőrizd a GitHub oldalon, hogy feltöltődött-e
