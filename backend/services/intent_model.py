from transformers import pipeline

# Carregar modelo de classificação de intenção
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def detect_intent(user_input: str):
    """Detecta a intenção do usuário usando NLP."""
    
    labels = ["calcular", "pesquisar na Wikipedia", "conversar com IA"]
    
    result = classifier(user_input, labels)

    # Retorna a intenção com maior confiança
    intent = result["labels"][0]
    
    if intent == "calcular":
        return "calculator"
    elif intent == "pesquisar na Wikipedia":
        return "wikipedia"
    else:
        return "llm"
