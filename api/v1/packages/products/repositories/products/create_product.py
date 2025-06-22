# Importação de bibliotecas
from core.base.base_repository import BaseRepository
from api.v1.packages.products.schemas.products_schema import ProductSchemaBase

class CreateProduct(BaseRepository):

    def execute(self, product : ProductSchemaBase):
        # Realiza a inserção do registro
        self.cursor.execute(
            """
            INSERT INTO products (product_id,
                                  user_id,
                                  situation_id,
                                  name,
                                  description,
                                  date_register,
                                  date_update)
            VALUES (%s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s)
            """,
            (
                product.product_id,
                product.user_id,
                product.situation_id,
                product.name,
                product.description,
                product.date_register,
                product.date_update
            ),
        )

        # Comita a transação
        self.commit()

        # Retorna como verdadeiro se for salvo com sucesso
        return True