# 🎓 E-Learning Assistant - AI Study Companion

An intelligent chatbot designed to help students and learners enhance their study experience through advanced document understanding, real-time information retrieval, and customizable response formats.

## 🌟 Features

### 1. **Smart Document Processing (RAG)**
Transform your study materials into an interactive knowledge base:
- Upload textbooks, notes, and study materials (PDF, TXT, DOCX, MD)
- Automatic organization and indexing of content
- Ask questions and get answers directly from your documents
- Find relevant information across multiple uploaded files instantly

### 2. **Live Web Search**
Stay updated with the latest information:
- Access real-time information from the internet
- Perfect for current events, recent research, and trending topics
- Automatically suggests web search when queries need fresh data
- Get answers with source citations for verification

### 3. **Adaptive Response Modes**
Choose how detailed you want your answers:
- **Concise Mode**: Quick, focused answers perfect for rapid review
- **Detailed Mode**: In-depth explanations with examples and context
- Switch modes anytime based on your learning needs

### 4. **Multi-Model Support**
Flexibility to choose different AI providers:
- Primary model for fast, accurate responses
- Alternative models for specialized tasks
- Seamless switching between providers

### 5. **Intuitive Interface**
Built for ease of use:
- Clean, distraction-free chat interface
- Simple document upload and management
- Easy-to-access controls and settings
- Mobile-friendly responsive design

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

### Required API Keys

The application requires API keys to function. You'll need to obtain these from the respective providers:

1. **Primary AI Model API Key**
   - Visit the provider's website and create an account
   - Generate an API key from their dashboard
   - Add it to your environment configuration

2. **Web Search API Key** (Optional but recommended)
   - Sign up at serper.dev for free tier (2,500 searches/month)
   - Get your API key from the dashboard
   - Add it to enable live web search features

### Setting Up API Keys

**For Local Development:**
Create a `.env` file in the project root:
```
GOOGLE_API_KEY=your_key_here
SERPER_API_KEY=your_key_here
```

**For Streamlit Cloud Deployment:**
Add keys in App Settings → Secrets section using TOML format:
```toml
GOOGLE_API_KEY = "your_key_here"
SERPER_API_KEY = "your_key_here"
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

This application is built specifically to enhance the learning experience for:

- **Students**: Get instant help with homework, clarify complex topics, and prepare for exams using your own study materials
- **Self-Learners**: Build a personalized knowledge base from books, articles, and notes you're studying
- **Teachers & Educators**: Create interactive study aids and provide quick reference materials for students
- **Researchers**: Quickly extract information from multiple documents and stay updated with latest developments

### Real-World Applications
- Converting static textbooks into interactive Q&A sessions
- Preparing for exams by querying your notes and study guides
- Learning new topics with explanations tailored to your preference (concise vs detailed)
- Staying current with latest research and developments in any field
- Creating study summaries from lengthy academic papers

## 🛠 Configuration

### Application Settings

The app comes with sensible defaults that can be customized in `config/config.py`:

**Document Processing:**
- Chunk size: 1000 characters (optimal for most documents)
- Chunk overlap: 200 characters (ensures context continuity)
- Maximum documents retrieved: 4 (balances relevance and speed)

**Response Configuration:**
- Concise mode: Quick answers (150 tokens)
- Detailed mode: Comprehensive responses (1000 tokens)

**Web Search:**
- Maximum search results: 5 (provides diverse sources)
- Automatic detection of queries needing current information

These settings can be adjusted based on your specific use case and performance requirements.

## 📊 Technical Implementation

### Core Features

**Smart Document Processing:**
- Supports multiple file formats (PDF, TXT, DOCX, MD)
- Intelligent text chunking for optimal retrieval
- Vector-based similarity search for finding relevant content
- Persistent storage for quick access across sessions

**Live Web Search:**
- Integration with search APIs for real-time data
- Intelligent query analysis to determine when web search is needed
- Source attribution for all web-retrieved information
- Formatted results for easy reading

**Flexible Response System:**
- Two distinct modes optimized for different learning scenarios
- Adaptive token management for efficient processing
- Context-aware responses that maintain conversation flow
- Clean, organized output formatting

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

### Common Issues and Solutions

**Import or Dependency Errors:**
- Ensure all packages are installed: `pip install -r requirements.txt`
- Try creating a fresh virtual environment
- Check Python version compatibility (3.8+)

**API Key Issues:**
- Verify keys are properly set in `.env` file or Streamlit secrets
- Check for extra spaces or quotes in key values
- Ensure environment variables are loaded correctly

**Document Processing Problems:**
- Confirm file format is supported (PDF, TXT, DOCX, MD)
- Check file size (keep under 10MB for best performance)
- Ensure file is not corrupted or password-protected

**Web Search Not Working:**
- Verify web search API key is configured
- Check internet connection
- Ensure API quota hasn't been exceeded

**Slow Response Times:**
- Try using concise mode for faster responses
- Reduce number of documents in knowledge base
- Check internet connection speed
- Consider API rate limits

## 📝 Development Notes

This project was built with a focus on:
- **Clean Architecture**: Modular structure with clear separation of concerns
- **Robust Error Handling**: Comprehensive try-except blocks throughout
- **Security**: API keys managed via environment variables
- **Maintainability**: Reusable functions and well-organized code
- **User Experience**: Intuitive interface with helpful feedback
- **Best Practices**: Following industry standards and coding conventions

The entire application was developed through careful planning, systematic implementation, and thorough testing to ensure reliability and performance.

## 🎨 Future Enhancements

- [ ] Support for more file formats (PPT, Excel)
- [ ] Multi-language support
- [ ] Voice input/output
- [ ] Study session tracking
- [ ] Quiz generation from documents
- [ ] Collaborative learning features

## 📄 License

This project is created for educational purposes.

---

**Built with Python, Streamlit, and modern AI technologies to enhance the learning experience.**
