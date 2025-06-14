from core.database import get_connection  # Conexão com MySQL via PyMySQL


class CompanyModel:
    """
    Classe de acesso direto à tabela `companies`.
    Não deve conter validações ou lógica de negócio.
    """

    @staticmethod
    def get_by_id(company_id: int) -> dict | None:
        """
        Retorna uma empresa pelo ID.
        """
        conn = None
        cur = None
        try:
            conn = get_connection()
            cur = conn.cursor()

            cur.execute("""
                SELECT company_id,
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
                       date_update
                FROM companies
                WHERE company_id = %s
            """, (company_id,))
            row = cur.fetchone()

            if row:
                return dict(row)
            return None
        except Exception as e:
            raise RuntimeError(f"Erro ao buscar empresa por ID: {e}")
        finally:
            if cur: cur.close()
            if conn: conn.close()

    @staticmethod
    def count_companies() -> int:
        """
        Retorna a quantidade total de empresas.
        """
        conn = None
        cur = None
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("SELECT COUNT(*) AS total FROM companies")
            return cur.fetchone()["total"]
        except Exception as e:
            raise RuntimeError(f"Erro ao contar empresas: {e}")
        finally:
            if cur: cur.close()
            if conn: conn.close()

    @staticmethod
    def get_all_companies(skip: int = 0, limit: int = 10) -> list[dict]:
        """
        Retorna lista paginada de empresas.
        """
        conn = None
        cur = None
        try:
            conn = get_connection()
            cur = conn.cursor()

            cur.execute("""
                SELECT company_id,
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
                       date_update
                FROM companies
                ORDER BY company_id
                LIMIT %s OFFSET %s
            """, (limit, skip))

            return [dict(row) for row in cur.fetchall()]
        except Exception as e:
            raise RuntimeError(f"Erro ao listar empresas: {e}")
        finally:
            if cur: cur.close()
            if conn: conn.close()
