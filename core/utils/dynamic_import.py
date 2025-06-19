import importlib

class DynamicImport:

    state = "go"
    base = "api.v1.packages"

    @staticmethod
    def service(package: str, class_name: str):
        try:
            module_file = f"{package}_service"
            path = f"{DynamicImport.base}.{package}.services.{DynamicImport.state}.{module_file}"
            module = importlib.import_module(path)
            clazz = getattr(module, class_name)
            return clazz
        except (ImportError, AttributeError) as e:
            raise ImportError(f"Erro ao importar '{class_name}' de '{path}': {e}")
