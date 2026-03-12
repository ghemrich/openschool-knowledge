# Discord – Diák útmutató

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

1. Kattints a tanártól kapott meghívó linkre
2. Fogadd el a meghívást
3. Olvasd el a `#szabályzat` csatornát

---

## 2. Csatornák áttekintése

A szerver több kurzust szolgál ki. A Projekt Labor kurzushoz ezeket a csatornákat használd:

| Csatorna | Mire való |
|----------|-----------|
| `#szabályzat` | Szerver szabályok – olvasd el először! |
| `#közlemények` | Tanári bejelentések – csak olvasható (🔧 jelöli a Projekt Labor híreket) |
| `#hasznos-linkek` | Dokumentáció linkek, segédanyagok |
| `#projekt-labor-általános` | Kurzussal kapcsolatos kérdések, beszélgetés |
| `#projekt-labor-segítség` | Fejlesztéssel kapcsolatos kérdések és hibakeresés |
| `#projekt-labor-megoldások` | Megoldások, kódrészletek, tanácsok megosztása |
| `#általános` | Szabadtéma, kurzusokon átívelő beszélgetés |
| `🔊 konzultáció` | Hangcsatorna – konzultációs időpontokban |

### Modul szálak

A `#projekt-labor-segítség` csatornán minden modulhoz van egy **szál** (Thread), pl. *„Modul 1 – Projekt indítás"*, *„Modul 3 – Kurzusok és haladás"*. Kérdezz az adott modul szálában, hogy átlátható maradjon a beszélgetés.

> **Megjegyzés:** Mivel a kurzus önütemezett, több diák lehet egyszerre különböző moduloknál. A szálak segítenek, hogy mindenki a saját moduljának kontextusában kérdezzen.

---

## 3. Kód küldése Discordon

### Egysoros kód

Használj **backtick**-eket (\`):

```
`docker compose up`
```

Eredmény: `docker compose up`

### Többsoros kód

Használj **három backtick**-et és írd oda a nyelvet:

````
```python
@app.get("/health")
def health_check():
    return {"status": "ok"}
```
````

Eredmény:
```python
@app.get("/health")
def health_check():
    return {"status": "ok"}
```

Más nyelvekhez:
- ` ```bash ` – terminál parancsok
- ` ```sql ` – SQL lekérdezések
- ` ```yaml ` – Docker Compose, GitHub Actions fájlok
- ` ```dockerfile ` – Dockerfile
- ` ```astro ` – Astro komponensek (Modul 5-től)

> **Mindig használj kódblokkot!** Formázatlan kód nehezen olvasható és nehezebb segíteni.

---

## 4. Hogyan kérj segítséget hatékonyan

### ✅ Jó kérdés

> A Modul 1-nél a Docker Compose nem indul el. A `docker-compose.yml`-em:
> ```yaml
> services:
>   backend:
>     build: ./backend
>     depends_on:
>       - db
> ```
> A hiba:
> ```
> ERROR: connection refused to localhost:5432
> ```
> A FastAPI app-ban `localhost`-ot használom. Mit rontok el?

### ❌ Rossz kérdés

> „Nem indul a Docker, segítsetek"

### Tippek a jó kérdéshez

1. **Melyik modul?** – Írd le, melyik modulnál tartasz
2. **Mit próbáltál?** – Másold be a kódot (kódblokkban!)
3. **Mi történt?** – Másold be a hibaüzenetet / stack trace-t
4. **Mit vártál?** – Írd le, mit kellett volna csinálnia
5. **Környezet** – Ha releváns: OS, Docker verzió, Python verzió

---

## 5. Szerver szabályok

1. **Felismerhető név** – Használj felismerhető becenevet (nickname), hogy a többiek könnyen beazonosíthassanak.
2. **Légy tisztelettudató** – Mindenki tanul, senkit nem szabad kigúnyolni kérdés miatt
3. **Használj kódblokkot** – Formázd a kódot (lásd 3. fejezet)
4. **Ne oszd meg a teljes megoldást** – Segíts, de ne csináld meg helyette
5. **Megfelelő csatornán írj** – Projekt Labor kérdés → `#projekt-labor-segítség`
6. **Használd a szálakat** – Kérdezz az adott modul szálában
7. **Nincs spam** – Ne küldj felesleges üzeneteket vagy emotikonokat tömegesen
8. **Privát üzenetek** – Kérdéseket inkább a nyilvános csatornákon tedd fel, mások is tanulhatnak belőle
9. **Hibaüzenetek** – A szöveget másold be (ne csak képet küldj), hogy kereshető legyen

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
| Miért nem tudok írni a `#közlemények`-be? | Ez szándékos – ott csak a tanár ír |
| Hogyan oszthatok meg képernyőképet? | Húzd be a képet a chat mezőbe, vagy Ctrl+V |
| Hogyan oszthatok meg hosszú kódot? | Használj szálat (Thread), vagy ha nagyon hosszú, GitHub Gist-et |
| Lehet mobilon használni? | Igen, töltsd le a Discord alkalmazást |
| Mi az a szál (Thread)? | Egy üzenet alatti albeszélgetés – kattints a 💬 ikonra |
| Látom a másik kurzus csatornáit? | Csak ha a tanár engedélyezte – ha nem látod, ez normális |
| Hol kérdezzek? | Az adott modul szálában a `#projekt-labor-segítség` csatornán |
| Mikor van konzultáció? | A `#közlemények` csatornán hirdeti meg a tanár |
| Milyen sorrendben haladjak? | Modul 1-től 7-ig – minden modul az előzőre épít |
