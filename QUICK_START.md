# 🚀 Quick Start Guide

## Get Started in 5 Minutes!

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

**Note**: This will install all required packages including:
- streamlit
- langchain and langchain-community
- langchain-google-genai (for Gemini)
- chromadb (vector store)
- pypdf, python-docx (document processing)
- requests (web search)
- python-dotenv (environment variables)

### Step 2: Set Up API Keys

#### Option A: Using config/config.py (Quick & Easy)

Open `config/config.py` and add your API key:

```python
# Google Gemini API Key (Required)
GOOGLE_API_KEY = "YOUR_ACTUAL_API_KEY_HERE"

# Serper API Key (Optional - for web search)
SERPER_API_KEY = "YOUR_SERPER_KEY_HERE"
```

#### Option B: Using Environment Variables (Recommended for Production)

Create a `.env` file in the project root:

```bash
cp .env.example .env
```

Edit `.env` and add your keys:
```
GOOGLE_API_KEY=your_actual_google_api_key
SERPER_API_KEY=your_actual_serper_key
```

### Step 3: Get Your API Keys

#### Google Gemini API (Required)
1. Go to [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Click "Create API Key"
3. Copy the key

#### Serper API (Optional)
1. Go to [Serper.dev](https://serper.dev/)
2. Sign up (free tier: 2,500 searches)
3. Get your API key from dashboard

### Step 4: Run the Application

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

### Step 5: Test the Features

1. **Navigate to Instructions** - Read the setup guide
2. **Go to Chat Page** - Start chatting!
3. **Upload a Document**:
   - Try `sample_documents/AI_Introduction.txt`
   - Click "Process Document"
4. **Ask Questions**:
   - "What are the types of AI?" (uses RAG)
   - "Latest AI trends 2025" (uses web search)
5. **Switch Response Modes**:
   - Try Concise mode for quick answers
   - Try Detailed mode for in-depth explanations

## 🎯 Testing Checklist

- [ ] App starts without errors
- [ ] Can navigate between pages
- [ ] Chat input works
- [ ] Document upload works
- [ ] RAG retrieves information from documents
- [ ] Web search returns results (if enabled)
- [ ] Response modes change output length
- [ ] Chat history persists during session
- [ ] Clear chat history works
- [ ] Reset vector store works

## 🐛 Common Issues

### Issue: Import errors when running
**Solution**: Install dependencies
```bash
pip install -r requirements.txt
```

### Issue: "API key not found"
**Solution**: Check `config/config.py` has your actual key (not placeholder text)

### Issue: Document upload fails
**Solution**: 
- Check file size (<10MB)
- Supported formats: PDF, TXT, DOCX, MD
- Ensure file is not corrupted

### Issue: Web search not working
**Solution**:
- Make sure Serper API key is set
- Check internet connection
- Verify API quota not exceeded

### Issue: ChromaDB errors
**Solution**:
```bash
pip install chromadb --upgrade
```

## 📊 Project Structure Quick Reference

```
AI_UseCase/
├── app.py                    # 👈 Run this file
├── config/
│   └── config.py            # 👈 Add API keys here
├── models/
│   ├── llm.py               # LLM initialization
│   └── embeddings.py        # RAG embeddings
├── utils/
│   ├── rag_utils.py         # RAG functions
│   └── web_search.py        # Web search
├── sample_documents/         # Sample files for testing
├── requirements.txt          # Dependencies
└── README.md                # Full documentation
```

## 🎓 Example Usage

### Example 1: Study with RAG
```
1. Upload: sample_documents/AI_Introduction.txt
2. Ask: "What is machine learning?"
3. Get: Answer from your document
```

### Example 2: Current Information
```
1. Enable: Web Search
2. Ask: "Latest breakthroughs in quantum computing"
3. Get: Recent web search results
```

### Example 3: Quick vs Detailed
```
Concise Mode:
Q: "Explain Python"
A: "Python is a high-level programming language known for readability and versatility."

Detailed Mode:
Q: "Explain Python"
A: "Python is a high-level, interpreted programming language... [full explanation with examples]"
```

## 🚀 Ready for Deployment?

Once everything works locally, follow `DEPLOYMENT_GUIDE.md` to deploy to Streamlit Cloud!

## 💡 Pro Tips

1. **Start with sample documents** to test RAG
2. **Use Concise mode** for quick answers while studying
3. **Use Detailed mode** when learning new concepts
4. **Enable web search** for current events and latest information
5. **Upload your own study materials** for personalized learning

## 📞 Need Help?

- Check `README.md` for detailed documentation
- Review `DEPLOYMENT_GUIDE.md` for deployment steps
- Check `PROJECT_SUMMARY.md` for technical details

---

**Happy Learning! 🎓**
