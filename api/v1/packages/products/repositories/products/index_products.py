# Importação de bibliotecas
from core.base.base_repository import BaseRepository

class IndexProducts(BaseRepository):

    def execute(self):

        # Busca todas os produtos
        self.cursor.execute(""" SELECT * FROM products p""")

        # Encerra a transação
        self.commit()

        # Retorno da informação desejada
        return [dict(row) for row in self.cursor.fetchall()]