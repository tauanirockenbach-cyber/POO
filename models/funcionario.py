class Funcionario:
    def __init__(self, id, nome, cargo, salario, setor):
        self.__id = id
        self.__nome = nome
        self.__cargo = cargo
        self.__salario = salario
        self.__setor = setor

    def apresentar(self):
        print("ID: ",self.__id)
        print("Nome: ",self.__nome)
        print("Cargo: ",self.__cargo)
        print("Salario: ",self.__salario)
        print("Setor: ", self.setor.nome)

    def aumentar_salario(self, percentual):
        aumento = self.__salario * (percentual/100)
        self.__salario += aumento

    def trocar_cargo(self, novo_cargo):
        self.__cargo = novo_cargo

    @property
    def setor(self):
        return self.__setor


    #getters
    @property
    def id(self):
        return self.__id

    @property
    def nome(self):
            return self.__nome

    @property
    def cargo(self):
            return self.__cargo

    @property
    def salario(self):
            return self.__salario

    #setters
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @cargo.setter
    def cargo(self, cargo):
        self.__cargo = cargo

    @salario.setter
    def salario(self, valor):
        if valor <0:
             raise ValueError(f"O salario {valor} não pode ser negativo!")
        self.__salario = valor

        
