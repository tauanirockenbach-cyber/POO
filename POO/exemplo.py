#classe em python
#class carro é o modelo de todos os carros do meu sistema
#def init é o metodo construtor, será executado sempre na criação de objetos
class carro:
    def __init__ (self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibir_dados(self):
        print("=== DADOS DO CARRO ===")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")

carro1 = carro("Suzuki","Jimmy", 2024)
carro2 = carro("Honda", "Civic", 2009)

carro1.exibir_dados()
print("-"*30)
carro2.exibir_dados()
print()