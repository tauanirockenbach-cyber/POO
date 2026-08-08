class Setor:
    def __init__(self, id, nome):
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
        print(f"ID: {self.id}")
        print(f"Nome setor: {self.nome}")

    @nome.setter
    def nome(self, novo_nome):
        if novo_nome =="":
            raise ValueError ("O Setor não pode estar vazio!")
        self.__nome = novo_nome

    