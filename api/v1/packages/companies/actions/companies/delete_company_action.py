# Importação de bibliotecas
from api.v1.packages.companies.repositories.companies.delete_company import DeleteCompany
from core.base.base_action import BaseAction


# Classe reponsável por remover uma empresa
class DeleteCompanyAction(BaseAction):
    # Método padrão de execução
    def execute(self, company_id: int):
        # Instânciamento do repositório
        deleteCompany = DeleteCompany()

        # BUsca dos dados
        return deleteCompany.execute(company_id)
