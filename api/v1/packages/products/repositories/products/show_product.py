from core.base.base_repository import BaseRepository
from api.v1.packages.products.schemas.products_schema import ProductSchemaBase

class ShowProduct(BaseRepository):

    def execute(self, product : ProductSchemaBase):

        # Realiza a busca de um produto especificos
        self.cursor.execute(""" SELECT * FROM products p WHERE p.product_id = %s """, product.product_id)

        # Comita a transação
        self.commit()

        # Retorno da informação desejado
        return [dict(row) for row in self.cursor.fetchall()]