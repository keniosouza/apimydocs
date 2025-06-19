# Importação de bibliotecas
from core.base.base_repository import BaseRepository


class ShowCompany(BaseRepository):
    """
    Classe de acesso direto à tabela `companies`.
    Não deve conter validações ou lógica de negócio.
    """

    def execute(self, company_id: int):
        # Realiza a busca do registro desejado
        self.cursor.execute(
            """SELECT * FROM companies c where c.company_id = %s""",
            (company_id,),
        )

        # Realiza o commit da transação
        self.commit()

        # Retorno da informação desejado
        return [dict(row) for row in self.cursor.fetchall()]
