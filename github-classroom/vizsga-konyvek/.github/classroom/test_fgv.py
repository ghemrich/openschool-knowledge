import sys
import os


def test_beolvasas():
    import fgv
    konyvek = fgv.beolvasas("konyvek.txt")
    assert isinstance(konyvek, list), "A beolvasas() nem listat ad vissza"
    assert len(konyvek) == 104, f"Vart: 104 konyv, kapott: {len(konyvek)}"
    assert isinstance(konyvek[0], dict), "A lista elemei nem szotarak"
    assert isinstance(konyvek[0]["ev"], int), "Az 'ev' nem egesz szam"
    assert isinstance(konyvek[0]["bevetel"], int), "A 'bevetel' nem egesz szam"
    print("PASS")


def test_darabszam():
    import fgv
    konyvek = fgv.beolvasas("konyvek.txt")
    assert fgv.darabszam(konyvek) == 104, f"Vart: 104, kapott: {fgv.darabszam(konyvek)}"
    print("PASS")


def test_nyelvek_szama():
    import fgv
    konyvek = fgv.beolvasas("konyvek.txt")
    szamlalo = fgv.nyelvek_szama(konyvek)
    assert isinstance(szamlalo, dict), "Nem szotarat ad vissza"
    assert len(szamlalo) == 3, f"Vart: 3 nyelv, kapott: {len(szamlalo)}"
    assert sum(szamlalo.values()) == 104, "A nyelvek osszege nem 104"
    print("PASS")


def test_legtobb_legkevesebb_bevetel():
    import fgv
    konyvek = fgv.beolvasas("konyvek.txt")
    legtobb, legkevesebb = fgv.legtobb_legkevesebb_bevetel(konyvek)
    assert isinstance(legtobb, dict), "A legtobb nem szotar"
    assert isinstance(legkevesebb, dict), "A legkevesebb nem szotar"
    assert legtobb["bevetel"] >= legkevesebb["bevetel"]
    for konyv in konyvek:
        assert konyv["bevetel"] <= legtobb["bevetel"]
        assert konyv["bevetel"] >= legkevesebb["bevetel"]
    print("PASS")


def test_konyv_keresese():
    import fgv
    konyvek = fgv.beolvasas("konyvek.txt")
    elso_cim = konyvek[0]["cim"]
    talalat = fgv.konyv_keresese(konyvek, elso_cim)
    assert talalat is not None, f"Nem talalta: {elso_cim}"
    assert talalat["cim"] == elso_cim
    nincs = fgv.konyv_keresese(konyvek, "Ez Biztosan Nem Letezik XYZ")
    assert nincs is None, "Nem letezo konyvre nem None-t adott vissza"
    print("PASS")


def test_konyv_fajlba_iras():
    import fgv
    konyvek = fgv.beolvasas("konyvek.txt")
    konyv = konyvek[0]
    fgv.konyv_fajlba_iras(konyv, "test_output_tmp.txt")
    assert os.path.exists("test_output_tmp.txt"), "Nem hozta letre a fajlt"
    with open("test_output_tmp.txt", "r", encoding="utf-8") as f:
        tartalom = f.read().strip()
    assert ";" in tartalom, "A fajl nem pontosvesszovel tagolt"
    os.remove("test_output_tmp.txt")
    print("PASS")


def test_mufajhoz_tartozo_konyvek():
    import fgv
    konyvek = fgv.beolvasas("konyvek.txt")
    mufajok = {}
    for konyv in konyvek:
        m = konyv["mufaj"]
        mufajok[m] = mufajok.get(m, 0) + 1
    for mufaj, db in mufajok.items():
        talalatok = fgv.mufajhoz_tartozo_konyvek(konyvek, mufaj)
        assert len(talalatok) == db, f"Vart: {db} {mufaj} konyv, kapott: {len(talalatok)}"
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
