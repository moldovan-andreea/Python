from Domain.tranzactie import Tranzactie
from Repository.file_repository import FileRepository
from ViewModel.view_model import TranzactieViewModel




class TranzactieService:

    def __init__(self, tranzactie_file_repository: FileRepository,
                 masina_file_repository: FileRepository,
                 card_file_repository: FileRepository):  # aceeasi ordine ca in apelarea in main!!
        self.__tranzactie_repository = tranzactie_file_repository
        self.__masina_repository = masina_file_repository
        self.__card_repository = card_file_repository

    def get_all(self):
        view_models = []
        for tranzactie in self.__tranzactie_repository.get_all():
            masina = self.__masina_repository.get_by_id(tranzactie.id_masina)
            card = self.__card_repository.get_by_id(tranzactie.id_card_client)
            tranzactie_view_model = TranzactieViewModel(tranzactie.id,masina,card,
                                                  tranzactie.suma_piese, tranzactie.suma_manopera, tranzactie.data_si_ora)
            view_models.append(tranzactie_view_model)
        return view_models


    def adaugare_tranzactie(self, id, id_masina, id_card_client, suma_piese, suma_manopera, data_si_ora):
        tranzactie = Tranzactie(id, id_masina, id_card_client, suma_piese, suma_manopera, data_si_ora)
        if self.__tranzactie_repository.get_by_id(id):
            raise KeyError("Exista deja o tranzactie cu id-ul", id)
        if self.__masina_repository.get_by_id(id_masina) is None:
            raise KeyError("Nu exista o masina cu id-ul", id_masina)
        if self.__card_repository.get_by_id(id_card_client) is None and id_card_client!="None":
            raise KeyError("Nu exista un card cu id-ul", id_card_client)

        self.__tranzactie_repository.adaugare(tranzactie)

    def stergere_tranzactie(self, id_de_sters):
        return self.__tranzactie_repository.stergere(id_de_sters)

    def modificare_tranzactie(self, id_de_modificat,id_masina,id_card_client, suma_piese_noua, suma_manopera_noua, data_si_ora_noua):
        tranzactie = self.__tranzactie_repository.get_by_id(id_de_modificat)
        if tranzactie is None:
            raise KeyError(f'id-ul {id_de_modificat} nu exista')
        if self.__masina_repository.get_by_id(id_masina) is None:
            raise KeyError("Nu exista o masina cu id-ul", id_masina)
        if self.__card_repository.get_by_id(id_card_client) is None and id_card_client!="None":
            raise KeyError("Nu exista un card cu id-ul", id_card_client)
        if id_masina!="":
            tranzactie.id_masina=id_masina
        if id_card_client!="":
            tranzactie.id_card_client=id_card_client
        if suma_piese_noua != 0:
            tranzactie.suma_piese = suma_piese_noua
        if suma_manopera_noua != 0:
            tranzactie.suma_manopera = suma_manopera_noua
        if data_si_ora_noua != "":
            tranzactie.data_si_ora = data_si_ora_noua

        self.__tranzactie_repository.adaugare(tranzactie)





