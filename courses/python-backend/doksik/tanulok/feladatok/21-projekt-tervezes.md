# Kiegészítő gyakorlatok – 21. hét: Projekt tervezés

> Ezek a feladatok a heti házi feladat melletti **extra gyakorlást** szolgálják.
> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz

---

### 21.1 – Alternatív téma kidolgozás ⭐
Gondolj ki egy 5. projektötletet (nem Todo, Blog, Webshop, Recept). Írj róla 3-5 mondatos leírást: mi a célja, kinek szól, milyen fő funkciói vannak.

### 21.2 – ER diagram ⭐⭐
Rajzolj ER diagramot a választott projektedhez (legalább 4 tábla). Jelöld:
- Primáris kulcsokat
- ForeignKey kapcsolatokat (és irányukat)
- Many-to-many kapcsolatokat (asszociációs táblával)

Használhatsz Mermaid, dbdiagram.io vagy papírt.

### 21.3 – User story-k ⭐⭐
Írj legalább 8 user story-t a projektedhez:
- Példa: "Mint vendeg, szeretnék regisztrálni, hogy hozzáférjek a funkciókhoz."
- Csoportosítsd prioritás szerint: MVP (kötelező), Nice-to-have, Jövőbeli

### 21.4 – Technikai döntések dokumentálása ⭐⭐
Készíts `docs/ARCHITECTURE.md` fájlt:
- Milyen csomagokat használsz és miért? (pl. passlib vs argon2, alembic vs raw SQL)
- Milyen a mappa struktúra és miért?
- Hogyan kezeled a konfigurációt?
- Milyen tesztelési stratégiát követsz?

### 21.5 – Kanban tábla ⭐⭐⭐
Hozz létre GitHub Projects-ben (vagy `docs/KANBAN.md`-ben) Kanban táblát:
- Oszlopok: Backlog, In Progress, Review, Done
- Legalább 15 feladat (ticket), mindegyik 1-3 órás munka
- Prioritás címkék: P0 (blocker), P1 (fontos), P2 (nice-to-have)
- Becslés: S, M, L méret
