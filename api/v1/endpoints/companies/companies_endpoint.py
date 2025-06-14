from typing import List
from fastapi import APIRouter, status, Depends, HTTPException, Query
from fastapi.responses import JSONResponse

# Schemas para entrada e saída de dados
from api.v1.schemas.companies.companies_schema import (
    CompanySchemaBase,
    CompanySchemaList,
    CompanyPaginationSchema
)

# Controller com as regras de negócio para companies
from api.v1.controllers.companies.companies_controller import (
    get_all_companies,
    get_company_by_id,
    count_companies
)

# Middleware para obter o usuário autenticado via JWT
from core.deps import get_current_user

# Inicializa o roteador para rotas de companies
router = APIRouter()


# ---------------------- ROTAS DE CONSULTA DE companies ----------------------

@router.get('/', response_model=CompanyPaginationSchema)
def list_companies(
    skip: int = Query(0, ge=0), 
    limit: int = Query(10, ge=1),
    current_user: dict = Depends(get_current_user)
):
    """
    Lista todas as companies com paginação.
    """
    companies = get_all_companies(skip=skip, limit=limit)
    total = count_companies()

    return {
        "total": total,
        "skip": skip,
        "limit": limit,
        "data": companies
    }


@router.get('/{company_id}', response_model=CompanySchemaBase, status_code=status.HTTP_200_OK)
def get_company(company_id: int, current_user: dict = Depends(get_current_user)):
    """
    Retorna os dados detalhados de uma empresa específica pelo ID.
    """
    company = get_company_by_id(company_id)
    if company:
        return company

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Empresa não encontrada."
    )
