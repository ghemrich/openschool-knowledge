# Open source projekt indítása — Általános útmutató

Útmutató egy nyílt forráskódú projekt professzionális felépítéséhez. Nem kötődik egyetlen kurzushoz sem — bármely projekthez alkalmazható. Az itt leírt elemek az ipari standard részeit képezik.

---

## 1. Repó alapok

Minden open source projekt néhány alapfájllal indul a gyökérmappában:

| Fájl | Szerepe |
|------|---------|
| `README.md` | A projekt arca — első dolog, amit bárki lát |
| `LICENSE` | Jogi keret — nélküle a kód nem open source |
| `.gitignore` | Verziókezelésből kizárt fájlok (build, cache, env) |
| `CONTRIBUTING.md` | Útmutató kontribútoroknak |
| `CHANGELOG.md` | Változások naplója verziónként |
| `CODE_OF_CONDUCT.md` | Viselkedési szabályok (opcionális, de ajánlott) |

### 1.1 README.md

A README az egyetlen fájl, amit garantáltan mindenki elolvas. Tömör, lényegre törő kell legyen.

**Ajánlott felépítés:**

```markdown
# Projekt neve

Egy mondatos leírás — mi ez, mire jó.

## Funkciók

- Rövid felsorolás a fő képességekről

## Telepítés

git clone, majd a minimális lépések a futtatásig.

## Használat

Egy rövid példa vagy parancs.

## Dokumentáció

Link a részletes dokumentációra (ha van).

## Hozzájárulás

Link a CONTRIBUTING.md-re.

## Licenc

Licenc típus és link a LICENSE fájlra.
```

**Gyakori hiba:** Túl hosszú README, ami mindent tartalmaz (API referencia, projekt struktúra, fejlesztői útmutató). Ezek külön dokumentumokba valók — a README csak linkeli őket.

### 1.2 LICENSE

Licenc nélkül a kód alapértelmezetten copyright-védett — senki nem használhatja legálisan. A licencválasztás a projekt legfontosabb jogi döntése.

| Licenc | Mikor válaszd |
|--------|---------------|
| **MIT** | Maximális szabadság, minimális megkötés. A leggyakoribb választás. |
| **Apache 2.0** | Mint az MIT, de szabadalmi védelmet is ad. Nagyobb projekteknél ajánlott. |
| **GPL 3.0** | Copyleft — az származtatott munkáknak is GPL alatt kell maradniuk. |
| **Unlicense** | Public domain — lemondás minden jogról. |

> **Tipp:** Ha nem tudod melyiket válaszd, válaszd az MIT-t. Választáshoz: [choosealicense.com](https://choosealicense.com/)

### 1.3 .gitignore

Minden nyelv és keretrendszer generál fájlokat, amelyeknek nincs helye a verziókezelésben.

**Tipikus kizárások:**

| Kategória | Példák |
|-----------|--------|
| Nyelv-specifikus | `__pycache__/`, `*.pyc`, `node_modules/`, `dist/` |
| IDE/editor | `.vscode/`, `.idea/`, `*.swp` |
| Környezet | `.env`, `.env.local` |
| Build | `build/`, `target/`, `*.o` |
| OS | `.DS_Store`, `Thumbs.db` |

> **Forrás:** [github.com/github/gitignore](https://github.com/github/gitignore) — kész sablonok nyelvek és keretrendszerek szerint.

---

## 2. Dokumentáció

A kód önmagában nem elég. Egy projekt akkor életképes, ha egy új ember el tud indulni a dokumentáció alapján.

### 2.1 Dokumentáció struktúra

Kisebb projekteknél (< 5 doc fájl) elég a gyökérmappában tartani őket. Nagyobb projekteknél a `docs/` mappa kategóriákra bontva:

```
docs/
├── getting-started/    ← telepítés, konfiguráció, architektúra
├── development/        ← fejlesztői útmutató, tesztelés
├── reference/          ← API referencia, adatbázis séma
├── operations/         ← karbantartás, deploy, monitoring
└── guides/             ← felhasználói útmutató, HowTo-k
```

### 2.2 Navigáció

Ha több dokumentum van, kell egy rendszer, amivel bárki megtalálja, amit keres:

- **README docs tábla** — csoportosított linkek kategóriánként
- **Nav bar a dokumentumokban** — egységes fejléc/lábléc navigáció minden doc fájlban
- **Dokumentációs útmutató** — leírja az elnevezési konvenciókat, a mappastruktúrát és a link szabályokat

### 2.3 Dokumentáció nyelve

Ha a közösség egy nyelvet beszél (pl. magyar tanulók), írj azon a nyelven. Ha nemzetközi közönséget célzol, angolul. Ne keverd a kettőt — egy nyelv, végig.

---

## 3. Kontribúciós útmutató (CONTRIBUTING.md)

Ez a fájl válaszolja meg: *„Hogyan járulhatok hozzá ehhez a projekthez?"*

### 3.1 Ajánlott tartalom

1. **Hogyan indulj el** — fork, clone, dev környezet felállítása
2. **Issue-k** — mikor és hogyan nyiss issue-t
3. **Branch konvenció** — `feature/`, `fix/`, `docs/` prefixek
4. **Commit üzenetek** — Conventional Commits formátum
5. **Pull Request** — hogyan küldj PR-t, mit írj a leírásba
6. **Code review** — mennyi idő alatt válaszolnak, mire figyelnek
7. **Kódstílus** — linter szabályok, formázás

### 3.2 Conventional Commits

Egységes commit üzenet formátum, ami automatizálható (CHANGELOG generálás, semantic versioning):

```
<típus>(<hatókör>): <leírás>

feat(auth): GitHub OAuth bejelentkezés
fix(api): 500-as hiba a courses végponton
docs(readme): telepítési lépések frissítése
test(auth): JWT token lejárat tesztek
chore(deps): FastAPI frissítés 0.115-re
```

| Típus | Mikor |
|-------|-------|
| `feat` | Új funkció |
| `fix` | Hibajavítás |
| `docs` | Csak dokumentáció változás |
| `test` | Teszt hozzáadás vagy javítás |
| `chore` | Build, CI, függőségek |
| `refactor` | Kód átszervezés, funkció változás nélkül |

> **Részletek:** [conventionalcommits.org](https://www.conventionalcommits.org/)

---

## 4. Issue és PR template-ek

A GitHub template-ek biztosítják, hogy minden bejelentés és PR egységes formátumú legyen.

### 4.1 Issue template-ek

Mappájuk: `.github/ISSUE_TEMPLATE/`

**Tipikus template-ek:**

| Fájl | Cél |
|------|-----|
| `bug_report.md` | Hiba bejelentése (lépések, elvárt viselkedés, környezet) |
| `feature_request.md` | Új funkció javaslata (leírás, motiváció, lehetséges megoldás) |

Opcionálisan: `config.yml` a menü testreszabásához (pl. „Blank issue" meghagyása vagy külső linkek).

### 4.2 PR template

Fájl: `.github/pull_request_template.md`

Minden PR nyitásánál automatikusan betölti a sablont. Tipikus elemek:
- Mi változik
- Kapcsolódó issue (`Closes #...`)
- PR típus (feature / fix / docs / test)
- Ellenőrzőlista (tesztek zöldek, linter OK, stb.)

---

## 5. CI/CD

A Continuous Integration legalapvetőbb feladata: **minden push és PR automatikusan tesztelve legyen**.

### 5.1 Alap CI pipeline

GitHub Actions-szel (`.github/workflows/ci.yml`):

```yaml
name: CI
on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main, develop]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Setup
        # nyelv-specifikus setup (Python, Node, stb.)
      - name: Install dependencies
        # pip install, npm install, stb.
      - name: Lint
        # ruff check, eslint, stb.
      - name: Test
        # pytest, jest, stb.
```

### 5.2 CI elvek

| Elv | Miért |
|-----|-------|
| Minden PR-nek zöldnek kell lennie merge előtt | A `main` branch mindig működőképes marad |
| A CI gyors legyen (< 5 perc) | Ha lassú, a fejlesztők megkerülik |
| Lint + teszt együtt | A kódstílus és a funkcionalitás is ellenőrzött |

### 5.3 CD (opcionális)

Continuous Deployment: a `main`-re merge után automatikus deploy az éles szerverre. Csak akkor, ha a CI zöld. Eszközök: GitHub Actions, Docker, SSH deploy, stb.

---

## 6. Branch stratégia

### 6.1 Ajánlott modell

```
main ──────────────────── (éles, védett)
  │
  ├── develop ─────────── (staging, védett)
  │     │
  │     ├── feature/... ── (új funkció)
  │     ├── fix/... ────── (hibajavítás)
  │     └── docs/... ───── (dokumentáció)
```

| Branch | Szerepe | Védett? |
|--------|---------|---------|
| `main` | Éles kód, mindig stabil | Igen — PR + CI + review kötelező |
| `develop` | Integrációs branch, ide mennek a feature PR-ek | Igen — PR + CI |
| `feature/`, `fix/`, `docs/` | Egyedi munkák, rövid életű | Nem |

### 6.2 Branch protection

GitHub-on: **Settings → Branches → Branch protection rules**

Ajánlott szabályok `main`-re:
- Require pull request before merging
- Require status checks to pass (CI)
- Require at least 1 review approval
- Do not allow force pushes

---

## 7. Verziókezelés és CHANGELOG

### 7.1 Semantic Versioning (SemVer)

```
MAJOR.MINOR.PATCH
  │     │     │
  │     │     └── Hibajavítás (nem töri a kompatibilitást)
  │     └──────── Új funkció (visszafelé kompatibilis)
  └────────────── Breaking change (nem kompatibilis változás)
```

Példák: `1.0.0` → `1.0.1` (fix) → `1.1.0` (feature) → `2.0.0` (breaking change).

> **Részletek:** [semver.org](https://semver.org/)

### 7.2 CHANGELOG

A CHANGELOG.md dokumentálja, mit változtattunk verziónként. Kézzel is írható, de ha Conventional Commits-ot használsz, automatizálható:

| Eszköz | Nyelv | Jellemző |
|--------|-------|----------|
| [git-cliff](https://git-cliff.org/) | Rust (bináris) | Gyors, rugalmas, TOML konfig |
| [standard-version](https://github.com/conventional-changelog/standard-version) | Node.js | npm ökoszisztéma |
| [python-semantic-release](https://python-semantic-release.readthedocs.io/) | Python | Python projektek CI-je |

---

## 8. Közösségépítés

### 8.1 Good first issue-k

Az új kontribútoroknak belépési pont kell. A `good first issue` címke jelöli azokat a feladatokat, amelyek:

- Jól definiáltak, kis scope
- Nem igényelnek mély architektúra ismeretet
- Tartalmaznak kontextust (melyik fájl, mi a cél)
- A megoldás ellenőrizhető teszttel

> **Tipp:** Tartsd fenn folyamatosan 3–5 nyitott `good first issue`-t. Ha elfogy, a projekt megközelíthetetlennek tűnik az újonnan érkezőknek.

### 8.2 Közösségi szerepkörök

Egy növekvő projektben érdemes definiálni az előrelépési útvonalat:

| Szint | Feltétel | Jogosultság |
|-------|----------|-------------|
| Felhasználó | Használja a projektet | Issue nyitás |
| Kontribútor | Elfogadott PR | Contributor címke |
| Reviewer | Rendszeres, minőségi kontribúció | Code review jogosultság |
| Maintainer | Meghívás a core csapattól | Write access, release |

### 8.3 Kommunikáció

A nyílt forráskódú projekt közössége valahol kommunikál. Eszközök:

| Eszköz | Mikor válaszd |
|--------|---------------|
| GitHub Issues / Discussions | Minden projekthez — a kód mellett van |
| Discord | Valós idejű chat, kisebb közösség |
| Slack | Szervezeti környezet |

A fontos döntéseket és megbeszéléseket mindig írd le publikusan (issue, PR, discussion) — a chat szálak eltűnnek, a GitHub megmarad.

---

## 9. Projekt tervezés

### 9.1 Roadmap

Egy publikus roadmap megmutatja, merre tart a projekt. Lehet:
- `docs/` mappában markdown fájlként (pl. `roadmap.md`)
- GitHub Milestones (issue-k csoportosítva mérföldkövekhez)
- GitHub Projects board (kanban tábla)

### 9.2 Labels (címkék)

Egységes címkerendszer a GitHub issue-khoz:

| Címke | Szín | Jelentés |
|-------|------|---------|
| `bug` | 🔴 | Hiba |
| `enhancement` | 🔵 | Új funkció |
| `documentation` | 🟢 | Dokumentáció |
| `good first issue` | 🟣 | Kezdőknek alkalmas |
| `help wanted` | 🟡 | Segítség kell |
| `wontfix` | ⚪ | Nem javítjuk |
| `duplicate` | ⚪ | Duplikált issue |

---

## 10. Ellenőrzőlista — Open source projekt indítás

Egy új projekt nyitásakor vagy egy meglévő open source-sá tételekor haladj végig ezen a listán:

### Alapok
- [ ] `README.md` — tömör, tartalmazza: leírás, telepítés, használat, licenc
- [ ] `LICENSE` — válassz licencet (MIT ajánlott)
- [ ] `.gitignore` — nyelv-specifikus kizárások

### Kontribúció
- [ ] `CONTRIBUTING.md` — fork, branch, commit, PR útmutató
- [ ] Issue template-ek (bug report + feature request)
- [ ] PR template ellenőrzőlistával

### Automatizálás
- [ ] CI pipeline (lint + teszt minden push/PR-re)
- [ ] Branch protection (`main` védett, PR + CI + review kötelező)
- [ ] CHANGELOG (kézi vagy automatikus)

### Közösség
- [ ] Legalább 3 `good first issue` nyitva
- [ ] Közösségi szerepkörök definiálva
- [ ] Kommunikációs csatorna (GitHub Discussions / Discord)
- [ ] Roadmap publikusan elérhető

---

## Hivatkozások

| Téma | Link |
|------|------|
| Licenc választás | [choosealicense.com](https://choosealicense.com/) |
| .gitignore sablonok | [github.com/github/gitignore](https://github.com/github/gitignore) |
| Conventional Commits | [conventionalcommits.org](https://www.conventionalcommits.org/) |
| Semantic Versioning | [semver.org](https://semver.org/) |
| GitHub Community docs | [docs.github.com/en/communities](https://docs.github.com/en/communities) |
| Open Source Guides | [opensource.guide](https://opensource.guide/) |
| git-cliff (CHANGELOG) | [git-cliff.org](https://git-cliff.org/) |
| Branch protection | [GitHub docs](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-a-branch-protection-rule) |
