#integrando os 4 pilares do poo
class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.__salario = salario
    def mostrar_dados(self):
        print(f"Funcionario: {self.nome}")
    def calcular_bonus(self):
        return self.__salario *0.10 + self.__salario
    
class gerente(Funcionario):
    def calcular_bonus(self):
        return 5000
    
class desenvolvedor(Funcionario):
    def calcular_bonus(self):
        return 2000
    
gerente = gerente("Carlos", 1000)
dev = desenvolvedor("Ana", 8000)

gerente.mostrar_dados()
print("Bônus: ", gerente.calcular_bonus())

print("-"*30)

dev.mostrar_dados()
print("Bônus: ", dev.calcular_bonus())

