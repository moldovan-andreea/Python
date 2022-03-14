from Service.card_service import CardService
from Service.masina_service import MasinaService
from Service.tranzactie_service import TranzactieService
import datetime

class Console:
    def __init__(self,masina_service: MasinaService,card_service:CardService,tranzactie_service:TranzactieService):
        self.__masina_service=masina_service
        self.__card_service=card_service
        self.__tranzactie_service=tranzactie_service

    def run_menu(self):
        while True:
            print("1.Adaugare/Stergere/Modificare MASINI")
            print("2.Adaugare/Stergere/Modificare CARDURI")
            print("3.Adaugare/Stergere/Modificare TRANZACTII")
            print("4.OPERATIUNI")
            print("5.iesire")
            optiune=input("Selectati optiunea: ")
            if optiune=="1":
                self.ui_run_crud_masina()
            elif optiune=="2":
                self.ui_run_crud_card()
            elif optiune=="3":
                self.ui_run_crud_tranzactii()
            elif optiune=="x":
                print("brrrrrrrrrr")
                break
            else:
                print("Nu e o optiune")

    def ui_run_crud_masina(self):
        while True:
            print("1. Adaugare masina")
            print("2. Stergere masina")
            print("3. Modificare masina")
            print("a. Afisare masini")
            print("x. Revenire la meniul principal")
            optiune = input("Alegeti o optiune:")
            if optiune == '1':
                self.ui_adaugare_masina()
            elif optiune == '2':
                self.ui_stergere_masina()
            elif optiune == '3':
                self.ui_modificare_masina()
            elif optiune == 'a':
                self.ui_print_masini()
            elif optiune == 'x':
                break
            else:
                print("Optiune invalida, reincercati!")

    def ui_adaugare_masina(self):
        try:
            id_masina = input("Dati id-ul masinii: ")
            model = input("Dati modelul masinii: ")
            an_achizitie = int(input("Dati anul achizitiei : "))
            an_fabricatie = int(input("Dati anul fabricatiei : "))
            nr_km = int(input("Dati nr de km (numar strict pozitiv): "))
            in_garantie = input("Dati garantia (da/nu): ")
            self.__masina_service.adaugare_masina(id_masina, model, an_achizitie, an_fabricatie, nr_km, in_garantie)

        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(e)

    def ui_stergere_masina(self):
        try:
            id_de_sters = input("Dati id-ul masinii de sters: ")

            self.__masina_service.stergere_masina(id_de_sters)

        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(e)

    def ui_modificare_masina(self):
        try:
            id_masina = input("Dati id-ul masinii de modificat: ")
            model = input("Dati modelul masinii de modificat sau enter daca nu doriti modificare: ")
            an_achizitie = int(input(
                "Dati anul achizitiei al masinii de modificat (numar strict pozitiv) sau 0 daca nu doriti modificare: "))
            an_fabricatie = int(input(
                "Dati anul fabricatiei al masinii de modificat (numar strict pozitiv) sau 0 daca nu doriti modificare: "))
            nr_km = int(
                input("Dati nr de km al masinii de modificat (numar strict pozitiv) sau 0 daca nu doriti modificare: "))
            garantie = input("Dati garantie masinii de modificat (da/nu) sau enter daca nu doriti modificare")
            self.__masina_service.modificare_masina(id_masina, model, an_achizitie, an_fabricatie, nr_km, garantie)

        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(e)

    def ui_print_masini(self):
        masini = self.__masina_service.get_all_service()
        for masina in masini:
            print(masina)

    def ui_run_crud_card(self):
        while True:
            print("1. Adaugare card")
            print("2. Stergere card")
            print("3. Modificare card")
            print("a. Afisare carduri")
            print("x. Revenire la meniul principal")
            optiune = input("Alegeti o optiune:")
            if optiune == '1':
                self.ui_adaugare_card()
            elif optiune == '2':
                self.ui_stergere_card()
            elif optiune == '3':
                self.ui_modificare_card()
            elif optiune == 'a':
                self.ui_print_carduri()
            elif optiune == 'x':
                break
            else:
                print("Optiune invalida, reincercati!")

    def ui_adaugare_card(self):
        try:
            id_card = input("Dati id-ul cardului")
            nume_client = input("Dati numele clientului")
            prenume_client = input("Dati prenumele ")
            cnp_client = int(input("Dati cnp "))
            ziua_nasterii = int(input("ziua nasterii:"))
            luna_nasterii = int(input("luna nasterii:"))
            anul_nasterii = int(input("anul nasterii:"))
            data_nasterii = str(datetime.datetime(anul_nasterii, luna_nasterii, ziua_nasterii))
            ziua_inregistrarii = int(input("ziua inregistrarii:"))
            luna_inregistrarii = int(input("luna inregistrarii:"))
            anul_inregistrarii = int(input("anul inregistrarii:"))
            data_inregistrarii = str(datetime.datetime(anul_inregistrarii, luna_inregistrarii, ziua_inregistrarii))
            self.__card_service.adaugare_card(id_card, nume_client, prenume_client, cnp_client, data_nasterii,
                                            data_inregistrarii)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def ui_stergere_card(self):
        try:
            id_de_stergere = input("Dati id-ul de sters")
            self.__card_service.stergere_card(id_de_stergere)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)

    def ui_modificare_card(self):
        try:
            id_de_modificat = input("Dati id-ul cardului de modificat")
            nume_client = input("Dati numele clientului")
            prenume_client = input("Dati prenumele ")
            cnp_client = int(input("Dati cnp "))
            ziua_nasterii = int(input("ziua nasterii:"))
            luna_nasterii = int(input("luna nasterii:"))
            anul_nasterii = int(input("anul nasterii:"))
            data_nasterii = str(datetime.datetime(anul_nasterii, luna_nasterii, ziua_nasterii))
            ziua_inregistrarii = int(input("ziua inregistrarii:"))
            luna_inregistrarii = int(input("luna inregistrarii:"))
            anul_inregistrarii = int(input("anul inregistrarii:"))
            data_inregistrarii = str(datetime.datetime(anul_inregistrarii, luna_inregistrarii, ziua_inregistrarii))

            self.__card_service.modificare_card(id_de_modificat, nume_client, prenume_client, cnp_client, data_nasterii,
                                              data_inregistrarii)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def ui_print_carduri(self):
        carduri = self.__card_service.get_all_service()
        for card in carduri:
            print(card)

    def ui_run_crud_tranzactii(self):
        while True:
            print("1.Adaugare tranzactie")
            print("2.Stergere tranzactie")
            print("3.Modificare tranzactie")
            print("____________________________")
            print("a.AFISAREA TRANZACTIILOR")
            print("x.INAPOI IN MENIU")

            optiune = input("Selectati optiunea")
            if optiune == "1":
                self.ui_adaugare_tranzactie()
            elif optiune == "2":
                self.ui_stergere_tranzactie()
            elif optiune == "3":
                self.ui_modificare_tranzactie()

            elif optiune == "a":
                self.ui_print_tranzactii()
            elif optiune == "x":
                break
            else:
                print("Nu e o optiune")

    def ui_adaugare_tranzactie(self):
        try:
            id = input("Dati id-ul tranzactie")
            id_masina = input("Dati id-ul masinii")
            id_card_client = input("Dati id-ul cardului client")
            suma_piese = int(input("Dati suma de piese"))
            suma_manopera = int(input("Dati suma de manopera"))
            ziua_tranzactie = int(input("ziua tranzactiei:"))
            luna_tranzactie = int(input("luna tranzactiei:"))
            anul_tranzactie = int(input("anul tranzactiei:"))
            ora_tranzactiei=int(input("Dati ora"))
            minutul_tranzactiei = int(input("Dati minutul"))

            data_si_ora = datetime.datetime(anul_tranzactie, luna_tranzactie, ziua_tranzactie,ora_tranzactiei,minutul_tranzactiei)

            self.__tranzactie_service.adaugare_tranzactie(id, id_masina, id_card_client, suma_piese, suma_manopera, data_si_ora)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def ui_stergere_tranzactie(self):
        try:
            id_de_stergere = input("Dati id-ul de sters")
            self.__tranzactie_service.stergere_tranzactie(id_de_stergere)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)

    def ui_modificare_tranzactie(self):
        try:
            id = input("Dati id-ul tranzactiei de modificat" )
            id_masina=input("Dati id-ul nou al masinii sau enter daca nu se modifica")
            id_card_client=input("Dati id-ul nou al cardului sau enter daca nu se modifica")
            suma_piese = int(input("Dati suma de piese sau sau 0 daca nu se modifica"))
            suma_manopera = int(input("Dati suma de manopera sau 0 daca nu se modifica"))
            data_si_ora = input("Dati data si ora sau enter daca nu se modifica")
            self.__tranzactie_service.modificare_tranzactie(id,id_masina,id_card_client, suma_piese, suma_manopera, data_si_ora)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def ui_print_tranzactii(self):
        tranzactii = self.__tranzactie_service.get_all()
        for tranzactie in tranzactii:
            print(tranzactie)


