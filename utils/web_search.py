import os
import sys

import requests

# Add parent directory to path for imports
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from config.config import SERPER_API_KEY, MAX_SEARCH_RESULTS


def search_web(query, num_results=MAX_SEARCH_RESULTS):
    """
    Perform a web search using Serper API
    
    Args:
        query (str): Search query
        num_results (int): Number of results to return
    
    Returns:
        dict: Search results containing organic results and information
    
    Raises:
        RuntimeError: If search fails
    """
    try:
        if not SERPER_API_KEY:
            raise ValueError("Serper API key not found. Please set SERPER_API_KEY in config.py or environment variables.")
        
        url = "https://google.serper.dev/search"
        
        payload = {
            "q": query,
            "num": num_results
        }
        
        headers = {
            "X-API-KEY": SERPER_API_KEY,
            "Content-Type": "application/json"
        }
        
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        
        return response.json()
    
    except Exception as e:
        raise RuntimeError(f"Web search failed: {str(e)}")


def format_search_results(search_results):
    """
    Format search results into a readable context string
    
    Args:
        search_results (dict): Raw search results from Serper API
    
    Returns:
        str: Formatted search results
    """
    try:
        if not search_results or "organic" not in search_results:
            return "No search results found."
        
        formatted_results = []
        
        for i, result in enumerate(search_results.get("organic", []), 1):
            title = result.get("title", "No title")
            link = result.get("link", "")
            snippet = result.get("snippet", "No description")
            
            formatted_results.append(
                f"{i}. **{title}**\n"
                f"   {snippet}\n"
                f"   Source: {link}\n"
            )
        
        return "\n".join(formatted_results)
    
    except Exception as e:
        raise RuntimeError(f"Failed to format search results: {str(e)}")


def get_search_context(query, num_results=MAX_SEARCH_RESULTS):
    """
    Get formatted search context for a query
    
    Args:
        query (str): Search query
        num_results (int): Number of results to retrieve
    
    Returns:
        str: Formatted search context
    
    Raises:
        RuntimeError: If search or formatting fails
    """
    try:
        search_results = search_web(query, num_results)
        formatted_context = format_search_results(search_results)
        
        return formatted_context
    
    except Exception as e:
        raise RuntimeError(f"Failed to get search context: {str(e)}")


def should_use_web_search(query, threshold_keywords=None):
    """
    Determine if a query should trigger a web search
    
    Args:
        query (str): User query
        threshold_keywords (list): Keywords that suggest need for current information
    
    Returns:
        bool: True if web search should be used
    """
    try:
        if threshold_keywords is None:
            threshold_keywords = [
                "latest", "recent", "current", "today", "now", "news",
                "2024", "2025", "this year", "update", "new"
            ]
        
        query_lower = query.lower()
        
        for keyword in threshold_keywords:
            if keyword in query_lower:
                return True
        
        return False
    
    except Exception as e:
        return False


def extract_search_snippets(search_results, max_length=500):
    """
    Extract and combine snippets from search results
    
    Args:
        search_results (dict): Raw search results
        max_length (int): Maximum length of combined snippets
    
    Returns:
        str: Combined snippets
    """
    try:
        snippets = []
        current_length = 0
        
        for result in search_results.get("organic", []):
            snippet = result.get("snippet", "")
            
            if current_length + len(snippet) <= max_length:
                snippets.append(snippet)
                current_length += len(snippet)
            else:
                break
        
        return " ".join(snippets)
    
    except Exception as e:
        return ""
