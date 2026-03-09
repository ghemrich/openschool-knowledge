import sys
import os


def test_beolvasas():
    import fgv
    zenek = fgv.beolvasas("zenek.txt")
    assert isinstance(zenek, list), "A beolvasas() nem listat ad vissza"
    assert len(zenek) == 100, f"Vart: 100 zene, kapott: {len(zenek)}"
    assert isinstance(zenek[0], dict), "A lista elemei nem szotarak"
    assert isinstance(zenek[0]["ev"], int), "Az 'ev' nem egesz szam"
    assert isinstance(zenek[0]["ertekeles"], float), "Az 'ertekeles' nem float"
    print("PASS")


def test_darabszam():
    import fgv
    zenek = fgv.beolvasas("zenek.txt")
    assert fgv.darabszam(zenek) == 100, f"Vart: 100, kapott: {fgv.darabszam(zenek)}"
    print("PASS")


def test_mufajok_szama():
    import fgv
    zenek = fgv.beolvasas("zenek.txt")
    szamlalo = fgv.mufajok_szama(zenek)
    assert isinstance(szamlalo, dict), "Nem szotarat ad vissza"
    assert len(szamlalo) == 4, f"Vart: 4 mufaj, kapott: {len(szamlalo)}"
    assert sum(szamlalo.values()) == 100, "A mufajok osszege nem 100"
    print("PASS")


def test_legjobb_legrosszabb():
    import fgv
    zenek = fgv.beolvasas("zenek.txt")
    legjobb, legrosszabb = fgv.legjobb_legrosszabb(zenek)
    assert isinstance(legjobb, dict), "A legjobb nem szotar"
    assert isinstance(legrosszabb, dict), "A legrosszabb nem szotar"
    assert legjobb["ertekeles"] >= legrosszabb["ertekeles"]
    for zene in zenek:
        assert zene["ertekeles"] <= legjobb["ertekeles"]
        assert zene["ertekeles"] >= legrosszabb["ertekeles"]
    print("PASS")


def test_zene_keresese():
    import fgv
    zenek = fgv.beolvasas("zenek.txt")
    elso_cim = zenek[0]["cim"]
    talalat = fgv.zene_keresese(zenek, elso_cim)
    assert talalat is not None, f"Nem talalta: {elso_cim}"
    assert talalat["cim"] == elso_cim
    nincs = fgv.zene_keresese(zenek, "Ez Biztosan Nem Letezik XYZ")
    assert nincs is None, "Nem letezo zenere nem None-t adott vissza"
    print("PASS")


def test_zene_fajlba_iras():
    import fgv
    zenek = fgv.beolvasas("zenek.txt")
    zene = zenek[0]
    fgv.zene_fajlba_iras(zene, "test_output_tmp.txt")
    assert os.path.exists("test_output_tmp.txt"), "Nem hozta letre a fajlt"
    with open("test_output_tmp.txt", "r", encoding="utf-8") as f:
        tartalom = f.read().strip()
    assert ";" in tartalom, "A fajl nem pontosvesszovel tagolt"
    os.remove("test_output_tmp.txt")
    print("PASS")


def test_mufajhoz_tartozo_zenek():
    import fgv
    zenek = fgv.beolvasas("zenek.txt")
    szamlalo = fgv.mufajok_szama(zenek)
    for mufaj, db in szamlalo.items():
        talalatok = fgv.mufajhoz_tartozo_zenek(zenek, mufaj)
        assert len(talalatok) == db, f"Vart: {db} {mufaj} zene, kapott: {len(talalatok)}"
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
