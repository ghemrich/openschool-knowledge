# Discord szerver – Mentori útmutató

Ez a dokumentum elmagyarázza, hogyan kell egy közös Discord szervert létrehozni és kezelni az összes kurzushoz. Egyetlen szerver szolgál minden kurzus kommunikációs platformjaként – kurzusonként egy-egy kategória (csatornacsoport) biztosítja az elkülönítést.

---

## 1. Szerver létrehozása

1. Nyisd meg a [Discord](https://discord.com) alkalmazást (asztali vagy böngészős verzió)
2. Kattints a bal oldali sávban a **+** gombra → **Create My Own**
3. Válaszd: **For a club or community**
4. Adj nevet a szervernek (pl. `Programozás kurzusok`). Ne tedd bele az évszámot – a szerver évről évre újrahasználható
5. Tölts fel egy ikont (opcionális, de segít a megkülönböztetésben)
6. Kattints: **Create**

---

## 2. Csatorna struktúra

Az alábbi struktúra egyetlen szerveren kezeli az összes kurzust. Új kurzus hozzáadása = egy új kategória 2–3 csatornával.

### 2.1 Ajánlott csatornaszerkezet

```
📋 INFORMÁCIÓ
  #szabályzat           → Szerver szabályok, viselkedési kódex
  #közlemények           → Mentori bejelentések, minden kurzushoz (csak olvasható tanulóknak)
  #hasznos-linkek        → Dokumentációk, tutorialok, eszközök

🐍 PYTHON ALAPOK
  #python-alapok-általános    → Kérdések, beszélgetés a kurzusról
  #python-alapok-segítség     → Feladatokkal kapcsolatos kérdések és hibakeresés
  #python-alapok-megoldások   → Megoldások, kódrészletek megosztása

⚡ BACKEND FASTAPI
  #backend-általános   → Kérdések, beszélgetés a kurzusról
  #backend-segítség    → Feladatokkal kapcsolatos kérdések és hibakeresés
  #backend-megoldások  → Kód review, megoldások megosztása

💬 KÖZÖSSÉG
  #általános             → Szabadtéma, kurzusokon átívelő beszélgetés
  #off-topic             → Nem kurzussal kapcsolatos

🎤 HANG
  🔊 konzultáció         → Hangcsatorna konzultációs időpontokhoz
  🔊 foglalkozás         → Hangcsatorna online alkalmakhoz (képernyőmegosztás)

🔒 TANÁRI (rejtett)
  #mentori-szoba          → Mentori megbeszélések, tanulók nem látják
  #értékelések           → Értékelési feljegyzések
```

### 2.2 Új kurzus hozzáadása

Ha később új kurzust indítasz, csak adj hozzá egy új kategóriát 2–3 csatornával:

1. Szerver név → **Create Category** (pl. `🌐 WEBFEJLESZTÉS`)
2. Hozz létre 2–3 csatornát alatta (pl. `#web-általános`, `#web-segítség`)
3. Állítsd be a jogosultságokat (lásd 3.2)

### 2.3 Heti témák kezelése szálakkal (Threads)

Heti csatornák helyett a `#kurzus-segítség` csatornákon használj **szálakat**:

1. Minden héten nyiss egy új szálat **évszámmal**: pl. *„2026 – 3. hét – Feltételes elágazások"*
2. A tanulók az adott szálban kérdeznek
3. A szál automatikusan archiválódik inaktivitás után, de visszanyitható

> **Miért évszám?** A csatornák évről évre ugyanazok. Az évszám a szál nevében biztosítja, hogy a jelenlegi és a korábbi évek szálai ne keveredjenek. A régebbi szálak megmaradnak referenciaként, de egyértelműen elkülönülnek.

> **Előny**: A csatornák száma fix marad, de hétről hétre és évről évre szervezett a kommunikáció. Új kurzus nem jelent 13–25 extra csatornát.

### 2.4 Csatornák létrehozása

1. Kattints a szerver nevére (bal felső sarok) → **Create Category**
2. Adj nevet a kategóriának (pl. `🐍 PYTHON ALAPOK`)
3. A kategória mellett kattints a **+** gombra → **Create Channel**
4. Válaszd: **Text** vagy **Voice**
5. Adj nevet a csatornának (pl. `python-alapok-segítség`)

---

## 3. Szerepkörök és jogosultságok

### 3.1 Szerepkörök létrehozása

Szerver beállítások → **Roles** → **Create Role**

| Szerepkör | Szín | Jogok |
|-----------|------|-------|
| `Mentor` | 🔴 Piros | Adminisztrátor |
| `Python Alapok – 2026` | 🟢 Zöld | Üzenetküldés, olvasás, reakciók, fájlcsatolás |
| `Backend FastAPI – 2026` | 🔵 Kék | Üzenetküldés, olvasás, reakciók, fájlcsatolás |

> **Tipp:** Az évszámot tedd a szerepkör nevébe (pl. `Python Alapok – 2026`), hogy évről évre könnyen kezeld, ki az aktív tanuló. A kurzusonkénti szerepkörökkel szabályozhatod, ki melyik kurzus csatornáit látja. Ha nem szükséges az elkülönítés, elég egyetlen `Tanuló – 2026` szerepkör.

> **Tipp:** Érdemes megkérni az új tagokat, hogy felismerhető nevet vagy azonosítót használjanak becenévként (nickname). Beállítás: jobb klikk a felhasználóra → **Change Nickname**.

### 3.2 Fontos jogosultság-beállítások

**`#közlemények` csatorna:**
1. Csatorna beállítások → **Permissions**
2. `@everyone` → ❌ **Send Messages** (tiltás)
3. `Mentor` → ✅ **Send Messages** (engedélyezés)

**`🔒 TANÁRI` kategória:**
1. Kategória beállítások → **Permissions**
2. `@everyone` → ❌ **View Channel** (tiltás)
3. `Mentor` → ✅ **View Channel** (engedélyezés)

**Kurzus-kategória elrejtése (opcionális):**
Ha szeretnéd, hogy a Python Alapok tanulók ne lássák a Backend FastAPI csatornákat:
1. `⚡ BACKEND FASTAPI` kategória → **Permissions**
2. `@everyone` → ❌ **View Channel**
3. `Backend FastAPI` szerepkör → ✅ **View Channel**
4. Fordítva is, a `🐍 PYTHON ALAPOK` kategóriánál

---

## 4. Meghívó link generálása

1. Kattints a szerver nevére → **Invite People**
2. Kattints: **Edit invite link**
3. Állítsd be:
   - **Expire after**: Never (a szerver évről évre él)
   - **Max uses**: No limit (vagy az összes tanuló száma + tartalék)
4. Másold ki a linket és oszd meg a tanulókkal (e-mailben, órán, vagy a GitHub Classroom README-ben)

> **Biztonság:** Ne tedd közzé a meghívó linket nyilvánosan. Csak a kurzusok tanulóinak oszd meg.

> **Tipp:** Ugyanazt a meghívó linket használhatod évről évre, ha „Never" lejáratot állítasz be.

---

## 5. Hasznos botok

### 5.1 GitHub bot (ajánlott)

Értesítés a push-okról és pull requestekről közvetlenül Discordon.

1. Írd be bármelyik csatornán: `/github subscribe ORGANIZATION/REPO`
2. Válaszd ki, milyen eseményekről kérj értesítést (pushok, issues, stb.)

> Telepítés: [github.com/integrations/discord](https://github.com/integrations/discord)

### 5.2 Carl-bot (opcionális)

Automatikus szerepkör-kiosztás, ütemezett üzenetek, moderáció.

- Heti emlékeztető a házi feladat határidejéről
- Automatikus szerepkör adása csatlakozáskor (pl. reakció alapján választhatják ki a kurzusukat)

> Telepítés: [carl.gg](https://carl.gg)

### 5.3 Webhook-ok beállítása (automatizáláshoz)

A webhook-ok lehetővé teszik, hogy a szkriptek (pl. `discord-webhook.py`) küldjenek üzeneteket a csatornákra bot telepítése nélkül. Minden csatornához külön webhook kell.

#### Melyik csatornához kell webhook?

| Webhook neve | Csatorna | Mire kell |
|--------------|----------|-----------|
| Közlemények | `#közlemények` | Mentori bejelentések mindkét kurzusnak |
| Python Alapok | `#python-alapok-segítség` | Heti szálnyitók, emlékeztetők |
| Backend FastAPI | `#backend-segítség` | Heti szálnyitók, emlékeztetők |

#### Webhook létrehozása lépésről lépésre

1. Nyisd meg a csatorna beállításait:
   - Kattints a csatornanév melletti **⚙️ fogaskerékre**, vagy
   - Jobb klikk a csatornán → **Edit Channel**

2. Navigálj a webhook-okhoz:
   - Bal oldali menü → **Integrations** (Integrációk)
   - **Webhooks** → **New Webhook** (Új webhook)

3. Állítsd be:
   - **Name** (Név): adj leíró nevet (pl. `Mentori Értesítések`, `Python10 Bot`)
   - **Channel** (Csatorna): ellenőrizd, hogy a megfelelő csatorna van kiválasztva
   - **Avatar** (opcionális): tölts fel egy ikont, hogy megkülönböztesse a bot üzeneteit

4. Másold ki a webhook URL-t:
   - Kattints a **Copy Webhook URL** gombra
   - Az URL ilyen formátumú: `https://discord.com/api/webhooks/1234567890/aBcDeFgHiJkL...`
   - **⚠️ Ezt az URL-t tartsd titokban!** Aki ismeri, üzeneteket küldhet a csatornára.

5. Ismételd meg a többi csatornára is (összesen 3 webhook kell).

#### Webhook URL-ek tárolása

Hozz létre egy `.env` fájlt az `tools/` mappában (ez a fájl `.gitignore`-ban van, nem kerül verziókezelésbe):

```bash
# tools/.env
DISCORD_WEBHOOK_KOZLEMENYEK=https://discord.com/api/webhooks/1234.../aBcD...
DISCORD_WEBHOOK_PYTHON=https://discord.com/api/webhooks/5678.../eFgH...
DISCORD_WEBHOOK_BACKEND=https://discord.com/api/webhooks/9012.../iJkL...
```

Vagy állítsd be a terminálban:

**Linux / macOS:**
```bash
export DISCORD_WEBHOOK_KOZLEMENYEK="https://discord.com/api/webhooks/..."
export DISCORD_WEBHOOK_PYTHON="https://discord.com/api/webhooks/..."
export DISCORD_WEBHOOK_BACKEND="https://discord.com/api/webhooks/..."
```

**Windows (PowerShell):**
```powershell
$env:DISCORD_WEBHOOK_KOZLEMENYEK = "https://discord.com/api/webhooks/..."
$env:DISCORD_WEBHOOK_PYTHON = "https://discord.com/api/webhooks/..."
$env:DISCORD_WEBHOOK_BACKEND = "https://discord.com/api/webhooks/..."
```

**Windows (cmd):**
```cmd
set DISCORD_WEBHOOK_KOZLEMENYEK=https://discord.com/api/webhooks/...
set DISCORD_WEBHOOK_PYTHON=https://discord.com/api/webhooks/...
set DISCORD_WEBHOOK_BACKEND=https://discord.com/api/webhooks/...
```

#### Tesztelés

```bash
# Teszt üzenet küldése
python tools/discord-webhook.py uzenet --webhook-url $DISCORD_WEBHOOK_PYTHON --uzenet "🧪 Teszt üzenet – ha ezt látod, a webhook működik!"
```

Ha a teszt sikeres, az üzenet megjelenik a `#python-alapok-segítség` csatornán.

#### Webhook kezelése

- **URL megváltoztatása**: Csatorna beállítások → Integrations → Webhooks → kattints a webhook-ra → **Reset Webhook URL** (a régi URL érvénytelenné válik!)
- **Törlés**: ugyanitt → **Delete Webhook**
- **Webhook probléma**: ha 404-es vagy 401-es hibát kapsz, a webhook törölve lett vagy az URL hibás – hozd létre újra

---

## 6. Moderációs beállítások

### 6.1 Alapbeállítások

Szerver beállítások → **Safety Setup**:

- **Verification Level**: Medium (regisztrált fiók + e-mail szükséges)
- **Explicit Media Content Filter**: Scan messages from all members
- **Default Notification Settings**: Only @mentions

### 6.2 AutoMod szabályok

Szerver beállítások → **AutoMod**:

1. **Spam szűrés** → Bekapcsolás
2. **Link szűrés** → Opcionális
3. **Mention spam** → Maximum 5 mention / üzenet

---

## 7. Napi használat – tippek

### Heti rutin

1. **Hét eleje**: Közlemény a `#közlemények` csatornán az aktuális hét témájáról (jelöld meg melyik kurzus: 🐍 vagy ⚡)
2. **Nyiss szálat**: A megfelelő `#kurzus-segítség` csatornán nyiss egy szálat az aktuális héthez
3. **A héten**: Kérdések megválaszolása a szálakban
4. **Határidő előtt**: Emlékeztető a házi feladat leadásáról

### Bevált gyakorlatok

- **Pineld** a fontos üzeneteket (jobb klikk → Pin Message)
- Használj **szálakat** a heti témákhoz — ez tartja tisztán a fő csatornát
- Ha egy tanuló privátban ír, irányítsd át a nyilvános csatornára — mások is tanulhatnak a válaszból
- **Reakciókkal** jelezd, hogy láttad a kérdést (👀) vagy hogy megoldódott (✅)
- A `#közlemények`-ben használj emojit a kurzus jelölésére: 🐍 Python Alapok, ⚡ Backend FastAPI

### Vizsga időszak

- Hozz létre egy ideiglenes szálat a vizsga kérdéseknek
- A vizsga alatt **némítsd** a szervert, hogy ne legyenek zavaró értesítések
- Vizsga után oszd meg az eredményeket a `#közlemények` csatornán

---

## 8. Évváltás – éves karbantartás

A szerver évről évre újrahasználható. Az alábbi lépéseket végezd el minden tanév elején:

### 8.1 Szerepkörök

1. Hozz létre új éves szerepköröket (pl. `Python Alapok – 2027`, `Backend FastAPI – 2027`)
2. Az új tanulóknak az új szerepkört add ki
3. A végzett tanulóktól vedd el az előző éves szerepkört, vagy hagyd meg – ők továbbra is olvashatják a régi szálakat, de az új szálakban nem aktívak

### 8.2 Szálak

- **Ne töröld** a régi szálakat – referenciaként hasznosak lehetnek (ugyanazok a kérdések merülnek fel évről évre)
- Az archivált szálak automatikusan eltűnnek a listából, de kereshetők maradnak
- Az új év szálai az évszám prefix miatt egyértelműen elkülönülnek (pl. *„2027 – 3. hét – Feltételes elágazások"*)

### 8.3 Közlemények

- A tanév elején írj egy üdvözlő közleményt a `#közlemények` csatornán az új tanévre
- Opcionális: pineld le az új tanév első közleményét

### 8.4 Takarítás (opcionális)

- Ha a `#kurzus-általános` csatornákon túl sok a régi üzenet, használd a Discord **Bulk Delete** funkciót (bot segítségével), vagy hagyd – a szálak elkülönítik a lényegi tartalmat
- A végzett tanulók eltávolítása nem kötelező, de csökkenti a szerver létszámát

---

## 9. Hibaelhárítás

| Probléma | Megoldás |
|----------|---------|
| Tanuló nem tud csatlakozni | Ellenőrizd a meghívó link érvényességét és a max. felhasználók számát |
| Tanuló nem lát csatornát | Ellenőrizd, hogy megkapta-e a megfelelő szerepkört |
| Bot nem működik | Ellenőrizd a bot jogosultságait a szerver beállításokban |
| Spam a csatornákon | Kapcsold be a Slowmode-ot (csatorna beállítások → 10 mp) |
| Tanuló nem tud írni a `#közlemények`-be | Ez szándékos – csak a `Mentor` szerepkör írhat oda |
| Túl sok szál | Az archivált szálak automatikusan eltűnnek, de visszakereshetők |
| Régi éves szálak zavarnak | Az évszám prefix segít megkülönböztetni – a régiek archiválva maradnak |
