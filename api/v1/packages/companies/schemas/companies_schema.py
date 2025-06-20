import re
from typing import Optional, List
from pydantic import BaseModel, EmailStr, field_validator
from datetime import date, datetime
from core.utils.text import Text
from core.utils.phone import Phone
from core.utils.cep import CEP
from core.utils.cnpj import CNPJ
from pydantic_core import PydanticCustomError

# Schema base usado para representar uma empresa retornada pela API
class CompanySchemaBase(BaseModel):
    company_id: Optional[int] = None  # ID da empresa
    situation_id: int  # Situação (ativo, inativo, etc.)
    nickname: Optional[str] = None  # Nome reduzido ou de exibição
    name_business: Optional[str] = None  # Nome empresarial (razão social)
    name_fantasy: Optional[str] = None  # Nome fantasia
    cnpj: Optional[str] = None  # CNPJ
    cns: Optional[str] = None  # CNS (registro sanitário, se aplicável)
    site: Optional[str] = None  # Website
    telephone: Optional[str] = None  # Telefone fixo
    cellphone: Optional[str] = None  # Celular
    email: Optional[EmailStr] = None  # E-mail da empresa (validado)
    password: Optional[str] = None  # Senha (criptografada no backend)
    responsible: Optional[str] = None  # Nome do responsável legal
    responsible_office: Optional[str] = None  # Cargo do responsável
    cep: Optional[str] = None  # CEP do endereço
    state_id: int  # ID do estado (chave estrangeira)
    city_id: int  # ID da cidade (chave estrangeira)
    district: Optional[str] = None  # Bairro
    complement: Optional[str] = None  # Complemento do endereço
    expiration_day: Optional[int] = None  # Dia do vencimento da mensalidade
    value_monthly: Optional[str] = None  # Valor da mensalidade
    stations: Optional[int] = None  # Número de estações (usuários)
    start_contract: Optional[date] = None  # Início do contrato
    first_payment: Optional[date] = None  # Data do primeiro pagamento
    history: Optional[str] = None  # Observações ou histórico da empresa
    date_register: Optional[datetime] = None  # Data de cadastro
    date_update: Optional[datetime] = None  # Última atualização

    class Config:
        from_attributes = True

    @field_validator('cnpj')
    @classmethod
    def cnpj_validator(cls, data):

        # Obtem apenas os números
        data = Text.just_numbers(data)

        # verifica se o cnpj é válido
        if not CNPJ.validate(data):
            # Retorna exceção reconhecida pelo FastApi
            raise PydanticCustomError(
                "cnpj_invalido",
                "Numero de cnpj informado inválido",
            )

    @field_validator('cellphone')
    @classmethod
    def cellphone_validator(cls, data):
        # Obtem apenas os numeros
        data = Text.just_numbers(data)

        # Verifica se o número de telefone é valido
        if not Phone.validate_cellphone(data):
            # Retorna exceção reconhecida pelo FastApi
            raise PydanticCustomError(
                "cellphone_invalido",
                "Número de celular inválido. Use o formato: (11) 98765-4321 ou +55 11 98765-4321.",
            )

        # Retorna informação formatada
        return data

    @field_validator('telephone')
    @classmethod
    def telephone_validator(cls, data):
        # Obtem apenas os numeros
        data = Text.just_numbers(data)

        # Verifica se o número de telefone é valido
        if not Phone.validate_telephone(data):

            # Retorna exceção reconhecida pelo FastApi
            raise PydanticCustomError(
                "telefone_invalido",
                "Número de telefone inválido. Use o formato: (11) 98765-4321 ou +55 11 98765-4321.",
            )

        # Retorna informação formatada
        return data

    @field_validator('cep')
    @classmethod
    def cep_validator(cls, data):
        # Obtem apenas os números
        data = Text.just_numbers(data)

        # Verifica se o número de CEP é válido
        if not CEP.validate(data):

            # Retorna exceção reconhecida pelo FastApi
            raise PydanticCustomError(
                "cep_invalido",
                "Numéro de cep inválido"
            )
