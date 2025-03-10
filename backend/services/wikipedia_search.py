import wikipedia

def search_wikipedia(query: str):
    """Busca um resumo sobre o termo na Wikipedia."""
    try:
        summary = wikipedia.summary(query, sentences=2)
        return summary
    except wikipedia.exceptions.PageError:
        return "Nenhuma página encontrada para esse termo."
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Existem múltiplas opções: {', '.join(e.options[:5])}."
    except Exception as e:
        return f"Erro na busca: {str(e)}"
