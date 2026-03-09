def bekeres():
    vezeteknev = input("Add meg a vezetékneved: ")
    keresztnev = input("Add meg a keresztneved: ")
    kedvenc_szam = input("Add meg a kedvenc számod: ")
    return vezeteknev, keresztnev, kedvenc_szam


def jelszavak_osszeallitasa(vezeteknev, keresztnev, kedvenc_szam):
    vezeteknev = vezeteknev.upper()
    keresztnev = keresztnev.upper()
    jelszo1 = keresztnev[-3:] + "_" + kedvenc_szam + vezeteknev[0]
    jelszo2 = vezeteknev[::-1] + kedvenc_szam
    jelszo3 = keresztnev[0] + kedvenc_szam + "#" + vezeteknev
    return jelszo1, jelszo2, jelszo3


def megjelenites(jelszo1, jelszo2, jelszo3):
    print(f"1. jelszó: {jelszo1}")
    print(f"2. jelszó: {jelszo2}")
    print(f"3. jelszó: {jelszo3}")


def main():
    vezeteknev, keresztnev, kedvenc_szam = bekeres()
    jelszo1, jelszo2, jelszo3 = jelszavak_osszeallitasa(vezeteknev, keresztnev, kedvenc_szam)
    megjelenites(jelszo1, jelszo2, jelszo3)


main()
