# Importação de bibliotecas
import traceback
from fastapi import HTTPException, status
from api.v1.packages.companies.services.companies_service import CompaniesService
from api.v1.packages.companies.schemas.companies_schema import CompanySchemaBase

# Classe de companies
class CompaniesController:

    # Lista todas as empresas
    def create(self, company : CompanySchemaBase):
        try:

            # Instânciamento de classe Service
            companiesService = CompaniesService()

            # Retorno da informação desejada
            return companiesService.create(company)

        except RuntimeError as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Erro interno ao criar empresas: {e}"
            )
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail={
                    "error_type": type(e).__name__,
                    "message": str(e),
                    "args": e.args,
                    "trace": traceback.format_exc()
                }
            )

    # Lista todas as empresas
    def index(self):
        try:

            # Instânciamento de classe Service
            companiesService = CompaniesService()

            # Retorno da informação desejada
            return companiesService.index()

        except RuntimeError as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Erro interno ao listar empresas: {e}"
            )
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Erro inesperado ao listar empresas: {e}"
            )

    # Lista todas as empresas
    def show(self, company_id : int):
        try:

            # Instânciamento de classe Service
            companiesService = CompaniesService()

            # Retorno da informação desejada
            return companiesService.show(company_id)

        except RuntimeError as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Erro interno ao listar empresa: {e}"
            )
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Erro inesperado ao listar empresa: {e}"
            )

    # Lista todas as empresas
    def delete(self, company_id: int):
        try:

            # Instânciamento de classe Service
            companiesService = CompaniesService()

            # Retorno da informação desejada
            return companiesService.delete(company_id)

        except RuntimeError as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Erro interno ao listar empresa: {e}"
            )
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Erro inesperado ao listar empresa: {e}"
            )