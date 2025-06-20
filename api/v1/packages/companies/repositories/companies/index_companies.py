# Importação de bibliotecas
from core.base.base_repository import BaseRepository


class IndexCompanies(BaseRepository):
    """
    Classe de acesso direto à tabela `companies`.
    Não deve conter validações ou lógica de negócio.
    """

    # Executa a ação em si
    def execute(self):
        # Realiza a busca de todos os registros
        self.cursor.execute(""" SELECT *
                                FROM companies """)

        # Realiza o commit da transação
        self.commit()

        # Retorno da informação desejada
        return [dict(row) for row in self.cursor.fetchall()]
