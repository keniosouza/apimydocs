from api.v1.packages.products.schemas.products_schema import ProductSchemaBase
from api.v1.packages.products.repositories.products.show_product import ShowProduct
from core.base.base_action import BaseAction

class ShowProductAction(BaseAction):

    def execute(self, product: ProductSchemaBase):

        # Instânciamento do repositório
        showProduct = ShowProduct()

        # Retorna os dados localizados
        return showProduct.execute(product)