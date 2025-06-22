from core.base.base_repository import BaseRepository
from api.v1.packages.products.schemas.products_schema import ProductSchemaBase

class DeleteProduct(BaseRepository):

    def execute(self, product : ProductSchemaBase):

        # Realiza a remoção
        self.cursor.execute(""" DELETE FROM products p WHERE p.product_id = %s""", (product.product_id))

        # Comita a transação
        self.commit()

        return True