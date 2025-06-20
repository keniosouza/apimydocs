import re
import html

class Text:

    @staticmethod
    def sanitize(data: str) -> str:
        """Trim spaces, escape HTML entities, collapse multiple spaces."""
        data = data.strip()
        data = html.escape(data)
        data = re.sub(r"\s+", " ", data)
        return data

    @staticmethod
    def just_numbers(data: str) -> str:
        """ Mantêm apenas os numeros """
        data = re.sub(r"[^\d]", "", data)
        return data