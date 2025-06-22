from api.v1.packages.products.schemas.products_schema import ProductSchemaBase
from api.v1.packages.products.repositories.products.create_product import CreateProduct
from core.base.base_action import BaseAction

class SaveProductAction(BaseAction):

    def execute(self, product : ProductSchemaBase):

        # Instância o repositório desejado
        createProduct = CreateProduct()

        # Executa o respositório desejado
        return createProduct.execute(product)