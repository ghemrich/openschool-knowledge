# Feladatok – 17. hét: Fájlkezelés és képfeltöltés

> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz
> A megoldásokat commitold és pushold a GitHub repódba.

---

### 17.1 – Fájl feltöltés ⭐
Készíts `POST /feltoltes` végpontot, amely fogad egy fájlt és visszaadja a nevét, méretét és típusát.

### 17.2 – Fájl mentés ⭐⭐
Módosítsd a végpontot: mentsd el a fájlt az `uploads/` mappába egyedi névvel (uuid). Add vissza az új fájlnevet.

### 17.3 – Validáció ⭐⭐
Adj hozzá fájltípus (csak JPEG, PNG) és méret (max 5 MB) validációt. Hibás fájlnál adj 400-as hibát részletes üzenettel.

### 17.4 – StaticFiles ⭐⭐
Mountolj `StaticFiles`-t az `uploads/` mappára. Teszteld, hogy a feltöltött képek elérhetők URL-en keresztül.

### 17.5 – Kép + Modell ⭐⭐⭐
Adj `kep_url` mezőt egy meglévő modellhez. Készíts `POST /termekek/{id}/kep` végpontot, amely feltölti a képet és elmenti az URL-t az adatbázisba. Írj tesztet a feltöltésre.
