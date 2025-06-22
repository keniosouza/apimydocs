# Importação de bibliotecas
from fastapi import APIRouter, status, Depends

# Controller com as regras de negócio do produto
from api.v1.packages.products.controllers.products_controller import ProductsController

# Schemas para vailidar as informações de entrada e saída
from api.v1.packages.products.schemas.products_schema import ProductSchemaBase

# Midleware para obter os dados do usuário autenticado
from core.deps import get_current_user

# Inicializar o roteaodr para as rotas de produtos
router = APIRouter()

# Instãnciamento do controller desejado
productsController = ProductsController()

@router.get("/", status_code=status.HTTP_200_OK)
async def index(current_user: dict = Depends(get_current_user)):
    # Busca todos os produtos cadastrados
    products = productsController.index()

    # Retornar os dados localizados
    return {
        "data": products
    }

@router.post('/', status_code=status.HTTP_201_CREATED)
async def index(product: ProductSchemaBase, current_user: dict = Depends(get_current_user)):

    # Salva o produto desejado
    product = productsController.create(product)

    # Retorna a informação desejada
    return {
        "data": product
    }

@router.get('/{product_id}', status_code=status.HTTP_200_OK)
async def index(product_id: int, current_user: dict = Depends(get_current_user)):
    # Armazena o produto id no Schema
    ProductSchemaBase.product_id = product_id

    # Salva o produto desejado
    products = productsController.show(ProductSchemaBase)

    # Retorna a informação desejada
    return {
        "data": products
    }

@router.delete('/{product_id}', status_code=status.HTTP_200_OK)
async def index(product_id : int, current_user: dict = Depends(get_current_user)):

    # Armazena o produto id no Schema
    ProductSchemaBase.product_id = product_id

    # Salva o produto desejado
    products = productsController.delete(ProductSchemaBase)

    # Retorna a informação desejada
    return {
        "data": products
    }