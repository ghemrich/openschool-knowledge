# Mentor útmutató

Ez az útmutató a mentorok számára készült — azoknak, akik segítik a tanulókat a kurzusok során, kód-átnézést végeznek, és visszajelzést adnak.

---

## Ki lehet mentor?

A mentori szerepkör az OpenSchool közösségen belül a tapasztaltabb tagok számára elérhető:

1. **Legalább egy kurzus sikeres elvégzése** (tanúsítvánnyal)
2. **Aktív közösségi részvétel** — segítőkészség a Discord csatornákon
3. **A mentor útmutató elolvasása** (ez a dokumentum)

> A mentori szerep nem kötelezettség, hanem lehetőség. Ha úgy érzed, hogy tudsz és szeretnél segíteni, jelentkezz a közösségi csatornán.

---

## A mentor szerepe

| Feladat | Leírás |
|---------|--------|
| Segítségnyújtás | Válaszolj a tanulók kérdéseire a Discord csatornákon |
| Kód-átnézés | Nézd át a beadott feladatokat, adj visszajelzést |
| Iránymutatás | Segíts megtalálni a helyes irányt, de ne oldd meg helyettük |
| Motiválás | Bátorítsd a tanulókat, különösen nehezebb heteknél |
| Hibakeresés segítése | Mutasd meg a hibakeresés módszereit, ne csak a megoldást |

---

## Hogyan segíts jól?

### Fő elv: Segíts gondolkodni, ne gondolkodj helyette

```
❌ Rossz: "Írd ezt: for i in range(len(lista)):..."
✅ Jó:   "Milyen ciklussal tudnál végigmenni egy listán? Mi a különbség a for és a while között?"

❌ Rossz: "A hiba az, hogy a 3. sorban print helyett input kell."
✅ Jó:   "Olvasd el a hibaüzenetet — melyik sorra mutat? Mit jelent az 'unexpected EOF'?"
```

### A segítés lépései

1. **Értsd meg a problémát** — kérdezz vissza: „Mit szeretnél, hogy csináljon a kód? Mi történik helyette?"
2. **Irányítsd a figyelmet** — „Nézd meg a hibaüzenet sorszámát" / „Mi az `x` értéke ezen a ponton?"
3. **Adj tippet, ne megoldást** — „Próbáld ki az `int()` függvényt" / „Gondolj a `while` feltételére"
4. **Ha elakad, mutass egy példát** — más kontextusban, ne a pontos megoldást
5. **Ha nagyon elakad, magyarázd el** — de kérd meg, hogy ismételje meg saját szavaival

### Segítés kérés struktúrája (amit elvárj a tanulótól)

Kérd meg a tanulókat, hogy kövessék a [Hogyan kérdezz jól?](kozossegi-utmutato.md#hogyan-kérdezz-jól) útmutatót — ez tartalmazza a kérdésfeltevés struktúráját és a jó példákat.

---

## Kód-átnézés (Code Review)

A kód-átnézés a tanulási folyamat egyik legfontosabb eleme. A cél: **segíteni a tanulót jobb kódot írni**, nem csak értékelni.

### Alapelvek

- **Pozitív visszajelzéssel kezdj** — „Jól van, a függvényre bontás szép, látszik a logika"
- **Kérdésként fogalmazz** — „Mi lenne, ha a felhasználó negatív számot adna meg?" (nem: „Kezeld a negatív számokat!")
- **Egy dolgot emelsz ki** — ne írd felül 10 megjegyzéssel. Fókuszálj a legfontosabb fejlődési pontra.
- **Adj kontextust** — magyarázd meg, *miért* jobb az egyik megoldás (olvashatóság, karbantarthatóság)
- **Dicsérj, ha fejlődés van** — „A múlt héthez képest sokkal szebben bontottad függvényekre!"

### Kurzus-specifikus ellenőrzőlisták

A részletes code review ellenőrzőlistákat a kurzusok értékelési módszertana tartalmazza:

- [Python Alapok — Code review szempontok](../courses/python-alapok/doksik/mentor/ertekeles-modszertan.md#4-mentori-kód-átnézés-code-review)
- [Backend FastAPI — Code review szempontok](../courses/python-backend/doksik/mentor/ertekeles-modszertan.md#4-mentori-kód-átnézés-code-review)

### Visszajelzés formátuma

GitHub-on (Pull Request vagy commit megjegyzés):

```markdown
## 🔍 Kód-átnézés — 3. hét

### ✅ Ami jó
- Szép, olvasható kódstruktúra
- A `while` ciklus logikusan van felépítve

### 💡 Fejlesztési javaslat
- A `szam_ellenorzes()` függvény túl sokat csinál — érdemes lenne szétbontani
  egy input kérő és egy validáló részre. Miért? Mert így könnyebb tesztelni.

### 📝 Megjegyzés
- Jó haladás a múlt héthez képest!
```

---

## Git történet elemzése

A Git history elemzés részletes módszertanát (ellenőrizendő szempontok, piros zászlók, git parancsok) a kurzusok értékelési módszertana tartalmazza:

- [Python Alapok — Git history elemzés](../courses/python-alapok/doksik/mentor/ertekeles-modszertan.md#5-git-history-elemzés)
- [Backend FastAPI — Git history elemzés](../courses/python-backend/doksik/mentor/ertekeles-modszertan.md#5-git-history-elemzés)

Ha gyanús mintát látsz, ne vádolj — kérdezz:
> „Látom, hogy egy commitban jött az egész feladat. Előfordult, hogy nem commitoltál közben, vagy szükséged van-e segítségre a Git munkafolyamatban?"

---

## Szóbeli visszakérdezés

Ha a kód-átnézés során kérdés merül fel, informális szóbeli visszakérdezéssel tisztázhatod. A kurzus-specifikus példakérdéseket és az értékelési hatást a részletes módszertan tartalmazza:

- [Python Alapok — Szóbeli ellenőrzés](../courses/python-alapok/doksik/mentor/ertekeles-modszertan.md#6-szóbeli-ellenőrzés)
- [Backend FastAPI — Szóbeli ellenőrzés](../courses/python-backend/doksik/mentor/ertekeles-modszertan.md#6-szóbeli-ellenőrzés)

### Hogyan reagálj

| Válasz minősége | Reakció |
|----------------|---------|
| Magabiztosan elmagyarázza | Minden rendben |
| Részben érti, bizonytalan | Segíts megérteni — ez tanulási alkalom |
| Nem tudja elmagyarázni a saját kódját | Beszéljétek meg, honnan másolta, és segíts megérteni |

---

## Discord mentori jelenlét

### Hol segíts?

| Csatorna | Mikor válaszolj |
|----------|-----------------|
| `#python-alapok-segítség` | Ha valaki elakadt a Python feladatokkal |
| `#backend-segítség` | Backend kurzus kérdések |
| `#általános` | Általános programozási kérdések |

### Hogyan válaszolj?

- **Használj szálakat (threads)** — ne a fő csatornába írd a hosszú magyarázatot
- **Kódot code blockban** — ` ```python ... ``` `
- **Reagálj emojival** ha láttad de nem tudsz most válaszolni — a tanuló tudja, hogy nem lett figyelmen kívül hagyva
- **Ha nem tudod a választ** — ne tippelj. Mondd, hogy utánanézel, vagy jelezd, hogy más mentor segíthet

### Válaszidő

- Nincs kötelező válaszidő — a mentorálás önkéntes
- Ha rendszeresen elérhető vagy, jelezd a profilodon (pl. „Általában este 18-21 között elérhető")

---

## Tippek

- **Légy türelmes** — ami neked egyszerű, annak a tanulónak az első alkalom
- **Emlékezz, te is tanuló voltál** — a saját tapasztalataid a legjobb tanítóeszköz
- **Kérdezz, mielőtt válaszolsz** — gyakran nem az a kérdés, amit elsőre feltesznek
- **Ne írd át a kódját** — ha muszáj kódot mutatnod, írd más kontextusban
- **Jelezz, ha kiégsz** — tarts szünetet, a közösség megérti

---

**Kapcsolódó útmutatók:**
- [Közösségi útmutató](kozossegi-utmutato.md)
- [GitHub Classroom — Tanuló útmutató](github-classroom-tanulo-utmutato.md)
- [Kezdő útmutató](kezdo-utmutato.md)
