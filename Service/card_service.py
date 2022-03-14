from Domain.card import Card
from Repository.file_repository import FileRepository


class CardService:

    def __init__(self,  card_repository: FileRepository,tranzactie_repository:FileRepository):
        self.__card_repository=card_repository
        self.__tranzactie_repository=tranzactie_repository

    def get_all_service(self):
        return self.__card_repository.get_all()

    def adaugare_card(self, id_card, nume_client, prenume_client, cnp_client, data_nasterii, data_inregistrarii):
        card=Card(id_card, nume_client, prenume_client, cnp_client, data_nasterii, data_inregistrarii)
        if self.__card_repository.get_by_id(id_card):
            raise KeyError("Exista deja un card cu id-ul", id_card)
        self.__card_repository.adaugare(card)

    def stergere_card(self,id_de_sters):
        tranzactii = self.__tranzactie_repository.get_all()
        for tranzactie in tranzactii:
            if tranzactie.id_masina == id_de_sters:
                raise KeyError(f"Nu se poate sterge masina cu id-ul {id_de_sters}, deoarece e utilizata in tranzactie")
        return self.__card_repository.stergere(id_de_sters)

    def modificare_card (self, id_de_modificat, nume_nou, prenume_nou, cnp_nou, data_nasterii_noua, data_inregistrarii_noua):
        card = self.__card_repository.get_by_id(id_de_modificat)

        if card is None:
            raise KeyError("Nu exista card cu id-ul", id_de_modificat)

        if nume_nou!="":
            card.nume = nume_nou
        if prenume_nou !="":
            card.prenume = prenume_nou
        if cnp_nou!=0:
           card.cnp = cnp_nou
        if data_nasterii_noua !="":
            card.data_nasterii = data_nasterii_noua
        if data_inregistrarii_noua!="":
            card.data_inregistrarii = data_inregistrarii_noua


        self.__card_repository.modificare(card)

