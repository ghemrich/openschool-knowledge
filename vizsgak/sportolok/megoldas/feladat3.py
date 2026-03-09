import fgv

sportolok = fgv.beolvasas("sportolok.txt")

# 2. Hány sportoló van
print(f"A listában {fgv.darabszam(sportolok)} sportoló található.")

# 3. Nemzetiségek szerinti darabszám
szamlalo = fgv.nemzetisegek_szama(sportolok)
for nemz, db in szamlalo.items():
    print(f"{nemz}: {db} db")

# 4. Legtöbb és legkevesebb éremmel rendelkező sportoló
legtobb, legkevesebb = fgv.legtobb_legkevesebb_erem(sportolok)
print(f"Legtöbb érem: {legtobb['nev']} ({legtobb['ermek']} érem)")
print(f"Legkevesebb érem: {legkevesebb['nev']} ({legkevesebb['ermek']} érem)")

# 5. Sportoló keresése és fájlba írás
nev = input("Add meg egy sportoló nevét: ")
sportolo = fgv.sportolo_keresese(sportolok, nev)
if sportolo:
    fgv.sportolo_fajlba_iras(sportolo, "valasztott_sportolo.txt")
    print("A sportoló adatai kiírva a valasztott_sportolo.txt fájlba.")
else:
    print("Nincs ilyen név a listában")

# 6. Sportág szerinti szűrés
sportag = input("Add meg a sportág nevét: ")
talalatok = fgv.sportaghoz_tartozo_sportolok(sportolok, sportag)
for nev, ermek in talalatok:
    print(f"{nev} ({ermek} érem)")
