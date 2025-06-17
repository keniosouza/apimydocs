# Importação de bibliotecas
from core.database import get_connection  # Conexão com MySQL via PyMySQL
from api.v1.packages.companies.schemas.companies_schema import CompanySchemaBase

"""
Classe de acesso direto à tabela `companies`.
Não deve conter validações ou lógica de negócio.
"""
class CreateCompany:

    def execute(self, company : CompanySchemaBase):

        """
        Retorna a empresa solicitada
        """
        conn = None
        cur = None
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("""
                        INSERT INTO companies (company_id,
                                           situation_id,
                                           nickname,
                                           name_business,
                                           name_fantasy,
                                           cnpj,
                                           cns,
                                           site,
                                           telephone,
                                           cellphone,
                                           email,
                                           password,
                                           responsible,
                                           responsible_office,
                                           cep,
                                           state_id,
                                           city_id,
                                           district,
                                           complement,
                                           expiration_day,
                                           value_monthly,
                                           stations,
                                           start_contract,
                                           first_payment,
                                           history,
                                           date_register,
                                           date_update)
                        VALUES (%s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s)
                        """, (company.company_id,
                              company.situation_id,
                              company.nickname,
                              company.name_business,
                              company.name_fantasy,
                              company.cnpj,
                              company.cns,
                              company.site,
                              company.telephone,
                              company.cellphone,
                              company.email,
                              company.password,
                              company.responsible,
                              company.responsible_office,
                              company.cep,
                              company.state_id,
                              company.city_id,
                              company.district,
                              company.complement,
                              company.expiration_day,
                              company.value_monthly,
                              company.stations,
                              company.start_contract,
                              company.first_payment,
                              company.history,
                              company.date_register,
                              company.date_update))
            conn.commit()
            return True
        except KeyError as e:
            raise e
        except Exception as e:
            if conn: conn.rollback()
            raise RuntimeError(f"Erro ao criar empresa: {e}")
        finally:
            if cur: cur.close()
            if conn: conn.close()
