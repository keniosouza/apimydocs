from api.v1.packages.products.actions.products.index_products_action import IndexProductsAction
from api.v1.packages.products.actions.products.save_product_action import SaveProductAction
from api.v1.packages.products.actions.products.show_product_action import ShowProductAction
from api.v1.packages.products.repositories.products.delete_product import DeleteProduct
from api.v1.packages.products.schemas.products_schema import ProductSchemaBase


class ProductsService:

    def index(self):

        # Instânciamento de ações
        indexProductsAction = IndexProductsAction()

        # Retorna todos produtos desejados
        return indexProductsAction.execute()

    def save(self, product : ProductSchemaBase):

        # Instânciamento de ações
        saveProductAction = SaveProductAction()

        # Retorna o resultado da operação
        return  saveProductAction.execute(product)

    def show(self, product : ProductSchemaBase):

        # Instânciamento de repositório
        showProduct = ShowProductAction()

        # Retorna o resultado da ação
        return showProduct.execute(product)

    def delete(self, product : ProductSchemaBase):

        # Instânciamento de ação
        deleteProduct = DeleteProduct()

        # Retorna o resultado da ação
        return deleteProduct.execute(product)