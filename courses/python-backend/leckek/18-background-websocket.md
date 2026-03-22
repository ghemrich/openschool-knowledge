# 📘 Lecke 18 – Background Tasks és WebSocket

> 📚 Dokumentáció:
> https://fastapi.tiangolo.com/tutorial/background-tasks/
> https://fastapi.tiangolo.com/advanced/websockets/

---

## 109–110. óra: Háttérfeladatok

### Mi a Background Task?

Olyan feladat, amit a válasz elküldése **után** hajt végre a szerver. Tipikus felhasználás:
- Email küldés
- Naplózás
- Értesítés generálás

### Alapvető használat

```python
from fastapi import BackgroundTasks

def log_mentes(uzenet: str):
    """Háttérben futó naplózó."""
    with open("app.log", "a") as f:
        f.write(f"{uzenet}\n")

@router.post("/items", status_code=201)
def create_item(
    item: schemas.ItemCreate,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    db_item = crud.create_item(db, item, user.id)
    background_tasks.add_task(log_mentes, f"Item létrehozva: {db_item.id}")
    return db_item
```

### 🧠 Részletes Magyarázat

- **`BackgroundTasks`** – FastAPI beépített osztály háttérfeladatok kezelésére. A végpont paraméterlistájába írjuk, és a FastAPI automatikusan injektálja (mint a `Depends()`).
- **`add_task(függvény, *args)`** – Regisztrál egy háttérfeladatot. Az első paraméter a függvény (nem hívás: `log_mentes`, nem `log_mentes()`!), a többi a függvény paraméterei.
- **Sorrend:** (1) `db_item` létrejön, (2) a válasz (`return db_item`) **azonnal** visszamegy a kliensnek, (3) a `log_mentes` **utána** fut le a háttérben. A kliens nem vár a naplózásra.
- **Mikor használjuk?** – Bármikor, amikor egy művelet az ügyfelet nem érdekli, de a szervernek fontos: email, log, push notification, statisztika.

### Email küldés háttérben (szimulált)

```python
def email_kuldes(cimzett: str, targy: str, szoveg: str):
    """Valós projektben SMTP-t használnánk."""
    import time
    time.sleep(2)  # szimuláció: lassú művelet
    print(f"Email elküldve: {cimzett} - {targy}")

@router.post("/auth/regisztracio", status_code=201)
def regisztracio(
    user: schemas.FelhasznaloCreate,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db)
):
    db_user = crud.create_user(db, user)
    background_tasks.add_task(
        email_kuldes,
        db_user.email,
        "Üdvözlünk!",
        f"Kedves {db_user.nev}, sikeres regisztráció!"
    )
    return db_user
```

### 🧠 Részletes Magyarázat

- **`time.sleep(2)`** – Szimulálja a lassú email küldést. Éles projektben itt SMTP hívás lenne (pl. `smtplib` vagy `sendgrid`). A lényeg: ez a 2 másodperc **nem lassítja** a regisztrációs választ. A kliens azonnal megkapja a 201-et.
- **Több `add_task` is lehetséges** – Egy végpontban többször is hívható: `add_task(email_kuldes, ...)` + `add_task(log_mentes, ...)`. Mindkét feladat a háttérben fut, sorrendben.
- **Hibakezelés** – Ha a háttérfeladat hibázik, a kliens **nem** kap hibaüzenetet (a válasz már elment). A hibát logolni kell a szerveren. Éles rendszerben érdemes try-except blokkot tenni a háttérfüggvénybe.

---

## 111–112. óra: WebSocket alapok

### Mi a WebSocket?

A HTTP egyirányú: kliens kérdez, szerver válaszol. A WebSocket **kétirányú**: a szerver is küldhet üzeneteket a kliensnek bármikor.

```
HTTP:      Kliens → Szerver → Kliens (egy kérés-válasz)
WebSocket: Kliens ↔ Szerver (folyamatos kapcsolat)
```

### 🧠 Részletes Magyarázat

- **HTTP** – Minden kommunikáció a **kliens** kezdeményezi. A szerver nem tud üzenetet küldeni, amíg nem kérdezik. Ha a kliens „valós idejű" frissítést akar, folyton kérdeznie kell (polling).
- **WebSocket** – Egyszer felépül a kapcsolat (handshake), utána **mindkét irány** nyitva marad. A szerver bármikor küldhet üzenetet. Nincs új HTTP kérés, a kapcsolat folyamatos.
- **Használati esetek** – Chat alkalmazás, valós idejű értesítések, játékok, tőzsdei adatok, kollaboratív szerkesztés.

### Egyszerű WebSocket végpont

```python
from fastapi import WebSocket, WebSocketDisconnect

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"Üzenet fogadva: {data}")
    except WebSocketDisconnect:
        print("Kliens lecsatlakozott")
```

### 🧠 Részletes Magyarázat

- **`@app.websocket("/ws")`** – WebSocket végpontot definiál (nem `@app.get()`!). A kliens `ws://localhost:8000/ws` URL-en csatlakozik.
- **`await websocket.accept()`** – Elfogadja a kapcsolatot. Ez a „handshake" – nélküle a kliens nem tud üzenetet küldeni.
- **`while True` ciklus** – A WebSocket kapcsolat folyamatos: addig fut, amíg valamelyik fél bontja. A `receive_text()` a kliens következő üzenetére vár (blokkoló, de async).
- **`WebSocketDisconnect`** – Kivétel, ami akkor keletkezik, ha a kliens bontja a kapcsolatot (bezárja a böngészőt, elveszti az internetet). A `try...except` elkapja és takarít.
- **Echo minta** – Ez az „echo server": amit a kliens küld, azt visszaküldi. Az alap, amire bármilyen WebSocket logikát építhetsz.

### Tesztelés böngészőből

```javascript
// Böngésző konzolban
const ws = new WebSocket("ws://localhost:8000/ws");
ws.onmessage = (event) => console.log(event.data);
ws.send("Helló szerver!");
```

### 🧠 Részletes Magyarázat

- **`new WebSocket("ws://...")`** – A böngésző beépített WebSocket API-jával kapcsolódik. Az `ws://` protokoll HTTP felett fut, az `wss://` a HTTPS-es változat.
- **`ws.onmessage`** – Eseménykezelő: minden szerveri üzenetnél meghívódik. Az `event.data` a szerver által küldött szöveg.
- **`ws.send()`** – Üzenetet küld a szervernek. Nincs kérés/válasz struktúra – egyszerűen küld egy stringet.

### Broadcast: üzenet mindenkinek

```python
class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)

manager = ConnectionManager()

@app.websocket("/ws/chat")
async def chat(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(f"Valaki írta: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
```

### 🧠 Részletes Magyarázat

- **`ConnectionManager`** – Osztály, ami nyilvántartja az összes aktív WebSocket kapcsolatot. Ez a „chat szoba" logika magja.
- **`active_connections`** – Lista, ami az összes csatlakozott WebSocket-et tárolja. Új klienskor `append`, távozáskor `remove`.
- **`broadcast()`** – Végigiterál az összes aktív kapcsolaton és mindenkinek elküldi az üzenetet. Ha 10 kliens csatlakozik, mindenki megkapja, amit bárki ír.
- **Globális `manager`** – A modul szintű változó az alkalmazás életciklusa alatt él. Minden WebSocket végpont ugyanazt a `manager`-t használja.
- **Skálázhatóság korlát** – Ez a minta egyetlen szerver-processzen belül működik. Több worker (gunicorn) vagy több szerver esetén Redis pub/sub kell a szinkronizációhoz.

---

## 113–114. óra: Tesztelés és gyakorlat

### Background Task tesztelése

```python
def test_background_task_nem_blokkol(client, auth_headers):
    """A válasz azonnal megérkezik, a háttérfeladat nem lassítja."""
    import time
    start = time.time()
    response = client.post("/items", json={
        "nev": "Gyors item", "ar": 100
    }, headers=auth_headers)
    duration = time.time() - start

    assert response.status_code == 201
    assert duration < 1.0  # nem kell email küldésre várni
```

### 🧠 Részletes Magyarázat

- **Időmérés** – A `time.time()` hívás előtt és után megjegyezzük az időt. Ha a válasz 1 másodpercnél gyorsabban jön (a háttérfeladat 2 másodperc), az bizonyítja, hogy nem blokkol.
- **`assert duration < 1.0`** – A háttérfeladat szimulált email küldése 2 másodperc. Ha a válasz kevesebb mint 1 másodperc alatt érkezik, a kliens nem várt az emailre.
- **Megjegyzés** – A TestClient alapértelmezetten szinkron, és a háttérfeladatokat a válasz előtt futtathatja. Éles szervernél a teszt mindig <1 sec.

### WebSocket tesztelése

```python
def test_websocket(client):
    with client.websocket_connect("/ws") as ws:
        ws.send_text("Helló")
        data = ws.receive_text()
        assert "Helló" in data
```

### 🧠 Részletes Magyarázat

- **`client.websocket_connect("/ws")`** – A TestClient WebSocket kapcsolatot is tud nyitni. A `with` blokk automatikusan bontja a kapcsolatot.
- **`ws.send_text()` → `ws.receive_text()`** – Küld egy üzenetet, majd vár a szerver válaszára. Az echo szerver esetén a válasz tartalmazza az elküldött szöveget.
- **`assert "Helló" in data`** – Nem pontos egyezést ellenőrzünk, mert a szerver „Üzenet fogadva: Helló" formátumban válaszol. Az `in` operátor részstring keresést végez.

---

## Gyakorlat

1. Adj háttérfeladatot egy meglévő végponthoz (naplózás vagy email)
2. Készíts egy egyszerű WebSocket echo végpontot
3. Készíts egy chat szobát a `ConnectionManager` mintával
4. Teszteld a WebSocket-et böngészőből és pytest-ből
5. Commitold és pushold
