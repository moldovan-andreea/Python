from Domain.masina import Masina
from Repository.file_repository import FileRepository
from Domain.masina_validator import MasinaValidator


class MasinaService:
    def __init__(self, masini_repository: FileRepository, masina_validator: MasinaValidator):
        self.__masina_repository = masini_repository
        self.__masina_validator = masina_validator

    def get_all_service(self):
        return self.__masina_repository.get_all()

    def get_by_id(self, id_masina):
        return self.__masina_repository.get_by_id(id_masina)

    def adaugare_masina(self, id_masina, model,an_achizitie, an_fabricatie,nr_km, in_garantie):
        masina = Masina(id_masina, model, an_achizitie, an_fabricatie, nr_km, in_garantie)

        self.__masina_validator.valideaza(masina)
        self.__masina_repository.adaugare(masina)

    def stergere_masina(self,id_de_sters):
        self.__masina_repository.stergere(id_de_sters)

    def modificare_masina(self,id_de_modificat, model_nou, an_achizitie_nou, an_fabricatie_nou, nr_km_nou, in_garantie_noua):
        """  #de ce nu facem o masina=Masina(id,model etc)
        masina=Masina(id_masina,model,an_achizitie,an_fabricatie,nr_km,in_garantie)"""
        masina = self.__masina_repository.get_by_id(id_de_modificat)
        if masina is None:
            raise KeyError("Nu exista masina cu id-ul", id_de_modificat)
        if model_nou != "":
            masina.model = model_nou
        if an_achizitie_nou != 0:
            masina.an_achizitie = an_achizitie_nou
        if an_fabricatie_nou != 0:
            masina.an_fabricatie = an_fabricatie_nou
        if nr_km_nou != 0:
            masina.nr_km = nr_km_nou
        if in_garantie_noua != "":
            masina.in_garantie = in_garantie_noua

        self.__masina_validator.valideaza(masina)
        self.__masina_repository.modificare(masina)


