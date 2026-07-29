#HERENCA
#Suponha que exista vários veículos
#Todos possuem: rodas, acelera, frear
#Logo, não faz sentido repetir código.
#Podemos criar uma classe geral
#DEPOIS FAZEMOS OUTRAS CLASSES HERDAREM DELA.

class veiculo:
    def __init__(self, rodas):
        self.rodas = rodas
    def acelerar(self):
        print(f"O{self.marca} {self.modelo} de {self.rodas} rodas acelerou!")

#FILHO
#O carro herda tudo da classe veículo
#É obrigatorio a declaração class filha(nome da classe pai)
#herança multipla -> class carroeletrico(carro, veiculo, ...)
class carro(veiculo):
    def __init__(self, marca, modelo):
        super().__init__(4) #executa o construtor da classe pai
        self.marca = marca
        self.modelo = modelo
        print(f"Criando um carro{self.marca} com {self.rodas} rodas.")


carro1 = carro(" toyota", "supra")
carro1.acelerar()