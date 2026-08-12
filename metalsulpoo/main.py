from database.conexao import Conexao
from datetime import datetime
from models import funcionario
from models.funcionario import Funcionario
from repositories.funcionario_repository import FuncionarioRepository
from menu import Menu

def main():
    menu = Menu()
    menu.exibir_menu()

#     # Definição das cores ANSI em tons de azul (degradê)
#     AZUL_CLARO = "\033[1;36m"   
#     AZUL_MEDIO = "\033[1;34m"   
#     AZUL_ESCURO = "\033[34m"    
#     RESET = "\033[0m"           

#     print("\n\033[34m--- BUSCANDO FUNCIONÁRIO PELO ID ---\033[0m")
#     repository = FuncionarioRepository()
#     funcionario = repository.buscar_por_id(4)
    
#     if funcionario:
#         # Divide as linhas do __str__ do funcionário para aplicar o degradê por linha
#         linhas = str(funcionario).split('\n')
#         for i, linha in enumerate(linhas):
#             if i % 3 == 0:
#                 print(f"{AZUL_CLARO}{linha}{RESET}")
#             elif i % 3 == 1:
#                 print(f"{AZUL_MEDIO}{linha}{RESET}")
#             else:
#                 print(f"{AZUL_ESCURO}{linha}{RESET}")
#     else:
#         print("Funcionário não encontrado.")
#     repository.fechar()

#     print("===============================================")
#     print("\n\033[46m--- LISTANDO FUNCIONÁRIOS ---\033[0m")
    
#     repository = FuncionarioRepository()
#     funcionarios = repository.listar()
    
#     if funcionarios:
#         # Aplica o degradê alternando a cor de cada funcionário da lista
#         for i, func in enumerate(funcionarios):
#             if i % 3 == 0:
#                 print(f"{AZUL_CLARO}{func}{RESET}")
#             elif i % 3 == 1:
#                 print(f"{AZUL_MEDIO}{func}{RESET}")
#             else:
#                 print(f"{AZUL_ESCURO}{func}{RESET}")
#             print(f"{AZUL_MEDIO}-----------------------------------{RESET}")
            
#     repository.fechar()

if __name__ == "__main__":
     main()


#     funcionario = Funcionario(
#     nome = "Luiza silva",
#     cpf = 7567445746,
#     rg = 576788669,
#     data_nascimento = datetime(2001, 7, 21),
#     sexo = "F",
#     estado_civil = "Casada",
#     email = "luiza.silva@gmail.com",
#     telefone = 156474678,
#     celular = 46456378,
#     cargo = "TI",
#     departamento = "Tecnologia",
#     salario = 5000.0,
#     data_admissao = datetime.today(),
#     data_demissao = None,
#     turno = "Tarde",
#     status = "ATIVO",
#     observacoes = "Funcionária dedicada e proativa, com excelente capacidade de trabalho em equipe.")
    
    # funcionario.__str__()
    # repository = FuncionarioRepository() #criação do objeto repository
    # repository.salvar(funcionario) #salvar o funcionário no banco de dados
    

        # print("\n--- ATUALIZANDO FUNCIONÁRIO ---")
        # # Altera alguma informação do objeto que você criou no início do main.py
        # funcionario.nome = "Tauani Krieser Alterado"
        # funcionario.id_funcionario = 1  # Garanta que o objeto tem o ID do banco que será atualizado
        
        # # Chama a função de atualizar do repositório
        # repository.atualizar(funcionario)

        # print("\n--- DELETANDO FUNCIONÁRIO ---")
        # repository.deletar(1)  # Apaga o funcionário que tem o ID 1 no banco