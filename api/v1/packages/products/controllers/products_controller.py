# Importação de bibliotecas
from core.utils.dynamic_import import DynamicImport
from api.v1.packages.products.schemas.products_schema import ProductSchemaBase

class ProductsController:

    def __init__(self):
        # Importação da classe desejad
        ProductsService = DynamicImport.service("products", "ProductsService")

        # Intânciamento da classe service
        self.productsService = ProductsService()

    def index(self):

        # Lista todos os produtos
        return self.productsService.index()

    def create(self, product : ProductSchemaBase):

        # Retorna o resultado da operação
        return self.productsService.save(product)

    def show(self, product : ProductSchemaBase):

        # Retorna o resultado da operação
        return self.productsService.show(product)

    def delete(self, product : ProductSchemaBase):

        # Retorna o resultado da operação
        return self.productsService.delete(product)