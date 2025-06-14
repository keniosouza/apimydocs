# core/security.py

from passlib.context import CryptContext  # Contexto de criptografia de senhas
from passlib.exc import UnknownHashError  # Exceção para hashes não reconhecidos

# Define contexto de criptografia com esquema bcrypt
CRYPTO = CryptContext(schemes=['bcrypt'], deprecated='auto')

def verify_senha_api(plain_senha_api: str, hashed_senha_api: str) -> bool:
    """
    Compara a senha fornecida em texto puro com o hash armazenado.
    Retorna False em caso de erro ou formato inválido.
    """
    try:
        if not plain_senha_api or not hashed_senha_api:
            return False  # Garante que nenhum dos valores seja nulo ou vazio

        # Verifica se a senha corresponde ao hash
        return CRYPTO.verify(plain_senha_api, hashed_senha_api)

    except UnknownHashError:
        return False  # Hash inválido ou não reconhecido pelo passlib

    except Exception:
        return False  # Falha genérica na verificação

def hash_senha_api(plain_senha_api: str) -> str:
    """
    Gera o hash da senha em texto puro.
    """
    return CRYPTO.hash(plain_senha_api)  # Retorna a senha criptografada com bcrypt
