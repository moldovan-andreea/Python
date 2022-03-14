class MasinaValidator:
    def valideaza(self, masina):
        erori=[]
        if masina.an_achizitie <=0:
            erori.append("Eroare la introducerea datelor: anul de achizitie trebuie sa fie pozitiv")
        elif masina.nr_km <=0:
            erori.append("Eroare la introducerea datelor: nr de km trebuie sa fie pozitiv")
        elif len(erori)>0:
            raise KeyError(erori)
