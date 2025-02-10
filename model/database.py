import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
from os import getenv

class Database:
    def __init__(self):
            load_dotenv()
            self.host = getenv('DB_HOST')
            self.username = getenv('DB_USER')
            self.password = getenv('DB_PSWD')
            self.name = getenv('DB_NAME')
            self.connection = None
            self.cursos = None

    def conectar(self):
        """Estabelece uma conexão com o banco de dados."""
        try: 
             self.connection = mysql.connector.connect(
                host = self.host,
                user = self.username,
                password = self.password,
                name =  self.name
             )