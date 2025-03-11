import re
from services.math_nlp import parse_math_expression

def calculate(expression: str):
    """Usa IA para interpretar expressões matemáticas em linguagem natural e calcular o resultado."""
    try:
        # Converter texto em expressão matemática
        math_expression = parse_math_expression(expression)

        # Validar expressão para evitar código malicioso
        if not re.match(r"^[0-9+\-*/(). ]+$", math_expression):
            return "Expressão inválida!"

        # Calcular o resultado
        result = eval(math_expression, {"__builtins__": {}})
        return result
    except Exception as e:
        return f"Erro ao calcular: {str(e)}"
