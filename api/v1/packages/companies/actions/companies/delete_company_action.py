# Importação de bibliotecas
from api.v1.packages.companies.repositories.delete_company import DeleteCompany

# Classe responsável por lista todos os registros
class DeleteCompanyAction:

    # Método padrão de execução
    def execute(self, company_id : int):

        # Instânciamento do repositório
        deleteCompany = DeleteCompany()

        # BUsca dos dados
        return deleteCompany.execute(company_id)