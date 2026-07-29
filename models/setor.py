class Setor:
    def __init__(self,id, nome):
        self.__id = id
        self.__nome = nome

    @property
    def id(self):
        return self.__id
    @property
    def nome(self):
        return self.__nome
    @property
    def apresentar(self):
        print("=== SETOR ===")
        print(f"ID:{self.id}")
        print(f"Nome Setor:{self.nome}")