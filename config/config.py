import os
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
load_dotenv()

# API Keys Configuration
# For security, use environment variables. You can also set them directly here for development
# But NEVER commit actual API keys to GitHub

# Google Gemini API Key
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "")

# OpenAI API Key (optional, for embeddings)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

# Groq API Key (optional alternative)
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")

# Serper API Key for web search (get from https://serper.dev/)
SERPER_API_KEY = os.getenv("SERPER_API_KEY", "")

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

# Vector Store Settings
VECTOR_STORE_PATH = "vector_store"
PERSIST_DIRECTORY = "./chroma_db"
