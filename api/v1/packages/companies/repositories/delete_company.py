# Importação de bibliotecas
from core.base.base_repository import BaseRepository


class DeleteCompany(BaseRepository):
    """
    Classe de acesso direto à tabela `companies`.
    Não deve conter validações ou lógica de negócio.
    """

    def execute(self, company_id: int):
        # Remove o registro desejado
        self.cursor.execute(
            """DELETE
                               FROM companies c
                               where c.company_id = %s""",
            (company_id,),
        )

        # Realiza o commit da transação
        self.commit()
