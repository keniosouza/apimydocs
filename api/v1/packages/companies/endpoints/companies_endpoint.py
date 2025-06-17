# Importação de bibliotecas
from fastapi import APIRouter, status, Depends, HTTPException, Query

# Controller com as regras de negócio para companies
from api.v1.packages.companies.controllers.companies_controller import CompaniesController
from api.v1.packages.companies.schemas.companies_schema import CompanySchemaBase

# Middleware para obter o usuário autenticado via JWT
from core.deps import get_current_user

# Inicializa o roteador para rotas de companies
router = APIRouter()

@router.post('/', status_code=status.HTTP_200_OK)
async def create(company : CompanySchemaBase, current_user: dict = Depends(get_current_user)):

    """ Lista todas as companies com paginação. """
    # Instânciamento do controller desejado
    companiesController = CompaniesController()

    # Busca as empresas cadastradas
    companies = companiesController.create(company)

    # Retorno da informação
    return {"data": companies}

@router.get('/', status_code=status.HTTP_200_OK)
async def index(current_user: dict = Depends(get_current_user)):

    """ Lista todas as companies com paginação. """
    # Instânciamento do controller desejado
    companiesController = CompaniesController()

    # Busca as empresas cadastradas
    companies = companiesController.index()

    # Retorno da informação
    return {"data": companies}

@router.get('/{company_id}', status_code=status.HTTP_200_OK)
async def show(company_id : int, current_user: dict = Depends(get_current_user)):

    """ Lista a empresa solicitada por id """
    # Instânciamento de controller desejado
    companiesController = CompaniesController()

    # Busca a empresa cadastrada
    company = companiesController.show(company_id)

    # Retorno da informação
    return {"data": company}

@router.delete('/{company_id}', status_code=status.HTTP_200_OK)
async def delete(company_id : int, current_user: dict = Depends(get_current_user)):

    """ Lista a empresa solicitada por id """
    # Instânciamento de controller desejado
    companiesController = CompaniesController()

    # Busca a empresa cadastrada
    company = companiesController.delete(company_id)

    # Retorno da informação
    return {"data": company}