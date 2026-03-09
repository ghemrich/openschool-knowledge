import sys
import os


def test_beolvasas():
    import fgv
    sportolok = fgv.beolvasas("sportolok.txt")
    assert isinstance(sportolok, list), "A beolvasas() nem listat ad vissza"
    assert len(sportolok) == 97, f"Vart: 97 sportolo, kapott: {len(sportolok)}"
    assert isinstance(sportolok[0], dict), "A lista elemei nem szotarak"
    assert isinstance(sportolok[0]["ev"], int), "Az 'ev' nem egesz szam"
    assert isinstance(sportolok[0]["ermek"], int), "Az 'ermek' nem egesz szam"
    assert isinstance(sportolok[0]["pontszam"], float), "A 'pontszam' nem float"
    print("PASS")


def test_darabszam():
    import fgv
    sportolok = fgv.beolvasas("sportolok.txt")
    assert fgv.darabszam(sportolok) == 97, f"Vart: 97, kapott: {fgv.darabszam(sportolok)}"
    print("PASS")


def test_nemzetisegek_szama():
    import fgv
    sportolok = fgv.beolvasas("sportolok.txt")
    szamlalo = fgv.nemzetisegek_szama(sportolok)
    assert isinstance(szamlalo, dict), "Nem szotarat ad vissza"
    assert len(szamlalo) == 4, f"Vart: 4 nemzetiseg, kapott: {len(szamlalo)}"
    assert sum(szamlalo.values()) == 97, "A nemzetisegek osszege nem 97"
    print("PASS")


def test_legtobb_legkevesebb_erem():
    import fgv
    sportolok = fgv.beolvasas("sportolok.txt")
    legtobb, legkevesebb = fgv.legtobb_legkevesebb_erem(sportolok)
    assert isinstance(legtobb, dict), "A legtobb nem szotar"
    assert isinstance(legkevesebb, dict), "A legkevesebb nem szotar"
    assert legtobb["ermek"] >= legkevesebb["ermek"]
    for sportolo in sportolok:
        assert sportolo["ermek"] <= legtobb["ermek"]
        assert sportolo["ermek"] >= legkevesebb["ermek"]
    print("PASS")


def test_sportolo_keresese():
    import fgv
    sportolok = fgv.beolvasas("sportolok.txt")
    elso_nev = sportolok[0]["nev"]
    talalat = fgv.sportolo_keresese(sportolok, elso_nev)
    assert talalat is not None, f"Nem talalta: {elso_nev}"
    assert talalat["nev"] == elso_nev
    nincs = fgv.sportolo_keresese(sportolok, "Ez Biztosan Nem Letezik XYZ")
    assert nincs is None, "Nem letezo sportolora nem None-t adott vissza"
    print("PASS")


def test_sportolo_fajlba_iras():
    import fgv
    sportolok = fgv.beolvasas("sportolok.txt")
    sportolo = sportolok[0]
    fgv.sportolo_fajlba_iras(sportolo, "test_output_tmp.txt")
    assert os.path.exists("test_output_tmp.txt"), "Nem hozta letre a fajlt"
    with open("test_output_tmp.txt", "r", encoding="utf-8") as f:
        tartalom = f.read().strip()
    assert ";" in tartalom, "A fajl nem pontosvesszovel tagolt"
    os.remove("test_output_tmp.txt")
    print("PASS")


def test_sportaghoz_tartozo_sportolok():
    import fgv
    sportolok = fgv.beolvasas("sportolok.txt")
    sportagak = {}
    for sportolo in sportolok:
        s = sportolo["sportag"]
        sportagak[s] = sportagak.get(s, 0) + 1
    for sportag, db in sportagak.items():
        talalatok = fgv.sportaghoz_tartozo_sportolok(sportolok, sportag)
        assert len(talalatok) == db, f"Vart: {db} {sportag} sportolo, kapott: {len(talalatok)}"
        assert isinstance(talalatok[0], tuple), "Az eredmeny elemei nem tuple-ok"
    print("PASS")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Hasznalat: python3 test_fgv.py <teszt_neve>")
        sys.exit(1)
    test_func = globals().get(sys.argv[1])
    if test_func is None:
        print(f"Ismeretlen teszt: {sys.argv[1]}")
        sys.exit(1)
    try:
        test_func()
    except AssertionError as e:
        print(f"FAIL: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"FAIL: {e}")
        sys.exit(1)
