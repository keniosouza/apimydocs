from typing import Optional, List
from pydantic import BaseModel, EmailStr
from datetime import date

# Representa os dados básicos de um usuário retornado pela API
class UserSchemaBase(BaseModel):
    user_id: Optional[int] = None             # ID único do usuário
    name: Optional[str] = None                # Nome completo
    email: Optional[EmailStr] = None          # E-mail (com validação de formato)
    nickname: Optional[str] = None            # Nome de exibição (apelido)
    office: Optional[str] = None              # Cargo ou função
    date_birth: Optional[date] = None         # Data de nascimento
    date_admission: Optional[date] = None     # Data de admissão
    phone: Optional[str] = None               # Telefone (campo extra, caso utilizado)

    class Config:
        from_attributes = True  # Permite criar o schema a partir de dicts (mesmo sem ORM)


# Schema usado para criação de um novo usuário (campos obrigatórios)
class UserSchemaCreate(BaseModel):
    name: str                           # Nome completo obrigatório
    email: EmailStr                     # E-mail obrigatório
    password: str                       # Senha (será criptografada)
    situation_id: int                   # Situação (ex: ativo, inativo)
    permission_id: int                  # Permissão (perfil de acesso)
    nickname: Optional[str] = None
    office: Optional[str] = None
    ctps: Optional[str] = None
    ctps_serie: Optional[str] = None
    pis: Optional[str] = None
    date_birth: Optional[date] = None
    date_admission: Optional[date] = None
    history: Optional[str] = None


# Schema para atualização parcial de usuário
class UserSchemaUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    situation_id: Optional[int] = None
    permission_id: Optional[int] = None
    nickname: Optional[str] = None
    office: Optional[str] = None
    ctps: Optional[str] = None
    ctps_serie: Optional[str] = None
    pis: Optional[str] = None
    date_birth: Optional[date] = None
    date_admission: Optional[date] = None
    history: Optional[str] = None

    class Config:
        from_attributes = True


# Schema usado para listagem detalhada de usuários (ex: em rotas de admin)
class UserSchemaList(BaseModel):
    user_id: int
    situation_id: int
    permission_id: int
    nickname: Optional[str]
    name: Optional[str]
    date_birth: Optional[date]
    office: Optional[str]
    ctps: Optional[str]
    ctps_serie: Optional[str]
    pis: Optional[str]
    date_admission: Optional[date]
    email: Optional[EmailStr]
    password: Optional[str]
    history: Optional[str]

    class Config:
        from_attributes = True


# Schema usado para paginação de usuários
class UserPaginationSchema(BaseModel):
    total: int                       # Total de registros
    skip: int                        # Quantidade ignorada (offset)
    limit: int                       # Quantidade por página (limit)
    data: List[UserSchemaList]      # Lista paginada de usuários
