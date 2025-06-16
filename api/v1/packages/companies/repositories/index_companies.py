from core.database import get_connection  # Conexão com MySQL via PyMySQL

class IndexCompanies:
    """
    Classe de acesso direto à tabela `companies`.
    Não deve conter validações ou lógica de negócio.
    """
    @staticmethod
    def execute():
        """
        Retorna lista paginada de empresas.
        """
        conn = None
        cur = None
        try:
            conn = get_connection()
            cur = conn.cursor()

            cur.execute("""
                SELECT * FROM companies
            """)

            return [dict(row) for row in cur.fetchall()]
        except Exception as e:
            raise RuntimeError(f"Erro ao listar empresas: {e}")
        finally:
            if cur: cur.close()
            if conn: conn.close()
