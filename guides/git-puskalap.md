# Git puskalap

A leggyakrabban használt Git parancsok és munkafolyamatok, gyors referenciának.

---

## Alapvető parancsok

```bash
# Repó klónozása
git clone https://github.com/SZERVEZET/REPO.git
cd REPO

# Aktuális állapot ellenőrzése
git status

# Változások megtekintése
git diff

# Commit történet
git log --oneline
```

---

## Napi munkafolyamat

```bash
# 1. Változások hozzáadása
git add .                      # Minden fájl
git add feladat1.py            # Egy konkrét fájl

# 2. Commit
git commit -m "leíró üzenet"

# 3. Push a szerverre
git push
```

---

## Változások visszavonása

```bash
# Fájl módosítás visszavonása (mentés előtt)
git checkout -- feladat1.py

# Utolsó commit visszavonása (fájlok megmaradnak)
git reset HEAD~1

# Staged fájl visszavonása (hozzáadás után, commit előtt)
git reset HEAD feladat1.py

# Fájl törlésének visszavonása
git checkout -- torölt_fajl.py
```

---

## Branch (ág) kezelés

```bash
# Ágak listázása
git branch

# Új ág létrehozása és átváltás
git checkout -b funkció-neve

# Átváltás meglévő ágra
git checkout main

# Ág beolvasztása a jelenlegi ágba
git merge funkció-neve

# Ág törlése (beolvasztás után)
git branch -d funkció-neve
```

---

## Távoli repó (Remote)

```bash
# Távoli repó ellenőrzése
git remote -v

# Változások letöltése
git pull

# Változások letöltése és rebase
git pull --rebase

# Változások feltöltése
git push

# Első push új ágon
git push -u origin ag-neve
```

---

## Hasznos parancsok

```bash
# Ki mit commitolt (utolsó 5)
git log --oneline -5

# Egy fájl történetének megtekintése
git log --oneline feladat1.py

# Commitok közötti különbségek
git diff HEAD~1

# .gitignore ellenőrzése
cat .gitignore

# Felhasználó beállítások ellenőrzése
git config user.name
git config user.email
```

---

## Első beállítás

```bash
# Név és email beállítása (egyszer kell)
git config --global user.name "Felhasználónév"
git config --global user.email "email@example.com"

# Alapértelmezett ág neve
git config --global init.defaultBranch main
```

---

## Gyakori hibák és megoldásaik

| Hiba | Megoldás |
|------|----------|
| `fatal: not a git repository` | Nem egy Git repó mappájában vagy. `cd` a repó mappájába. |
| `nothing to commit` | Nincs változás, vagy már commitoltad. `git status` |
| `error: failed to push` | `git pull --rebase` majd `git push` |
| `CONFLICT (content)` | Merge konfliktus — nyisd meg a fájlt, válaszd ki a helyes verziót, majd `git add .` és `git commit` |
| `Permission denied (publickey)` | SSH kulcs nincs beállítva. Használj HTTPS URL-t, vagy állítsd be az SSH kulcsot. |
| Rossz fájlokat commitoltam | `git reset HEAD~1` visszavonja az utolsó commitot |
| A `.env` fájl bekerült a repóba | Töröld a nyomkövetésből: `git rm --cached .env`, add hozzá a `.gitignore`-hoz |

---

## `.gitignore` minta

```gitignore
# Python
__pycache__/
*.pyc
venv/

# Környezeti változók
.env

# IDE
.vscode/
.idea/

# OS
.DS_Store
Thumbs.db
```

---

## Commit üzenet tippek

```bash
# Jó commit üzenetek
git commit -m "1. feladat: input kezelés kész"
git commit -m "fgv.py: szűrő függvény hozzáadva"
git commit -m "README frissítve: használati útmutató"

# Rossz commit üzenetek
git commit -m "done"
git commit -m "asdf"
git commit -m "."
```

---

**Kapcsolódó útmutatók:**
- [Környezet beállítás](kornyezet-beallitas.md)
- [GitHub Classroom — Tanuló útmutató](github-classroom-tanulo-utmutato.md)
- [Hibaelhárítás](hibaelharitas.md)
