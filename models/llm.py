import os
import sys
from PIL import Image

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage

# Add parent directory to path for imports
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from config.config import (
    GOOGLE_API_KEY, 
    OPENAI_API_KEY, 
    GROQ_API_KEY, 
    DEFAULT_LLM_MODEL
)


def get_gemini_model(model_name=DEFAULT_LLM_MODEL, temperature=0.7, max_tokens=None):
    """
    Initialize and return the Google Gemini chat model (Primary LLM)
    
    Args:
        model_name (str): Name of the Gemini model
        temperature (float): Sampling temperature (0.0 to 1.0)
        max_tokens (int): Maximum tokens in response
    
    Returns:
        ChatGoogleGenerativeAI: Configured Gemini chat model
    
    Raises:
        RuntimeError: If model initialization fails
    """
    try:
        if not GOOGLE_API_KEY:
            raise ValueError("Google API key not found. Please set GOOGLE_API_KEY in config.py or environment variables.")
        
        gemini_model = ChatGoogleGenerativeAI(
            model=model_name,
            google_api_key=GOOGLE_API_KEY,
            temperature=temperature,
            max_output_tokens=max_tokens
        )
        
        return gemini_model
    
    except Exception as e:
        raise RuntimeError(f"Failed to initialize Gemini model: {str(e)}")


def get_openai_model(model_name="gpt-4o-mini", temperature=0.7, max_tokens=None):
    """
    Initialize and return the OpenAI chat model (Alternative)
    
    Args:
        model_name (str): Name of the OpenAI model
        temperature (float): Sampling temperature
        max_tokens (int): Maximum tokens in response
    
    Returns:
        ChatOpenAI: Configured OpenAI chat model
    
    Raises:
        RuntimeError: If model initialization fails
    """
    try:
        if not OPENAI_API_KEY:
            raise ValueError("OpenAI API key not found. Please set OPENAI_API_KEY in config.py or environment variables.")
        
        openai_model = ChatOpenAI(
            model=model_name,
            api_key=OPENAI_API_KEY,
            temperature=temperature,
            max_tokens=max_tokens
        )
        
        return openai_model
    
    except Exception as e:
        raise RuntimeError(f"Failed to initialize OpenAI model: {str(e)}")


def get_groq_model(model_name="llama-3.1-70b-versatile", temperature=0.7, max_tokens=None):
    """
    Initialize and return the Groq chat model (Alternative)
    
    Args:
        model_name (str): Name of the Groq model
        temperature (float): Sampling temperature
        max_tokens (int): Maximum tokens in response
    
    Returns:
        ChatGroq: Configured Groq chat model
    
    Raises:
        RuntimeError: If model initialization fails
    """
    try:
        if not GROQ_API_KEY:
            raise ValueError("Groq API key not found. Please set GROQ_API_KEY in config.py or environment variables.")
        
        groq_model = ChatGroq(
            api_key=GROQ_API_KEY,
            model=model_name,
            temperature=temperature,
            max_tokens=max_tokens
        )
        
        return groq_model
    
    except Exception as e:
        raise RuntimeError(f"Failed to initialize Groq model: {str(e)}")


def get_chat_model(provider="gemini", model_name=None, temperature=0.7, max_tokens=None):
    """
    Get a chat model based on the specified provider
    
    Args:
        provider (str): Model provider ("gemini", "openai", or "groq")
        model_name (str): Optional specific model name
        temperature (float): Sampling temperature
        max_tokens (int): Maximum tokens in response
    
    Returns:
        Chat model instance
    
    Raises:
        ValueError: If provider is not supported
        RuntimeError: If model initialization fails
    """
    try:
        provider = provider.lower()
        
        if provider == "gemini":
            return get_gemini_model(
                model_name=model_name or DEFAULT_LLM_MODEL,
                temperature=temperature,
                max_tokens=max_tokens
            )
        elif provider == "openai":
            return get_openai_model(
                model_name=model_name or "gpt-4o-mini",
                temperature=temperature,
                max_tokens=max_tokens
            )
        elif provider == "groq":
            return get_groq_model(
                model_name=model_name or "llama-3.1-70b-versatile",
                temperature=temperature,
                max_tokens=max_tokens
            )
        else:
            raise ValueError(f"Unsupported provider: {provider}. Choose from 'gemini', 'openai', or 'groq'.")
    
    except Exception as e:
        raise RuntimeError(f"Failed to get chat model: {str(e)}")


# For backward compatibility
def get_chatgroq_model():
    """Legacy function for backward compatibility"""
    return get_groq_model()


def get_vision_response(image_data, question, model_name="gemini-2.0-flash"):
    """
    Get response from Gemini Vision model for image analysis
    
    Args:
        image_data: PIL Image object or image bytes
        question (str): Question about the image
        model_name (str): Gemini model with vision capabilities
    
    Returns:
        str: Model response about the image
    
    Raises:
        RuntimeError: If vision model fails
    """
    try:
        if not GOOGLE_API_KEY:
            raise ValueError("Google API key not found for vision model")
        
        # Initialize Gemini model with vision support
        vision_model = ChatGoogleGenerativeAI(
            model=model_name,
            google_api_key=GOOGLE_API_KEY,
            temperature=0.4
        )
        
        # Prepare message with image
        message = HumanMessage(
            content=[
                {"type": "text", "text": question},
                {
                    "type": "image_url",
                    "image_url": image_data
                }
            ]
        )
        
        # Get response
        response = vision_model.invoke([message])
        return response.content
    
    except Exception as e:
        raise RuntimeError(f"Failed to get vision response: {str(e)}")
