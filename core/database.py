import pymysql
from urllib.parse import urlparse, unquote
from core.configs import settings
from core.utils.config import Config

def get_connection():
    """
    Constrói e retorna uma conexão com o banco MySQL
    utilizando os dados da URL definida nas configurações.
    """

    # Obtem as configurações de banco de dados
    database = Config.get()

    # Cria e retorna a conexão com o banco de dados
    return pymysql.connect(
        host=database.mysql.host,
        port=database.mysql.port,
        user=database.mysql.user,
        password=database.mysql.password,
        database=database.mysql.name,
        charset=database.mysql.charset,  # Compatível com emojis e caracteres especiais
        cursorclass=pymysql.cursors.DictCursor  # Retorna resultados como dicionários
    )
