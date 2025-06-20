import re

class Email:

    @staticmethod
    def validate(data: str) -> str:
        # Validação de email
        default = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(default, data):
            raise f"Email inválido: {data}"