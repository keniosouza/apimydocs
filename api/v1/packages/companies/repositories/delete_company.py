# Importação de bibliotecas
from core.database import get_connection  # Conexão com MySQL via PyMySQL

""" Classe para remoção de um registro """
class DeleteCompany:

    @staticmethod
    def execute(company_id : int):

        conn = None
        cur = None
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("DELETE FROM companies WHERE company_id = %s", (company_id,))
            conn.commit()
            return True
        except KeyError as e:
            raise e
        except Exception as e:
            if conn: conn.rollback()
            raise RuntimeError(f"Erro ao deletar empresa: {e}")
        finally:
            if cur: cur.close()
            if conn: conn.close()
