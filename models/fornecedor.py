class Fornecedor:
    def __init__(self, id, razao_social, cnpj, telefone, email):
        self.__id = id
        self.__razao_social = razao_social
        self.__cnpj = cnpj
        self.__telefone = telefone
        self.__email = email

        @property
        def id(self):
            return self.__id

        @property
        def razao_social(self):
            return self.__razao_social

        @property
        def cnpj(self):
            return self.__cnpj

        @property
        def telefone(self):
            return self.__telefone

        @property
        def email(self):
            return self.__email

        @razao_social.setter
        def razao_social(self, nome):
            if nome == "":
                raise ValueError("A razão social não pode estar vazia!")
            self.__razao_social = nome

        @telefone.setter
        def telefone(self, telefone):
            if telefone == "":
                raise ValueError("O telefone não pode estar vazio!")
            self.__telefone = telefone

        @email.setter
        def email(self, email):
            if email == "":
                raise ValueError("O email não pode estar vazio!")
            self.__email = email

        