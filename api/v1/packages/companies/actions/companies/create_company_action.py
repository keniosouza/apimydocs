# Importação de bibliotecas
from api.v1.packages.companies.repositories.create_company import CreateCompany
from api.v1.packages.companies.schemas.companies_schema import CompanySchemaBase

# Classe reponsável por cadastrar uma nova empresa
class CreateCompanyAction:

    # Método padrão de execução
    def execute(self, company : CompanySchemaBase):

        # Instânciamento do repositório
        createCompany = CreateCompany()

        # Busca os dos dados
        return createCompany.execute(company)