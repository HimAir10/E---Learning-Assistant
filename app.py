import streamlit as st
import os
import sys
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from PIL import Image

# Add current directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from models.llm import get_chat_model, get_vision_response
from models.embeddings import get_embedding_model
from utils.rag_utils import (
    process_uploaded_file, 
    create_vector_store, 
    load_vector_store,
    retrieve_relevant_docs,
    format_docs_for_context
)
from utils.web_search import get_search_context, should_use_web_search
from utils.image_utils import prepare_image_for_gemini
from config.config import (
    DEFAULT_SYSTEM_PROMPT,
    CONCISE_INSTRUCTION,
    DETAILED_INSTRUCTION,
    CONCISE_MAX_TOKENS,
    DETAILED_MAX_TOKENS,
    SUPPORTED_FILE_TYPES,
    MAX_FILE_SIZE_MB,
    SUPPORTED_IMAGE_TYPES,
    MAX_IMAGE_SIZE_MB,
    GOOGLE_API_KEY
)


def get_chat_response(chat_model, messages, system_prompt, use_rag=False, use_web_search=False, query=""):
    """
    Get response from the chat model with optional RAG and web search
    
    Args:
        chat_model: LLM model instance
        messages: Conversation history
        system_prompt: System prompt for the model
        use_rag: Whether to use RAG for context
        use_web_search: Whether to use web search
        query: Current user query
    
    Returns:
        str: Model response
    """
    try:
        # Build context from RAG if enabled
        rag_context = ""
        if use_rag and "vector_store" in st.session_state and st.session_state.vector_store is not None:
            try:
                relevant_docs = retrieve_relevant_docs(query, st.session_state.vector_store)
                if relevant_docs:
                    rag_context = "\n\n**Context from uploaded documents:**\n" + format_docs_for_context(relevant_docs)
            except Exception as e:
                st.warning(f"RAG retrieval failed: {str(e)}")
        
        # Build context from web search if enabled
        web_context = ""
        if use_web_search:
            try:
                web_results = get_search_context(query)
                if web_results and web_results != "No search results found.":
                    web_context = "\n\n**Recent information from web search:**\n" + web_results
            except Exception as e:
                st.warning(f"Web search failed: {str(e)}")
        
        # Combine contexts
        additional_context = rag_context + web_context
        
        # Prepare messages for the model
        formatted_messages = [SystemMessage(content=system_prompt)]
        
        # Add conversation history
        for msg in messages[:-1]:  # Exclude the last message (current query)
            if msg["role"] == "user":
                formatted_messages.append(HumanMessage(content=msg["content"]))
            else:
                formatted_messages.append(AIMessage(content=msg["content"]))
        
        # Add current query with context
        current_query = query
        if additional_context:
            current_query = f"{additional_context}\n\n**User Question:** {query}"
        
        formatted_messages.append(HumanMessage(content=current_query))
        
        # Get response from model
        response = chat_model.invoke(formatted_messages)
        return response.content
    
    except Exception as e:
        return f"Error getting response: {str(e)}"

def instructions_page():
    """Instructions and setup page"""
    st.title("🎓 E-Learning Assistant - Setup Guide")
    st.markdown("Welcome to your intelligent study companion! Follow these instructions to get started.")
    
    st.markdown("""
    ## 🎯 Use Case: E-Learning & Education
    
    This chatbot is designed to help students and learners with:
    - **Understanding complex concepts** with clear explanations
    - **Study materials and exam preparation** through document uploads
    - **Real-time information** via web search integration
    - **Personalized learning** with concise or detailed response modes
    
    ## 🔧 Installation
    
    First, install the required dependencies:
    
    ```bash
    pip install -r requirements.txt
    ```
    
    ## 🔑 API Key Setup
    
    ### Required: Google Gemini API Key (Primary Model)
    
    1. Visit [Google AI Studio](https://aistudio.google.com/app/apikey)
    2. Create a new API key
    3. Add to `config/config.py`:
       ```python
       GOOGLE_API_KEY = "your_api_key_here"
       ```
       Or set as environment variable:
       ```bash
       export GOOGLE_API_KEY="your_api_key_here"
       ```
    
    ### Optional: Web Search (Serper API)
    
    1. Visit [Serper.dev](https://serper.dev/)
    2. Sign up and get your API key (2,500 free searches)
    3. Add to `config/config.py`:
       ```python
       SERPER_API_KEY = "your_api_key_here"
       ```
    
    ### Optional: Alternative Models
    
    #### OpenAI
    - Visit [OpenAI Platform](https://platform.openai.com/api-keys)
    - Create API key and add to config
    
    #### Groq
    - Visit [Groq Console](https://console.groq.com/keys)
    - Create API key and add to config
    
    ## ✨ Features
    
    ### 1. 📚 RAG (Retrieval-Augmented Generation)
    - Upload PDF, TXT, DOCX, or Markdown files
    - The chatbot extracts and uses information from your documents
    - Perfect for studying from textbooks, notes, and research papers
    
    ### 2. 🖼️ Image Analysis & Text Extraction
    - Upload images (PNG, JPG, JPEG, WEBP)
    - Extract text from handwritten notes, diagrams, or screenshots
    - Ask questions about visual content
    - Perfect for analyzing charts, graphs, and educational diagrams
    
    ### 3. 🌐 Live Web Search
    - Automatically searches the web for current information
    - Triggered by keywords like "latest", "recent", "current", etc.
    - Or manually enable in the sidebar
    
    ### 4. ⚡ Response Modes
    - **Concise Mode**: Brief, to-the-point answers (2-3 sentences)
    - **Detailed Mode**: Comprehensive explanations with examples
    
    ### 5. 🤖 Multiple AI Models
    - **Gemini 2.0 Flash** (Primary): Fast, intelligent, and efficient
    - **OpenAI GPT**: Alternative high-quality model
    - **Groq Llama**: Fast open-source alternative
    
    ## 📖 How to Use
    
    1. **Go to the Chat page** using the sidebar navigation
    2. **Upload study materials** (optional):
       - Documents (PDF, TXT, DOCX, MD) for RAG functionality
       - Images (PNG, JPG, JPEG, WEBP) for visual analysis
    3. **Choose response mode**: Concise or Detailed
    4. **Enable web search** if you need current information
    5. **Start asking questions** about your studies!
    
    ## 💡 Example Use Cases
    
    - *"Explain quantum mechanics in simple terms"* (Detailed mode)
    - *"What are the key points of photosynthesis?"* (Concise mode)
    - *"Latest developments in AI"* (Auto web search)
    - Upload a PDF textbook and ask *"Summarize chapter 5"* (RAG)
    - Upload an image of handwritten notes and ask *"What does this say?"* (Image analysis)
    - Upload a diagram and ask *"Explain this flowchart"* (Image understanding)
    
    ## 🛠 Troubleshooting
    
    - **API Key Issues**: Verify keys are set correctly in `config/config.py`
    - **Document Processing Fails**: Check file format and size (<10MB)
    - **Web Search Not Working**: Ensure Serper API key is configured
    - **Model Errors**: Check your API credits and internet connection
    
    ## 📝 Tips for Best Results
    
    - Use **specific questions** for better answers
    - Upload **relevant documents** for accurate RAG responses
    - Choose **Concise mode** for quick reviews
    - Choose **Detailed mode** for learning new concepts
    - Enable **web search** for current events or recent information
    
    ---
    
    Ready to start learning? Navigate to the **Chat** page using the sidebar! 🚀
    """)


def chat_page():
    """Main chat interface page with RAG and web search"""
    st.title("🎓 E-Learning Assistant")
    st.markdown("*Your intelligent study companion powered by AI*")
    
    # Sidebar configuration
    with st.sidebar:
        st.header("⚙️ Configuration")
        
        # Response Mode Selection
        st.subheader("📝 Response Mode")
        response_mode = st.radio(
            "Choose response style:",
            ["Concise", "Detailed"],
            help="Concise: Short summaries | Detailed: Comprehensive explanations"
        )
        
        # Model Provider Selection
        st.subheader("🤖 AI Model")
        provider = st.selectbox(
            "Select model provider:",
            ["Gemini (Primary)", "OpenAI", "Groq"],
            help="Gemini 2.0 Flash is the primary model"
        )
        
        # Feature Toggles
        st.subheader("🔧 Features")
        use_rag = st.checkbox(
            "📚 Use RAG (Document Knowledge)",
            value=True,
            help="Retrieve information from uploaded documents",
            disabled="vector_store" not in st.session_state or st.session_state.vector_store is None
        )
        
        use_web_search = st.checkbox(
            "🌐 Enable Web Search",
            value=False,
            help="Search the web for current information"
        )
        
        # Document Upload Section
        st.subheader("📄 Upload Documents")
        uploaded_file = st.file_uploader(
            "Upload study materials",
            type=SUPPORTED_FILE_TYPES,
            help=f"Supported: {', '.join(SUPPORTED_FILE_TYPES)} (Max {MAX_FILE_SIZE_MB}MB)"
        )
        
        if uploaded_file:
            if st.button("Process Document", type="primary"):
                with st.spinner("Processing document..."):
                    try:
                        file_path, documents, chunks = process_uploaded_file(uploaded_file)
                        st.session_state.vector_store = create_vector_store(chunks)
                        st.session_state.uploaded_docs = st.session_state.get("uploaded_docs", [])
                        st.session_state.uploaded_docs.append(uploaded_file.name)
                        st.success(f"✅ Processed {len(chunks)} chunks from {uploaded_file.name}")
                    except Exception as e:
                        st.error(f"❌ Error processing document: {str(e)}")
        
        # Show uploaded documents
        if "uploaded_docs" in st.session_state and st.session_state.uploaded_docs:
            st.subheader("📚 Loaded Documents")
            for doc in st.session_state.uploaded_docs:
                st.text(f"✓ {doc}")
    
    # Prepare system prompt based on response mode
    system_prompt = DEFAULT_SYSTEM_PROMPT
    max_tokens = None
    
    if response_mode == "Concise":
        system_prompt += CONCISE_INSTRUCTION
        max_tokens = CONCISE_MAX_TOKENS
    else:
        system_prompt += DETAILED_INSTRUCTION
        max_tokens = DETAILED_MAX_TOKENS
    
    # Initialize chat model based on provider
    try:
        provider_map = {
            "Gemini (Primary)": "gemini",
            "OpenAI": "openai",
            "Groq": "groq"
        }
        chat_model = get_chat_model(
            provider=provider_map[provider],
            temperature=0.7,
            max_tokens=max_tokens
        )
    except Exception as e:
        st.error(f"❌ Failed to initialize model: {str(e)}")
        st.info("💡 Please check your API keys in config/config.py")
        return
    
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            # Display image if present in message
            if "image" in message and message["image"] is not None:
                st.image(message["image"], caption="Uploaded Image", width=300)
            st.markdown(message["content"])
    
    # Show attached image preview above chat input
    if "current_image" in st.session_state:
        col_preview1, col_preview2 = st.columns([5, 1])
        with col_preview1:
            st.info(f"🖼️ Image attached: {st.session_state.current_image['filename']}")
        with col_preview2:
            if st.button("❌", help="Remove attached image", key="remove_img"):
                del st.session_state.current_image
                if "last_uploaded_image" in st.session_state:
                    del st.session_state.last_uploaded_image
                st.rerun()
    
    # Compact image upload button (ChatGPT style)
    uploaded_image = st.file_uploader(
        "📎 Attach Image",
        type=SUPPORTED_IMAGE_TYPES,
        help="Upload an image (PNG, JPG, JPEG, WEBP)",
        key="chat_image_uploader",
        label_visibility="visible"
    )
    
    # Process uploaded image
    if uploaded_image:
        if "last_uploaded_image" not in st.session_state or st.session_state.get("last_uploaded_image") != uploaded_image.name:
            try:
                image_data = prepare_image_for_gemini(uploaded_image)
                st.session_state.current_image = image_data
                st.session_state.last_uploaded_image = uploaded_image.name
                st.success(f"✅ {uploaded_image.name} attached")
            except Exception as e:
                st.error(f"❌ {str(e)}")
    
    # Chat input (original position)
    prompt = st.chat_input("Ask me anything about your studies...")
    
    # Process chat input
    if prompt:
        # Check if there's an attached image
        has_image = "current_image" in st.session_state
        current_image_data = st.session_state.get("current_image") if has_image else None
        
        # Add user message to chat history (with image if attached)
        user_message = {
            "role": "user", 
            "content": prompt,
            "image": current_image_data["image"] if has_image else None
        }
        st.session_state.messages.append(user_message)
        
        # Display user message
        with st.chat_message("user"):
            if has_image:
                st.image(current_image_data["image"], caption="Uploaded Image", width=300)
            st.markdown(prompt)
        
        # Check if web search should be auto-enabled
        auto_web_search = should_use_web_search(prompt) if not use_web_search else False
        final_use_web_search = use_web_search or auto_web_search
        
        # Display info about features being used
        features_used = []
        if use_rag and "vector_store" in st.session_state:
            features_used.append("📚 RAG")
        if final_use_web_search:
            features_used.append("🌐 Web Search")
        if has_image:
            features_used.append("🖼️ Image Analysis")
        if response_mode == "Concise":
            features_used.append("⚡ Concise Mode")
        else:
            features_used.append("📖 Detailed Mode")
        
        if features_used:
            st.caption(f"Using: {' | '.join(features_used)}")
        
        # Generate and display bot response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                # Build combined prompt with image understanding, RAG, and web search
                combined_prompt = prompt
                
                # Add image analysis if present
                if has_image:
                    try:
                        import base64
                        image_bytes = current_image_data["bytes"]
                        image_base64 = base64.b64encode(image_bytes).decode('utf-8')
                        image_url = f"data:image/jpeg;base64,{image_base64}"
                        
                        # Get image description/understanding
                        image_analysis = get_vision_response(
                            image_url, 
                            "Describe this image in detail, focusing on any text, diagrams, or educational content."
                        )
                        
                        # Add image context to the prompt
                        combined_prompt = f"[Image Content]: {image_analysis}\n\n[User Question]: {prompt}"
                    except Exception as e:
                        st.warning(f"Image analysis failed: {str(e)}")
                
                # Get response with RAG and web search
                response = get_chat_response(
                    chat_model=chat_model,
                    messages=st.session_state.messages[:-1],  # Exclude current message
                    system_prompt=system_prompt,
                    use_rag=use_rag,
                    use_web_search=final_use_web_search,
                    query=combined_prompt
                )
                st.markdown(response)
        
        # Add bot response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response, "image": None})
        
        # Clear attached image after sending
        if has_image:
            del st.session_state.current_image
            if "last_uploaded_image" in st.session_state:
                del st.session_state.last_uploaded_image

def main():
    st.set_page_config(
        page_title="E-Learning Assistant | AI Study Companion",
        page_icon="🎓",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Initialize session state
    if "vector_store" not in st.session_state:
        st.session_state.vector_store = None
    if "uploaded_docs" not in st.session_state:
        st.session_state.uploaded_docs = []
    
    # Navigation
    with st.sidebar:
        st.title("🎓 E-Learning Assistant")
        st.markdown("---")
        page = st.radio(
            "Navigation:",
            ["💬 Chat", "📖 Instructions"],
            index=0
        )
        
        # Add clear chat button in sidebar for chat page
        if page == "💬 Chat":
            st.markdown("---")
            if st.button("🗑️ Clear Chat History", use_container_width=True):
                st.session_state.messages = []
                st.rerun()
            
            if st.button("🔄 Reset Vector Store", use_container_width=True):
                st.session_state.vector_store = None
                st.session_state.uploaded_docs = []
                st.success("Vector store reset!")
                st.rerun()
        
        # Footer
        st.markdown("---")
        st.caption("Built with Streamlit & LangChain")
        st.caption("Powered by Google Gemini 2.0 Flash")
    
    # Route to appropriate page
    if page == "📖 Instructions":
        instructions_page()
    if page == "💬 Chat":
        chat_page()

if __name__ == "__main__":
    main()