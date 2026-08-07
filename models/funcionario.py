from database.conexao import Conexao
from datetime import datetime

#classe Funcionario
class Funcionario:
    def __init__(self, id_funcionario = None, nome = "", cpf = "", rg = "", data_nascimento = None, sexo = "", estado_civil = "", email = "", telefone = "", celular = "",
                 cargo = "", departamento = "", salario = 0.0, data_admissao = "", data_demissao = "", turno = "", status = "ATIVO", observacoes = ""):
        self.id_funcionario = id_funcionario
        self.nome = nome
        self.cpf = cpf
        self.rg = rg
        self.data_nascimento = data_nascimento
        self.sexo = sexo
        self.estado_civil = estado_civil
        self.email = email
        self.telefone = telefone
        self.celular = celular
        self.cargo = cargo
        self.departamento = departamento
        self.salario = salario
        self.data_admissao = data_admissao
        self.data_demissao = data_demissao
        self.turno = turno
        self.status = status
        self.observacoes = observacoes

    def __str__(self):
        print(f"\033[36m=== DADOS FUNCIONÁRIO ===\033[0m")
        print()
        return (
        f"Funcionário: {self.nome}\n"
        f"CPF do funcionário: {self.cpf}\n"
        f"RG do funcionário: {self.rg}\n"
        f"Data de nascimento do funcionário: {self.data_nascimento}\n"
        f"Sexo do funcionário: {self.sexo}\n"
        f"Estado civil do funcionário: {self.estado_civil}\n"
        f"E-mail do funcionário: {self.email}\n"
        f"Telefone do funcionário: {self.telefone}\n"
        f"Celular do funcionário: {self.celular}\n"
        f"Cargo do funcionário: {self.cargo}\n"
        f"Departamento do funcionário: {self.departamento}\n"
        f"Salário do funcionário: {self.salario}\n"
        f"Data de admissão do funcionário: {self.data_admissao}\n"
        f"Data de demissão do funcionário: {self.data_demissao}\n"
        f"Turno: {self.turno}\n"
        f"Status: {self.status}\n"
        f"Observações: {self.observacoes}\n"
        f"{'='*30}"
    )


 