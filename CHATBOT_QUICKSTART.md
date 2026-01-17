# Quick Start Guide - Groq AI Chatbot Integration

## Prerequisites
- Python 3.8+
- Groq API Key (get from https://console.groq.com/)

## Setup Steps

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

The following new package has been added:
- `groq>=1.0.0` - Groq AI API client

### 2. Set Environment Variable (Important!)
```bash
# Windows PowerShell
$env:GROQ_API_KEY = "your-api-key-here"

# Windows CMD
set GROQ_API_KEY=your-api-key-here

# Linux/Mac
export GROQ_API_KEY=your-api-key-here
```

### 3. Start Backend Server
```bash
python -m uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```

You should see:
```
INFO:     Uvicorn running on http://0.0.0.0:8000
```

### 4. Open Frontend
- Open `index.html` in your browser
- Or serve via local server

### 5. Test the Feature
1. Click **"Talk with Your Future Self"** in the navigation menu
2. Choose a career from the grid
3. Type a question to your future self
4. Get AI-powered mentorship responses!

## What to Expect

### Available Careers
- Software Engineer
- Data Scientist
- Product Manager
- UX Designer
- Management Consultant
- Nurse
- Graphic Designer
- Business Analyst
- Cybersecurity Specialist
- Marketing Manager
- Mechanical Engineer
- Psychologist

### Example Interactions
**You**: "What should I focus on in high school?"
**Future You**: "As a Software Engineer 5 years from now, I can tell you that the most important decision I made was to start coding early. Learn Python or JavaScript - these skills will open many doors..."

**You**: "Do you regret any decisions?"
**Future You**: "I sometimes wish I had been more serious about soft skills earlier. Technical knowledge is important, but communication and teamwork have been just as critical to my success..."

## Troubleshooting

### Backend won't start
- Check Python is installed: `python --version`
- Install dependencies: `pip install -r requirements.txt`
- Port 8000 already in use? Change port: `--port 8001`

### Chatbot returns generic responses
- Groq API key might not be set
- Check environment variable is set correctly
- Fallback mode provides responses without Groq API

### Frontend can't connect to backend
- Ensure backend is running on port 8000
- Check browser console (F12) for CORS errors
- Clear browser cache and reload

### Career not found error
- Career names are case-sensitive
- Available careers listed in careers_riasec_database.json
- Check backend console for any errors

## Files Modified

### Frontend
- `index.html` - Added chatbot menu, page, and JavaScript functions

### Backend
- `backend/main.py` - Added chatbot endpoints and Groq integration
- `requirements.txt` - Added groq package

### Documentation
- `CHATBOT_INTEGRATION.md` - Full technical documentation
- `CHATBOT_QUICKSTART.md` - This file

### Data Used
- `TestGroq/careers_riasec_database.json` - Career data and RIASEC profiles

## Key Features

✅ **12 Career Options** - Choose which future profession to explore
✅ **AI Mentorship** - Get advice from your future self
✅ **Context-Aware** - Chatbot knows about the career's RIASEC profile
✅ **Conversation History** - Maintains context throughout chat
✅ **Fallback Mode** - Works even if Groq API is unavailable
✅ **Responsive Design** - Works on desktop and mobile
✅ **No Data Storage** - Conversations aren't saved (privacy-friendly)

## API Endpoints

### Get Available Careers
```
GET /api/chatbot/careers
Response: {"careers": ["Software Engineer", "Data Scientist", ...]}
```

### Initialize Chat
```
POST /api/chatbot/init
Body: {"career": "Software Engineer", "years_ahead": 5}
Response: {"greeting": "Hi! I'm you, 5 years from now..."}
```

### Send Message
```
POST /api/chatbot/chat
Body: {
  "career": "Software Engineer",
  "years_ahead": 5,
  "message": "What should I study?",
  "conversation_history": [...]
}
Response: {"response": "...AI generated response..."}
```

## Advanced Configuration

### Change Default Time Period
In `index.html`, find `chatbot.yearsAhead = 5` and change to 10 or 20

### Add More Careers
Add entries to `TestGroq/careers_riasec_database.json`:
```json
{
  "New Career": {
    "realistic": 50,
    "investigative": 50,
    "artistic": 50,
    "social": 50,
    "enterprising": 50,
    "conventional": 50
  }
}
```

### Customize AI Model
In `backend/main.py`, change:
```python
model="mixtral-8x7b-32768"  # Change to different Groq model
```

Available models: Check Groq documentation

## Next Steps
1. ✅ Setup is complete
2. 🚀 Start using "Talk with Your Future Self"
3. 📝 Collect feedback from users
4. 🎯 Consider future enhancements (export chats, avatars, etc.)

---

**Need Help?**
- Check `CHATBOT_INTEGRATION.md` for detailed technical documentation
- Review backend logs for API errors
- Check browser console (F12) for frontend errors
