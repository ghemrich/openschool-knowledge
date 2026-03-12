# Discord – Tanuló útmutató

Ez a dokumentum elmagyarázza, hogyan csatlakozz a kurzusok közös Discord szerveréhez és hogyan használd hatékonyan.

---

## 1. Csatlakozás

### 1.1 Discord fiók létrehozása

1. Nyisd meg: [discord.com](https://discord.com)
2. Kattints: **Register** (vagy töltsd le az asztali/mobil alkalmazást)
3. Add meg az e-mail címedet, felhasználóneved és jelszavad
4. Erősítsd meg az e-mail címedet
5. Állíts be egy felismerhető becenevet a szerveren (lásd lent)

> **Ajánlott:** Használj felismerhető becenevet (nickname) a szerveren, hogy a többiek könnyen beazonosíthassanak. A Discord felhasználóneved bármi lehet, de a szerver-becenév legyen informatív.
>
> Beállítás: Kattints a szerver nevére (bal felső sarok) → **Edit Server Profile** → **Nickname** mezőbe írd be a választott neved.

### 1.2 Csatlakozás a szerverhez

1. Kattints a mentortól kapott meghívó linkre
2. Fogadd el a meghívást
3. Olvasd el a `#szabályzat` csatornát

---

## 2. Csatornák áttekintése

A szerver több kurzust szolgál ki. A Python Alapok kurzushoz ezeket a csatornákat használd:

| Csatorna | Mire való |
|----------|-----------|
| `#szabályzat` | Szerver szabályok – olvasd el először! |
| `#közlemények` | Mentori bejelentések – csak olvasható (🐍 jelöli a Python Alapok híreket) |
| `#hasznos-linkek` | W3Schools, Python dokumentáció, egyéb segédanyagok |
| `#python-alapok-általános` | Kurzussal kapcsolatos kérdések, beszélgetés |
| `#python-alapok-segítség` | Feladatokkal kapcsolatos kérdések és hibakeresés |
| `#python-alapok-megoldások` | Saját megoldások, kódrészletek megosztása |
| `#általános` | Szabadtéma, kurzusokon átívelő beszélgetés |
| `🔊 konzultáció` | Hangcsatorna – konzultációs időpontokban |

### Heti szálak

A `#python-alapok-segítség` csatornán a mentor minden héten nyit egy **szálat** (Thread) az aktuális témához, évszámmal jelölve (pl. *„2026 – 3. hét – Feltételes elágazások"*). Kérdezz az adott hét szálában, hogy átlátható maradjon a beszélgetés.

> **Megjegyzés:** Régebbi évek szálai is láthatók lehetnek a csatornán. Mindig az aktuális év szálait használd.

---

## 3. Kód küldése Discordon

### Egysoros kód

Használj **backtick**-eket (\`):

```
`print("Hello")`
```

Eredmény: `print("Hello")`

### Többsoros kód

Használj **három backtick**-et és írd oda, hogy `python`:

````
```python
nev = input("Neved: ")
print(f"Szia, {nev}!")
```
````

Eredmény:
```python
nev = input("Neved: ")
print(f"Szia, {nev}!")
```

> **Mindig használj kódblokkot!** Formázatlan kód nehezen olvasható és nehezebb segíteni.

---

## 4. Hogyan kérj segítséget hatékonyan

### ✅ Jó kérdés

> A 3. heti feladatnál az `if-elif` nem működik. Ezt írtam:
> ```python
> szam = input("Szám: ")
> if szam > 10:
>     print("nagy")
> ```
> A hiba: `TypeError: '>' not supported between instances of 'str' and 'int'`
> Mit rontok el?

### ❌ Rossz kérdés

> „Nem működik a kód, segítsetek"

### Tippek a jó kérdéshez

1. **Melyik feladat?** – Írd le, melyik hét és melyik feladat
2. **Mit próbáltál?** – Másold be a kódot (kódblokkban!)
3. **Mi történt?** – Másold be a hibaüzenetet (ha van)
4. **Mit vártál?** – Írd le, mit kellett volna csinálnia a kódnak

---

## 5. Szerver szabályok

1. **Felismerhető név** – Használj felismerhető becenevet (nickname), hogy a többiek könnyen beazonosíthassanak.
2. **Légy tisztelettudató** – Mindenki tanul, senkit nem szabad kigúnyolni kérdés miatt
3. **Használj kódblokkot** – Formázd a kódot (lásd 3. fejezet)
4. **Ne oszd meg a teljes megoldást** – Segíts, de ne csináld meg helyette
5. **Megfelelő csatornán írj** – Python Alapok kérdés → `#python-alapok-segítség`, ne az `#általános`-on
6. **Használd a szálakat** – Kérdezz az aktuális hét szálában
7. **Nincs spam** – Ne küldj felesleges üzeneteket vagy emotikonokat tömegesen
8. **Privát üzenetek** – Kérdéseket inkább a nyilvános csatornákon tedd fel, mások is tanulhatnak belőle

---

## 6. Értesítések beállítása

Ha túl sok értesítést kapsz:

1. Kattints a szerver nevére (bal felső sarok)
2. **Notification Settings**
3. Válaszd: **Only @mentions** – így csak akkor kapsz értesítést, ha valaki megjelöl
4. Opcionális: Egyes csatornáknál jobb klikk → **Mute Channel**, ha nem érdekel

---

## 7. Gyakori kérdések

| Kérdés | Válasz |
|--------|--------|
| Miért nem tudok írni a `#közlemények`-be? | Ez szándékos – ott csak a mentor ír |
| Hogyan oszthatok meg képernyőképet? | Húzd be a képet a chat mezőbe, vagy Ctrl+V |
| Lehet mobilon használni? | Igen, töltsd le a Discord alkalmazást |
| Mi az a szál (Thread)? | Egy üzenet alatti albeszélgetés – kattints a 💬 ikonra |
| Látom a másik kurzus csatornáit? | Csak ha a mentor engedélyezte – ha nem látod, ez normális |
| Hol kérdezzek? | Az aktuális év + hét szálában a `#python-alapok-segítség` csatornán |
| Látom régi évek szálait is? | Igen, ez normális – te mindig az aktuális éves szálakba írj |
