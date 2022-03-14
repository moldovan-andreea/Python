from Domain.card import Card
from Domain.masina import Masina


class TranzactieViewModel:
    def __init__(self, id_tranzactie, masina: Masina, card: Card, suma_piese, suma_manopera, data_ora):
        self.id_tranzactie = id_tranzactie
        self.masina = masina
        self.card = card
        self.suma_piese = suma_piese
        self.suma_manopera = suma_manopera
        self.data_ora = data_ora

    def __str__(self):
        return f'id tranzactie:{self.id_tranzactie} \n-------cu masina {self.masina} \n-------si cardul client {self.card},\n-------suma piese: {self.suma_piese}, ' \
               f'suma manopera: {self.suma_manopera}, data si ora: {self.data_ora}'