# ⏰ Time-Travel Career Advisor Chatbot

A conversational AI application that lets high school students talk to their future selves! Uses the Groq API and RIASEC career profiles to provide personalized career guidance.

## Features

✨ **Chat with Your Future Self**
- Select a career from 12+ professional fields
- Choose a time period (5, 10, or 20 years in the future)
- Have authentic conversations with your AI-powered future self
- Discuss regrets, good decisions, and skills to learn early
- Get specific advice based on your RIASEC profile

📊 **Reverse Planning Mode**
- Work backward from your future success to today
- Get milestone-based timeline recommendations
- Receive specific action items for the next 3 months
- Build a practical roadmap to your career goal

🎯 **RIASEC-Based Guidance**
- Each career has a detailed RIASEC profile
- Responses are tailored to your career's skill requirements
- Personalized advice based on interest/aptitude combinations

## Setup Instructions

### 1. Install Dependencies
```bash
pip install groq
```

### 2. Set Up Groq API Key
Get your free API key from [console.groq.com](https://console.groq.com)

Set as environment variable:
```bash
# Windows PowerShell
$env:GROQ_API_KEY="your-api-key-here"

# Windows CMD
set GROQ_API_KEY=your-api-key-here

# Linux/Mac
export GROQ_API_KEY="your-api-key-here"
```

Or the Groq client will automatically look for it in your environment.

### 3. Career Database (Optional)
The app includes a built-in career database with 12 careers and their RIASEC profiles. You can:

- Use the default database (already included in the code)
- Create your own `careers_riasec_database.json` in the same folder as the script
- Load a custom database by modifying the code to use `load_career_database(filepath)`

### 4. Run the Application
```bash
python TimeTravel_CareerAdvisor.py
```

## How to Use

### Main Menu
When you start the app, you'll see three options:
1. **Chat with Your Future Self** - Direct conversation with your future professional self
2. **Reverse Planning** - Get a timeline roadmap from future to today
3. **Exit**

### Chat Flow

1. Select a career from the available options (e.g., "Software Engineer", "Nurse", "Product Manager")
2. Choose your time period (5, 10, or 20 years from now)
3. Start a conversation with your future self
4. Ask about:
   - Career path decisions
   - Regrets and lessons learned
   - Skills you should learn in high school
   - Day-to-day work and challenges
   - Advice for building a strong foundation
5. Type `quit` to exit the conversation

### Reverse Planning Flow

1. Select your desired career
2. Choose your target timeframe
3. Receive a detailed roadmap with:
   - Milestone recommendations at key stages
   - Required skills at each step
   - Education/certification path
   - Internship recommendations
   - 3-month action plan

## RIASEC Profiles Included

The app includes RIASEC (Holland Codes) profiles for:

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

Each career has percentages for:
- **Realistic** - Working with tools, hands-on
- **Investigative** - Analytical, research-focused
- **Artistic** - Creative expression
- **Social** - Helping, teaching, collaborating
- **Enterprising** - Leadership, persuasion
- **Conventional** - Organization, detail-oriented

## Customization

### Add More Careers
Edit the `CAREER_DATABASE` dictionary or `careers_riasec_database.json`:

```json
{
  "Your Career": {
    "realistic": 50,
    "investigative": 60,
    "artistic": 40,
    "social": 70,
    "enterprising": 55,
    "conventional": 65
  }
}
```

### Change AI Model
In the code, modify this line:
```python
model="mixtral-8x7b-32768"
```

Available Groq models:
- `mixtral-8x7b-32768` (fast, good for conversation)
- `llama2-70b-4096` (more capable)
- `gemma-7b-it` (lightweight)

### Adjust Temperature
Change the `temperature` parameter (0.0-1.0):
- Lower (0.3-0.5): More consistent, focused responses
- Higher (0.8-1.0): More creative, varied responses

## Example Interactions

### Example 1: Chat Mode
```
You: What are the biggest challenges you faced in your first year as a software engineer?

Future You: The biggest challenge was definitely imposter syndrome. I had learned to code, 
but working on a real product with experienced developers was intimidating at first. 
What really helped was asking questions and contributing small features. I wish I had 
been more confident in asking for help earlier...
```

### Example 2: Reverse Planning
```
Career: Product Manager | Timeline: 10 years

📊 REVERSE PLANNING ROADMAP

Year 10 (You as PM):
- Leading cross-functional teams
- Making strategic product decisions
- Key skills: Data analysis, leadership, business acumen

Year 5 (Senior Associate):
- First PM role or PM-adjacent position
- Key skills: Analytics, communication, market research
- ...
```

## Tips for Students

1. **Explore Multiple Careers** - Try different careers to see what resonates
2. **Take Notes** - Write down specific skills and advice your future self mentions
3. **Ask Follow-up Questions** - Get deeper into topics that interest you
4. **Use Reverse Planning** - Build an actual action plan based on the roadmap
5. **Revisit Later** - Come back to explore other careers as your interests evolve

## Troubleshooting

**"API key error"**
- Make sure your Groq API key is set as an environment variable
- Get a free key at [console.groq.com](https://console.groq.com)

**"Rate limit error"**
- Groq free tier has limits. Wait a moment and try again

**"Career not found"**
- Make sure you're selecting from the displayed list (enter the number, not the name)

## Future Enhancements

- Integration with actual RIASEC assessment tools
- Save conversations and roadmaps to files
- Multi-language support
- Comparison between different career paths
- Integration with real job market data
- Mentor matching based on conversations
- Track progress against the generated roadmap

## License & Attribution

This app is designed for educational purposes to help high school students explore careers. The RIASEC framework is based on John Holland's career theory.

---

**Remember: Your future is shaped by the choices you make today!** 🚀
