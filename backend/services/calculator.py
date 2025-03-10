import re

def calculate(expression: str):
    """Avalia expressões matemáticas básicas com segurança."""
    try:
        # Permitir apenas números e operadores básicos
        if not re.match(r"^[0-9+\-*/(). ]+$", expression):
            return "Expressão inválida!"

        # Avalia a expressão de forma segura
        result = eval(expression, {"__builtins__": {}})
        return result
    except Exception as e:
        return f"Erro ao calcular: {str(e)}"
