# Kiegészítő gyakorlatok – 7. hét: Random modul és játéklogika

> Ezek a feladatok a heti házi feladat melletti **extra gyakorlást** szolgálják.
> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz

---

### 7.1 – Érmedobás ⭐
Írj programot, amely szimulál 100 érmedobást (fej/írás). Írd ki, hányszor lett fej és hányszor írás. Melyik lett több?

### 7.2 – Véletlenszerű jelszó ⭐
Generálj egy 12 karakteres véletlenszerű jelszót, amely tartalmaz kisbetűket, nagybetűket és számokat. Írd ki a jelszót.

> Tipp: `random.choice()` egy listából véletlenszerűen választ.

### 7.3 – Blackjack (egyszerűsített) ⭐⭐
Készíts egy egyszerű Blackjack játékot:
- A gép kioszt neked 2 véletlenszerű kártyát (2–11 közötti számok)
- Kiírja az összegüket
- Megkérdezi: „Kérsz még lapot? (i/n)"
- Ha az összeg meghaladja a 21-et: „Bust! Vesztettél."
- Ha a játékos megáll: a gép is húz lapokat (amíg 17 alatt van)
- Aki közelebb van a 21-hez (túllépés nélkül), nyer

### 7.4 – Véletlenszerű kvíz ⭐⭐
Hozz létre egy listát legalább 8 kérdés-válasz párral (szótárak listája). A program véletlenszerűen kiválaszt 5 kérdést és felteszi sorban. A végén írd ki a pontszámot.

### 7.5 – Szómester ⭐⭐⭐
Készíts szókitaláló (akasztófa-szerű) játékot:
- A program véletlenszerűen választ egy szót egy listából
- Kiírja a szót aláhúzásokkal (pl. „_ _ _ _ _")
- A játékos betűket tippel
- Ha eltalálja, a betű megjelenik a helyén
- Maximum 6 rossz tipp engedélyezett
- Tartsd nyilván a már tippelt betűket

### 7.6 – Torpedó ⭐⭐⭐
Készíts egyszerű torpedó játékot:
- 5×5-ös pálya (lista listájaként)
- A gép véletlenszerűen elhelyez 3 darab egymezős hajót
- A játékos koordinátákat ad meg (sor, oszlop)
- Találat esetén „X", mellélövés esetén „O" jelenik meg
- A pályát minden körben kirajzolod
- A játék addig tart, amíg az összes hajót el nem süllyeszti
