# Importação de bibliotecas
from api.v1.packages.companies.repositories.index_companies import IndexCompanies

"""
Lista as empresas cadastradas no sistema

Args:

Returns:
   List[Dict[str, str]]: Lista de dicionários com os dados das empresas.
"""
class IndexCompaniesAction:

    # Método padrão de execução
    def execute(self):

        # Instância o repositório
        indexCompanies = IndexCompanies()

        # Busca dos dados
        return indexCompanies.execute()