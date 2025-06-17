# Importação de bibliotecas
from api.v1.packages.companies.services.companies_service import CompaniesService
from api.v1.packages.companies.schemas.companies_schema import CompanySchemaBase

# Classe de companies
class CompaniesController:

    # Cria uma nova empresa
    def create(self, company : CompanySchemaBase):

        # Instânciamento de classe Service
        companiesService = CompaniesService()

        # Retorno da informação desejada
        return companiesService.create(company)

    # Lista todas as empresas
    def index(self):

        # Instânciamento de classe Service
        companiesService = CompaniesService()

        # Retorno da informação desejada
        return companiesService.index()

    # Busca uma empresa especifíca
    def show(self, company_id : int):

        # Instânciamento de classe Service
        companiesService = CompaniesService()

        # Retorno da informação desejada
        return companiesService.show(company_id)

    # Remove uma empresa
    def delete(self, company_id: int):

        # Instânciamento de classe Service
        companiesService = CompaniesService()

        # Retorno da informação desejada
        return companiesService.delete(company_id)