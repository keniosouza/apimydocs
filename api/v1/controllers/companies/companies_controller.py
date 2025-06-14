from typing import Optional
from fastapi import HTTPException, status

# Schemas atualizados para empresas
from api.v1.schemas.companies.companies_schema import (
    CompanySchemaBase,
    CompanySchemaList,
    CompanyPaginationSchema
)

# Model de acesso ao banco (MySQL) para empresas
from api.v1.models.companies.companies_model import CompanyModel

# Utilitário para sanitizar entradas, se necessário
from core.validation import InputSanitizer


# Lista todas as empresas com suporte a paginação
def get_all_companies(skip: int = 0, limit: int = 10) -> list[CompanySchemaList]:
    try:
        companies = CompanyModel.get_all_companies(skip=skip, limit=limit)
        return [CompanySchemaList(**c) for c in companies]
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


# Retorna a quantidade total de empresas
def count_companies() -> int:
    try:
        return CompanyModel.count_companies()
    except RuntimeError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro ao contar empresas: {e}"
        )


# Busca uma empresa específica pelo ID
def get_company_by_id(company_id: int) -> CompanySchemaBase:
    try:
        company = CompanyModel.get_by_id(company_id)
        if not company:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Empresa com ID {company_id} não encontrada."
            )
        return CompanySchemaBase(**company)
    except RuntimeError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro interno ao buscar empresa por ID: {e}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro inesperado ao buscar empresa por ID: {e}"
        )
