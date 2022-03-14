from copy import deepcopy

import jsonpickle

from Domain.entitate import Entitate


class FileRepository:
    def __init__(self, file_name):
        self.__file_name = file_name
        self.__storage = {}  # dictionar avand drept chei id-urile entitatilor si drept valori entitatile in sine

    def __read_file(self):
        try:
            with open(self.__file_name, "r") as fp:
                self.__storage = jsonpickle.decode(fp.read())
        except:
            self.__storage = {}

    def __write_file(self):
        with open(self.__file_name, "w") as fp:
            fp.write(jsonpickle.encode(self.__storage))

    def get_by_id(self, id_entitate):
        self.__read_file()
        if id_entitate in self.__storage:
            return deepcopy(self.__storage[id_entitate])
        return None

    def get_all(self):
        self.__read_file()
        return deepcopy(list(self.__storage.values()))

    def adaugare(self, entitate:Entitate):
        if self.get_by_id(entitate.id_entitate):
            raise KeyError("Exista deja o entitate cu id-ul ", entitate.id_entitate)
        self.__storage[entitate.id_entitate] = entitate
        self.__write_file()

    def stergere(self,id_de_sters):
        if self.get_by_id(id_de_sters)is None:
            raise KeyError(f'id-ul de sters {id_de_sters} nu exista')
        del self.__storage[id_de_sters]
        self.__write_file()

    def modificare(self, entitate:Entitate):
        if self.get_by_id(entitate.id_entitate) is None:
            raise KeyError(f' ID-ul {entitate.id_entitate} nu exista')
        self.__storage[entitate.id_entitate]=entitate
        self.__write_file()

