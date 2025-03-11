from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from transformers import pipeline
from services.calculator import calculate
from services.wikipedia_search import search_wikipedia
from services.intent_model import detect_intent

app = FastAPI()

# Hugging Face model import
llm = pipeline("text-generation", model="gpt2")

# CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)


@app.get("/")
def read_root():
    return {"message": "API ready!"}

@app.post("/chat")
def chat(input_text: str):
    """Determina a intenção do usuário usando NLP e responde de acordo."""
    
    intent = detect_intent(input_text)

    if intent == "calculator":
        return {"response": calculate(input_text)}
    
    elif intent == "wikipedia":
        term = input_text.lower().replace("wikipedia", "").strip()
        return {"response": search_wikipedia(term)}

    else:  # Caso seja um pedido normal de chat
        response = llm(input_text, max_length=100, do_sample=True)
        return {"response": response[0]["generated_text"]}