# Importação de bibliotecas
from api.v1.packages.companies.repositories.index_companies import IndexCompanies

# Classe responsável por lista todos os registros
class IndexCompaniesAction:

    # Método padrão de execução
    def execute(self):

        # Instânciamento do repositório
        indexCompanies = IndexCompanies

        # BUsca dos dados
        return indexCompanies.execute()