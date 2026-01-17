# Groq AI Chatbot Integration - "Talk with Your Future Self"

## Overview
The Groq AI chatbot has been successfully integrated into the LuminaV web application. This feature allows users to chat with their future selves in different career paths using AI-powered conversations.

## What's New

### Frontend Changes (index.html)

1. **New Menu Option**: "Talk with Your Future Self" added to the main navigation menu
2. **New Page**: Chatbot page (id="page-chatbot") with:
   - Career selection grid showing all available careers from the JSON database
   - Interactive chat interface with message history
   - Message bubbles with user/assistant distinction
   - Real-time conversation display

3. **New JavaScript Functions**:
   - `loadCareersForChatbot()` - Fetches available careers from backend
   - `selectCareersForChat(career)` - Initializes chat with selected career
   - `sendChatMessage()` - Sends user messages and receives AI responses
   - `addChatMessage(role, content)` - Displays messages in the UI
   - `backToCareers()` - Returns to career selection

### Backend Changes (backend/main.py)

1. **New Imports**: Added Pydantic models for request validation
   - `ChatInitRequest` - For chatbot initialization
   - `ChatRequest` - For chat messages

2. **New Endpoints**:
   - `GET /api/chatbot/careers` - Returns list of available careers
   - `POST /api/chatbot/init` - Initializes chatbot with greeting
   - `POST /api/chatbot/chat` - Main chat endpoint for conversations

3. **New Functions**:
   - `load_career_database()` - Loads careers from JSON file
   - `generate_future_self_persona()` - Creates AI personality based on career and RIASEC profile

4. **Groq Integration**: 
   - Uses Groq API with `mixtral-8x7b-32768` model
   - Includes fallback responses if Groq is unavailable
   - Maintains conversation history for context-aware responses

## Available Careers
The chatbot supports the following careers from `TestGroq/careers_riasec_database.json`:
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

## How It Works

### User Flow:
1. User clicks "Talk with Your Future Self" in the navigation menu
2. User sees a grid of available careers
3. User clicks on a career (e.g., "Software Engineer")
4. Chatbot initializes with a greeting: "Hi! I'm you, 5 years from now..."
5. User can type questions and receive AI-powered responses
6. Conversation history is maintained throughout the session
7. User can click "← Back" to return to career selection

### AI Behavior:
- The AI takes on the persona of a professional in the selected career
- Uses RIASEC profile data to inform personality and advice
- Gives practical, actionable career guidance
- Answers questions about career path, decisions, and skills
- Maintains a conversational tone (2-3 paragraphs max per response)

## Configuration

### API Key Setup
For Groq integration to work:
1. Ensure `GROQ_API_KEY` environment variable is set
2. Install groq package: `pip install groq>=1.0.0`

### Fallback Mode
If Groq is not available (ImportError), the app provides:
- Pre-configured responses for each career
- Generic fallback for unknown careers
- Full functionality without external API calls

## Dependencies

### New Dependencies (added to requirements.txt):
```
groq>=1.0.0
```

### Existing Dependencies Used:
- FastAPI 0.104.1
- Uvicorn 0.24.0
- Pydantic (FastAPI dependency)

## File Structure
```
hackher/
├── index.html (Updated)
│   ├── Navigation menu (Added chatbot link)
│   ├── Page-chatbot section (New)
│   └── JavaScript chatbot functions (New)
├── backend/
│   └── main.py (Updated)
│       ├── Pydantic models (New)
│       ├── /api/chatbot/careers endpoint (New)
│       ├── /api/chatbot/init endpoint (New)
│       └── /api/chatbot/chat endpoint (New)
├── TestGroq/
│   └── careers_riasec_database.json (Used for career data)
└── requirements.txt (Updated with groq package)
```

## Testing the Integration

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Start Backend Server
```bash
# On Windows with start_backend.bat or start_backend.ps1
# Or manually:
cd <project_root>
python -m uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```

### Step 3: Open Frontend
- Open `index.html` in a browser or serve via a local server
- Click "Talk with Your Future Self" in the navigation menu

### Step 4: Test Chat
1. Click on a career (e.g., "Software Engineer")
2. Type a question like: "What should I study now?"
3. Receive AI-generated response from your future self
4. Continue the conversation

## Environment Variables

### Required (for Groq API):
- `GROQ_API_KEY` - Your Groq API key from https://console.groq.com/

### Optional:
- `GROQ_API_BASE` - Can customize if needed (defaults to Groq's official API)

## Features Implemented
✅ Menu integration with "Talk with Your Future Self" option
✅ Career selection grid UI
✅ Chat interface with message history
✅ Backend API endpoints for careers and chat
✅ Groq AI integration with persona-based responses
✅ RIASEC profile customization per career
✅ Fallback responses for when Groq is unavailable
✅ Conversation history maintained
✅ Mobile-friendly responsive design
✅ Error handling and user feedback

## Future Enhancements (Optional)
- Multiple time periods (5, 10, 20 years ahead)
- Export chat conversations to text/PDF
- Save favorite conversations
- Compare multiple careers in chat
- Analytics on user questions
- Real-time streaming responses
- Image generation for future self avatar

## Notes
- The chatbot maintains conversation context throughout the session
- Career names must match exactly with entries in careers_riasec_database.json
- Each career has pre-defined RIASEC scores that influence AI personality
- The system is designed to provide realistic, mentoring-style guidance
- No data is stored on the server (stateless conversation)

## Support & Troubleshooting

### Issue: "Error loading careers"
- Ensure careers_riasec_database.json is in the TestGroq folder
- Check backend server is running on port 8000
- Verify CORS is enabled in main.py

### Issue: "Groq API Error"
- Verify GROQ_API_KEY environment variable is set
- Check internet connection
- Ensure groq package is installed: `pip install groq`

### Issue: Chat not responding
- Check browser console for errors (F12)
- Verify backend is running with no errors
- Try fallback mode (leave Groq key unset)
- Check message is not empty

---

**Last Updated**: January 17, 2026
**Integration Status**: Complete and Ready for Testing
