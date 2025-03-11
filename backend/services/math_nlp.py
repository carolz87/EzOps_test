from transformers import pipeline

# Carregar modelo NLP especializado
math_model = pipeline("text2text-generation", model="google/flan-t5-small")

def parse_math_expression(text: str):
    """Usa IA para converter linguagem natural em uma expressão matemática."""
    prompt = f"Converta esta pergunta para uma expressão matemática: {text}"
    
    result = math_model(prompt, max_length=20, do_sample=False)
    
    return result[0]["generated_text"]
