import re
from services.math_nlp import parse_math_expression

def calculate(expression: str):
    """Calculate the result of a math expression."""
    
    try:
        math_expression = parse_math_expression(expression)

        if not re.match(r"^[0-9+\-*/(). ]+$", math_expression):
            return "Invalid expression!"

        result = eval(math_expression, {"__builtins__": {}})
      
        return result
    except Exception as e:
        return f"Error: {str(e)}"
