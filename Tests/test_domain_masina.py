from Domain.masina import Masina


def test_masina():
    masina = Masina('1','dacia', 2009, 2000, 50000,'da')

    assert masina.id_entitate == '1'
    assert masina.model == 'sport'
    assert masina.an_achizitie == 2009
    assert masina.an_fabricatie == 2000
    assert masina.nr_km == 50000
    assert masina.in_garantie == 'da'