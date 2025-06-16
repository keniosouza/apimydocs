# Importação de bibliotecas
from fastapi import APIRouter, status, Depends, HTTPException, Query

# Controller com as regras de negócio para companies
from api.v1.controllers.companies.companies_controller import CompaniesController

# Middleware para obter o usuário autenticado via JWT
from core.deps import get_current_user

# Inicializa o roteador para rotas de companies
router = APIRouter()

@router.get('/', status_code=status.HTTP_200_OK)
def index(current_user: dict = Depends(get_current_user)):

    """ Lista todas as companies com paginação. """

    # Instânciamento do controller desejado
    companiesController = CompaniesController()

    # Busca as empresas cadastradas
    companies = companiesController.index()

    # Retorno da informação
    return {"data": companies}