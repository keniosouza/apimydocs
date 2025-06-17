# Importação de bibliotecas
from core.database import get_connection

""" Repoistório para buscar todas as empresas """
class IndexCompanies:

    # Inicializa a class realizando a conexão com o banco de dados
    def __init__(self):
        self.cursor = get_connection().cursor()

    # Executa a ação em si
    def execute(self):

        # Realiza a busca de todos os registros
        self.cursor.execute(""" SELECT * FROM companies """)

        return [dict(row) for row in self.cursor.fetchall()]