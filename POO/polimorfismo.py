#POLIMOFISMO
#OBJETOS DIFERENTES PODEM RESPONDeR AO MESMO MÉTODO
#TODOS POSSUEM O MÉTODO: FALAR
#MAS CADA UM FALA DIFERENTE -> EXEMPLO: CACHORROS
class cachorro:
    #def __init__(self):
    def falar(self):
        print("Au Au")
class gato:
    def falar(self):
        print("Miau Miau")
class vaca:
    def falar(self):
        print("Muuu Muuu")

def emitir_som(animal):
    animal.falar()

cachorro = cachorro()
gato = gato()
vaca = vaca()

emitir_som(cachorro)
emitir_som(gato)
emitir_som(vaca)