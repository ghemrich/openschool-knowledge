# 5. hét – Response modellek és hibakezelés

> **Határidő:** a következő óra előtt
> **Beadás:** commitold és pushold a megoldásaidat ebbe a repóba!
> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz

---

Ezen a héten megtanulod, hogyan készíts tisztán definiált API válaszokat és hogyan kezeld a hibákat. A response modellek biztosítják, hogy az API mindig a várt formátumban válaszoljon, a hibakezelés pedig érthető visszajelzést ad a kliensnek.

---

## 5.1 – Response model ⭐
A `models.py` fájlban módosítsd a `Termek` modellt: adj hozzá egy `titkos_kod: str` mezőt. Készíts egy külön `TermekResponse` modellt, ami ugyanazokat a mezőket tartalmazza, **kivéve** a `titkos_kod`-ot. A végpontoknál használd `response_model=TermekResponse`-ként – így az API válaszban nem jelenik meg a titkos kód.

## 5.2 – Status kódok ⭐
Állítsd be a helyes HTTP status kódokat a végpontokon: `POST` → `201 Created`, `DELETE` → `200 OK`, `GET` nem létező elemre → `404 Not Found`. A `status_code` paramétert a végpont dekorátorában adhatod meg (pl. `@app.post("/termekek", status_code=201)`).

## 5.3 – HTTPException ⭐⭐
Készíts `GET /felhasznalok/{id}` végpontot, ami:
- `404`-et ad vissza, ha a felhasználó nem létezik
- `403`-at ad vissza, ha `id == 0` (admin felhasználó, nem elérhető)
- Mindkét esetben részletes `detail` üzenettel (pl. `"Felhasználó nem található: {id}"`)

## 5.4 – Egyedi kivétel ⭐⭐
Hozz létre egy saját `NemTalalhatoError(Exception)` kivétel osztályt, és regisztrálj hozzá egyedi kezelőt az `@app.exception_handler(NemTalalhatoError)` dekorátorral. A válasz formátuma: `{"hiba": true, "uzenet": "..."}`. Használd ezt a kivételt a végpontjaidban `raise NemTalalhatoError("...")` módon.

## 5.5 – Hibakód gyűjtemény ⭐⭐⭐
Készíts API-t, ami 5 különböző HTTP hibakódot ad vissza: `400 Bad Request`, `401 Unauthorized`, `403 Forbidden`, `404 Not Found`, `422 Unprocessable Entity`. Dokumentáld a végpontokat a `responses` paraméterrel, hogy a Swagger UI-ban megjelenjenek a lehetséges hibaválaszok.

---

## Dokumentáció

- [Response Model](https://fastapi.tiangolo.com/tutorial/response-model/)
- [HTTPException](https://fastapi.tiangolo.com/tutorial/handling-errors/)
- [Status Codes](https://fastapi.tiangolo.com/tutorial/response-status-code/)

## 📚 Kapcsolódó anyagok

Az ehhez a héthez tartozó elméleti anyagot és további gyakorlófeladatokat itt találod:

- 📖 [Lecke: Response és hibakezelés](../../doksik/tanulok/leckek/05-response-hibak.md)
- 📝 [Gyakorlófeladatok: Response és hibakezelés](../../doksik/tanulok/feladatok/05-response-hibak.md)

## Beadás

1. `main.py` + `models.py` legyen a repóban
2. Commitolj értelmes üzenetekkel
3. `git push` – ez a beadás!
