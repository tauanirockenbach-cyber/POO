 #restrição por encapsulamento != validação
"""
        A distinção entre encapsular e validar é um pilar fundamental da Programação Orientada a Objetos, pois o encapsulamento, por si só, 
        apenas restringe os canais de acesso e modificação dos atributos. 
        A garantia de que um dado é íntegro e condizente com as regras do negócio permanece sob a responsabilidade do desenvolvedor, que deve programar os critérios de validação. 
        É exatamente por essa razão que métodos modificadores como set_nome(), 
        set_salario() e set_cargo() tornam-se indispensáveis: eles atuam como pontos centralizados de alteração dentro da classe, 
        o que viabiliza a implementação e a futura manutenção de regras de validação sem a necessidade de reescrever ou impactar o restante do sistema.
"""

from models.funcionario import Funcionario
from models.setor import Setor
from models.fornecedor import Fornecedor

try:
    fornecedor1 = Fornecedor(1, "Fornecedor A", "12345678901234", "123456789", "fornecedorA@email.com")
    fornecedor1.apresentar()
    setor1 = Setor(1,"TA")
    funcionario1 = Funcionario(1, "Matheus", "Dev", 5500.00, setor1)
    funcionario1.apresentar()
    print()

    funcionario1.salario = 70000.00   
    funcionario1.cargo = "DEV TATI"    
    funcionario1.nome = "Tauani" 

    print(funcionario1.nome)     
    print(funcionario1.salario)  
    print()

    funcionario1.apresentar()
    fornecedor1.razao_social = "Fornecedor B"
    fornecedor1.telefone = "987654321"
    fornecedor1.email = "fornecedorB@email.com"
    fornecedor1.apresentar()
except ValueError as e:
    print(f"Erro de validação: {e}")

