# Importação de bibliotecas
from api.v1.packages.companies.repositories.companies.show_company import ShowCompany
from core.base.base_action import BaseAction

"""
Busca uma empresa especifíca no sistema

Args:
    company_id (int): Id da empresa que deve ser bsucada.

Returns:
   List[Dict[str, str]]: Lista de dicionários com os dados das empresas.
"""


class ShowCompanyAction(BaseAction):
    # Método padrão de execução
    def execute(self, company_id: int):
        # Instânciamento do repositório
        showCompany = ShowCompany()

        # BUsca dos dados
        return showCompany.execute(company_id)
