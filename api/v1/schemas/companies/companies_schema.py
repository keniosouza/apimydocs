from typing import Optional, List
from pydantic import BaseModel, EmailStr
from datetime import date, datetime

# Schema base usado para representar uma empresa retornada pela API
class CompanySchemaBase(BaseModel):
    company_id: Optional[int] = None                     # ID da empresa
    situation_id: int                                    # Situação (ativo, inativo, etc.)
    nickname: Optional[str] = None                       # Nome reduzido ou de exibição
    name_business: Optional[str] = None                  # Nome empresarial (razão social)
    name_fantasy: Optional[str] = None                   # Nome fantasia
    cnpj: Optional[str] = None                           # CNPJ
    cns: Optional[str] = None                            # CNS (registro sanitário, se aplicável)
    site: Optional[str] = None                           # Website
    telephone: Optional[str] = None                      # Telefone fixo
    cellphone: Optional[str] = None                      # Celular
    email: Optional[EmailStr] = None                     # E-mail da empresa (validado)
    password: Optional[str] = None                       # Senha (criptografada no backend)
    responsible: Optional[str] = None                    # Nome do responsável legal
    responsible_office: Optional[str] = None             # Cargo do responsável
    cep: Optional[str] = None                            # CEP do endereço
    state_id: int                                        # ID do estado (chave estrangeira)
    city_id: int                                         # ID da cidade (chave estrangeira)
    district: Optional[str] = None                       # Bairro
    complement: Optional[str] = None                     # Complemento do endereço
    expiration_day: Optional[int] = None                 # Dia do vencimento da mensalidade
    value_monthly: Optional[str] = None                  # Valor da mensalidade
    stations: Optional[int] = None                       # Número de estações (usuários)
    start_contract: Optional[date] = None                # Início do contrato
    first_payment: Optional[date] = None                 # Data do primeiro pagamento
    history: Optional[str] = None                        # Observações ou histórico da empresa
    date_register: Optional[datetime] = None             # Data de cadastro
    date_update: Optional[datetime] = None               # Última atualização

    class Config:
        from_attributes = True


# Schema usado para listagem de empresas (exibição resumida ou paginada)
class CompanySchemaList(BaseModel):
    company_id: int
    name_fantasy: Optional[str]
    name_business: Optional[str]
    email: Optional[EmailStr]
    telephone: Optional[str]
    cellphone: Optional[str]
    site: Optional[str]

    class Config:
        from_attributes = True


# Schema usado para paginação de resultados
class CompanyPaginationSchema(BaseModel):
    total: int                               # Total de registros encontrados
    skip: int                                # Quantidade de registros ignorados (offset)
    limit: int                               # Quantidade por página (limit)
    data: List[CompanySchemaList]            # Lista de empresas (parcial)
