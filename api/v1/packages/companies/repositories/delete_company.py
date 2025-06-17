# Importação de bibliotecas
from core.database import get_connection  # Conexão com MySQL via PyMySQL

"""
Classe de acesso direto à tabela `companies`.
Não deve conter validações ou lógica de negócio.
"""
class DeleteCompany:

    @staticmethod
    def execute(company_id : int):

        """
        Retorna a empresa solicitada
        """
        conn = None
        cur = None
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("SELECT 1 FROM companies WHERE company_id = %s", (company_id,))
            if not cur.fetchone():
                raise KeyError("Empresa não encontrado.")
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
