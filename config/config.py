import os
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
load_dotenv()

# Try to load from Streamlit secrets if available (for Streamlit Cloud deployment)
try:
    import streamlit as st
    GOOGLE_API_KEY = st.secrets.get("GOOGLE_API_KEY", os.getenv("GOOGLE_API_KEY", ""))
    OPENAI_API_KEY = st.secrets.get("OPENAI_API_KEY", os.getenv("OPENAI_API_KEY", ""))
    GROQ_API_KEY = st.secrets.get("GROQ_API_KEY", os.getenv("GROQ_API_KEY", ""))
    SERPER_API_KEY = st.secrets.get("SERPER_API_KEY", os.getenv("SERPER_API_KEY", ""))
except (ImportError, FileNotFoundError):
    # Fallback to environment variables if not on Streamlit Cloud
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
    GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
    SERPER_API_KEY = os.getenv("SERPER_API_KEY", "")

# API Keys Configuration
# For security, use environment variables. You can also set them directly here for development
# But NEVER commit actual API keys to GitHub

# I have used Gemini 2.0 Flash model as primary llm only, and not used OpenAI and Groq models.
# And I have used Serper API for web search. 

#Set these api keys in your .env file. 
#SERPER_API_KEY=83243bb427456c389cdea87cc8421ea3f9ebd4c6
#GOOGLE_API_KEY=AIzaSyA7tETTV8jQkRyhVMhWn90Ws5PRlyW4MYM



# Model Configuration
DEFAULT_LLM_MODEL = "gemini-2.0-flash"  # Google Gemini 2.0 Flash
DEFAULT_EMBEDDING_MODEL = "models/embedding-001"  # Google's embedding model

# RAG Configuration
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200
MAX_RETRIEVED_DOCS = 4

# Response Mode Settings
CONCISE_MAX_TOKENS = 150
DETAILED_MAX_TOKENS = 1000

# System Prompts
DEFAULT_SYSTEM_PROMPT = """You are an intelligent E-Learning & Education Assistant. You help students and learners with:
- Explaining complex concepts in simple terms
- Study materials, course content, and exam preparation
- Problem-solving and step-by-step guidance
- Research assistance and academic resources
- Learning strategies and study techniques

Provide accurate, educational, and encouraging responses. Use examples and analogies to make concepts clear. Adapt your explanations based on the learner's level."""

CONCISE_INSTRUCTION = "\n\nProvide a brief, concise response (2-3 sentences maximum)."
DETAILED_INSTRUCTION = "\n\nProvide a comprehensive, detailed response with explanations, examples, and actionable insights."

# Web Search Settings
WEB_SEARCH_ENABLED = True
MAX_SEARCH_RESULTS = 5

# Document Upload Settings
SUPPORTED_FILE_TYPES = ["pdf", "txt", "docx", "md"]
MAX_FILE_SIZE_MB = 10

# Image Upload Settings
SUPPORTED_IMAGE_TYPES = ["png", "jpg", "jpeg", "webp"]
MAX_IMAGE_SIZE_MB = 5
IMAGE_MAX_DIMENSIONS = (1024, 1024)  # Max width and height

# Vector Store Settings
VECTOR_STORE_PATH = "vector_store"
PERSIST_DIRECTORY = "./chroma_db"
