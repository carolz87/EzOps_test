def parse_math_expression(text: str):
    """Parse a math expression from a text."""
    number_map = {
        "zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
        "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9",
        "um": "1", "dois": "2", "três": "3", "quatro": "4",
        "cinco": "5", "seis": "6", "sete": "7", "oito": "8", "nove": "9"
    }
    operators = {
        "plus": "+", "minus": "-", "times": "*", "divided by": "/",
        "mais": "+", "menos": "-", "vezes": "*", "dividido por": "/"
    }

    for word, num in number_map.items():
        text = text.replace(word, num)

    for word, op in operators.items():
        text = text.replace(word, op)

    return text