# Lecke 18 – Background Tasks és WebSocket

> **Dokumentáció:** [FastAPI Background Tasks](https://fastapi.tiangolo.com/tutorial/background-tasks/) · [WebSockets](https://fastapi.tiangolo.com/advanced/websockets/)

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

---

## 111–112. óra: WebSocket alapok

### Mi a WebSocket?

A HTTP egyirányú: kliens kérdez, szerver válaszol. A WebSocket **kétirányú**: a szerver is küldhet üzeneteket a kliensnek bármikor.

```
HTTP:      Kliens → Szerver → Kliens (egy kérés-válasz)
WebSocket: Kliens ↔ Szerver (folyamatos kapcsolat)
```

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

### Tesztelés böngészőből

```javascript
// Böngésző konzolban
const ws = new WebSocket("ws://localhost:8000/ws");
ws.onmessage = (event) => console.log(event.data);
ws.send("Helló szerver!");
```

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

### WebSocket tesztelése

```python
def test_websocket(client):
    with client.websocket_connect("/ws") as ws:
        ws.send_text("Helló")
        data = ws.receive_text()
        assert "Helló" in data
```

---

## Gyakorlat

1. Adj háttérfeladatot egy meglévő végponthoz (naplózás vagy email)
2. Készíts egy egyszerű WebSocket echo végpontot
3. Készíts egy chat szobát a `ConnectionManager` mintával
4. Teszteld a WebSocket-et böngészőből és pytest-ből
5. Commitold és pushold
