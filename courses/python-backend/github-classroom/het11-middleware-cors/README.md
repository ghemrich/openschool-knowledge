# 11. hét – Middleware és CORS

> **Beadás:** commitold és pushold a megoldásaidat ebbe a repóba!
> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz

---

Ezen a héten megismerkedsz a middleware-ekkel és a CORS (Cross-Origin Resource Sharing) beállítással. A middleware-ek minden kérés előtt/után futnak (pl. naplózás), a CORS pedig lehetővé teszi, hogy más domainről is elérjék az API-dat.

---

## 11.1 – Naplózó middleware ⭐
Készíts middleware-t, amely minden kérésről kiírja: `[GET] /konyvek - 200 (0.015s)`. Adj hozzá a `main.py`-hoz.

## 11.2 – CORS ⭐⭐
Konfiguráld a CORS-t: `http://localhost:3000` és `http://localhost:5173` engedélyezett. Írd le kommentben, miért ne használjunk `allow_origins=["*"]` éles környezetben.

## 11.3 – Request ID ⭐⭐
Készíts middleware-t, amely `X-Request-ID` (uuid4) headert ad minden válaszhoz.

## 11.4 – Lifespan ⭐⭐
Használd a `lifespan` kontextuskezelőt: induláskor írja ki "API elindult", leálláskor "API leállt".

## 11.5 – Teljes main.py ⭐⭐⭐
Készítsd el a végleges `main.py`-t: CORS, naplózó middleware, lifespan, összes router regisztrálva, health endpoint. Minden konfigurálható `.env`-ből.

---

## Dokumentáció

- [Middleware](https://fastapi.tiangolo.com/tutorial/middleware/)
- [CORS](https://fastapi.tiangolo.com/tutorial/cors/)
- [Lifespan](https://fastapi.tiangolo.com/advanced/events/)

## 📚 Kapcsolódó anyagok

Az ehhez a héthez tartozó elméleti anyagot és további gyakorlófeladatokat itt találod:

- 📖 [Lecke: Middleware és CORS](https://github.com/ghemrich/openschool-knowledge/blob/master/courses/python-backend/leckek/11-middleware-cors.md)

## Beadás

1. `main.py` a teljes konfigurációval legyen a repóban
2. Commitolj értelmes üzenetekkel
3. `git push` – ez a beadás!
