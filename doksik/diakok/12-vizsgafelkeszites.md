# 12. hét – Vizsgafelkészítés

> **Dokumentáció:** [W3Schools – Python referencia](https://www.w3schools.com/python/python_reference.asp)

## 23. óra: Próbavizsga

Oldd meg az alábbi feladatokat önállóan, 90 perc alatt!

A vizsgát a **GitHub Classroom**-on kapod: a tanárod megadja a meghívó linket.

### Vizsga menete:
1. Fogadd el a GitHub Classroom feladatot (a kapott linken)
2. Klónozd le a repot: `git clone <link>`
3. A repóban már ott van a forrásfájl (`filmek.txt` vagy `konyvek.txt`) és a feladatleírás
4. Dolgozz, és rendszeresen commitolj!
5. Az utolsó `git push` a beadás

### Szabályok:
- Internet használható
- Saját jegyzet használható
- 90 perc áll rendelkezésre
- Feladatonként külön fájl (`feladat1.py`, `feladat2.py`, `feladat3.py`, `fgv.py`)
- Rendszeresen commitolj és pusholj (ne csak a végén)!

---

## 24. óra: Próbavizsga megbeszélése

### Tipikus hibák és megoldásuk

**1. feladat – gyakori hibák:**
- Elfelejtett `.lower()` → a nevek nagybetűsek maradnak
- Az `input()` eredményét nem tároljuk változóban
- Hiányzó függvényekre bontás

**2. feladat – gyakori hibák:**
- `random` modul importálásának hiánya
- Érvénytelen tartomány nem ellenőrzött (pl. 0 vagy 40 is elfogadott)
- A `while` feltétel nem megfelelő → végtelen ciklus vagy nem ismétlődik
- Tippek számolójának inicializálása hiányzik

**3. feladat – gyakori hibák:**
- Fájl kódolás hiánya → ékezetes karakterek problémája
- `.strip()` hiánya → sorvégi `\n` marad az adatban
- Típuskonverzió (`int()`, `float()`) elfelejtése
- A modul (`fgv.py`) nincs ugyanabban a mappában
- `fgv.` előtag hiánya a függvényhívásoknál

### Pontozási tippek

| Feladat | Max pont | Minimum az elégségeshez |
|---------|----------|------------------------|
| 1. feladat | 8 | 4 |
| 2. feladat | 14 | 7 |
| 3. feladat | 18 | 9 |
| **Összesen** | **40** | **20 (50%)** |

### Ellenőrző lista a vizsgához

**Python:**
- [ ] Minden feladatot külön fájlba írtam
- [ ] A függvények definiálva vannak és meg is hívom őket
- [ ] A `random` modult importáltam
- [ ] A fájl megnyitásnál `encoding="utf-8"` szerepel
- [ ] Minden `.split()` előtt `.strip()` van
- [ ] A számokat `int()`-tel vagy `float()`-tal konvertáltam
- [ ] A `fgv.py` modult létrehoztam és importáltam
- [ ] A program lefut hiba nélkül

**Git:**
- [ ] Rendszeresen commitoltam (nem csak a végén)
- [ ] Értelmes commit üzeneteket írtam
- [ ] Az utolsó `git push` megtörtént
- [ ] A GitHubon ellenőriztem, hogy minden fájl feltöltődött
