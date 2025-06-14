from fastapi import APIRouter  # Importa o gerenciador de rotas do FastAPI

# Importa os módulos de rotas específicos
from api.v1.endpoints.users import users_endpoint
from api.v1.endpoints.companies import companies_endpoint

# Cria uma instância do APIRouter que vai agregar todas as rotas da API
api_router = APIRouter()

# Inclui as rotas de "users" no roteador principal, com prefixo /users e tag 'Usuarios'
api_router.include_router(
    users_endpoint.router, prefix='/users', tags=['Usuários']
)

# Inclui as rotas de "c_caixa_item no roteador principal, com prefixo /c_caixa_items e tag 'Empresas'
api_router.include_router(
    companies_endpoint.router, prefix='/companies', tags=['Empresas']
)