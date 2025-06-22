from core.base.base_action import BaseAction
from api.v1.packages.products.schemas.products_schema import ProductSchemaBase
from api.v1.packages.products.repositories.products.delete_product import DeleteProduct

class DeleteProductAction(BaseAction):

    def execute(self, product : ProductSchemaBase):

        # Instânciamento de repoistório
        deleteProduct = DeleteProduct()

        # Retorna o resultado da operação
        return deleteProduct.execute(product)