# Importação de bibliotecas
from api.v1.packages.companies.repositories.companies.index_companies import IndexCompanies
from core.base.base_action import BaseAction


class IndexCompaniesAction(BaseAction):
    """
    Lista as empresas cadastradas no sistema

    Args:

    Returns:
       List[Dict[str, str]]: Lista de dicionários com os dados das empresas.
    """

    # Método padrão de execução
    def execute(self):
        # Instância o repositório
        indexCompanies = IndexCompanies()

        # Busca dos dados
        return indexCompanies.execute()
