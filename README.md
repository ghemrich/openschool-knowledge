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
| [Python alapok](courses/python-alapok/) | 13 hét | Python 3.10+ | Változók, ciklusok, függvények, fájlkezelés, adatfeldolgozás |
| [Backend FastAPI](courses/python-backend/) | 25 hét | Python + FastAPI + PostgreSQL | REST API, autentikáció, tesztelés, Docker, CI/CD |

## Projekt szerkezet

```
├── courses/                     # Kurzusok
│   ├── python-alapok/           #   Python alapok (13 hét)
│   └── python-backend/          #   Backend FastAPI (25 hét)
├── tools/                       # Automatizálási szkriptek
│   ├── github-setup.sh / .ps1  #   Template repók létrehozása
│   ├── github-update.sh / .ps1 #   Template repók frissítése
│   └── discord-webhook.py      #   Discord értesítések
├── CONTRIBUTING.md
├── CHANGELOG.md                 # Változásnapló
├── LICENSE                      # MIT (kód)
└── LICENSE-CC-BY-SA             # CC BY-SA 4.0 (tartalom)
```

## Eszközök

Automatizálási szkriptek: → [tools/](tools/)

| Eszköz | Leírás |
|--------|--------|
| `github-setup.sh` / `.ps1` | Template repók létrehozása egy GitHub Organization alatt |
| `github-update.sh` / `.ps1` | Template repók frissítése |
| `discord-webhook.py` | Bejelentések, emlékeztetők és szálnyitók küldése Discord csatornákra |

## Kapcsolódó projekt

Az **[OpenSchool Platform](https://github.com/ghemrich/openschool-platform)** a webalkalmazás, amely erre a tudásbázisra épül: kurzusok böngészése, haladáskövetés GitHub Classroom integrációval, tanúsítvány kiállítás.

## Közreműködés

Szívesen fogadunk hozzájárulásokat! Lásd a [CONTRIBUTING.md](CONTRIBUTING.md) fájlt a részletekért.
