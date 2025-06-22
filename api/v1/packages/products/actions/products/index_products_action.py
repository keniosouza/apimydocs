from api.v1.packages.products.repositories.products.index_products import IndexProducts
from core.base.base_action import BaseAction

class IndexProductsAction(BaseAction):

    def execute(self):

        # Instânciamento de repositório
        indexProducts = IndexProducts()

        # Retorna todos produtos
        return indexProducts.execute()