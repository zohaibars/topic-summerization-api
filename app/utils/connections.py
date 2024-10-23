import chromadb
from sqlalchemy import create_engine
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from app.utils.settings import (
    POSTGRES_STT_HOST,
    POSTGRES_STT_DATABASE,
    POSTGRES_STT_USER,
    POSTGRES_STT_PASSWORD,
    POSTGRES_STT_PORT,
    GROQ_API_KEY,
    OPENAI_API_KEY,
    LOCAL_LLM_API_KEY,
    LOCAL_LLM_BASE_URL
)
from openai import OpenAI


def chromadb_connection(collection: str):
    db = chromadb.PersistentClient("./chromadb")
    chroma_collection = db.get_or_create_collection(collection)
    return chroma_collection

def llms_clients_lang(temp: float = 0.3, model: str = "llama-3.1-70b-versatile"):
    
    api_key=GROQ_API_KEY
    chat_llm = ChatGroq(model=model,
    api_key=api_key,
    temperature=temp,
    max_retries=3
    )
    #triton_url = "localhost:8001"
    #model_name = "ensemble"
    #chat_llm = TritonTensorRTLLM(server_url=triton_url, model_name=model_name)
    return chat_llm

def postgres_connection():
    connection_string = f'postgresql://{POSTGRES_STT_USER}:{POSTGRES_STT_PASSWORD}@{POSTGRES_STT_HOST}:{POSTGRES_STT_PORT}/{POSTGRES_STT_DATABASE}'
    print(connection_string)
    engine = create_engine(connection_string)
    return engine

def openai_client():
    llm = ChatOpenAI(
        model="gpt-4o",
        temperature=0.3,
        max_tokens=None,
        timeout=None,
        api_key=OPENAI_API_KEY,
    )
    return llm

def ollama_client():
    llm = OpenAI(
        base_url=LOCAL_LLM_BASE_URL,
        api_key=LOCAL_LLM_API_KEY
        )
    return llm

check_post = postgres_connection()
