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

A szerver több kurzust szolgál ki. A Backend FastAPI kurzushoz ezeket a csatornákat használd:

| Csatorna | Mire való |
|----------|-----------|
| `#szabályzat` | Szerver szabályok – olvasd el először! |
| `#közlemények` | Tanári bejelentések – csak olvasható (⚡ jelöli a Backend FastAPI híreket) |
| `#hasznos-linkek` | FastAPI, SQLAlchemy, Docker dokumentáció, egyéb segédanyagok |
| `#backend-általános` | Kurzussal kapcsolatos kérdések, beszélgetés |
| `#backend-segítség` | Feladatokkal kapcsolatos kérdések és hibakeresés |
| `#backend-megoldások` | Kód review, megoldások megosztása |
| `#általános` | Szabadtéma, kurzusokon átívelő beszélgetés |
| `🔊 konzultáció` | Hangcsatorna – konzultációs időpontokban |

### Heti szálak

A `#backend-segítség` csatornán a tanár minden héten nyit egy **szálat** (Thread) az aktuális témához, évszámmal jelölve (pl. *„2026 – 7. hét – Docker és PostgreSQL"*). Kérdezz az adott hét szálában, hogy átlátható maradjon a beszélgetés.

> **Megjegyzés:** Régebbi évek szálai is láthatók lehetnek a csatornán. Mindig az aktuális év szálait használd.

---

## 3. Kód küldése Discordon

### Egysoros kód

Használj **backtick**-eket (\`):

```
`response.status_code`
```

Eredmény: `response.status_code`

### Többsoros kód

Használj **három backtick**-et és írd oda a nyelvet:

````
```python
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
```
````

Eredmény:
```python
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
```

Más nyelvekhez:
- ` ```bash ` – terminál parancsok
- ` ```sql ` – SQL lekérdezések
- ` ```json ` – JSON válaszok
- ` ```yaml ` – Docker Compose, GitHub Actions fájlok
- ` ```dockerfile ` – Dockerfile

> **Mindig használj kódblokkot!** Formázatlan kód nehezen olvasható és nehezebb segíteni.

---

## 4. Hogyan kérj segítséget hatékonyan

### ✅ Jó kérdés

> A 7. heti feladatnál a Docker container nem indul el. A `docker-compose.yml`-em:
> ```yaml
> services:
>   db:
>     image: postgres:16
>     environment:
>       POSTGRES_PASSWORD: secret
> ```
> A hiba:
> ```
> ERROR: connection refused to localhost:5432
> ```
> A FastAPI app-ban `localhost`-ot használok. Mit rontok el?

### ❌ Rossz kérdés

> „Nem indul a Docker, segítsetek"

### Tippek a jó kérdéshez

1. **Melyik feladat?** – Írd le, melyik hét és melyik feladat
2. **Mit próbáltál?** – Másold be a kódot (kódblokkban!)
3. **Mi történt?** – Másold be a hibaüzenetet / stack trace-t
4. **Mit vártál?** – Írd le, mit kellett volna csinálnia
5. **Környezet** – Ha releváns: OS, Python verzió, Docker verzió

---

## 5. Szerver szabályok

1. **Felismerhető név** – Használj felismerhető becenevet (nickname), hogy a többiek könnyen beazonosíthassanak.
2. **Légy tisztelettudató** – Mindenki tanul, senkit nem szabad kigúnyolni kérdés miatt
3. **Használj kódblokkot** – Formázd a kódot (lásd 3. fejezet)
4. **Ne oszd meg a teljes megoldást** – Segíts, de ne csináld meg helyette (különösen házi feladatnál)
5. **Megfelelő csatornán írj** – Backend FastAPI kérdés → `#backend-segítség`
6. **Használd a szálakat** – Kérdezz az aktuális hét szálában
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
| Hol kérdezzek? | Az aktuális év + hét szálában a `#backend-segítség` csatornán |
| Látom régi évek szálait is? | Igen, ez normális – te mindig az aktuális éves szálakba írj |
| Mikor van konzultáció? | A `#közlemények` csatornán hirdeti meg a tanár |
