# Kiegészítő gyakorlatok – 2. hét: Bevitel és szövegkezelés

> Ezek a feladatok a heti házi feladat melletti **extra gyakorlást** szolgálják.
> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz

---

### 2.1 – Összadó ⭐
Kérd be két szám értékét a felhasználótól! Számold ki és írd ki az összegüket, különbségüket és szorzatukat. Ne felejtsd el `int()`-re vagy `float()`-ra alakítani a bekért értéket!

### 2.2 – Kör kerülete ⭐
Kérd be egy kör sugarát! Számold ki a kerületét (2 × π × r) és a területét (π × r²). Használj f-stringet és 2 tizedesjegy pontosságot. A π értéke legyen 3.14159.

### 2.3 – Szöveg statisztika ⭐⭐
Kérd be a felhasználótól egy mondatot! Írd ki:
- A mondat hosszát (karakterszám)
- A szavak számát
- A magánhangzók számát (a, e, i, o, u – kis- és nagybetű is)
- A mondatot csupa nagybetűvel és csupa kisbetűvel

### 2.4 – E-mail cím generátor ⭐⭐
Kérd be a felhasználó vezetéknevét, keresztnevét és születési évét! Generálj 3 e-mail cím javaslatot:
1. `keresztnev.vezeteknev@iskola.hu` (kisbetűvel)
2. `vnev_ékezet-nélkül + születési év utolsó 2 számjegye@iskola.hu`
3. `vezeteknev + keresztnév első betűje@iskola.hu`

### 2.5 – Szöveg titkosítás ⭐⭐
Kérd be a felhasználótól egy szöveget! Titkosítsd úgy, hogy minden betűt az ábécében 3 hellyel utána lévőre cserélsz (Caesar-rejtjel). Csak az angol kisbetűkkel kell foglalkoznod. Írd ki az eredeti és a titkosított szöveget.

> Tipp: `ord()` karakterből ASCII számot ad, `chr()` visszaalakít.

### 2.6 – Személyleírás ⭐⭐⭐
Kérd be a következő adatokat: név, magasság (cm), súly (kg), szem színe, haj színe. Számold ki a BMI-t (súly / (magasság_m)²). Írd ki az adatokat formázott „személyleírás" kártya formában, a BMI-t 1 tizedesjegyre kerekítve, és írd mellé, hogy alultáplált (<18.5), normál (18.5–25), túlsúlyos (25–30) vagy elhízott (>30).
