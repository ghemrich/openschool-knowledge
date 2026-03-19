# Kiegészítő gyakorlatok – 5. hét: Listák

> Ezek a feladatok a heti házi feladat melletti **extra gyakorlást** szolgálják.
> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz

---

### 5.1 – Osztálynévsor ⭐
Hozz létre egy listát 8 névvel! Írd ki a listát ABC sorrendben, majd fordított ABC sorrendben. Írd ki a lista hosszát is.

### 5.2 – Lista másolás ⭐
Adott a lista: `[10, 20, 30, 40, 50, 60, 70, 80]`. Készíts belőle:
- Egy másolatot az első 3 elemmel (szeletelés)
- Egy másolatot az utolsó 3 elemmel
- Egy másolatot minden második elemmel

### 5.3 – Tombola ⭐⭐
Hozz létre egy listát a számokkal 1-től 30-ig! Keverd össze véletlenszerűen (`random.shuffle()`), majd húzd ki az első 5 elemet. Írd ki a kihúzott számokat növekvő sorrendben.

### 5.4 – Szavazás ⭐⭐
Készíts programot, ahol 3 jelölt nevét tárold egy listában. Kérj be szavazatokat (a jelölt neve), amíg „vége" nem jön. Tartsd nyilván egy másik listában a szavazatokat. A végén írd ki, ki hány szavazatot kapott, és ki nyert.

### 5.5 – Lista összehasonlítás ⭐⭐
Hozz létre két listát számokkal! Írd ki:
- A közös elemeket (metszet)
- Az elemeket, amelyek csak az elsőben vannak
- Az elemeket, amelyek csak a másodikban vannak
- Az összes elemet egyszer (unió)

Ne használj `set()`-et, oldd meg ciklusokkal!

### 5.6 – Mátrix szorzás ⭐⭐⭐
Hozz létre egy 3×3-as mátrixot (lista listájaként) és egy 3 elemű vektort (listát). Számold ki a mátrix-vektor szorzatát ciklussal! Írd ki az eredményt.

> Tipp: `eredmeny[i] = sum(matrix[i][j] * vektor[j] for j in range(3))`
