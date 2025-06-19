# Importação de bibliotecas
from fastapi import HTTPException, status
from api.v1.packages.companies.services.companies_service import CompaniesService


# Classe de companies
class CompaniesController:
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
                detail=f"Erro interno ao listar empresas: {e}",
            )
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Erro inesperado ao listar empresas: {e}",
            )

    # Lista todas as empresas
    def show(self):
        try:
            # Instânciamento de classe Service
            companiesService = CompaniesService()

            # Retorno da informação desejada
            return companiesService.show()

        except RuntimeError as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Erro interno ao listar empresa: {e}",
            )
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Erro inesperado ao listar empresa: {e}",
            )
