# Modul 7 — Open source és közösség

## Cél

Az OpenSchool platform előkészítése arra, hogy mások is hozzájáruljanak. A modul végére:

> **Háttérolvasmány:** Az open source projektek általános felépítését (README, LICENSE, CI/CD, branch stratégia, verziókezelés, közösségépítés) lásd az [Open source projekt útmutatóban](../../../../guides/open-source-projekt-utmutato.md). Ez a modul az OpenSchool platformra alkalmazza ezeket a gyakorlatokat.

- A repó professzionálisan dokumentált, készen áll kontribútorok fogadására
- Van CONTRIBUTING guide, issue és PR template
- A branch stratégia és review folyamat definiált
- A közösségi szerepkörök és az előrelépési útvonal tiszta

## 7.1 LICENSE

Az OpenSchool open source — a licencnek engedélyeznie kell a szabad felhasználást.

**Kettős licencelés:**

Az OpenSchool projektek kettős licencet használnak:

| Licenc | Vonatkozik | Jellemző |
|--------|-----------|----------|
| MIT | Kód (szkriptek, tesztek, konfigurációk) | Minimális megkötés, bárki használhatja bármire |
| CC BY-SA 4.0 | Oktatási tartalom (leckék, feladatok, útmutatók) | Szabad felhasználás, de a származékos művek is nyíltak maradnak |

**Feladat:**
- Adj hozzá egy `LICENSE` fájlt (MIT, kódra) a repó gyökerébe
- Adj hozzá egy `LICENSE-CC-BY-SA` fájlt (CC BY-SA 4.0, tartalomra)
- A `README.md`-ben is szerepeljen mindkét licenc típus

## 7.2 CONTRIBUTING.md

Útmutató új kontribútoroknak: hogyan járulhatsz hozzá a projekthez.

**Tartalma:**
1. **Hogyan indulj el** — repó fork-olása, lokális fejlesztői környezet felállítása
2. **Issue-k** — hogyan nyiss issue-t, milyen címkéket használunk
3. **Branch-ek** — elnevezési konvenció: `feature/`, `fix/`, `docs/`
4. **Commit üzenetek** — konvenció: `feat:`, `fix:`, `docs:`, `test:`
5. **Pull Request** — hogyan küldj PR-t, mit írj a leírásba
6. **Code review** — mire figyelünk, mennyi idő alatt válaszolunk
7. **Kódstílus** — ruff szabályok, típusannotáció ajánlás

**Feladat:**
- Írd meg a `CONTRIBUTING.md` fájlt
- Legyen magyar nyelvű (a közösség magyar)
- Tartalmazza a lokális fejlesztői környezet felállítását lépésről lépésre

## 7.3 Issue template-ek

GitHub issue template-ek a `.github/ISSUE_TEMPLATE/` mappában:

**Bug report (`bug_report.md`):**
```markdown
---
name: Hibajelentés
about: Hiba bejelentése a platformmal kapcsolatban
labels: bug
---

## Hiba leírása
<!-- Mi a hiba? -->

## Reprodukálás lépései
1.
2.
3.

## Elvárt viselkedés
<!-- Mi lenne a helyes működés? -->

## Környezet
- OS:
- Böngésző:
```

**Feature request (`feature_request.md`):**
```markdown
---
name: Funkció kérés
about: Új funkció vagy fejlesztés javaslata
labels: enhancement
---

## Leírás
<!-- Mit szeretnél? -->

## Motiváció
<!-- Miért lenne hasznos? -->

## Lehetséges megoldás
<!-- Van ötleted a megvalósításra? -->
```

**Feladat:**
- Hozd létre mindkét issue template-et
- Adj hozzá egy `config.yml`-t is, ami a "Blank issue" opciót is meghagyja

## 7.4 PR template

`.github/pull_request_template.md`:

```markdown
## Mit változtat ez a PR?
<!-- Rövid leírás -->

## Kapcsolódó issue
Closes #

## Típus
- [ ] Új funkció (feature)
- [ ] Hibajavítás (fix)
- [ ] Dokumentáció (docs)
- [ ] Teszt
- [ ] Egyéb

## Ellenőrzőlista
- [ ] A tesztek zöldek (`pytest -v`)
- [ ] A linter nem jelez hibát (`ruff check .`)
- [ ] A kód dokumentált (ha szükséges)
```

**Feladat:**
- Hozd létre a PR template-et
- Teszteld: nyiss egy PR-t és ellenőrizd, hogy a template megjelenik

## 7.5 Branch stratégia

```
main ─────────────────────────────── (éles, védett)
  │
  ├── develop ────────────────────── (staging)
  │     │
  │     ├── feature/user-profile ── (új funkció)
  │     ├── fix/login-redirect ──── (hibajavítás)
  │     └── docs/api-guide ──────── (dokumentáció)
```

**Szabályok:**
- `main`: védett branch, csak PR-on keresztül, CI zöld kell
- `develop`: staging branch, ide mennek a feature branch-ek
- Feature branch-ek: `feature/`, `fix/`, `docs/` prefix
- Kötelező PR review: legalább 1 reviewer jóváhagyása

**GitHub branch protection beállítás:**
- `main`: require PR, require CI pass, require 1 review
- `develop`: require PR, require CI pass

**Feladat:**
- Állítsd be a branch protection szabályokat a GitHub repóban
- Dokumentáld a branch stratégiát a CONTRIBUTING.md-ben

## 7.6 Közösségi szerepkörök

Az OpenSchool közösségben négy szint van:

| Szerepkör | Hogyan lehet elérni | Jogosultság |
|-----------|---------------------|-------------|
| **Tanuló** | Beiratkozás egy kurzusra | Részvétel, issue nyitás |
| **Kontribútor** | Elfogadott PR (akár 1 is) | "Contributor" címke, Discord rang |
| **Mentor** | 5+ elfogadott PR + aktív code review | Code review jogosultság, mentorálás |
| **Maintainer** | Meghívás a core csapattól | Write access, release, admin |

**Előrelépési útvonal:**
```
Kurzus befejezése → Első PR → Rendszeres kontribúció → Mentor meghívás → Maintainer
```

**Feladat:**
- Dokumentáld a szerepköröket a CONTRIBUTING.md-ben vagy egy külön `COMMUNITY.md`-ben
- Állítsd be a GitHub Teams-et: `contributors`, `mentors`, `maintainers`
- A Discord szerveren legyen megfelelő rang minden szerepkörhöz

## 7.7 Good first issue-k

Az új kontribútoroknak szükségük van belépési pontra.

**Good first issue kritériumok:**
- Jól definiált, kis scope
- Nem igényel mély architektúra ismeretet
- Van hozzá kontextus (melyik fájl, mi a cél)
- A megoldás ellenőrizhető teszttel

**Példák:**
- "Adj hozzá egy `GET /api/courses/{id}/stats` endpoint-ot, ami visszaadja a beiratkozott felhasználók számát"
- "Írd meg a hiányzó teszteket a certificate service-hez"
- "Fordítsd le a hibaüzeneteket magyarra"
- "Adj hozzá `alt` szöveget a frontend képekhez"

**Feladat:**
- Hozz létre legalább 5 `good first issue` címkéjű issue-t
- Minden issue tartalmazza: kontextus, cél, érintett fájlok, elfogadási kritérium
- A README-ben és CONTRIBUTING-ban hivatkozz a `good first issue` szűrőre

## 7.8 Discord integráció

A `openschool-platform` repó eseményei jelenjenek meg a Discord szerveren.

**GitHub → Discord webhook:**
- Csatorna: `#platform-fejlesztes`
- Események: push, PR opened, PR merged, issue opened

**Beállítás:**
1. Discord: Server Settings → Integrations → Webhooks → New Webhook
2. GitHub: Repó Settings → Webhooks → Add webhook → Discord webhook URL

**Feladat:**
- Állítsd be a GitHub → Discord webhook-ot
- Teszteld: nyiss egy issue-t → megjelenik a Discord csatornán

## Háttéranyag

Ezeket nem kell elejétől végig elolvasni — használd referenciaként, amikor az adott témánál tartasz.

| Téma | Link | Miért hasznos |
|------|------|---------------|
| Choose a License | [choosealicense.com](https://choosealicense.com/) | Licenc választás — MIT, Apache 2.0, GPL összehasonlítás |
| GitHub Community docs | [docs.github.com/en/communities](https://docs.github.com/en/communities) | Issue/PR template-ek, Code of Conduct, CONTRIBUTING |
| Conventional Commits | [conventionalcommits.org](https://www.conventionalcommits.org/) | Commit üzenet konvenciók (feat:, fix:, docs:) |
| Semantic Versioning | [semver.org](https://semver.org/) | Verzió számozás: MAJOR.MINOR.PATCH |
| GitHub Branch Protection | [docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-a-branch-protection-rule](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-a-branch-protection-rule) | Branch védelmi szabályok beállítása |
| GitHub Teams | [docs.github.com/en/organizations/organizing-members-into-teams](https://docs.github.com/en/organizations/organizing-members-into-teams) | Közösségi szerepkörök kezelése |

## Verifikációs tesztek

A modul végén futtasd a verifikációs teszteket:

```bash
cd openschool-platform
pytest tesztek/modul-07/ -v
```

**Mit ellenőriznek a tesztek:**

| Tesztfájl | Ellenőrzések |
|-----------|---------------|
| `test_community.py` | LICENSE létezik és nem üres; CONTRIBUTING.md létezik és tartalmaz útmutatót (fork/PR/issue); legalább 2 issue template; PR template létezik; README említi a licencet és a CONTRIBUTING-ot |

> **Megjegyzés:** A közösségi szerepkörök (GitHub Teams, Discord rangok) és a `good first issue`-k manuális ellenőrzést igényelnek — ezeket a tesztek nem tudják automatikusan verifikálni.

## Ellenőrzőlista

- [ ] `LICENSE` fájl a repóban (MIT)
- [ ] `CONTRIBUTING.md` magyar nyelvű útmutatóval
- [ ] Issue template-ek: bug report + feature request
- [ ] PR template ellenőrzőlistával
- [ ] Branch protection: main + develop védett
- [ ] Közösségi szerepkörök dokumentálva
- [ ] Legalább 5 `good first issue` nyitva
- [ ] Discord webhook működik (GitHub → Discord)
- [ ] `pytest tesztek/modul-07/ -v` → minden zöld (verifikációs tesztek)
