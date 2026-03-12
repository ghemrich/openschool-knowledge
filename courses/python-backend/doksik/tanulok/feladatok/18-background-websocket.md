# Feladatok – 18. hét: Background Tasks és WebSocket

> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz
> A megoldásokat commitold és pushold a GitHub repódba.

---

### 18.1 – Naplózó háttérfeladat ⭐
Adj `BackgroundTasks`-ot egy végponthoz, amely háttérben fájlba írja: `"{időbélyeg} - {method} {path}"`.

### 18.2 – Email szimuláció ⭐⭐
Készíts "email küldő" háttérfeladatot a regisztrációhoz. A függvény `time.sleep(2)`-vel szimulál lassú műveletet. Mérd, hogy a válasz azonnal megérkezik.

### 18.3 – WebSocket echo ⭐⭐
Készíts WebSocket végpontot (`/ws`), amely visszaküldi a kapott üzenetet "Echo: " prefixszel. Teszteld a Swagger UI-ban vagy böngészőből.

### 18.4 – WebSocket teszt ⭐⭐
Írj pytest tesztet a WebSocket végpontra `client.websocket_connect()` használatával.

### 18.5 – Chat szoba ⭐⭐⭐
Készíts `ConnectionManager` osztályt és `/ws/chat` végpontot. Több kliens tud csatlakozni, és az üzeneteket mindenki megkapja (broadcast). Teszteld két böngésző fülön.
