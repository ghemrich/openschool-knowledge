# Közreműködés

Köszönjük, hogy hozzá szeretnél járulni az OpenSchool tudásbázishoz! Ez az útmutató segít az első lépésekben.

## Hogyan segíthetsz?

- **Hibák javítása** — elírások, hibás kódrészletek, elavult linkek
- **Tartalom bővítése** — új leckék, feladatok, magyarázatok
- **Fordítás** — a tartalom jelenleg magyar nyelvű, de szívesen fogadunk fordításokat
- **Visszajelzés** — nyiss egy Issue-t, ha valami nem egyértelmű vagy hiányzik

## Lépések

1. **Forkold** a repót
2. Hozz létre egy **feature branch**-et: `git checkout -b javitas/rovid-leiras`
3. Végezd el a módosításokat
4. **Commitolj** beszédes üzenettel: `git commit -m "docs: elírás javítás a het03 leckében"`
5. **Pushold** a branch-edet: `git push origin javitas/rovid-leiras`
6. Nyiss egy **Pull Request**-et

## Commit üzenet formátum

```
<típus>: <rövid leírás>

Típusok:
  docs     — dokumentáció, lecke, feladat módosítás
  fix      — hiba javítás (kód vagy tartalom)
  feat     — új tartalom (lecke, feladat, kurzus)
  chore    — karbantartás (CI, config, szerkezet)
```

## Tartalmi irányelvek

- **Nyelv:** magyar (a kódpéldákban az angol változónevek elfogadottak)
- **Stílus:** közérthető, gyakorlatias, tömör
- **Kódpéldák:** működő, tesztelhető kódrészletek
- **Nehézségi szintek:** használd a ⭐ jelölést (⭐ könnyű, ⭐⭐ közepes, ⭐⭐⭐ haladó)

## Struktúra

```
courses/
├── python-alapok/       # Python alapok kurzus
└── python-backend/      # Backend FastAPI kurzus
tools/                   # Automatizálási szkriptek
```

## Licenc

A hozzájárulásoddal elfogadod, hogy a munkád a projekt licencelése szerint kerül közzétételre:
- **Oktatási tartalom** (leckék, feladatok, útmutatók): [CC BY-SA 4.0](LICENSE-CC-BY-SA)
- **Kód** (szkriptek, tesztek, konfigurációk): [MIT](LICENSE)

## Kérdéseid vannak?

Nyiss egy Issue-t a GitHub repóban, és szívesen segítünk!
