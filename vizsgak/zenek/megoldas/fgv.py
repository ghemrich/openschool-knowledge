def beolvasas(fajlnev):
    zenek = []
    with open(fajlnev, "r", encoding="utf-8") as f:
        for sor in f:
            adatok = sor.strip().split(";")
            zene = {
                "cim": adatok[0],
                "mufaj": adatok[1],
                "ev": int(adatok[2]),
                "hossz": int(adatok[3]),
                "ertekeles": float(adatok[4])
            }
            zenek.append(zene)
    return zenek


def darabszam(zenek):
    return len(zenek)


def mufajok_szama(zenek):
    szamlalo = {}
    for zene in zenek:
        mufaj = zene["mufaj"]
        szamlalo[mufaj] = szamlalo.get(mufaj, 0) + 1
    return szamlalo


def legjobb_legrosszabb(zenek):
    legjobb = zenek[0]
    legrosszabb = zenek[0]
    for zene in zenek:
        if zene["ertekeles"] > legjobb["ertekeles"]:
            legjobb = zene
        if zene["ertekeles"] < legrosszabb["ertekeles"]:
            legrosszabb = zene
    return legjobb, legrosszabb


def zene_keresese(zenek, cim):
    for zene in zenek:
        if zene["cim"] == cim:
            return zene
    return None


def zene_fajlba_iras(zene, fajlnev):
    with open(fajlnev, "w", encoding="utf-8") as f:
        sor = f"{zene['cim']};{zene['mufaj']};{zene['ev']};{zene['hossz']};{zene['ertekeles']}"
        f.write(sor)


def mufajhoz_tartozo_zenek(zenek, mufaj):
    talalatok = []
    for zene in zenek:
        if zene["mufaj"] == mufaj:
            talalatok.append((zene["cim"], zene["ev"]))
    return talalatok
