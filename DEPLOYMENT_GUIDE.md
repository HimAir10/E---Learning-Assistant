# 🚀 Deployment Guide - Streamlit Cloud

This guide will walk you through deploying your E-Learning Assistant to Streamlit Cloud.

## Prerequisites

- GitHub account
- Streamlit Cloud account (free)
- Google Gemini API key
- (Optional) Serper API key for web search

## Step 1: Prepare Your Repository

### 1.1 Initialize Git Repository (if not already done)

```bash
cd "/Users/himanshujha/Downloads/NeoStats AI Engineer Use Case/AI_UseCase"
git init
```

### 1.2 Add Files to Git

```bash
git add .
git commit -m "Initial commit: E-Learning Assistant with RAG and Web Search"
```

### 1.3 Create GitHub Repository

1. Go to [GitHub](https://github.com)
2. Click "New Repository"
3. Name it (e.g., "elearning-assistant-ai")
4. DO NOT initialize with README (you already have one)
5. Click "Create repository"

### 1.4 Push to GitHub

```bash
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git branch -M main
git push -u origin main
```

## Step 2: Set Up Streamlit Cloud

### 2.1 Sign Up for Streamlit Cloud

1. Visit [Streamlit Cloud](https://streamlit.io/cloud)
2. Click "Sign up" or "Continue with GitHub"
3. Authorize Streamlit to access your GitHub repositories

### 2.2 Deploy New App

1. Click "New app" button
2. Select your repository
3. Choose the branch (usually `main`)
4. Set main file path: `app.py`
5. (Optional) Customize your app URL

## Step 3: Configure Secrets (API Keys)

### 3.1 Add Secrets in Streamlit Cloud

1. Click on "Advanced settings" before deploying
2. Or go to App settings → Secrets after deployment
3. Add your API keys in TOML format:

```toml
# Required
GOOGLE_API_KEY = "your_google_gemini_api_key_here"

# Optional (for web search)
SERPER_API_KEY = "your_serper_api_key_here"

# Optional (alternative models)
OPENAI_API_KEY = "your_openai_api_key_here"
GROQ_API_KEY = "your_groq_api_key_here"
```

### 3.2 Access Secrets in Code

Your `config/config.py` already handles this with:
```python
import os
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "")
```

## Step 4: Deploy the App

1. Click "Deploy!" button
2. Wait for the app to build (2-5 minutes)
3. Once deployed, you'll get a public URL like:
   `https://your-app-name.streamlit.app`

## Step 5: Test Your Deployed App

### 5.1 Basic Functionality
- ✅ App loads without errors
- ✅ Navigation works (Chat / Instructions pages)
- ✅ Chat input is responsive

### 5.2 Test Features
1. **Test Chat**: Ask a simple question
2. **Test Response Modes**: Switch between Concise and Detailed
3. **Test Document Upload**: Upload a sample document
4. **Test RAG**: Ask questions about uploaded document
5. **Test Web Search**: Enable web search and ask about current events

## Step 6: Monitor and Maintain

### 6.1 View Logs

1. Go to your app on Streamlit Cloud
2. Click "Manage app"
3. View logs to debug issues

### 6.2 Update Your App

```bash
# Make changes locally
git add .
git commit -m "Update: description of changes"
git push

# Streamlit Cloud auto-deploys on push
```

### 6.3 Reboot App

If the app becomes unresponsive:
1. Go to "Manage app"
2. Click "Reboot app"

## Common Deployment Issues & Solutions

### Issue 1: Import Errors

**Error**: `ModuleNotFoundError`

**Solution**: Ensure all dependencies are in `requirements.txt`

```bash
pip freeze > requirements.txt
```

### Issue 2: API Key Not Found

**Error**: `API key not found`

**Solution**: 
- Check secrets are set correctly in Streamlit Cloud
- Verify the key names match exactly
- No quotes around keys in TOML format

### Issue 3: Memory Errors

**Error**: App crashes with memory error

**Solution**:
- Reduce `CHUNK_SIZE` in config
- Limit `MAX_RETRIEVED_DOCS`
- Use smaller documents for testing

### Issue 4: Slow Performance

**Solution**:
- Use Gemini 2.0 Flash (already configured) - fastest model
- Enable caching with `@st.cache_data` or `@st.cache_resource`
- Reduce vector store size

### Issue 5: File Upload Fails

**Solution**:
- Check `MAX_FILE_SIZE_MB` in config
- Ensure file format is supported
- Verify Streamlit Cloud storage limits

## Performance Optimization

### 1. Add Caching

Update `app.py` with caching:

```python
import streamlit as st

@st.cache_resource
def get_cached_model():
    return get_chat_model(provider="gemini")

@st.cache_resource
def get_cached_vector_store():
    return load_vector_store()
```

### 2. Optimize Vector Store

```python
# In config.py - reduce for faster performance
CHUNK_SIZE = 800  # Reduced from 1000
MAX_RETRIEVED_DOCS = 3  # Reduced from 4
```

### 3. Add Loading States

```python
with st.spinner("Processing..."):
    # Long-running operation
```

## Security Best Practices

### ✅ DO:
- Store API keys in Streamlit Secrets
- Use `.gitignore` to exclude sensitive files
- Validate user inputs
- Set file size limits
- Use HTTPS (automatic on Streamlit Cloud)

### ❌ DON'T:
- Commit API keys to Git
- Expose secrets in logs
- Allow unlimited file uploads
- Trust user input without validation

## Sharing Your App

### Public URL
Your app URL: `https://your-app-name.streamlit.app`

### Embed Options
Streamlit Cloud provides embed codes for:
- iFrame embedding
- Social media sharing

### Custom Domain (Optional)
Streamlit Cloud supports custom domains (requires subscription)

## Monitoring Usage

### Free Tier Limits
- Limited compute resources
- 1 GB storage
- Public apps only
- Community support

### Upgrade Options
For production apps, consider:
- Streamlit Cloud Teams
- Streamlit Cloud Enterprise

## Presentation & Submission

### PPT Deck Should Include:

1. **Title Slide**
   - Project name
   - Your name
   - Date

2. **Use Case**
   - E-Learning Assistant
   - Target audience: Students & Learners
   - Problem it solves

3. **Approach**
   - Technology stack
   - Architecture diagram
   - Design decisions

4. **Features Implemented**
   - ✅ RAG with document upload
   - ✅ Live web search
   - ✅ Concise vs Detailed modes
   - ✅ Multiple AI models
   - ✅ Clean UI/UX

5. **Technical Implementation**
   - Code structure
   - Key algorithms
   - Integration points

6. **Challenges & Solutions**
   - Technical challenges faced
   - How you solved them
   - Lessons learned

7. **Demo**
   - Screenshots or video
   - Live demo link

8. **Deployment**
   - **Live URL**: `https://your-app.streamlit.app`
   - GitHub repository
   - How to use

9. **Future Enhancements**
   - Potential improvements
   - Scalability considerations

10. **Q&A**
    - Thank you slide

## Final Checklist

Before submission:

- [ ] Code is clean and well-commented
- [ ] All features are working
- [ ] README.md is complete
- [ ] .gitignore excludes sensitive files
- [ ] No API keys in code
- [ ] App is deployed and accessible
- [ ] Tested all major features
- [ ] PPT presentation is ready
- [ ] GitHub repository is public/shared
- [ ] Deployment URL is working

## Support Resources

- [Streamlit Documentation](https://docs.streamlit.io)
- [Streamlit Cloud Docs](https://docs.streamlit.io/streamlit-community-cloud)
- [LangChain Documentation](https://python.langchain.com/)
- [Google Gemini API Docs](https://ai.google.dev/docs)

---

**Good Luck with Your Deployment! 🚀**

If you encounter issues, check:
1. Streamlit Cloud logs
2. GitHub Actions (if configured)
3. API key validity
4. Dependencies in requirements.txt
