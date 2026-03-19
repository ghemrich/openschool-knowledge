# Kiegészítő gyakorlatok – 24. hét: Vizsga

> Ezek a feladatok a vizsgára való **extra felkészülést** szolgálják.
> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz

---

### 24.1 – Sprint protótípus ⭐⭐
Gyakorold: építs új API-t egy eddig nem használt témával (pl. rendezvénykezelő, álláskereső, szavazó rendszer). Pydantic modell + in-memory CRUD + 5 végpont. Célidő: 20 perc.

### 24.2 – Hibakereső kihvís ⭐⭐
Az alábbi kódrészletek mindegyikében van 1-2 hiba. Keresd meg:
1. `db.query(User).filter(User.id == id).first()` – mi a probléma, ha `id` str típusú?
2. `return db.query(Item).all()` egy async végpontban – miért problémás?
3. `pwd_context.hash(password)` a response modellben – mi a biztonsági kockázat?
4. `token = jwt.encode({"sub": email})` – mi hiányzik?
5. `@app.on_event("startup")` – miért deprecated?

### 24.3 – Elméleti kérdések ⭐⭐
Válaszolj röviden (2-3 mondat):
1. Miért használunk Alembic-et a `create_all()` helyett?
2. Mi a különbség az unit és integrációs teszt között?
3. Mi a CORS és miért fontos?
4. Miért ne tároljunk jelszót plain textben?
5. Mi az előnye a Docker-nek lokális fejlesztésnél?

### 24.4 – Időnyomás gyakorlat ⭐⭐⭐
Készíts teljes API-t 90 perc alatt:
- Téma: Könyvtár kezelő (könyvek, tagok, kölcsönzések)
- Követelmények: SQLAlchemy + Alembic, auth, CRUD, 5 teszt
- Bónusz: Docker Compose

Mérd az időt stopperrel. Vizsgán hasonló tempra lesz szükség.

### 24.5 – Vizsgaszimuláció ⭐⭐⭐
Végezz teljes vizsgaszimulációt:
- Nincs internet (zárd be a dokumentációs oldalakat)
- Csak a salát jegyzeteidet használhatod
- 240 perc: teljes API + DB + Auth + tesztek + Docker
- Ha elkészültél, értékeld: melyik rész ment nehezen? Mit kell még gyakorolni?
