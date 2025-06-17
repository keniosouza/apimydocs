# Importação de bibliotecas
from core.database import get_connection  # Conexão com MySQL via PyMySQL

"""
Classe de acesso direto à tabela `companies`.
Não deve conter validações ou lógica de negócio.
"""
class ShowCompany:

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

            cur.execute("""
                        SELECT * FROM companies c where c.company_id = %s
                    """, (company_id,))

            return [dict(row) for row in cur.fetchall()]
        except Exception as e:
            raise RuntimeError(f"Erro ao listar empresas: {e}")
        finally:
            if cur: cur.close()
            if conn: conn.close()
