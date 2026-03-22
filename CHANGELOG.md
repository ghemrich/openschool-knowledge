# Változásnapló (Changelog)

Az OpenSchool tudásbázis főbb változásainak nyomon követése.

A formátum a [Keep a Changelog](https://keepachangelog.com/hu/1.0.0/) ajánlásán alapul.

---

## [Kiadatlan]

### Módosítva
- **Dokumentáció szinkronizálás** — README.md, CONTRIBUTING.md, tools/README.md frissítése a tényleges repószerkezethez: nem létező kurzusok (html-css-alapok, projekt-labor), guides/ mappa és hivatkozásaik eltávolítva, hiányzó github-update szkriptek hozzáadva

## [0.5.0] – 2025-03-12

### Hozzáadva
- **11 új útmutató** a `guides/` mappában (`bd70d13`):
  - Kezdő útmutató, Környezet beállítás, Közösségi útmutató
  - GitHub Classroom tanuló útmutató, Mentor útmutató, Kurzus készítési útmutató
  - Hibaelhárítás és GYIK, Szótár, Git puskalap, Docker puskalap
  - Változásnapló
- **Dokumentáció-keresési útmutató** (`guides/dokumentacio-kereses.md`) — önálló tanulás, hibaüzenet-olvasás (`58365f0`)
- **Projekt Labor mentori dokumentáció** (`courses/projekt-labor/doksik/mentor/`) — mentori útmutató, értékelési módszertan (`552b125`)
- **Link-ellenőrző CI workflow** (`.github/workflows/link-check.yml`) — belső markdown linkek automatikus ellenőrzése (`552b125`)

### Módosítva
- **Közösségi nyelvezet** — diák → tanuló, tanár → mentor átnevezés mappákban, fájlnevekben és tartalomban, 49 fájl (`8a79e87`)
- **Jegyrendszer eltávolítása** — 1-5 osztályzatok helyett szintalapú értékelés: Kiváló/Haladó/Megfelelő/Kezdő/Nem teljesített, 12 fájl (`e46e382`)
- **Repó migráció** — `test-org-hfig/testing` → `ghemrich/openschool-knowledge` hivatkozások frissítése (`3d1a1a9`)
- **Dokumentáció redundanciák megszüntetése** — ismétlődő tartalom eltávolítása, közös útmutatókra hivatkozás (`491d3a4`)
- **Backend GitHub Classroom útmutató** kibővítése önálló leírássá (`4d9fba2`)

### Javítva
- **GitHub Classroom tesztek** — `fetch-depth: 0` hozzáadása 10 classroom.yml fájlhoz, commit-számláló tesztek javítása (`33fcdb0`)

## [0.4.0] – 2025-01-20

### Módosítva
- Valódi név követelmény eltávolítva — felismerhető becenév ajánlás (`85fd549`)
- 5 fájl frissítve: discord-hasznalat.md, github-classroom-utmutato.md fájlok

## [0.3.0] – 2025-01-20

### Módosítva
- Intézményi hivatkozások eltávolítása — iskolarendszertől független tartalom (`d01d4ad`)
- Esti tagozat, felnőttképzés, nappali tagozat hivatkozások eltávolítva
- Szervezet nevek: `iskola-` → `openschool-`
- Évfolyam → Szint, tanóra → foglalkozás átnevezés
- 9 fájl frissítve

## [0.2.0] – 2025-01-20

### Módosítva
- Évfolyam-specifikus hivatkozások eltávolítása (`3e8bfb6`)
- Python 10 → Python Alapok, Backend 13 → Backend FastAPI átnevezés
- Discord azonosítók, csatornák, környezeti változók egységesítve
- 37 fájl frissítve

## [0.1.0] – 2025-01-19

### Hozzáadva
- Repó átszervezése OpenSchool nyílt forráskódú tudásbázisként (`a501c76`)
- Tartalom konzisztencia javítások (`101841c`)
- Régi útvonalak és placeholder URL-ek frissítése (`fd8c72d`)

### Korábbi változások
- Projekt labor kurzus hozzáadása (`51721a8`)
- Backend FastAPI kurzus hozzáadása (`c4240a3`)
- Repó inicializálás és alapstruktúra (`ccbe990`)
