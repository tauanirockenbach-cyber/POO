# ENCAPSULAMENTO = Prática de proteger os dados internos de uma classe, ocultando os detalhes de sua implementação.

class ContaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.__titular = titular      
        self.__saldo = saldo_inicial   #__ indica um atributo privado

    # Getter para o titular (permite apenas ler o nome)
    def get_titular(self):
        return self.__titular

    # Getter para o saldo (substitui ou complementa o mostrar_saldo)
    def get_saldo(self):
        return self.__saldo

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor  # Alteração interna segura
            print("Depósito realizado com sucesso!")
        else:
            print("Valor inválido.")

    def sacar_valor(self, valor):
        if 0 < valor <= self.__saldo:  # Verificação interna segura
            self.__saldo -= valor
            print("Saque realizado com sucesso!")
        else:
            print("Saldo insuficiente.")

    def mostrar_saldo(self):
        print(f"Titular atual: {self.__titular}")
        print(f"Saldo Atual: R${self.__saldo:.2f}")

# Exemplo de uso:
print("-"*30)
conta01 = ContaBancaria("João", 1000)
conta01.mostrar_saldo()
conta01.depositar(500)
conta01.mostrar_saldo()
conta01.sacar_valor(200)
conta01.mostrar_saldo()

print("-"*30)

conta02 = ContaBancaria("Tauani", 2000)
conta02.mostrar_saldo()

print("-"*30)
