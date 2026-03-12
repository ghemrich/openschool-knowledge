# Lecke 00 – Git, GitHub, parancssor alapok

> **Dokumentáció:** [Git kézikönyv](https://git-scm.com/book/en/v2) · [Linux parancsok](https://www.tutorialspoint.com/unix/unix-useful-commands.htm) · [GitHub Docs](https://docs.github.com/en)

---

## 1–2. óra: Parancssor alapok

### Miért tanuljuk a parancssort?

Backend fejlesztőként minden nap használod a terminált: szerveren futtatsz programokat, fájlokat kezelsz, konténereket indítasz. A grafikus felület nem mindig elérhető.

> **Windows:** Használhatod a PowerShell-t, a Parancssort (cmd), a VS Code beépített terminálját, vagy a Git Bash-t (a Git telepítővel jön). A Git Bash Windowson is biztosítja a lenti Linux parancsokat.

### Navigáció

```bash
pwd                    # Aktuális könyvtár kiírása
ls                     # Fájlok listázása
ls -la                 # Részletes lista (rejtett fájlokkal)
cd mappanev            # Belépés mappába
cd ..                  # Vissza egy szinttel
cd ~                   # Home könyvtár
```

### Fájlműveletek

```bash
mkdir projekt          # Mappa létrehozása
touch fajl.txt         # Üres fájl létrehozása
cp fajl.txt masolat.txt  # Másolás
mv fajl.txt ujnev.txt    # Átnevezés / mozgatás
rm fajl.txt            # Törlés (NINCS lomtár!)
rm -r mappa/           # Mappa törlés rekurzívan
cat fajl.txt           # Fájl tartalmának kiírása
nano fajl.txt          # Szerkesztés terminálban
```

### Jogosultságok

```bash
ls -la                 # Jogosultságok megtekintése
chmod +x script.sh     # Futtatási jog hozzáadása
chmod 644 fajl.txt     # Olvasás mindenkinek, írás tulajdonosnak
```

---

## 3–4. óra: Git ismétlés és haladó funkciók

### Alapparancsok ismétlése

```bash
git init                          # Repo inicializálás
git add .                         # Minden fájl stage-elése
git commit -m "üzenet"            # Commit
git push origin main              # Push
git pull origin main              # Pull
git status                        # Állapot
git log --oneline                 # Rövid napló
```

### .gitignore

Hozz létre `.gitignore` fájlt a projekt gyökerében:

```
venv/
__pycache__/
*.pyc
.env
.idea/
.vscode/
```

### Branch-ek

```bash
git branch                        # Branch-ek listázása
git branch feature/uj-vegpont     # Új branch létrehozása
git checkout feature/uj-vegpont   # Váltás arra a branch-re
git checkout -b feature/login     # Létrehozás + váltás egyben
git merge feature/uj-vegpont      # Merge az aktuális branch-be
git branch -d feature/uj-vegpont  # Branch törlése
```

### Konfliktuskezelés

Ha két branch ugyanazt a sort módosítja:

```
<<<<<<< HEAD
ez az aktuális branch tartalma
=======
ez a másik branch tartalma
>>>>>>> feature/login
```

Megoldás: szerkeszd a fájlt, válaszd ki a helyes verziót, majd:

```bash
git add .
git commit -m "konfliktus feloldva"
```

---

## 5–6. óra: GitHub Classroom munkafolyamat

### Lépésről lépésre

1. **Meghívó link** – A mentortól kapott linken fogadd el a feladatot
2. **Klónozás** – `git clone <repo-url>`
3. **Munka** – Oldd meg a feladatokat, commitolj folyamatosan
4. **Push** – `git push` → automatikus tesztek futnak
5. **Eredmény** – A GitHub Actions fülön látod az eredményt

### Automatikus tesztek értelmezése

| Jel | Jelentés |
|-----|----------|
| ✅ | A teszt sikeres |
| ❌ | A teszt sikertelen |
| 🔄 | Tesztek futnak |

Ha egy teszt sikertelen, kattints rá, és olvasd el a hibaüzenetet!

---

## Gyakorlat

1. Nyiss terminált és hozz létre egy `backend-kurzus` mappát
2. Inicializálj benne git repót
3. Hozz létre benne egy `README.md` fájlt a nevedddel
4. Commitold és pushold a GitHub Classroom repóba
5. Ellenőrizd, hogy az automatikus tesztek lefutottak
