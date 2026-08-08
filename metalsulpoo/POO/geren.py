#Sistema de gerenciamento de tarefas(aplicar a programação estruturada)
def exibir_menu():
    print("\n"+"="*30)
    print("SISTEMA DE TAREFAS")
    print("="*30)
    print("1. Listar tarefa")
    print("2. Adicionar tarefa")
    print("3. Concluir tarefa")
    print("4. Remover tarefa")
    print("5. Sair")
    print("="*30)

#função para listar tarefas
def listar_tarefas(tarefas):
    """Mostra todas as tarefas cadastradas e seus status"""
    print("\n ---  LISTA DE TAREFAS ---")
    if not tarefas:
        print("Nenhuma tarefa.")
        return 
    for indice, tarefa in enumerate(tarefas, start=1):
        status = "concluido" if tarefa ['concluida'] else "pendentes"
        print(f"{indice}. [{status}] {tarefa['descricao']}")

def adicionar_tarefa (tarefas):
    """adicionar uma nova tarefa """
    descricao = input("\nDigite a descrição da tarefa: ")
    if descricao:
        nova_tarefa = {"descricao":descricao, "concluida":False}
        tarefas.append(nova_tarefa)
        print(f"tarefa '{descricao}' adicionada com sucesso!")
    else:
        print("A descrição não pode estar vazia!")

def concluir_tarefa(tarefas):
    """marcar tarefa como concluida"""
    listar_tarefas(tarefas)
    if not tarefas:
        return
    try:
        escolha = int(input("\nDigite o número da tarefa que deseja concluir: "))
        if 1 <= escolha <= len(tarefas):
            tarefas[escolha -1]["concluida"]= True
            print("Tarefas marcada como concluida!")
    except ValueError:
        print("Por favor, digite um número válido!")

def remover_tarefa(tarefas):
    """Remove tarefas da lista"""
    listar_tarefas(tarefas)
    if not tarefas:
        return
    try:
        escolha = int(input("\nDigite o número da tarefa que deseja remover: "))
        if 1 <= escolha <= len(tarefas):
            tarefas_removida = tarefas.pop(escolha-1)
            print(f"Tarefa' {tarefas_removida['descricao']} 'removida com sucesso!")
        else:
            print("Número de tarefa inválida!")
    except ValueError:
        print("Por favor, digite um número válido.")

def main():
    tarefas = []
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção(1-5): ")
        if opcao =="1":
            listar_tarefas(tarefas)
        elif opcao =="2": 
            adicionar_tarefa(tarefas)
        elif opcao =="3":
            concluir_tarefa(tarefas)
        elif opcao =="4":
            remover_tarefa(tarefas)
        elif opcao =="5":
            print("\nSaindo do sistema. xauuu")
            break
        else:
            print("\nOpcao inválida!")
          
main()