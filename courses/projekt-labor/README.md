# Projekt Labor

**Az OpenSchool platform felépítése nulláról élesig.**

Gyakorlati kurzus, amelyben egy valódi, működő webalkalmazást építünk — az OpenSchool online tanulási platformot. A kurzus végére a platform fut egy VPS-en, fogad felhasználókat, követi a haladásukat, és tanúsítványt állít ki.

## Előfeltételek

- [Backend FastAPI](../python-backend/) kurzus (vagy azzal egyenértékű tudás)
- Saját VPS + domain (ajánlott, de nem kötelező az első modulokhoz)

## Tech stack

| Technológia | Szerep |
|-------------|--------|
| FastAPI | Backend API |
| PostgreSQL | Adatbázis |
| Alembic | Migrációk |
| Docker Compose | Fejlesztői és éles környezet |
| pytest | Tesztelés |
| Astro | Frontend (statikus oldal generátor) |
| nginx | Reverse proxy |
| GitHub Actions | CI/CD |
| GitHub OAuth | Felhasználói belépés |

## Modulok

| # | Modul | Eredmény |
|---|-------|----------|
| 1 | [Projekt indítás](doksik/modulok/01-projekt-inditas.md) | Teljesen konfigurált, futó, tesztelhető projekt |
| 2 | [Felhasználókezelés](doksik/modulok/02-felhasznalokezeles.md) | GitHub OAuth belépés, JWT session, szerepkörök |
| 3 | [Kurzusok és haladás](doksik/modulok/03-kurzusok-haladas.md) | Beiratkozás, GitHub API progress tracking |
| 4 | [Tanúsítvány rendszer](doksik/modulok/04-tanusitvany.md) | PDF generálás, verifikációs URL |
| 5 | [Frontend](doksik/modulok/05-frontend.md) | Astro weboldal, dashboard, API integráció |
| 6 | [Éles üzem](doksik/modulok/06-eles-uzem.md) | VPS deploy, SSL, CD pipeline, monitoring |
| 7 | [Open source és közösség](doksik/modulok/07-open-source.md) | Kontribútorok fogadása, közösségi szerepkörök |

## Verifikációs tesztek

Minden modulhoz tartozik egy verifikációs tesztcsomag, amivel ellenőrizheted, hogy a munkád kész. Ezeket mi adjuk — a saját tesztjeiddel ellentétben ezeket nem neked kell megírni, csak futtatni.

```bash
# Modul 1 ellenőrzése
pytest tesztek/modul-01/ -v
```

→ [tesztek/](tesztek/) — teljes útmutató és tesztfájlok

## Platform repó

A kurzus során épített kód egy külön repóban él: `openschool-platform`

## Dokumentáció

→ [doksik/](doksik/)

### Első lépések

1. [Környezet beállítás](doksik/tanulok/kornyezet-beallitas.md) — szoftverek telepítése
2. [Discord csatlakozás](doksik/tanulok/discord-hasznalat.md) — közösség és segítségkérés
3. [Modul 1](doksik/modulok/01-projekt-inditas.md) — indulás!
