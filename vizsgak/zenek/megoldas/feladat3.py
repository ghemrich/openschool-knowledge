import fgv

zenek = fgv.beolvasas("zenek.txt")

# 2. Hány zene van
print(f"A listában {fgv.darabszam(zenek)} zene található.")

# 3. Műfajok szerinti darabszám
szamlalo = fgv.mufajok_szama(zenek)
for mufaj, db in szamlalo.items():
    print(f"{mufaj}: {db} db")

# 4. Legjobb és legrosszabb értékelésű zene
legjobb, legrosszabb = fgv.legjobb_legrosszabb(zenek)
print(f"Legjobb értékelésű: {legjobb['cim']} ({legjobb['ertekeles']})")
print(f"Legrosszabb értékelésű: {legrosszabb['cim']} ({legrosszabb['ertekeles']})")

# 5. Zene keresése és fájlba írás
cim = input("Add meg egy zene címét: ")
zene = fgv.zene_keresese(zenek, cim)
if zene:
    fgv.zene_fajlba_iras(zene, "valasztott_zene.txt")
    print("A zene adatai kiírva a valasztott_zene.txt fájlba.")
else:
    print("Nincs ilyen cím a listában")

# 6. Műfaj szerinti szűrés
mufaj = input("Add meg a műfaj nevét: ")
talalatok = fgv.mufajhoz_tartozo_zenek(zenek, mufaj)
for cim, ev in talalatok:
    print(f"{cim} ({ev})")
