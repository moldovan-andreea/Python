from Domain.entitate import Entitate


class Masina(Entitate):
    def __init__(self, id_masina, model, an_achizitie, an_fabricatie, nr_km, in_garantie):
        super().__init__(id_masina)
        self.__model = model
        self.__an_achizitie = an_achizitie
        self.__an_fabricatie = an_fabricatie
        self.__nr_km = nr_km
        self.__in_garantie = in_garantie

    def __str__(self):
        return f"id-ul masinii: {self.id_entitate}, model: {self.__model}, anul achizitiei:{self.__an_achizitie},"\
                f"anul fabricatiei:{self.__an_fabricatie}, numar km:{self.__nr_km}, in garantie:{self.__in_garantie}"
    @property
    def model(self):
        return self.__model
    @model.setter
    def model(self, model_nou):
        self.__model=model_nou

    @property
    def an_achizitie(self):
        return self.__an_achizitie
    @an_achizitie.setter
    def an_achizitie(self, an_achizitie_nou):
        self.__an_achizitie=an_achizitie_nou

    @property
    def an_fabricatie(self):
        return self.__an_fabricatie
    @an_fabricatie.setter
    def an_fabricatie(self,an_fabricatie_nou):
        self.__an_fabricatie=an_fabricatie_nou

    @property
    def nr_km(self):
        return self.__nr_km
    @nr_km.setter
    def nr_km(self, nr_km_nou):
        self.__nr_km = nr_km_nou

    @property
    def in_garantie(self):
        return self.__in_garantie
    @in_garantie.setter
    def in_garantie(self, in_garantie_nou):
        self.__in_garantie = in_garantie_nou

