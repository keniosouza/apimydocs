# Importação de bibliotecas
from api.v1.packages.companies.repositories.show_company import ShowCompany

# Classe responsável por lista todos os registros
class ShowCompanyAction:

    # Método padrão de execução
    def execute(self, company_id : int):

        # Instânciamento do repositório
        showCompany = ShowCompany

        # BUsca dos dados
        return showCompany.execute(company_id)