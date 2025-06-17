import pymysql
from urllib.parse import urlparse, unquote
from core.configs import settings

def get_connection():
    """
    Constrói e retorna uma conexão com o banco MySQL
    utilizando os dados da URL definida nas configurações.
    """

    # Faz o parse da URL do banco de dados
    parsed = urlparse(settings.DB_URL)

    # Extrai os dados individuais da URL
    user = parsed.username
    password = unquote(parsed.password or '')  # Decodifica senha com caracteres especiais
    host = parsed.hostname
    port = parsed.port or 3306  # Porta padrão do MySQL
    database = parsed.path.lstrip('/')  # Remove a barra inicial do caminho

    # Cria e retorna a conexão com o banco de dados
    return pymysql.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=database,
        charset='utf8mb4',  # Compatível com emojis e caracteres especiais
        cursorclass=pymysql.cursors.DictCursor  # Retorna resultados como dicionários
    )
