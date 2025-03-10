from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from transformers import pipeline
from services.calculator import calculate
from services.wikipedia_search import search_wikipedia

app = FastAPI()

# Hugging Face model import
llm = pipeline("text-generation", model="gpt2")

# CORS meddleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)


@app.get("/")
def read_root():
    return {"message": "API de LLM rodando!"}

@app.post("/chat")
def chat(input_text: str):
      
    if any(op in input_text for op in ["+", "-", "*", "/"]):
        return {"response": calculate(input_text)}
    
    elif "wikipedia" in input_text.lower():
        term = input_text.lower().replace("wikipedia", "").strip()
        return {"response": search_wikipedia(term)}

    response = llm(input_text, max_length=100, do_sample=True)
    return {"response": response[0]["generated_text"]}