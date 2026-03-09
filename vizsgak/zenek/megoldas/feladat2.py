import random


def szimbolumok_huzasa():
    szimbolumok = [random.randint(1, 10) for _ in range(3)]
    return szimbolumok


def tipp_bekerese():
    tipp = int(input("Tippelj, mennyi a három szimbólum összege: "))
    return tipp


def tipp_kiertekeles(tipp, osszeg):
    if tipp < 3 or tipp > 30:
        print("HIBA: nem lehetséges érték!")
        return False
    elif tipp < osszeg:
        print("Ennél több")
        return False
    elif tipp > osszeg:
        print("Ennél kevesebb")
        return False
    else:
        print("Talált!")
        return True


def jatek():
    szimbolumok = szimbolumok_huzasa()
    osszeg = sum(szimbolumok)
    tippek_szama = 0
    talalt = False

    while not talalt:
        tipp = tipp_bekerese()
        tippek_szama += 1
        talalt = tipp_kiertekeles(tipp, osszeg)

    print(f"\nA húzott szimbólumok: {szimbolumok}")
    print(f"A tippek száma: {tippek_szama}")
    print("Köszönjük a játékot!")


jatek()
