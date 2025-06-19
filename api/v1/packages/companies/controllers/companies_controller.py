# Importação de bibliotecas
from core.utils.dynamic_import import DynamicImport
from api.v1.packages.companies.schemas.companies_schema import CompanySchemaBase


# Classe de companies
class CompaniesController:
    def __init__(self):
        # Importa a classe desejada
        CompaniesService = DynamicImport.service("companies", "CompaniesService")
        # Instânciamento de classe Service
        self.companiesService = CompaniesService()

    # Cria uma nova empresa
    def create(self, company: CompanySchemaBase):
        # Retorno da informação desejada
        return self.companiesService.create(company)

    # Lista todas as empresas
    def index(self):
        # Usa normalmente
        return self.companiesService.index()

    # Busca uma empresa especifíca
    def show(self, company_id: int):
        # Retorno da informação desejada
        return self.companiesService.show(company_id)

    # Remove uma empresa
    def delete(self, company_id: int):
        # Retorno da informação desejada
        return self.companiesService.delete(company_id)
