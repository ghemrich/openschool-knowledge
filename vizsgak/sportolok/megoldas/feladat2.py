import random


def golyok_huzasa():
    golyok = [random.randint(1, 5) for _ in range(4)]
    return golyok


def tipp_bekerese():
    tipp = int(input("Tippelj, mennyi a négy golyó összege: "))
    return tipp


def tipp_kiertekeles(tipp, osszeg):
    if tipp < 4 or tipp > 20:
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
    golyok = golyok_huzasa()
    osszeg = sum(golyok)
    tippek_szama = 0
    talalt = False

    while not talalt:
        tipp = tipp_bekerese()
        tippek_szama += 1
        talalt = tipp_kiertekeles(tipp, osszeg)

    print(f"\nA húzott golyók: {golyok}")
    print(f"A tippek száma: {tippek_szama}")
    print("Köszönjük a játékot!")


jatek()
