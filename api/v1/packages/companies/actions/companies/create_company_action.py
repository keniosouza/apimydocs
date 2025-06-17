# Importação de bibliotecas
from api.v1.packages.companies.repositories.create_company import CreateCompany
from api.v1.packages.companies.schemas.companies_schema import CompanySchemaBase

# Classe responsável por lista todos os registros
class CreateCompanyAction:

    # Método padrão de execução
    def execute(self, company : CompanySchemaBase):

        # Instânciamento do repositório
        createCompany = CreateCompany()

        # BUsca dos dados
        return createCompany.execute(company)