# Integrált munkafolyamat útmutató

A mentori munkafolyamat két eszközre épül: **GitHub Classroom** (feladatok kiadása és automatikus értékelés) és **Discord** (kommunikáció és értesítések). Ez a dokumentum leírja, hogyan kapcsolódnak össze.

---

## 1. Félév indításkor (egyszeri beállítás)

### 1.1 GitHub Classroom előkészítése

**Linux / macOS:**
```bash
# Template repók létrehozása az Organizationben
cd tools/
./github-setup.sh iskolam-org ../courses/python-alapok/github-classroom
```

**Windows (PowerShell):**
```powershell
# Template repók létrehozása az Organizationben
cd tools/
.\github-setup.ps1 -Organization iskolam-org -TemplateMappa ..\courses\python-alapok\github-classroom
```

```bash
# Classroom-ban: Create Assignment → válaszd a template repót → engedélyezd az autograding-et
```

Minden hétre létrejön egy template repó (pl. `het01-alapok`, `het02-bevitel-szoveg`), amelyet a GitHub Classroom assignment-hez kapcsolhatsz.

### 1.2 Discord szerver

Ha még nincs szerver, kövesd a [Discord szerver útmutatót](discord-szerver-utmutato.md).

Ha már van szerver, csak az éves karbantartást kell elvégezni (lásd útmutató 8. fejezet):
- Új éves szerepkörök létrehozása (`Python Alapok – 2026`)
- Régi szálak archiválása

### 1.3 Webhook-ok beállítása

A szkriptek webhook-okon keresztül küldenek üzeneteket a Discord csatornákra. A részletes beállítási útmutatót (létrehozás, .env fájl, tesztelés) lásd:
**[Discord szerver útmutató – 5.3 Webhook-ok](discord-szerver-utmutato.md#53-webhook-ok-beállítása-automatizáláshoz)**

Röviden: 3 webhook kell (`#közlemények`, `#python-alapok-segítség`, `#backend-segítség`), az URL-eket a `tools/.env` fájlban tárold:

```bash
# tools/.env
DISCORD_WEBHOOK_KOZLEMENYEK=https://discord.com/api/webhooks/...
DISCORD_WEBHOOK_PYTHON=https://discord.com/api/webhooks/...
DISCORD_WEBHOOK_BACKEND=https://discord.com/api/webhooks/...
```

---

## 2. Heti rutin

### 2.1 Óra előtt – szál nyitása és bejelentés

```bash
cd tools/

# Heti szál nyitása a kurzus csatornáján
python discord-webhook.py szal --kurzus python --het 3 --tema "Feltételes elágazások"

# Bejelentés (opcionális)
python discord-webhook.py bejelentes --kurzus python --het 3 --tema "Feltételes elágazások" --megjegyzes "Ma az if/elif/else szerkezeteket nézzük meg."
```

### 2.2 Házi feladat kiadása

1. GitHub Classroom-ban: **Create Assignment** → válaszd a heti template-et
2. Az invite linket küldd el Discord-on:

```bash
python discord-webhook.py uzenet --webhook-url $DISCORD_WEBHOOK_PYTHON --uzenet "📎 Házi feladat: https://classroom.github.com/a/XXXXXX"
```

### 2.3 Határidő emlékeztető

```bash
# Határidő előtt 1-2 nappal
python discord-webhook.py emlekezteto --kurzus python --het 3 --hatarido "2026-03-14"
```

### 2.4 Eredmények letöltése

GitHub Classroom → **Download Grades** → CSV fájl.

Az autograding automatikusan értékeli a beadásokat:
- **Python Alapok:** shell-alapú tesztek (`test -f megoldas.py && python megoldas.py < bemenet.txt | diff - vart_kimenet.txt`)
- **Backend FastAPI:** pytest tesztek (`pytest test_*.py`)

---

## 3. Eszközök összefoglalása

| Mikor | Eszköz | Parancs |
|-------|--------|---------|
| Félév eleje | `github-setup.sh` / `.ps1` | Template repók létrehozása |
| Heti | `discord-webhook.py szal` | Heti szál nyitása |
| Heti | `discord-webhook.py bejelentes` | Bejelentés küldése |
| Házi kiadásakor | `discord-webhook.py uzenet` | Invite link megosztása |
| Határidő előtt | `discord-webhook.py emlekezteto` | Emlékeztető küldése |

---

## 4. Mappaszerkezet hivatkozások

```
courses/
    python-alapok/              ← Python alapok kurzusanyag
    python-backend/             ← Backend FastAPI kurzusanyag
    projekt-labor/              ← Projekt Labor
tools/                          ← szkriptek
    github-setup.sh
    discord-webhook.py
guides/                         ← közös dokumentáció
    discord-szerver-utmutato.md ← szerver beállítás
    integralt-munkafolyamat.md  ← ez a fájl
    open-source-projekt-utmutato.md
```
