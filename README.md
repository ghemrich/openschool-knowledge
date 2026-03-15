# OpenSchool

Nyílt forráskódú, magyar nyelvű programozásoktatási tudásbázis, amely a valódi fejlesztői munkafolyamatokra építi a tanulást — Git, CI/CD, csapatkommunikáció és automatikus tesztelés az első naptól.

**Nyelv:** magyar | **Licenc:** [MIT](LICENSE) (kód) + [CC BY-SA 4.0](LICENSE-CC-BY-SA) (tartalom) | **Platform:** [openschool-platform](https://github.com/ghemrich/openschool-platform)

---

## Miért jó ez a projekt?

A programozásoktatás gyakran iskolai platformokra épül: a diák feltölt egy fájlt, a tanár kézzel javít, a visszajelzés napokkal később érkezik. A tanuló nem találkozik verziókezeléssel, automatikus tesztekkel vagy fejlesztői kommunikációs csatornákkal — azokkal az eszközökkel, amelyeket az első munkanapján használnia kell majd.

Az OpenSchool megközelítése: **a munkafolyamat maga legyen a tananyag része**.

| Amit a tanuló csinál | Ipari megfelelő |
|----------------------|-----------------|
| GitHub repóba pushol | Verziókezelés, commitolási kultúra |
| GitHub Actions futtatja a teszteket | CI pipeline, automatikus tesztelés |
| Discord szálakban kérdez | Csapatkommunikáció |
| VS Code + terminál | Ipari fejlesztőkörnyezet |
| Docker + PostgreSQL | Konténerizált fejlesztés |
| pytest / shell tesztek | Tesztvezérelt gondolkodás |

### Alapelvek

| Elv | Megvalósítás |
|-----|-------------|
| **Valódi eszközök** | GitHub, Discord, VS Code, Docker — nem iskolai pótlékok |
| **Gyakorlat az elmélet előtt** | Rövid elméleti bevezető, utána azonnal gyakorlati feladatok |
| **CI mint visszajelzés** | Az automatikus tesztek azonnal megmutatják, mi működik |
| **A git történet számít** | A commitok mutatják a fejlődést, nem csak a végeredmény |

### Kinek való?

- **Mentoroknak:** magyar nyelvű, strukturált, GitHub Classroom-ra épülő kurzusanyagok
- **Tanulóknak:** leckék, feladatok, vizsgaminták — valódi fejlesztői környezetben
- **Önálló tanulóknak:** teljes tananyag a Python alapoktól a backend fejlesztésig

---

## Kurzusok

| Kurzus | Időtartam | Technológia | Leírás |
|--------|-----------|-------------|--------|
| [Python alapok](courses/python-alapok/) | 13 hét, heti 2 óra | Python 3.10+ | Változók, ciklusok, függvények, fájlkezelés, adatfeldolgozás |
| [HTML & CSS alapok](courses/html-css-alapok/) | 13 hét, heti 2 óra | HTML5 + CSS3 | Dokumentum szerkezet, szemantikus HTML, CSS box model, Flexbox, reszponzív dizájn |
| [Backend FastAPI](courses/python-backend/) | 25 hét, heti 6 óra | Python + FastAPI + PostgreSQL | REST API, autentikáció, tesztelés, Docker, CI/CD |
| [Projekt Labor](courses/projekt-labor/) | 7 modul, egyéni tempó | FastAPI + Docker + Astro | Az OpenSchool platform felépítése nulláról élesig |

A **Projekt Labor** nem hagyományos kurzus: a résztvevő az OpenSchool platform kódját építi fel az alapoktól — a végeredmény egy működő, open source webalkalmazás.

## Projekt szerkezet

```
├── courses/                     # Kurzusok
│   ├── python-alapok/           #   Python alapok (13 hét)
│   ├── html-css-alapok/         #   HTML & CSS alapok (13 hét)
│   ├── python-backend/          #   Backend FastAPI (25 hét)
│   └── projekt-labor/           #   Projekt Labor (7 modul)
├── guides/                      # Kurzusokon átívelő útmutatók
│   ├── kezdo-utmutato.md       #   Hogyan kezdj hozzá?
│   ├── kornyezet-beallitas.md   #   Fejlesztői környezet telepítése
│   ├── kozossegi-utmutato.md    #   Közösség, Discord, viselkedési kódex
│   ├── github-classroom-tanulo-utmutato.md  # Feladatok beadása
│   ├── mentor-utmutato.md       #   Mentorálás, kód-átnézés
│   ├── kurzus-keszitesi-utmutato.md  # Új kurzus készítése
│   ├── hibaelharitas.md         #   Gyakori problémák és megoldások
│   ├── szotar.md                #   Technikai fogalmak szótára
│   ├── git-puskalap.md          #   Git parancsok gyors referencia
│   ├── docker-puskalap.md       #   Docker parancsok gyors referencia
│   ├── discord-szerver-utmutato.md
│   ├── integralt-munkafolyamat.md
│   └── open-source-projekt-utmutato.md
├── tools/                       # Automatizálási szkriptek
│   ├── github-setup.sh / .ps1  #   Template repók létrehozása
│   └── discord-webhook.py      #   Discord értesítések
├── CONTRIBUTING.md
├── CHANGELOG.md                 # Változásnapló
├── LICENSE                      # MIT (kód)
└── LICENSE-CC-BY-SA             # CC BY-SA 4.0 (tartalom)
```

## Útmutatók

Kurzusokon átívelő dokumentumok: → [guides/](guides/)

### Első lépések
- **[Kezdő útmutató — Hogyan kezdj hozzá?](guides/kezdo-utmutato.md)** — tanulási útvonal, kurzus előfeltételek, hol kezdd
- **[Környezet beállítás](guides/kornyezet-beallitas.md)** — Python, Git, VS Code, Docker telepítés minden operációs rendszeren
- **[Közösségi útmutató](guides/kozossegi-utmutato.md)** — Discord csatornák, szerepkörök, viselkedési kódex, hogyan kérdezz jól

### Tanulóknak
- **[GitHub Classroom — Tanuló útmutató](guides/github-classroom-tanulo-utmutato.md)** — feladat elfogadás, tesztek értelmezése, munkafolyamat
- **[Hibaelhárítás és GYIK](guides/hibaelharitas.md)** — gyakori problémák és megoldásaik kurzusonként
- **[Hogyan keress dokumentációt?](guides/dokumentacio-kereses.md)** — önálló tanulás, hibaüzenet-olvasás, hatékony keresés
- **[Szótár](guides/szotar.md)** — technikai fogalmak magyar magyarázattal

### Gyors referenciák
- **[Git puskalap](guides/git-puskalap.md)** — leggyakoribb Git parancsok
- **[Docker puskalap](guides/docker-puskalap.md)** — Docker és Docker Compose parancsok

### Mentoroknak és közreműködőknek
- **[Mentor útmutató](guides/mentor-utmutato.md)** — mentorálás, kód-átnézés, visszajelzés
- **[Kurzus készítési útmutató](guides/kurzus-keszitesi-utmutato.md)** — mappastruktúra, elnevezési konvenciók, autograding
- **[Discord szerver útmutató](guides/discord-szerver-utmutato.md)** — szerver beállítás, csatornák, webhook-ok, moderáció
- **[Integrált munkafolyamat](guides/integralt-munkafolyamat.md)** — félév eleji beállítástól a félév végéig, lépésről lépésre
- **[Open source projekt útmutató](guides/open-source-projekt-utmutato.md)** — nyílt forráskódú projekt felépítése

## Eszközök

Automatizálási szkriptek: → [tools/](tools/)

| Eszköz | Leírás |
|--------|--------|
| `github-setup.sh` / `.ps1` | Template repók létrehozása egy GitHub Organization alatt |
| `discord-webhook.py` | Bejelentések, emlékeztetők és szálnyitók küldése Discord csatornákra |

## Kapcsolódó projekt

Az **[OpenSchool Platform](https://github.com/ghemrich/openschool-platform)** a webalkalmazás, amely erre a tudásbázisra épül: kurzusok böngészése, haladáskövetés GitHub Classroom integrációval, tanúsítvány kiállítás.

## Közreműködés

Szívesen fogadunk hozzájárulásokat! Lásd a [CONTRIBUTING.md](CONTRIBUTING.md) fájlt a részletekért.
