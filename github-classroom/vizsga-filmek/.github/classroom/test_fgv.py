import sys
import os


def test_beolvasas():
    import fgv
    filmek = fgv.beolvasas("filmek.txt")
    assert isinstance(filmek, list), "A beolvasas() nem listat ad vissza"
    assert len(filmek) == 100, f"Vart: 100 film, kapott: {len(filmek)}"
    assert isinstance(filmek[0], dict), "A lista elemei nem szotarak"
    assert isinstance(filmek[0]["ev"], int), "Az 'ev' nem egesz szam"
    assert isinstance(filmek[0]["ertekeles"], float), "Az 'ertekeles' nem float"
    print("PASS")


def test_darabszam():
    import fgv
    filmek = fgv.beolvasas("filmek.txt")
    assert fgv.darabszam(filmek) == 100, f"Vart: 100, kapott: {fgv.darabszam(filmek)}"
    print("PASS")


def test_kategoriak_szama():
    import fgv
    filmek = fgv.beolvasas("filmek.txt")
    szamlalo = fgv.kategoriak_szama(filmek)
    assert isinstance(szamlalo, dict), "Nem szotarat ad vissza"
    assert len(szamlalo) == 4, f"Vart: 4 kategoria, kapott: {len(szamlalo)}"
    assert sum(szamlalo.values()) == 100, "A kategoriak osszege nem 100"
    print("PASS")


def test_legjobb_legrosszabb():
    import fgv
    filmek = fgv.beolvasas("filmek.txt")
    legjobb, legrosszabb = fgv.legjobb_legrosszabb(filmek)
    assert isinstance(legjobb, dict), "A legjobb nem szotar"
    assert isinstance(legrosszabb, dict), "A legrosszabb nem szotar"
    assert legjobb["ertekeles"] >= legrosszabb["ertekeles"]
    for film in filmek:
        assert film["ertekeles"] <= legjobb["ertekeles"]
        assert film["ertekeles"] >= legrosszabb["ertekeles"]
    print("PASS")


def test_film_keresese():
    import fgv
    filmek = fgv.beolvasas("filmek.txt")
    elso_cim = filmek[0]["cim"]
    talalat = fgv.film_keresese(filmek, elso_cim)
    assert talalat is not None, f"Nem talalta: {elso_cim}"
    assert talalat["cim"] == elso_cim
    nincs = fgv.film_keresese(filmek, "Ez Biztosan Nem Letezik XYZ")
    assert nincs is None, "Nem letezo filmre nem None-t adott vissza"
    print("PASS")


def test_film_fajlba_iras():
    import fgv
    filmek = fgv.beolvasas("filmek.txt")
    film = filmek[0]
    fgv.film_fajlba_iras(film, "test_output_tmp.txt")
    assert os.path.exists("test_output_tmp.txt"), "Nem hozta letre a fajlt"
    with open("test_output_tmp.txt", "r", encoding="utf-8") as f:
        tartalom = f.read().strip()
    assert ";" in tartalom, "A fajl nem pontosvesszovel tagolt"
    os.remove("test_output_tmp.txt")
    print("PASS")


def test_kategoriahoz_tartozo_filmek():
    import fgv
    filmek = fgv.beolvasas("filmek.txt")
    szamlalo = fgv.kategoriak_szama(filmek)
    for kat, db in szamlalo.items():
        talalatok = fgv.kategoriahoz_tartozo_filmek(filmek, kat)
        assert len(talalatok) == db, f"Vart: {db} {kat} film, kapott: {len(talalatok)}"
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
