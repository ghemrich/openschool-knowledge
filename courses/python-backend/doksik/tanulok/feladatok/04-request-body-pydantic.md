# Kiegészítő gyakorlatok – 4. hét: Request body és Pydantic

> Ezek a feladatok a heti házi feladat melletti **extra gyakorlást** szolgálják.
> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz

---

### 4.1 – Kapcsolatfelvételi űrlap ⭐
Hozz létre `Kapcsolat` Pydantic modellt (nev: str, email: str, targy: str, uzenet: str). Készíts `POST /kapcsolat` végpontot. Validáld: név min 2 karakter, email `@` jelet tartalmaz, üzenet min 10 karakter.

### 4.2 – Validator gyakorlás ⭐
Készíts `Felhasznalo` modellt a következő field_validator-okkal:
- `email`: kisbetűsre alakítja, tartalmaz `@`-ot
- `felhasznalonev`: csak betű és szám, min 3 karakter
- `szuletesi_ev`: 1900 és aktuális év között

### 4.3 – Recept API ⭐⭐
Készíts in-memory CRUD API-t `Recept` modellel:
- Recept: nev, elkeszitesi_ido_perc, nehezseg (Enum), hozzavalok: list[Hozzavalo]
- Hozzavalo: nev, mennyiseg, mertekegyseg
- Végpontok: listázás, létrehozás, lekérés, törlés
- Az id-t a szerver generálja (UUID vagy sorszám)

### 4.4 – model_validator ⭐⭐
Készíts `Foglalás` modellt (nev, kezdes: datetime, befejezes: datetime, vendegek_szama: int). `model_validator`-ral ellenőrizd, hogy `befejezes > kezdes` és a foglalás max 7 napos. Ha nem, dobj `ValueError`-t.

### 4.5 – Verzionált API ⭐⭐⭐
Készíts API-t, ahol a `Cikk` (cim, tartalom, szerzo, cimkek: list[str]) modellnek két verziója van:
- `CikkCreateV1`: cim, tartalom (egyszerű)
- `CikkCreateV2`: cim, tartalom, szerzo, cimkek, kivonat (bővített)

Készíts `POST /v1/cikkek` és `POST /v2/cikkek` végpontokat. A háttértárolás egységes, de a `v1` hiányzó mezőket alapértékekkel tölti ki.
