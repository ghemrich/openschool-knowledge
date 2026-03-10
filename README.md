# DevSchool

Oktatási keretrendszer, amely az iskolai programozástanulást a valódi fejlesztői munkafolyamatokra építi — Git, CI/CD, aszinkron kommunikáció és automatikus tesztelés az első naptól.

**Operációs rendszer:** Windows 10+, Linux, macOS

---

## Miért jó ez a projekt?

### A probléma

A programozásoktatás gyakran iskolai platformokra épül: a diák feltölt egy fájlt, a tanár kézzel javít, a visszajelzés napokkal később érkezik. A diák nem találkozik verziókezeléssel, automatikus tesztekkel vagy aszinkron kommunikációs csatornákkal — azokkal az eszközökkel, amelyeket az első munkanapján használnia kell majd. Az iskola megtanítja a nyelvet, de nem a szakmát.

A tanár oldalán ugyanez tükröződik: félévente kézzel épít fel repókat, kézzel javít, kézzel összesít. Az ismétlődő adminisztráció elnyeli azt az időt, amit kódátnézésre, egyéni mentorálásra és valódi visszajelzésre kellene fordítani.

### A megoldás

A diákok nem iskolai platformon dolgoznak, hanem **ugyanazokkal az eszközökkel, amelyeket a szakmában is használnak**:

| Iskolai verzió | Ipari megfelelő | Mit tanul a diák? |
|----------------|-----------------|-------------------|
| GitHub repóba pushol | Fejlesztő commitol és pushol | Verziókezelés, commitolási kultúra, kódtörténet |
| GitHub Actions futtatja a teszteket | CI pipeline ellenőriz minden PR-t | Automatikus tesztelés, zöld build = kész |
| Discord szálakban kérdez | Slack/Discord csatornákon kommunikál a csapat | Aszinkron kommunikáció, kérdésfeltevés, segítségkérés |
| VS Code + terminál | Ipari fejlesztőkörnyezet | Szerkesztő, CLI, git parancsok |
| Docker + PostgreSQL (13. évf.) | Konténerizált fejlesztés | Reprodukálható környezet, adatbáziskezelés |
| pytest / shell tesztek | Unit és integrációs tesztek | Tesztvezérelt gondolkodás |

A cél nem az, hogy a diák egy feladatbeadó rendszert tanuljon meg használni, hanem hogy **a munkafolyamat maga legyen a tananyag része**. Amikor a diák commitol, pushol, olvassa a teszt kimenetét és Discord-on kérdez — már fejlesztőként dolgozik.

### Alapelvek

| Elv | Megvalósítás |
|-----|-------------|
| **Valódi eszközök, nem iskolai pótlékok** | GitHub (nem Google Classroom), Discord (nem Kréta üzenet), VS Code (nem online editor), Docker (nem szimulált környezet). |
| **Gyakorlat az elmélet előtt** | Max 15 perc elmélet, utána live coding. A programozás kézműves szakma — kézzel kell írni, nem slideokon nézni. |
| **A vizsga nem meglepetés** | Minden házi feladat egy vizsgafeladat-típust gyakoroltat. A félév végére a diák már 10× megcsinálta, amit a vizsgán kérünk. |
| **CI mint visszajelzés** | Az automatikus tesztek nem büntetnek — azonnal megmutatják, mi működik és mi nem. A diák megtanulja olvasni a teszt kimenetet, ahogy egy fejlesztő a CI logot. |
| **A git történet számít** | A tanár nem csak a végeredményt nézi, hanem a commitokat: mikor dolgozott, hogyan építette fel, mennyit írt egyszerre. Ez fejleszti a folyamatos, iteratív munkastílust. |
| **Növekedési szemlélet** | A házi feladat visszajelzés, nem büntetés. A fejlődés számít, nem a hibátlanság. |

### Mi hiányzik még?

A projekt jelenleg az **egyéni munkát** fedi le. Egy valódi fejlesztői környezethez még közelebb vinné:

| Hiányzó elem | Ipari megfelelő |
|-------------|-----------------|
| Pull Request alapú beadás | Kód review, branch-elés, merge |
| GitHub Issues használata | Feladat- és hibakezelés |
| Közös repón dolgozás (csapatmunka) | Együttműködés, konfliktuskezelés |
| Éles szerverre deploy | CI/CD pipeline VPS-re |
| Projekt board (GitHub Projects) | Kanban, sprint tervezés |
| Dokumentáció írás (README, docstring) | Fejlesztői dokumentáció |

### Kinek való?

Programozástanároknak, akik:
- GitHub Classroom-ot használnak (vagy szeretnének)
- szeretnék automatizálni az ismétlődő adminisztrációt
- magyar nyelvű, kulturálisan illeszkedő anyagokat keresnek
- egy jól strukturált kiindulópontot akarnak, amit a saját igényeikre szabhatnak

---

## Kurzusok

| Kurzus | Évfolyam | Időtartam | Nyelv / Keretrendszer | Vizsga |
|--------|----------|-----------|----------------------|--------|
| [Python alapok](kurzusok/python/10/) | 10. (nappali) | 13 hét, heti 2 óra | Python 3.10+ | 40 pont, 90 perc |
| [Backend FastAPI](kurzusok/python/13/) | 13. (esti / felnőtt) | 25 hét, heti 6 óra | Python + FastAPI | 60 pont, 240 perc |

## Projekt szerkezet

```
├── kurzusok/                # Kurzus-specifikus tartalom
│   └── python/
│       ├── 10/              #   Python alapok (13 hét)
│       └── 13/              #   Backend FastAPI (25 hét)
├── kozos/                   # Kurzusokon átívelő közös dokumentáció
│   ├── discord-szerver-utmutato.md
│   └── integralt-munkafolyamat.md
├── sablonok/                # Új kurzus létrehozásához sablonok
├── eszkozok/                # Szkriptek, segédeszközök
│   ├── github-setup.sh      #   Template repók létrehozása (bash)
│   ├── github-setup.ps1     #   Template repók létrehozása (PowerShell)
│   ├── discord-webhook.py   #   Discord értesítések küldése
│   └── jegy-szamolo.py      #   Félév végi jegy kiszámítása
└── adatok/                  # Tanulói adatok – .gitignore-olt
    └── {év}/{kurzus}/classroom/
```

### Kurzus mappastruktúra

Minden kurzus azonos mappastruktúrát követ:

```
kurzusok/python/{évfolyam}/
├── doksik/                  # Dokumentáció
│   ├── diakok/              #   Leckék + feladatok
│   ├── tanar/               #   Tanári útmutató, értékelés
│   └── tanterv/             #   Tanterv
├── vizsgak/                 # Vizsgavariánsok (feladatlap, megoldás, értékelés)
└── github-classroom/        # GitHub Classroom template repók
```

## Közös dokumentáció

Kurzusokon átívelő dokumentumok: → [kozos/](kozos/)

- **[Discord szerver útmutató](kozos/discord-szerver-utmutato.md)** — szerver beállítás, csatornák, webhook-ok, moderáció
- **[Integrált munkafolyamat](kozos/integralt-munkafolyamat.md)** — félév eleji beállítástól a jegyek kiszámításáig, lépésről lépésre

## Eszközök

A tanári munkát automatizáló szkriptek: → [eszkozok/](eszkozok/)

| Eszköz | Leírás |
|--------|--------|
| `github-setup.sh` / `.ps1` | Template repók létrehozása egy GitHub Organization alatt |
| `discord-webhook.py` | Bejelentések, emlékeztetők és szálnyitók küldése Discord csatornákra |
| `jegy-szamolo.py` | Házi feladatok összesítése és végső jegy kiszámítása |

## Értékelés

Mindkét kurzus GitHub Classroom-on keresztül működik: a diákok hetente pusholják a megoldásaikat, az automatikus tesztek (pytest / shell) azonnal pontoznak.

| Komponens | Python 10 | Backend 13 |
|-----------|-----------|------------|
| Házi feladatok | 25% | 20% |
| Órai munka | 15% | 15% |
| Próbavizsga | 10% | 15% |
| Vizsga | 50% | 50% |

A félév végi jegyek a `jegy-szamolo.py` szkripttel számíthatók ki a GitHub Classroom CSV exportokból (lásd [integrált munkafolyamat](kozos/integralt-munkafolyamat.md)).
