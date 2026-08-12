from database.conexao import Conexao
from datetime import datetime
from models.funcionario import Funcionario

def main():
    funcionario = Funcionario(nome="Tauani Krieser", cpf="123.456.789-00",
                              cargo="TI dev", departamento="TECH", salario=7000.0, data_admissao= datetime.today())

    print(funcionario)

if __name__ == "__main__":
    main()
    