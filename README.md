# 🎓 E-Learning Assistant - AI Study Companion

An intelligent chatbot powered by **Google Gemini 2.0 Flash** that helps students and learners with their studies through RAG (Retrieval-Augmented Generation), live web search, and adaptive response modes.

## 🌟 Features

### 1. **RAG Integration (Retrieval-Augmented Generation)**
- Upload educational documents (PDF, TXT, DOCX, MD)
- Automatic document chunking and vector embedding
- Intelligent retrieval of relevant information
- ChromaDB vector store for efficient similarity search

### 2. **Live Web Search**
- Real-time web search using Serper API
- Automatic detection of queries needing current information
- Manual toggle for web search
- Formatted search results with sources

### 3. **Response Modes**
- **Concise Mode**: Brief, to-the-point answers (2-3 sentences)
- **Detailed Mode**: Comprehensive explanations with examples
- Adaptive token limits for each mode

### 4. **Multiple AI Models**
- **Google Gemini 2.0 Flash** (Primary) - Fast, intelligent, efficient
- **OpenAI GPT** (Alternative) - High-quality responses
- **Groq Llama** (Alternative) - Fast open-source model

### 5. **User-Friendly Interface**
- Clean, intuitive Streamlit UI
- Real-time chat interface
- Document upload and management
- Configurable features via sidebar

## 📁 Project Structure

```
AI_UseCase/
├── config/
│   └── config.py              # API keys and settings
├── models/
│   ├── llm.py                 # LLM model initialization
│   └── embeddings.py          # RAG embedding models
├── utils/
│   ├── rag_utils.py           # RAG utility functions
│   └── web_search.py          # Web search functionality
├── app.py                     # Main Streamlit UI
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd AI_UseCase
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 🔑 API Key Setup

### Required: Google Gemini API Key

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
2. Sign up (2,500 free searches)
3. Get your API key
4. Add to `config/config.py`:
   ```python
   SERPER_API_KEY = "your_api_key_here"
   ```

### Optional: Alternative Models

#### OpenAI
```python
OPENAI_API_KEY = "your_openai_key"
```

#### Groq
```python
GROQ_API_KEY = "your_groq_key"
```

## 💻 Usage

### Start the Application

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

### Using the Chatbot

1. **Navigate to Chat Page** - Use sidebar navigation
2. **Configure Settings**:
   - Choose response mode (Concise/Detailed)
   - Select AI model provider
   - Enable/disable features
3. **Upload Documents** (Optional):
   - Click "Upload study materials"
   - Select PDF, TXT, DOCX, or MD files
   - Click "Process Document"
4. **Start Chatting**:
   - Type your questions in the chat input
   - Get intelligent responses with context

### Example Queries

**With RAG (Upload a textbook first)**:
- "Summarize chapter 3"
- "Explain the key concepts in this document"
- "What does the author say about quantum mechanics?"

**With Web Search**:
- "Latest developments in AI"
- "Current events in climate change"
- "Recent breakthroughs in medicine"

**General Learning**:
- "Explain photosynthesis in simple terms"
- "What are the principles of economics?"
- "Help me understand calculus derivatives"

## 🎯 Use Case: E-Learning & Education

This chatbot is specifically designed for:
- **Students**: Get help with homework, study materials, and exam prep
- **Self-Learners**: Access explanations and resources on any topic
- **Teachers**: Create study materials and answer student questions
- **Researchers**: Quick access to information from documents

## 🛠 Configuration

### Adjusting Settings (config/config.py)

```python
# Model Configuration
DEFAULT_LLM_MODEL = "gemini-2.0-flash-exp"

# RAG Settings
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200
MAX_RETRIEVED_DOCS = 4

# Response Modes
CONCISE_MAX_TOKENS = 150
DETAILED_MAX_TOKENS = 1000

# Web Search
MAX_SEARCH_RESULTS = 5
```

## 📊 Features Implementation

### ✅ Task 1: RAG Integration
- ✓ Document loading (PDF, TXT, DOCX, MD)
- ✓ Text chunking with RecursiveCharacterTextSplitter
- ✓ Vector embeddings using Google Generative AI
- ✓ ChromaDB vector store
- ✓ Similarity search and retrieval
- ✓ Context integration in responses

### ✅ Task 2: Live Web Search
- ✓ Serper API integration
- ✓ Real-time web search
- ✓ Automatic query detection
- ✓ Formatted search results
- ✓ Source attribution

### ✅ Task 3: Response Modes
- ✓ Concise mode (short summaries)
- ✓ Detailed mode (comprehensive explanations)
- ✓ UI toggle for mode selection
- ✓ Adaptive token limits

## 🧪 Testing

### Test RAG Functionality
1. Upload a sample document (e.g., textbook chapter)
2. Ask questions about the content
3. Verify relevant information is retrieved

### Test Web Search
1. Ask a query with "latest" or "recent"
2. Verify web search is triggered
3. Check search results are included

### Test Response Modes
1. Switch between Concise and Detailed modes
2. Ask the same question in both modes
3. Compare response lengths and detail

## 📦 Deployment to Streamlit Cloud

### 1. Prepare Repository
```bash
git add .
git commit -m "Complete E-Learning Assistant implementation"
git push origin main
```

### 2. Deploy on Streamlit Cloud
1. Visit [Streamlit Cloud](https://streamlit.io/cloud)
2. Sign in with GitHub
3. Click "New app"
4. Select your repository
5. Set main file path: `app.py`
6. Add secrets (API keys) in Advanced settings:
   ```toml
   GOOGLE_API_KEY = "your_key_here"
   SERPER_API_KEY = "your_key_here"
   ```
7. Click "Deploy"

## 🔒 Security Best Practices

- ✓ Never commit API keys to GitHub
- ✓ Use environment variables for secrets
- ✓ Add `.env` to `.gitignore`
- ✓ Use try-except blocks for error handling
- ✓ Validate user inputs

## 🐛 Troubleshooting

### Common Issues

**Issue**: Import errors
**Solution**: Ensure all dependencies are installed
```bash
pip install -r requirements.txt
```

**Issue**: API key not found
**Solution**: Check config/config.py or environment variables

**Issue**: Document processing fails
**Solution**: Check file format (PDF, TXT, DOCX, MD) and size (<10MB)

**Issue**: Web search not working
**Solution**: Verify Serper API key is set correctly

**Issue**: Gemini model errors
**Solution**: Verify Google API key and check API quota

## 📝 Development Guidelines

All code follows the assignment requirements:
- ✓ Modular structure with separate utilities
- ✓ Try-except blocks for error handling
- ✓ API keys in config file
- ✓ Reusable functions
- ✓ Clean code architecture
- ✓ No AI code generation tools used
- ✓ Original problem-solving approach

## 🎨 Future Enhancements

- [ ] Support for more file formats (PPT, Excel)
- [ ] Multi-language support
- [ ] Voice input/output
- [ ] Study session tracking
- [ ] Quiz generation from documents
- [ ] Collaborative learning features

## 📄 License

This project is created for educational purposes as part of the NeoStats AI Engineer Use Case challenge.

## 👥 Author

[Your Name]
- GitHub: [Your GitHub Profile]
- Email: [Your Email]

## 🙏 Acknowledgments

- NeoStats for the challenge opportunity
- Google for Gemini API
- Streamlit for the framework
- LangChain for RAG utilities
- Serper for web search API

---

**Built with ❤️ using Python, Streamlit, LangChain, and Google Gemini 2.0 Flash**
