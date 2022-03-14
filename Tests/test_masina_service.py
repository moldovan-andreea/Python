from Domain.masina_validator import MasinaValidator
from Repository.file_repository import FileRepository
from Service.masina_service import MasinaService
from Tests.utils import clear_file


def test_add_masina_service():
    clear_file('repository_test.txt')
    masini_repository = FileRepository("repository_test.txt")
    masina_validator = MasinaValidator()
    service = MasinaService(masini_repository,masina_validator)

    service.adaugare_masina('1','sport', 2009, 2000, 50000, 'da')
    assert len(masini_repository.get_all()) == 1
    added = masini_repository.get_by_id('1')
    assert added is not None
    assert added.id_entitate == '1'
    assert added.model == 'sport'
    assert added.an_achizitie == 2009
    assert added.an_fabricatie == 2000
    assert added.nr_km == 50000
    assert added.garantie == 'da'

    try:
        service.adaugare_masina('1','sport', 2009, 2000, 50000, 'da')
        assert False
    except KeyError:
        assert True
    except Exception:
        assert False

def test_delete_masina_service():
    clear_file('repository_test.txt')
    masini_repository = FileRepository('repository_test.txt')
    masina_validator = MasinaValidator()
    service = MasinaService(masini_repository, masina_validator)

    service.adaugare_masina('1','dacia', 2009, 2000, 50000,'da')
    service.adaugare_masina('2','dacia', 2009, 2000, 50000,'da')

    try:
        service.stergere_masina(3)
        assert False
    except KeyError:
        assert True
    except Exception:
        assert False

    service.stergere_masina('1')
    assert len(masini_repository.get_all()) == 1
    deleted = masini_repository.get_by_id('1')
    assert deleted is None
    remaining = masini_repository.get_by_id('2')
    assert remaining is not None
    assert remaining.id_entitate == '2'
    assert remaining.model == 'dacia'
    assert remaining.an_achizitie == 2009
    assert remaining.an_fabricatie == 2000
    assert remaining.nr_km == 50000
    assert remaining.garantie == 'da'

def test_update_masina_service():
    clear_file('repository_test.txt')
    masini_repository = FileRepository('repository_test.txt')
    masina_validator = MasinaValidator()
    service = MasinaService(masini_repository, masina_validator)

    service.adaugare_masina('1', 'dacia', 2009, 2000, 50000,'da')
    service.adaugare_masina('2', 'dacia', 2009, 2000, 50000, 'da')

    service.modificare_masina('1', 'opel', 2009, 2000, 50000,'nu')
    updated = masini_repository.get_by_id('1')
    assert updated is not None
    assert updated.id_entitate == '1'
    assert updated.model == 'opel'
    assert updated.an_achizitie == 2009
    assert updated.an_fabricatie == 2000
    assert updated.nr_km == 50000
    assert updated.garantie == 'nu'

    unchanged = masini_repository.get_by_id('2')
    assert unchanged is not None
    assert unchanged.id_entitate == '2'
    assert unchanged.model == 'dacia'
    assert unchanged.an_achizitie == 2009
    assert unchanged.an_fabricatie == 2000
    assert unchanged.nr_km == 50000
    assert unchanged.garantie == 'da'

    try:
        service.modificare_masina('3', 'opel', 2009, 2000, 50000,'da')
        assert False
    except KeyError:
        assert True
    except Exception:
        assert False
