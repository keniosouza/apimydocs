# Importação de bibliotecas
from api.v1.packages.companies.actions.companies.index_companies_action import (
    IndexCompaniesAction,
)
from api.v1.packages.companies.actions.companies.show_company_action import (
    ShowCompanyAction,
)
from api.v1.packages.companies.actions.companies.delete_company_action import (
    DeleteCompanyAction,
)
from api.v1.packages.companies.actions.companies.create_company_action import (
    CreateCompanyAction,
)
from api.v1.packages.companies.schemas.companies_schema import CompanySchemaBase


# Controle da regra de negócio
class CompaniesService:
    # Método para listagem de empresas
    def create(self, company: CompanySchemaBase):
        # Instânciamento de action
        createCompanyAction = CreateCompanyAction()

        # Realiza a busca das empresas
        return createCompanyAction.execute(company)

    # Método para listagem de empresas
    def index(self):
        # Instânciamento de action
        indexCompaniesAction = IndexCompaniesAction()

        # Realiza a busca das empresas
        return indexCompaniesAction.execute()

    # Método para listar empresa especifica
    def show(self, company_id: int):
        # Instânciamento de action
        showCompanyAction = ShowCompanyAction()

        # Realiza a busca das empresas
        return showCompanyAction.execute(company_id)

    # Método para listar empresa especifica
    def delete(self, company_id: int):
        # Instânciamento de action
        deleteCompanyAction = DeleteCompanyAction()

        # Realiza a busca das empresas
        return deleteCompanyAction.execute(company_id)
