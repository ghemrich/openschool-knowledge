def beolvasas(fajlnev):
    sportolok = []
    with open(fajlnev, "r", encoding="utf-8") as f:
        for sor in f:
            adatok = sor.strip().split(";")
            sportolo = {
                "nev": adatok[0],
                "sportag": adatok[1],
                "nemzetiseg": adatok[2],
                "ev": int(adatok[3]),
                "ermek": int(adatok[4]),
                "pontszam": float(adatok[5])
            }
            sportolok.append(sportolo)
    return sportolok


def darabszam(sportolok):
    return len(sportolok)


def nemzetisegek_szama(sportolok):
    szamlalo = {}
    for sportolo in sportolok:
        nemz = sportolo["nemzetiseg"]
        szamlalo[nemz] = szamlalo.get(nemz, 0) + 1
    return szamlalo


def legtobb_legkevesebb_erem(sportolok):
    legtobb = sportolok[0]
    legkevesebb = sportolok[0]
    for sportolo in sportolok:
        if sportolo["ermek"] > legtobb["ermek"]:
            legtobb = sportolo
        if sportolo["ermek"] < legkevesebb["ermek"]:
            legkevesebb = sportolo
    return legtobb, legkevesebb


def sportolo_keresese(sportolok, nev):
    for sportolo in sportolok:
        if sportolo["nev"] == nev:
            return sportolo
    return None


def sportolo_fajlba_iras(sportolo, fajlnev):
    with open(fajlnev, "w", encoding="utf-8") as f:
        sor = f"{sportolo['nev']};{sportolo['sportag']};{sportolo['nemzetiseg']};{sportolo['ev']};{sportolo['ermek']};{sportolo['pontszam']}"
        f.write(sor)


def sportaghoz_tartozo_sportolok(sportolok, sportag):
    talalatok = []
    for sportolo in sportolok:
        if sportolo["sportag"] == sportag:
            talalatok.append((sportolo["nev"], sportolo["ermek"]))
    return talalatok
