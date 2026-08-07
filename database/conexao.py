#Guarda a conexão com o banco de dados e fornece métodos para commit, rollback e fechamento da conexão
import os
import psycopg
from dotenv import load_dotenv

load_dotenv() #carrega as variáveis de ambiente do arquivo .env

class Conexao:
    
    def __init__(self):
        self.host = os.getenv("DB_HOST")
        self.port = os.getenv("DB_PORT")
        self.database = os.getenv("DB_NAME")
        self.user = os.getenv("DB_USER")
        self.password = os.getenv("DB_PASSWORD")
        self.conexao = psycopg.connect(
            host=self.host,
            port=self.port,
            dbname=self.database,
            user=self.user,
            password=self.password
        )

        self.cursor = self.conexao.cursor()
# commit = consolida as alterações feitas na transação atual no banco de dados
    def commit(self):
        self.conexao.commit()
# roollback = desfaz as alterações feitas na transação atual no banco de dados
    def rollback(self):
        self.conexao.rollback()
# close = fecha a conexão com o banco de dados
    def fechar(self):
        self.cursor.close()
        self.conexao.close()