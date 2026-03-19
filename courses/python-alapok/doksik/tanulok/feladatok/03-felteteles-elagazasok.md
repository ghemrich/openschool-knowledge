# Kiegészítő gyakorlatok – 3. hét: Feltételes elágazások

> Ezek a feladatok a heti házi feladat melletti **extra gyakorlást** szolgálják.
> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz

---

### 3.1 – Páros vagy páratlan ⭐
Kérj be egy egész számot! Írd ki, hogy páros vagy páratlan. Ha a szám 0, írd ki külön: „A nulla speciális eset!"

### 3.2 – Évszak meghatározó ⭐
Kérd be a hónap számát (1–12)! Írd ki, melyik évszakot jelenti:
- 12, 1, 2: Tél
- 3, 4, 5: Tavasz
- 6, 7, 8: Nyár
- 9, 10, 11: Ősz
- Egyéb: „Érvénytelen hónap!"

### 3.3 – Kalória számláló ⭐⭐
Kérd be a felhasználó nemét (férfi/nő), életkorát, súlyát (kg) és magasságát (cm). Számold ki az alap kalóriaszükségletét a Harris-Benedict képlettel:
- Férfi: 88.36 + (13.4 × súly) + (4.8 × magasság) − (5.7 × kor)
- Nő: 447.6 + (9.2 × súly) + (3.1 × magasság) − (4.3 × kor)

Írd ki az eredményt egész számra kerekítve.

### 3.4 – Másodfokú egyenlet ⭐⭐
Kérd be az `a`, `b`, `c` együtthatókat! Számold ki a diszkriminánst (D = b² − 4ac). Írd ki:
- Ha D > 0: két valós gyök
- Ha D = 0: egy valós gyök (kettős gyök)
- Ha D < 0: nincs valós gyök

> Tipp: gyökvonáshoz `d ** 0.5`

### 3.5 – Zsebpénz beosztó ⭐⭐
Kérd be a havi zsebpénz összegét és a hónap napjainak számát! Számold ki a napi keretet. Kérd be egy napi kiadást, és írd ki:
- Ha a kiadás a napi keret alatt van: „Okosan költesz! Marad [összeg] Ft-od mára."
- Ha pont annyi: „Pont elköltötted a mai keretedet."
- Ha több: „Túllépted a napi keretedet [összeg] Ft-tal!"

### 3.6 – Jegyautomata ⭐⭐⭐
Kérd be az utazás típusát (helyi/távolsági), az utas kategóriáját (gyerek/felnőtt/nyugdíjas), és hogy van-e bérlete (igen/nem). Árak:
- Helyi: felnőtt 350 Ft, gyerek 200 Ft, nyugdíjas ingyenes
- Távolsági: felnőtt 1500 Ft, gyerek 750 Ft, nyugdíjas 500 Ft
- Bérlettel mindenhol 50% kedvezmény
- A végeredményt kerekítsd egész számra

Írd ki a jegy adatait és a fizetendő összeget.
