from Domain.entitate import Entitate


class Card(Entitate):

    def __init__(self, id_card, nume_client, prenume_client, cnp_client, data_nasterii, data_inregistrarii):
        super().__init__(id_card)
        self.__nume_client=nume_client
        self.__prenume_client=prenume_client
        self.__cnp_client = cnp_client
        self.__data_nasterii= data_nasterii
        self.__data_inregistrarii=data_inregistrarii

    def __str__(self):
        return f"id card:{self.id_entitate},nume client: {self.nume_client}, prenume client: {self.prenume_client}, cnp: {self.cnp_client}"\
                f" data nasterii: {self.data_nasterii}, data inregistrarii: {self.data_inregistrarii}"

    def __eq__(self, other):
        return type(self) == type(other) and self.__id_entitate == other.__id_entitate

    @property
    def nume_client(self):
        return self.__nume_client

    @nume_client.setter
    def nume_client(self, nume_client_nou):
        self.__nume_client = nume_client_nou

    @property
    def prenume_client(self):
        return self.__prenume_client

    @prenume_client.setter
    def prenume_client(self, prenume_client_nou):
        self.__prenume_client = prenume_client_nou

    @property
    def cnp_client(self):
        return self.__cnp_client

    @cnp_client.setter
    def cnp_client(self, cnp_client_nou):
        self.__cnp_client = cnp_client_nou

    @property
    def data_nasterii(self):
        return self.__data_nasterii

    @data_nasterii.setter
    def data_nasterii(self, data_nasterii_noua):
        self.__data_nasterii = data_nasterii_noua

    @property
    def data_inregistrarii(self):
        return self.__data_inregistrarii

    @data_inregistrarii.setter
    def data_inregistrarii(self, data_inregistrarii_noua):
        self.__data_inregistrarii = data_inregistrarii_noua
