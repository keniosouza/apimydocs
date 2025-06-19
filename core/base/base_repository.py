from abc import ABC, abstractmethod
from core.database import get_connection

class BaseRepository(ABC):
    """
    Classe abstrata base para todos os repositórios do sistema.
    Fornece conexão com o banco de dados e obriga implementação de um método execute().
    """

    def __init__(self):
        """
        Inicializa a conexão e o cursor do banco de dados.
        Essa conexão deve ser usada pelas subclasses.
        """
        self.conn = get_connection()
        self.cursor = self.conn.cursor()

    @abstractmethod
    def execute(self, *args, **kwargs):
        """
        Método abstrato obrigatório a ser implementado pelas subclasses.
        Deve conter a lógica principal do repositório.
        """
        pass

    def commit(self):
        """
        Realiza o commit da transação.
        """
        self.conn.commit()

    def rollback(self):
        """
        Realiza o rollback da transação.
        """
        self.conn.rollback()

    def close(self):
        """
        Fecha cursor e conexão.
        """
        self.cursor.close()
        self.conn.close()
