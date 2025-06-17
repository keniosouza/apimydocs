from fastapi import HTTPException, status
from typing import Optional

from api.v1.packages.users.schemas.users.users_schema import (
    UserSchemaBase,
    UserSchemaCreate,
    UserSchemaUpdate,
    UserSchemaList,
    UserPaginationSchema
)

from api.v1.packages.users.models.users.users_model import UserModel
from core.security import verify_senha_api, hash_senha_api
from core.validation import InputSanitizer


# Autentica usuário por e-mail e senha
def authenticate_user(email: str, password: str) -> Optional[dict]:
    email = InputSanitizer.clean_text(email)
    try:
        user = UserModel.get_by_email(email)
        if not user or not verify_senha_api(password, user["password"]):
            return None
        return user
    except RuntimeError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro interno ao autenticar: {e}"
        )


# Cria novo usuário com validações e hash da senha
def create_user(user_data: UserSchemaCreate) -> UserSchemaBase:
    try:
        # Sanitiza campos
        name = InputSanitizer.clean_text(user_data.name)
        email = InputSanitizer.clean_text(user_data.email)
        password = InputSanitizer.clean_text(user_data.password)

        # Validações
        if not InputSanitizer.is_valid_email(email):
            raise HTTPException(status_code=400, detail="E-mail inválido.")
        if not InputSanitizer.is_safe(name + email + password):
            raise HTTPException(status_code=400, detail="Dados maliciosos detectados.")

        hashed_password = hash_senha_api(password)

        result = UserModel.create(
            name=name,
            email=email,
            password=hashed_password,
            situation_id=user_data.situation_id,
            permission_id=user_data.permission_id,
            nickname=user_data.nickname,
            office=user_data.office,
            ctps=user_data.ctps,
            ctps_serie=user_data.ctps_serie,
            pis=user_data.pis,
            date_birth=user_data.date_birth,
            date_admission=user_data.date_admission,
            history=user_data.history
        )

        return UserSchemaBase(**result)

    except ValueError as e:
        raise HTTPException(status_code=409, detail=str(e))
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=f"Erro ao criar usuário: {e}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro inesperado: {e}")


# Retorna lista paginada de usuários
def get_all(skip: int = 0, limit: int = 10) -> UserPaginationSchema:
    try:
        users = UserModel.get_all(skip=skip, limit=limit)
        total = UserModel.count_users()
        return {
            "total": total,
            "skip": skip,
            "limit": limit,
            "data": [UserSchemaList(**u) for u in users]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao listar usuários: {e}")


# Retorna total de usuários
def count_users() -> int:
    try:
        return UserModel.count_users()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao contar usuários: {e}")


# Retorna um usuário específico pelo ID
def get_user_by_id(user_id: int) -> UserSchemaBase:
    try:
        user = UserModel.get_by_id(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="Usuário não encontrado.")
        return UserSchemaBase(**user)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao buscar usuário: {e}")


# Atualiza dados de um usuário
def update_user(user_id: int, user_data: UserSchemaUpdate) -> UserSchemaBase:
    try:
        # Sanitização condicional
        name = InputSanitizer.clean_text(user_data.name) if user_data.name else None
        email = InputSanitizer.clean_text(user_data.email) if user_data.email else None
        password = InputSanitizer.clean_text(user_data.password) if user_data.password else None
        hashed_password = hash_senha_api(password) if password else None

        # Segurança mínima
        if email and not InputSanitizer.is_valid_email(email):
            raise HTTPException(status_code=400, detail="E-mail inválido.")
        if any([name, email, password]) and not InputSanitizer.is_safe((name or '') + (email or '') + (password or '')):
            raise HTTPException(status_code=400, detail="Dados maliciosos detectados.")

        success = UserModel.update(
            user_id=user_id,
            name=name,
            email=email,
            password=hashed_password,
            situation_id=user_data.situation_id,
            permission_id=user_data.permission_id,
            nickname=user_data.nickname,
            office=user_data.office,
            ctps=user_data.ctps,
            ctps_serie=user_data.ctps_serie,
            pis=user_data.pis,
            date_birth=user_data.date_birth,
            date_admission=user_data.date_admission,
            history=user_data.history
        )

        if not success:
            raise HTTPException(status_code=400, detail="Nada foi alterado.")

        return get_user_by_id(user_id)

    except KeyError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except ValueError as e:
        raise HTTPException(status_code=409, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao atualizar usuário: {e}")


# Remove um usuário pelo ID
def delete_user(user_id: int) -> bool:
    try:
        success = UserModel.delete(user_id)
        if not success:
            raise HTTPException(status_code=404, detail="Usuário não encontrado para exclusão.")
        return True
    except KeyError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao excluir usuário: {e}")
