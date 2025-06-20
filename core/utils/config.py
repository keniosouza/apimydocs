import json
from types import SimpleNamespace
from pathlib import Path


class Config:

    @staticmethod
    def get():
        # Caminho absoluto do arquivo atual
        base_dir = Path(__file__).resolve().parent

        # Caminho absoluto para o config.json (subindo dois níveis e entrando em config/)
        config_path = base_dir.parent.parent / 'config' / 'database.json'

        # Carrega o JSON como objeto acessível por ponto
        with open(config_path, 'r') as f:
            config = json.load(f, object_hook=lambda d: SimpleNamespace(**d))

        return config