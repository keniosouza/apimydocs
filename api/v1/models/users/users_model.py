import pymysql
from core.database import get_connection
from datetime import date
from typing import Optional


class UserModel:
    """
    Classe de acesso direto à tabela `users` no MySQL.
    Nenhuma lógica de negócio deve estar aqui.
    """

    @staticmethod
    def get_by_email(email: str) -> dict | None:
        conn = None
        cur = None
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("""
                SELECT user_id, email, password, name
                FROM users
                WHERE email = %s
            """, (email,))
            row = cur.fetchone()
            return dict(row) if row else None
        except Exception as e:
            raise RuntimeError(f"Erro ao buscar usuário por e-mail: {e}")
        finally:
            if cur: cur.close()
            if conn: conn.close()

    @staticmethod
    def get_by_id(user_id: int) -> dict | None:
        conn = None
        cur = None
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("""
                SELECT *
                FROM users
                WHERE user_id = %s
            """, (user_id,))
            row = cur.fetchone()
            return dict(row) if row else None
        except Exception as e:
            raise RuntimeError(f"Erro ao buscar usuário por ID: {e}")
        finally:
            if cur: cur.close()
            if conn: conn.close()

    @staticmethod
    def count_users() -> int:
        conn = None
        cur = None
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("SELECT COUNT(*) AS total FROM users")
            return cur.fetchone()["total"]
        except Exception as e:
            raise RuntimeError(f"Erro ao contar usuários: {e}")
        finally:
            if cur: cur.close()
            if conn: conn.close()

    @staticmethod
    def get_all(skip: int = 0, limit: int = 10) -> list[dict]:
        conn = None
        cur = None
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("""
                SELECT *
                FROM users
                ORDER BY user_id
                LIMIT %s OFFSET %s
            """, (limit, skip))
            return [dict(row) for row in cur.fetchall()]
        except Exception as e:
            raise RuntimeError(f"Erro ao listar usuários: {e}")
        finally:
            if cur: cur.close()
            if conn: conn.close()

    @staticmethod
    def create(
        name: str,
        email: str,
        password: str,
        situation_id: int,
        permission_id: int,
        nickname: Optional[str] = None,
        office: Optional[str] = None,
        ctps: Optional[str] = None,
        ctps_serie: Optional[str] = None,
        pis: Optional[str] = None,
        date_birth: Optional[date] = None,
        date_admission: Optional[date] = None,
        history: Optional[str] = None
    ) -> dict:
        conn = None
        cur = None
        try:
            conn = get_connection()
            cur = conn.cursor()

            # Verifica duplicidade de e-mail
            cur.execute("SELECT 1 FROM users WHERE email = %s", (email,))
            if cur.fetchone():
                raise ValueError("E-mail já cadastrado.")

            cur.execute("""
                INSERT INTO users (
                    name, email, password, situation_id, permission_id,
                    nickname, office, ctps, ctps_serie, pis,
                    date_birth, date_admission, history
                ) VALUES (
                    %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s,
                    %s, %s, %s
                )
            """, (
                name, email, password, situation_id, permission_id,
                nickname, office, ctps, ctps_serie, pis,
                date_birth, date_admission, history
            ))

            conn.commit()
            user_id = cur.lastrowid

            return {
                "user_id": user_id,
                "name": name,
                "email": email,
                "nickname": nickname,
                "office": office,
                "date_birth": date_birth,
                "date_admission": date_admission
            }

        except Exception as e:
            if conn: conn.rollback()
            raise RuntimeError(f"Erro ao criar usuário: {e}")
        finally:
            if cur: cur.close()
            if conn: conn.close()

    @staticmethod
    def update(
        user_id: int,
        name: Optional[str],
        email: Optional[str],
        password: Optional[str],
        situation_id: Optional[int],
        permission_id: Optional[int],
        nickname: Optional[str],
        office: Optional[str],
        ctps: Optional[str],
        ctps_serie: Optional[str],
        pis: Optional[str],
        date_birth: Optional[date],
        date_admission: Optional[date],
        history: Optional[str]
    ) -> bool:
        conn = None
        cur = None
        try:
            conn = get_connection()
            cur = conn.cursor()

            # Verifica se o usuário existe
            cur.execute("SELECT 1 FROM users WHERE user_id = %s", (user_id,))
            if not cur.fetchone():
                raise KeyError("Usuário não encontrado.")

            updates = []
            values = []

            campos = {
                "name": name,
                "email": email,
                "password": password,
                "situation_id": situation_id,
                "permission_id": permission_id,
                "nickname": nickname,
                "office": office,
                "ctps": ctps,
                "ctps_serie": ctps_serie,
                "pis": pis,
                "date_birth": date_birth,
                "date_admission": date_admission,
                "history": history
            }

            for campo, valor in campos.items():
                if valor is not None:
                    if campo == "email":
                        cur.execute("SELECT 1 FROM users WHERE email = %s AND user_id != %s", (valor, user_id))
                        if cur.fetchone():
                            raise ValueError("E-mail já em uso por outro usuário.")
                    updates.append(f"{campo} = %s")
                    values.append(valor)

            if not updates:
                return False

            query = f"UPDATE users SET {', '.join(updates)} WHERE user_id = %s"
            values.append(user_id)
            cur.execute(query, values)
            conn.commit()
            return True

        except (KeyError, ValueError) as e:
            raise e
        except Exception as e:
            if conn: conn.rollback()
            raise RuntimeError(f"Erro ao atualizar usuário: {e}")
        finally:
            if cur: cur.close()
            if conn: conn.close()

    @staticmethod
    def delete(user_id: int) -> bool:
        conn = None
        cur = None
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("SELECT 1 FROM users WHERE user_id = %s", (user_id,))
            if not cur.fetchone():
                raise KeyError("Usuário não encontrado.")
            cur.execute("DELETE FROM users WHERE user_id = %s", (user_id,))
            conn.commit()
            return True
        except KeyError as e:
            raise e
        except Exception as e:
            if conn: conn.rollback()
            raise RuntimeError(f"Erro ao deletar usuário: {e}")
        finally:
            if cur: cur.close()
            if conn: conn.close()
