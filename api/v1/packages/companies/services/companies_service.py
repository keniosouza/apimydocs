# Importação de bibliotecas
from api.v1.packages.companies.actions.companies.index_companies_action import IndexCompaniesAction

# Controle da regra de negócio
class CompaniesService:

    # Método para listagem de empresas
    def index(self):

        # Instânciamento de action
        indexCompaniesAction = IndexCompaniesAction()

        # Realiza a busca das empresas
        return indexCompaniesAction.execute()