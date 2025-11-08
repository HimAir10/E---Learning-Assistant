import os
import sys

from langchain_google_genai import GoogleGenerativeAIEmbeddings

# Add parent directory to path for imports
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from config.config import GOOGLE_API_KEY, DEFAULT_EMBEDDING_MODEL


def get_embedding_model():
    """
    Initialize and return the Google Generative AI embedding model
    
    Returns:
        GoogleGenerativeAIEmbeddings: Configured embedding model
    
    Raises:
        RuntimeError: If the embedding model fails to initialize
    """
    try:
        if not GOOGLE_API_KEY:
            raise ValueError("Google API key not found. Please set GOOGLE_API_KEY in config.py or environment variables.")
        
        embeddings = GoogleGenerativeAIEmbeddings(
            model=DEFAULT_EMBEDDING_MODEL,
            google_api_key=GOOGLE_API_KEY
        )
        
        return embeddings
    
    except Exception as e:
        raise RuntimeError(f"Failed to initialize embedding model: {str(e)}")


def embed_text(text, embedding_model=None):
    """
    Generate embeddings for a given text
    
    Args:
        text (str): Text to embed
        embedding_model: Optional pre-initialized embedding model
    
    Returns:
        list: Vector embedding of the text
    
    Raises:
        RuntimeError: If embedding generation fails
    """
    try:
        if embedding_model is None:
            embedding_model = get_embedding_model()
        
        embedding = embedding_model.embed_query(text)
        return embedding
    
    except Exception as e:
        raise RuntimeError(f"Failed to generate embedding: {str(e)}")


def embed_documents(texts, embedding_model=None):
    """
    Generate embeddings for multiple documents
    
    Args:
        texts (list): List of texts to embed
        embedding_model: Optional pre-initialized embedding model
    
    Returns:
        list: List of vector embeddings
    
    Raises:
        RuntimeError: If embedding generation fails
    """
    try:
        if embedding_model is None:
            embedding_model = get_embedding_model()
        
        embeddings = embedding_model.embed_documents(texts)
        return embeddings
    
    except Exception as e:
        raise RuntimeError(f"Failed to generate document embeddings: {str(e)}")
