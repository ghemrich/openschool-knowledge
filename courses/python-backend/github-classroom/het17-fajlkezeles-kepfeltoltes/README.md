# 17. hét – Fájlkezelés és képfeltöltés

> **Beadás:** commitold és pushold a megoldásaidat ebbe a repóba!
> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz

---

Ezen a héten megtanulod, hogyan kezelj fájlfeltöltéseket FastAPI-ban. Képfeltöltést valósítasz meg validációval (fájlméret, típus) és a feltöltött képeket termékekhez rendeled.

---

## Feladat

Bővítsd a Termék API-t fájlfeltöltéssel.

### 17.1 – Alap fájlfeltöltés ⭐
Készíts egy `POST /feltoltes` végpontot, ami fogad egy fájlt (`UploadFile` típussal) és visszaadja a fájl nevét és méretét:

```json
{"fajlnev": "pelda.txt", "meret_byte": 1234}
```

### 17.2 – Képfeltöltés validációval ⭐⭐
Készíts egy `POST /feltoltes/kep` végpontot, ami:
- Csak JPEG és PNG fájlokat fogad el (ellenőrizd a MIME típust)
- Maximum 5 MB méretű fájlokat enged (nagyobb fájl → `400 Bad Request`)
- A feltöltött képet az `uploads/` mappába menti
- Ha az `uploads/` mappa nem létezik, hozd létre automatikusan

### 17.3 – Kép hozzárendelése termékhez ⭐⭐⭐
Készíts egy `POST /termekek/{id}/kep` végpontot, ami:
- Feltölti a képet az `uploads/` mappába
- A `Termek` modellben frissíti a `kep_url` mezőt a feltöltött fájl elérési útjával
- Ha a termék nem létezik, `404` választ ad

### 17.4 – Tesztelés ⭐⭐
Írj teszteket a fájlfeltöltéshez. Használd az `io.BytesIO`-t teszt fájlok létrehozásához:

```python
from io import BytesIO
file = BytesIO(b"fake image data")
response = client.post("/feltoltes/kep", files={"file": ("test.jpg", file, "image/jpeg")})
```

---

## Dokumentáció

- [FastAPI File Upload](https://fastapi.tiangolo.com/tutorial/request-files/)
- [StaticFiles](https://fastapi.tiangolo.com/tutorial/static-files/)

## 📚 Kapcsolódó anyagok

Az ehhez a héthez tartozó elméleti anyagot és további gyakorlófeladatokat itt találod:

- 📖 [Lecke: Fájlkezelés és képfeltöltés](https://github.com/ghemrich/openschool-knowledge/blob/master/courses/python-backend/leckek/17-fajlkezeles-kepfeltoltes.md)

## Beadás

1. `app/` csomag + `tests/` mappa legyen a repóban
2. Commitolj értelmes üzenetekkel
3. `git push` – ez a beadás!
