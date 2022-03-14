from Domain.entitate import Entitate


class Tranzactie(Entitate):
    def __init__(self,id_tranzactie, id_masina, id_card_client , suma_piese, suma_manopera, data_si_ora):
        super().__init__(id_tranzactie)
        self.id_masina = id_masina
        self.id_card_client = id_card_client
        self.suma_piese = suma_piese
        self.suma_manopera = suma_manopera
        self.data_si_ora = data_si_ora

    def __str__(self):
        return f"id:{self.id_entitate},id masina:{self.id_masina},id card client:{self.id_card_client},suma piese:{self.suma_piese}" \
                f" suma manopera:{self.suma_manopera}, data si ora:{self.data_si_ora}"

    @property
    def suma_piese(self):
        return self.__suma_piese

    @suma_piese.setter
    def suma_piese(self, suma_piese_noua):
        self.__suma_piese = suma_piese_noua

    @property
    def suma_manopera(self):
        return self.__suma_manopera

    @suma_manopera.setter
    def suma_manopera(self, suma_manopera_noua):
        self.__suma_manopera = suma_manopera_noua

    @property
    def data_si_ora(self):
        return self.__data_si_ora

    @data_si_ora.setter
    def data_si_ora(self, data_si_ora_noua):
        self.__data_si_ora = data_si_ora_noua

