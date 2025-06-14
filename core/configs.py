from pydantic_settings import BaseSettings

# Classe de configurações globais da aplicação
class Settings(BaseSettings):
    # Prefixo base das rotas da API
    API_V1_STR: str = '/api/v1'

    # URL de conexão com o banco MySQL
    # Formato: mysql://usuario:senha@host:porta/banco
    DB_URL: str = "mysql://root:root@127.0.0.1:3306/mydocs"

    # Chave secreta para geração dos tokens JWT
    JWT_SECRET: str = 'WYe1zwtlDkh39_X3X3qTSICFDxts4VQrMyGLxnEpGUg'

    # Algoritmo usado para assinar o token
    ALGORITHM: str = 'HS256'

    # Tempo de expiração do token JWT (em minutos): 1 semana
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7

    # Configuração interna do Pydantic
    class Config:
        case_sensitive = True  # Respeita letras maiúsculas/minúsculas nas variáveis de ambiente

# Instância única das configurações
settings: Settings = Settings()
