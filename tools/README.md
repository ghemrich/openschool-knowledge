# Eszközök (Tools)

Automatizálási szkriptek a kurzusok adminisztrálásához.

## Szkriptek

| Szkript | Leírás |
|---|---|
| `github-setup.sh` | GitHub Classroom template repók létrehozása (Linux/macOS) |
| `github-setup.ps1` | GitHub Classroom template repók létrehozása (Windows) |
| `github-update.sh` | GitHub Classroom template repók frissítése (Linux/macOS) |
| `github-update.ps1` | GitHub Classroom template repók frissítése (Windows) |
| `discord-webhook.py` | Discord webhook üzenetküldő — bejelentések |

## GitHub Setup

Template repókat hoz létre egy GitHub Organization alatt a `github-classroom/` mappa almappáiból.

**Előfeltételek:**
- [GitHub CLI (gh)](https://cli.github.com) telepítve és bejelentkezve
- Az Organization már létezik a GitHubon

**Használat:**

```bash
# Linux/macOS
./github-setup.sh <ORGANIZATION> <TEMPLATE_MAPPA>
./github-setup.sh openschool-python-2026 ../../courses/python-alapok/github-classroom

# Windows (PowerShell)
.\github-setup.ps1 <ORGANIZATION> <TEMPLATE_MAPPA>
.\github-setup.ps1 openschool-python-2026 ..\..\courses\python-alapok\github-classroom
```

## GitHub Update

Meglévő template repókat frissíti a helyi fájlok alapján. A szkript klónozza a repót, lecseréli a tartalmát, és pusholja a változásokat. Csak akkor commitol, ha van tényleges változás.

**`--classroom` mód:** A GitHub Classroom saját nevű template repókat hoz létre (pl. `python-alapok-git-alapok-het00-git-alapok`). A `--classroom` kapcsolóval a szkript a mappa neve alapján megkeresi a hozzá tartozó repót az Organization-ben.

**Előfeltételek:**
- [GitHub CLI (gh)](https://cli.github.com) telepítve és bejelentkezve
- A repók már létre lettek hozva a `github-setup` szkripttel

**Használat:**

```bash
# Linux/macOS
./github-update.sh <ORGANIZATION> <TEMPLATE_MAPPA> [--classroom]
./github-update.sh OpenSchool-HU ../courses/python-alapok/github-classroom
./github-update.sh OpenSchool-HU ../courses/python-alapok/github-classroom --classroom

# Windows (PowerShell)
.\github-update.ps1 <ORGANIZATION> <TEMPLATE_MAPPA> [-Classroom]
.\github-update.ps1 OpenSchool-HU ..\courses\python-alapok\github-classroom
.\github-update.ps1 OpenSchool-HU ..\courses\python-alapok\github-classroom -Classroom
```

## Discord Webhook

Heti bejelentések és szabad üzenetek küldése Discord csatornákra.

**Előfeltételek:**
- Webhook URL-ek környezeti változókban (vagy `.env` fájl):
  - `DISCORD_WEBHOOK_KOZLEMENYEK` → #közlemények csatorna
  - `DISCORD_WEBHOOK_PYTHON` → #python-alapok-segítség csatorna
  - `DISCORD_WEBHOOK_BACKEND` → #backend-segítség csatorna

**Használat:**

```bash
# Bejelentés küldése
python discord-webhook.py bejelentes --kurzus python --het 3 --tema "Feltételes elágazások"

# Szabad üzenet
python discord-webhook.py uzenet --webhook-url URL --uzenet "Szabad szöveg"
```


