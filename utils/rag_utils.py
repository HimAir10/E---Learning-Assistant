import os
import sys

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader, TextLoader, Docx2txtLoader
from langchain_community.vectorstores import Chroma
from langchain.schema import Document

# Add parent directory to path for imports
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from models.embeddings import get_embedding_model
from config.config import CHUNK_SIZE, CHUNK_OVERLAP, MAX_RETRIEVED_DOCS, PERSIST_DIRECTORY


def load_document(file_path):
    """
    Load a document based on its file extension
    
    Args:
        file_path (str): Path to the document file
    
    Returns:
        list: List of Document objects
    
    Raises:
        ValueError: If file type is not supported
        RuntimeError: If document loading fails
    """
    try:
        file_extension = os.path.splitext(file_path)[1].lower()
        
        if file_extension == '.pdf':
            loader = PyPDFLoader(file_path)
        elif file_extension == '.txt' or file_extension == '.md':
            loader = TextLoader(file_path, encoding='utf-8')
        elif file_extension == '.docx':
            loader = Docx2txtLoader(file_path)
        else:
            raise ValueError(f"Unsupported file type: {file_extension}")
        
        documents = loader.load()
        return documents
    
    except Exception as e:
        raise RuntimeError(f"Failed to load document: {str(e)}")


def split_documents(documents, chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP):
    """
    Split documents into smaller chunks for better retrieval
    
    Args:
        documents (list): List of Document objects
        chunk_size (int): Size of each chunk
        chunk_overlap (int): Overlap between chunks
    
    Returns:
        list: List of chunked Document objects
    
    Raises:
        RuntimeError: If splitting fails
    """
    try:
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            length_function=len,
            separators=["\n\n", "\n", " ", ""]
        )
        
        chunks = text_splitter.split_documents(documents)
        return chunks
    
    except Exception as e:
        raise RuntimeError(f"Failed to split documents: {str(e)}")


def create_vector_store(documents, persist_directory=PERSIST_DIRECTORY):
    """
    Create a vector store from documents using embeddings
    
    Args:
        documents (list): List of Document objects
        persist_directory (str): Directory to persist the vector store
    
    Returns:
        Chroma: Vector store object
    
    Raises:
        RuntimeError: If vector store creation fails
    """
    try:
        embedding_model = get_embedding_model()
        
        # Create vector store
        vector_store = Chroma.from_documents(
            documents=documents,
            embedding=embedding_model,
            persist_directory=persist_directory
        )
        
        return vector_store
    
    except Exception as e:
        raise RuntimeError(f"Failed to create vector store: {str(e)}")


def load_vector_store(persist_directory=PERSIST_DIRECTORY):
    """
    Load an existing vector store from disk
    
    Args:
        persist_directory (str): Directory where vector store is persisted
    
    Returns:
        Chroma: Loaded vector store object
    
    Raises:
        RuntimeError: If loading fails
    """
    try:
        embedding_model = get_embedding_model()
        
        vector_store = Chroma(
            persist_directory=persist_directory,
            embedding_function=embedding_model
        )
        
        return vector_store
    
    except Exception as e:
        raise RuntimeError(f"Failed to load vector store: {str(e)}")


def retrieve_relevant_docs(query, vector_store, k=MAX_RETRIEVED_DOCS):
    """
    Retrieve relevant documents from vector store based on query
    
    Args:
        query (str): User query
        vector_store: Vector store object
        k (int): Number of documents to retrieve
    
    Returns:
        list: List of relevant Document objects
    
    Raises:
        RuntimeError: If retrieval fails
    """
    try:
        relevant_docs = vector_store.similarity_search(query, k=k)
        return relevant_docs
    
    except Exception as e:
        raise RuntimeError(f"Failed to retrieve documents: {str(e)}")


def format_docs_for_context(docs):
    """
    Format retrieved documents into a context string
    
    Args:
        docs (list): List of Document objects
    
    Returns:
        str: Formatted context string
    """
    try:
        if not docs:
            return ""
        
        context = "\n\n---\n\n".join([doc.page_content for doc in docs])
        return context
    
    except Exception as e:
        raise RuntimeError(f"Failed to format documents: {str(e)}")


def process_uploaded_file(uploaded_file, save_directory="uploaded_docs"):
    """
    Process an uploaded file and prepare it for RAG
    
    Args:
        uploaded_file: Streamlit uploaded file object
        save_directory (str): Directory to save uploaded files
    
    Returns:
        tuple: (file_path, documents, chunks)
    
    Raises:
        RuntimeError: If processing fails
    """
    try:
        # Create directory if it doesn't exist
        os.makedirs(save_directory, exist_ok=True)
        
        # Save uploaded file
        file_path = os.path.join(save_directory, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        # Load and split documents
        documents = load_document(file_path)
        chunks = split_documents(documents)
        
        return file_path, documents, chunks
    
    except Exception as e:
        raise RuntimeError(f"Failed to process uploaded file: {str(e)}")
