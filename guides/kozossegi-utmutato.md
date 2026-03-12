# Közösségi útmutató

Az OpenSchool egy nyílt közösség, ahol tanulhatsz, kérdezhetsz, segíthetsz másoknak, és akár a platform fejlesztésébe is bekapcsolódhatsz.

---

## Csatlakozás

### Discord szerver

A közösség elsődleges kommunikációs felülete a Discord. Itt kérdezhetsz, segíthetsz, és részt vehetsz a beszélgetésekben.

1. Regisztrálj a [discord.com](https://discord.com) oldalon (ha még nincs fiókod)
2. Csatlakozz az OpenSchool Discord szerverhez a meghívó linkkel
3. Állíts be egy felismerhető becenevet (nickname), hogy a többiek könnyen beazonosíthassanak

### GitHub

A tananyag és a platform kódja nyílt forráskódú a GitHubon:
- **Tudásbázis:** [github.com/ghemrich/openschool-knowledge](https://github.com/ghemrich/openschool-knowledge) — kurzusok, leckék, feladatok
- **Platform:** [github.com/ghemrich/openschool-platform](https://github.com/ghemrich/openschool-platform) — webalkalmazás

---

## Discord csatornaszerkezet

| Csatorna | Mire való |
|----------|-----------|
| `#szabályzat` | Szerver szabályok, viselkedési kódex |
| `#közlemények` | Fontos bejelentések |
| `#hasznos-linkek` | Dokumentáció, útmutatók, eszközök |
| `#python-alapok-általános` | Python Alapok kurzussal kapcsolatos beszélgetés |
| `#python-alapok-segítség` | Segítségkérés a heti feladatokhoz |
| `#python-alapok-megoldások` | Megoldások, tippek megosztása |
| `#backend-általános` | Backend FastAPI kurzussal kapcsolatos beszélgetés |
| `#backend-segítség` | Backend feladatokkal kapcsolatos kérdések |
| `#backend-megoldások` | Backend megoldások, kódrészletek |
| `#általános` | Szabadtéma, közösségi beszélgetés |

---

## Közösségi szerepkörök

Az OpenSchool közösségben a szerepkörök a hozzájárulás és a tapasztalat alapján alakulnak:

| Szerepkör | Hogyan érheted el? | Mit csinálhatsz? |
|-----------|-------------------|-------------------|
| **Tanuló** | Regisztrálj az OpenSchool platformon | Kurzusok elvégzése, tanúsítvány igénylése |
| **Közreműködő** | Küldj be egy elfogadott Pull Requestet | Közreműködő címke a profildodon |
| **Mentor** | Tanúsítványok megszerzése + aktív közösségi részvétel | Tanulók segítése, kód-átnézés, visszajelzés |
| **Platform fejlesztő** | „Platform fejlesztés" kurzus elvégzése | Kurzusok létrehozása, platform fejlesztés |

### A mentor út

```
Kurzusok elvégzése → Tanúsítványok megszerzése
        │
        ▼
Aktív közösségi részvétel (segítés, válaszadás)
        │
        ▼
Mentor szerepkör → Tanulók haladásának követése, visszajelzés
        │
        ▼
Platform fejlesztő → Kurzusok írása, platform fejlesztés, code review
```

---

## Viselkedési kódex

1. **Légy tisztelettudó** — mindenki tanul, senkit nem szabad kigúnyolni kérdés miatt
2. **Segíts, de ne csináld meg helyette** — mutasd meg az irányt, ne a teljes megoldást
3. **Formázd a kódot** — használj kódblokkot (lásd: [hogyan formázzak kódot Discordon?](hibaelharitas.md))
4. **Megfelelő csatornán írj** — Python kérdés → `#python-alapok-segítség`, ne az `#általános`-on
5. **Használd a szálakat** — ha egy heti feladathoz kérdezel, válaszolj a hét szálában
6. **Ne oszd meg mások személyes adatait** — tiszteld a magánszférát

---

## Hogyan kérdezz jól?

Egy jó kérdés segít a válaszolóknak gyorsan segíteni:

1. **Írd le, mit próbáltál** — ne csak azt, hogy „nem működik"
2. **Másold be a hibaüzenetet** — a pontos szöveg számít
3. **Mutasd meg a kódot** — kódblokk formátumban (három backtick: ` ``` `)
4. **Mondd el, mit vártál** — mi lett volna a helyes eredmény?

**Példa egy jó kérdésre:**

> A het03 3. feladatnál a `while` ciklus végtelen ciklusba kerül. A kódom:
> ```python
> szam = input("Adj meg egy számot: ")
> while szam != 0:
>     szam = input("Adj meg egy számot: ")
> ```
> A probléma az, hogy hiába írok 0-t, nem áll meg. Mit rontok el?

---

## Hogyan járulj hozzá?

### Tananyag javítás / bővítés

1. Forkold az [openschool-knowledge](https://github.com/ghemrich/openschool-knowledge) repót
2. Hozz létre egy branch-et: `git checkout -b javitas/het03-leckeben-eliras`
3. Végezd el a módosítást
4. Nyiss egy Pull Request-et

### Platform fejlesztés

1. Forkold az [openschool-platform](https://github.com/ghemrich/openschool-platform) repót
2. Nézd meg az Issue-kat — a `good first issue` címke jó kiindulópont
3. Kövesd a [CONTRIBUTING.md](../CONTRIBUTING.md) útmutatót

### Hibák jelzése

Ha hibát találsz (elírás, nem működő kód, hibás link), nyiss egy **Issue**-t a megfelelő repóban.

---

**Következő lépés:** [Kezdő útmutató — Hogyan kezdj hozzá?](kezdo-utmutato.md)
