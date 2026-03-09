def bekeres():
    vezeteknev = input("Add meg a vezetékneved: ")
    keresztnev = input("Add meg a keresztneved: ")
    szuletesi_ev = input("Add meg a születési éved: ")
    return vezeteknev, keresztnev, szuletesi_ev


def becenevek_osszeallitasa(vezeteknev, keresztnev, szuletesi_ev):
    vezeteknev = vezeteknev.lower()
    keresztnev = keresztnev.lower()
    ev_veg = szuletesi_ev[-2:]
    becenev1 = keresztnev[:3] + ev_veg
    becenev2 = vezeteknev + "_" + keresztnev[-1] + ev_veg
    becenev3 = keresztnev + ev_veg + "." + vezeteknev[::-1]
    return becenev1, becenev2, becenev3


def megjelenites(becenev1, becenev2, becenev3):
    print(f"1. becenév: {becenev1}")
    print(f"2. becenév: {becenev2}")
    print(f"3. becenév: {becenev3}")


def main():
    vezeteknev, keresztnev, szuletesi_ev = bekeres()
    becenev1, becenev2, becenev3 = becenevek_osszeallitasa(vezeteknev, keresztnev, szuletesi_ev)
    megjelenites(becenev1, becenev2, becenev3)


main()
