# Importa o gerenciador de rotas do FastAPI
from fastapi import APIRouter

# Importa os módulos de rotas específicos
from api.v1.packages.users.endpoints.users import users_endpoint
from api.v1.packages.companies.endpoints import companies_endpoint
from api.v1.packages.products.endpoints import procuts_endpoint

# Cria uma instância do APIRouter que vai agregar todas as rotas da API
api_router = APIRouter()

# Inclui as rotas de "users" no roteador principal, com prefixo /users e tag 'Usuarios'
api_router.include_router(users_endpoint.router, prefix="/users", tags=["Usuários"])

# Inclui as rotas de empresa
api_router.include_router(
    companies_endpoint.router, prefix="/companies", tags=["Empresas"]
)


# Inclui as rotas de produts
api_router.include_router(
    procuts_endpoint.router, prefix="/products", tags=["Produtos"]
)
