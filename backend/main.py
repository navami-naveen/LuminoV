
from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
try:
    from . import data
except ImportError:
    import data
import json
import os
import csv

class ChatInitRequest(BaseModel):
    career: str
    years_ahead: int = 5

class ChatRequest(BaseModel):
    career: str
    years_ahead: int = 5
    message: str
    conversation_history: Optional[list] = None




app = FastAPI()

# Enable CORS for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- DICTIONARY DATA ---
DICTIONARY_FILE = os.path.join(os.path.dirname(__file__), "..", "jarg_FUN.csv")
DICTIONARY_DATA = {}

def load_dictionary():
    global DICTIONARY_DATA
    if not os.path.exists(DICTIONARY_FILE):
        print(f"Dictionary file not found: {DICTIONARY_FILE}")
        return
    
    try:
        with open(DICTIONARY_FILE, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                career = row.get("Career", "").strip()
                jargon = row.get("Jargon", "").strip()
                if career:
                    DICTIONARY_DATA[career.lower()] = {
                        "career": career,
                        "jargon": jargon
                    }
        print(f"Loaded {len(DICTIONARY_DATA)} entries into Dictionary.")
    except Exception as e:
        print(f"Error loading dictionary: {e}")

load_dictionary()

load_dictionary()

# --- PIVOT MATRIX DATA ---
PIVOT_FILE = os.path.join(os.path.dirname(__file__), "..", "career_pivot_matrix.csv")
PIVOT_DATA = []

def load_pivot_matrix():
    global PIVOT_DATA
    if not os.path.exists(PIVOT_FILE):
        return
    try:
        with open(PIVOT_FILE, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Convert numeric values
                for k in ["Analytical", "Creative", "Technical", "Social", "Enterprising", "Operational"]:
                    try:
                        row[k] = float(row[k])
                    except:
                        row[k] = 0.0
                PIVOT_DATA.append(row)
        print(f"Loaded {len(PIVOT_DATA)} careers into Pivot Matrix.")
    except Exception as e:
        print(f"Error loading pivot matrix: {e}")

load_pivot_matrix()

@app.get("/api/pivot/careers")
def get_pivot_careers():
    return {"careers": [c["Career_Path"] for c in PIVOT_DATA]}

@app.post("/api/pivot/calculate")
def calculate_pivot(
    target_career: str = Body(...),
    user_scores: dict = Body(...)
):
    # Map User RIASEC scores (0-1 range approx)
    # The matrix values are 0-1. User scores from quiz are counts (e.g. 2 out of 6)
    # Total questions usually 6 in this simple app
    total_q = sum(user_scores.values()) or 6
    user_profile = {
        "Technical": user_scores.get("R", 0) / total_q,
        "Analytical": user_scores.get("I", 0) / total_q,
        "Creative": user_scores.get("A", 0) / total_q,
        "Social": user_scores.get("S", 0) / total_q,
        "Enterprising": user_scores.get("E", 0) / total_q,
        "Operational": user_scores.get("C", 0) / total_q
    }

    target = next((c for c in PIVOT_DATA if c["Career_Path"] == target_career), None)
    if not target:
        return {"error": "Target career not found"}

    analysis = []
    skills = ["Analytical", "Creative", "Technical", "Social", "Enterprising", "Operational"]
    
    for skill in skills:
        target_val = target[skill]
        user_val = user_profile[skill]
        delta = max(0, target_val - user_val)
        
        # User thresholds:
        # Delta <= 0.2: Hot (Orange/Red)
        # Delta 0.3 to 0.5: Warm (Yellow)
        # Delta > 0.5: Cold (Blue)
        
        if delta <= 0.2:
            status = "Hot"
            color = "red"
        elif delta <= 0.5:
            status = "Warm"
            color = "orange"
        else:
            status = "Cold"
            color = "blue"
        
        analysis.append({
            "skill": skill,
            "target": target_val,
            "user": round(user_val, 2),
            "delta": round(delta, 2),
            "status": status,
            "color": color
        })

    # Find highest RIASEC score for the profile display
    top_trait_code = max(user_scores, key=user_scores.get) if user_scores else "R"
    trait_names = {
        'R': 'Realistic (Technical)', 'I': 'Investigative (Analytical)', 'A': 'Artistic (Creative)',
        'S': 'Social (Social)', 'E': 'Enterprising (Enterprising)', 'C': 'Conventional (Operational)'
    }
    top_trait_name = trait_names.get(top_trait_code, top_trait_code)

    return {
        "career": target_career, 
        "analysis": analysis, 
        "user_top_trait": top_trait_name
    }

@app.get("/api/search-degree")
def search_degree(q: str = ""):
    q = q.lower().strip()
    if not q:
        return {"results": []}
    
    # Simple fuzzy search: find all careers that contain the query
    results = []
    for key, val in DICTIONARY_DATA.items():
        if q in key:
            results.append(val)
            if len(results) >= 10: # Limit results
                break
    
    return {"results": results}

@app.get("/api/questions")
def get_questions():
    return data.DATA["questions"]



@app.post("/api/evaluate")
def evaluate_quiz(
    answers: List[str] = Body(...), 
    tags: List[str] = Body(...),
    stream: str = Body(...),
    marks: float = Body(...)
):
    # Calculate top trait
    scores = {}
    for t in answers:
        scores[t] = scores.get(t, 0) + 1
    
    top_trait = max(scores, key=scores.get) if scores else "R"
    
    # Map user stream to data categories
    stream_map = {
        "Science (PCM)": ["Engineering", "Science", "Architecture", "Robotics", "Aviation"],
        "Science (PCB)": ["Medicine", "Science", "Forensics", "Nursing", "Biotech"],
        "Commerce": ["Commerce", "Management", "Finance", "Actuarial"],
        "Arts/Humanities": ["Arts", "Design", "Law", "Social", "Media"],
        "Class 10": ["Science", "Commerce", "Arts", "Engineering", "Medicine", "Design"]
    }
    user_target_categories = stream_map.get(stream, ["Science", "Commerce", "Arts"])

    # Get basic profile
    result = data.DATA["descriptions"].get(top_trait, data.DATA["descriptions"]["R"])
    
    # Filter courses from the trait description that match the user's stream
    all_trait_courses = result["courses"].split(", ")
    recommended_courses_list = []
    
    # Keyword mapping for course filtering
    category_keywords = {
        "Engineering": ["B.Tech", "Engineering", "Mech", "Civil", "CS", "ECE"],
        "Medicine": ["MBBS", "BDS", "Nursing", "B.Pharm", "Medicine", "Vet"],
        "Science": ["B.Sc", "M.Sc", "Physics", "Chem", "Botany", "Science", "Forensic", "Forestry", "Agri", "Astro"],
        "Commerce": ["B.Com", "CA", "BBA", "MBA", "Finance", "Accountant", "Actuarial", "Banking"],
        "Arts": ["BA", "Literature", "Arts", "Fine Arts", "Film", "Animation", "Writing", "VFX"],
        "Design": ["B.Des", "Design", "Fashion", "Interior", "UX"],
        "Law": ["Law", "LLB", "LLM", "Legal"],
        "Architecture": ["B.Arch", "Architecture"],
        "Social": ["Psychology", "MSW", "Social", "B.Ed", "Teaching", "Sociology", "Physio"],
        "Robotics": ["Robotics", "Automation", "AI", "ML"],
        "Aviation": ["Pilot", "Aviation", "Merchant Navy"],
        "Hospitality": ["Hotel", "Culinary", "Event"],
        "Media": ["Journalism", "Mass Comm", "Marketing", "PR"]
    }

    allowed_keywords = []
    for cat in user_target_categories:
        allowed_keywords.extend(category_keywords.get(cat, []))

    for course in all_trait_courses:
        if stream == "Class 10":
            recommended_courses_list.append(course)
        else:
            if any(kw.lower() in course.lower() for kw in allowed_keywords):
                recommended_courses_list.append(course)
    
    if not recommended_courses_list:
        recommended_courses_list = all_trait_courses[:6]

    # Optimized to show only the Top 3 most relevant career paths
    recommended_courses_list = recommended_courses_list[:3]

    # Get detailed careers from Interests.xlsx data
    top_careers = data.DATA["careers"].get(top_trait, [])
    
    # Get key exams - filter by stream too
    all_exams_map = {} # Use name as key to avoid duplicates
    
    def add_exams(key):
        for e in data.DATA["exams"].get(key, []):
            all_exams_map[e["name"]] = e

    if "Engineering" in user_target_categories: add_exams("top")
    if "Medicine" in user_target_categories: add_exams("top")
    if "Design" in user_target_categories: add_exams("design")
    if "Law" in user_target_categories: add_exams("law")
    if "Commerce" in user_target_categories: 
        add_exams("commerce")
        add_exams("management")
    if "Architecture" in user_target_categories: add_exams("architecture")
    if "Science" in user_target_categories: add_exams("arts_science")
    if "Social" in user_target_categories: add_exams("arts_science")
    if "Nursing" in user_target_categories: add_exams("nursing")
    
    exams = list(all_exams_map.values())
    if not exams: exams = [{"name": "University Entrance Tests", "reg": "Ongoing", "exam": "Check Website"}]

    # Get recommended colleges
    all_recommended_colleges = []
    for c in data.DATA["colleges"]:
        # Match by stream
        stream_match = any(s in c["streams"] for s in user_target_categories)
        if stream_match:
            all_recommended_colleges.append(c)

    # Sort colleges by Tier/Elite status and filter by marks logic
    def get_college_rank(college):
        t = college.get("type", "").lower()
        if "global" in t: return 1
        if "elite" in t or "#1" in t: return 2
        if "national" in t: return 3
        if "premier" in t: return 4
        if "govt" in t: return 5
        return 6

    all_recommended_colleges.sort(key=get_college_rank)
    
    # If marks are very high, keep elite colleges. If marks are lower, prioritize more realistic ones
    if marks < 75:
        # Move elite/global to the end of the list for lower marks (sorting)
        all_recommended_colleges.sort(key=lambda x: get_college_rank(x) if get_college_rank(x) > 2 else 10)
    
    # Structured Combined Recommendation
    combined_recommendations = []
    
    for course_name in recommended_courses_list:
        # Find colleges offering this specific course or similar
        course_colleges = []
        for c in all_recommended_colleges:
            if any(course_name.lower() in cc.lower() or cc.lower() in course_name.lower() for cc in c.get("courses", [])):
                course_colleges.append({
                    "name": c["name"],
                    "loc": c["loc"],
                    "cutoff": c["cutoff"],
                    "url": c.get("url", "#")
                })
        
        # Fallback to top stream-matched colleges if no specific ones found
        if not course_colleges:
            course_colleges = [{"name": c["name"], "loc": c["loc"], "cutoff": c["cutoff"], "url": c.get("url", "#")} for c in all_recommended_colleges[:5]]
            
        # Find careers related to this course (improved keyword search)
        course_careers = []
        clean_course = course_name.lower().replace("(", "").replace(")", "").replace(".", "")
        keywords = set(clean_course.split() + clean_course.split("/"))
        
        for career in top_careers:
            if any(kw in career.lower() for kw in keywords if len(kw) > 2):
                course_careers.append(career)
        
        if not course_careers:
            course_careers = top_careers[:4]
            
        # Get course-specific specifics (Skills, Tech, Sources)
        specs = data.DATA.get("course_specifics", {}).get(course_name, {})
        if not specs:
            for k, v in data.DATA.get("course_specifics", {}).items():
                if k.lower() in course_name.lower() or course_name.lower() in k.lower():
                    specs = v
                    break
        if not specs:
            specs = {
                "skills": result.get("skills", []),
                "tech": result.get("tech", []),
                "sources": [{"name": s, "url": "#"} for s in result.get("sources", [])]
            }

        # Find related exams for this specific course
        course_exams = []
        exam_cat_map = {
            "B.Tech": "top", "MBBS": "top", "B.Sc Nursing": "nursing",
            "B.Des": "design", "NID": "design", "NIFT": "design",
            "Law": "law", "LLB": "law", "CLAT": "law",
            "B.Com": "commerce", "CA": "commerce",
            "BBA": "management", "MBA": "management", "IPMAT": "management",
            "B.Arch": "architecture", "Architecture": "architecture",
            "B.A.": "arts_science", "Psychology": "arts_science", "TISS": "arts_science"
        }
        
        for kw, cat in exam_cat_map.items():
            if kw.lower() in course_name.lower():
                course_exams.extend(data.DATA["exams"].get(cat, []))
        
        # Unique list based on name
        course_exams = list({e["name"]: e for e in course_exams}.values())
        
        # If no specific exams found for this course, provide a subset of relevant global ones
        if not course_exams:
            course_exams = exams[:2] if exams else []

        combined_recommendations.append({
            "course": course_name,
            "colleges": course_colleges[:6],
            "careers": course_careers[:5],
            "skills": specs.get("skills", []),
            "tech": specs.get("tech", []),
            "sources": specs.get("sources", []),
            "related_exams": course_exams[:3]
        })

    # Calculate percentages
    total_answers = len(answers)
    percentages = {trait: round((count / total_answers) * 100, 1) for trait, count in scores.items()}
    match_percentage = percentages.get(top_trait, 0)

    return {
        "trait": top_trait,
        "match_percentage": match_percentage,
        "percentages": percentages,
        "title": result["title"],
        "traits_desc": result["traits"],
        "combined_recommendations": combined_recommendations,
        "exams": exams,
        "values": tags,
        "academic_profile": {"stream": stream, "marks": marks}
    }


# --- CHATBOT ENDPOINTS ---
# Load career database
CAREER_DB_PATH = os.path.join(os.path.dirname(__file__), "..", "TestGroq", "careers_riasec_database.json")
CAREER_DATABASE = {}

def load_career_database():
    global CAREER_DATABASE
    if os.path.exists(CAREER_DB_PATH):
        try:
            with open(CAREER_DB_PATH, 'r') as f:
                CAREER_DATABASE = json.load(f)
        except Exception as e:
            print(f"Error loading career database: {e}")
            CAREER_DATABASE = {}

load_career_database()

@app.get("/api/chatbot/careers")
def get_chatbot_careers():
    """Return list of available careers for chatbot"""
    careers = list(CAREER_DATABASE.keys())
    return {"careers": sorted(careers)}

def generate_future_self_persona(career: str, years: int, riasec_scores: dict) -> str:
    """Generate persona for the future self"""
    persona = f"""You are a {career} professional who is exactly {years} years older than the user (who is a high school student today). 

Your RIASEC profile as a professional in {career}:
- Realistic (hands-on): {riasec_scores.get('realistic', 50)}%
- Investigative (analytical): {riasec_scores.get('investigative', 50)}%
- Artistic (creative): {riasec_scores.get('artistic', 50)}%
- Social (helping): {riasec_scores.get('social', 50)}%
- Enterprising (leadership): {riasec_scores.get('enterprising', 50)}%
- Conventional (organized): {riasec_scores.get('conventional', 50)}%

You have {years} years of real-world experience in this field. You are speaking to your high school self.

Your role is to:
1. Share authentic insights about your career path
2. Discuss decisions that turned out well
3. Discuss decisions you regret or wish you'd done differently
4. Share skills you wish you had learned earlier in high school
5. Provide practical advice for building a strong foundation now
6. Work backward from your current professional success to today

Be conversational, warm, and genuine. Share real-sounding challenges and victories. Give specific, actionable advice."""
    
    return persona

@app.post("/api/chatbot/init")
def init_chatbot(request: ChatInitRequest):
    """Initialize chatbot with greeting"""
    if not request.career or request.career not in CAREER_DATABASE:
        return {"error": "Invalid career"}
    
    greeting = f"Hi! I'm you, {request.years_ahead} years from now, working as a {request.career}. I'm excited to share my journey with you and answer your questions about this career path! What would you like to know?"
    
    return {"greeting": greeting}

@app.post("/api/chatbot/chat")
def chat_with_future_self(request: ChatRequest):
    """Chat endpoint for future self conversations"""
    if not request.career or request.career not in CAREER_DATABASE:
        return {"error": "Invalid career"}
    
    if not request.message:
        return {"error": "Message required"}
    
    conversation_history = request.conversation_history if request.conversation_history else []
    
    try:
        from groq import Groq
        
        # Initialize Groq client
        client = Groq()
        
        # Get career RIASEC scores
        riasec_scores = CAREER_DATABASE.get(request.career, {})
        
        # Generate persona
        persona = generate_future_self_persona(request.career, request.years_ahead, riasec_scores)
        
        # Create system message with persona
        system_message = f"""{persona}

ADDITIONAL GUIDELINES:
- Always stay in character as the future professional version of the user
- Reference specific skills, experiences, or advice relevant to {request.career}
- When asked about regrets, be honest but constructive
- When asked about good decisions, explain the long-term impact
- When asked about skills to learn now, be specific (e.g., "Learn Python" not just "programming")
- Keep responses conversational and not too long (2-3 paragraphs max)
- Use "I" and "we" (your future self speaking to your current self)"""
        
        # Prepare messages with system message first
        messages_with_system = [
            {"role": "system", "content": system_message}
        ] + conversation_history
        
        # Call Groq API
        completion = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=messages_with_system,
            temperature=0.8,
            max_completion_tokens=1000,
            top_p=0.9
        )
        
        response_text = completion.choices[0].message.content
        
        return {"response": response_text}
        
    except ImportError:
        # Groq not installed, provide fallback response
        fallback_responses = {
            "Software Engineer": f"I'm glad you asked! As a Software Engineer {request.years_ahead} years from now, I can tell you that the most important decision I made was to start coding early. Learn Python or JavaScript now - these skills will open many doors. I've been building amazing applications and the demand for skilled engineers never stops growing!",
            "UX Designer": f"As a UX Designer in {request.years_ahead} years, I can say that understanding both design principles and user psychology has been crucial. Start by learning Figma and studying great design. Also, don't overlook soft skills - empathy and communication are just as important as technical skills!",
            "Data Scientist": f"From my perspective as a Data Scientist now, I wish I had been more serious about statistics and mathematics in high school. The math you're learning now will directly apply to the machine learning work I do daily. Also, start learning Python early!",
            "Psychologist": f"As a Psychologist with {request.years_ahead} years of experience, I can tell you that curiosity about human behavior has been my greatest asset. Take psychology electives if available, read widely about human behavior, and develop strong listening skills. The empathy you build now will serve you well.",
            "Product Manager": f"Working as a Product Manager now, I realize that understanding both business and users is key. Start thinking about why products succeed or fail, learn to communicate clearly, and develop leadership qualities early. These soft skills matter more than you'd think!",
            "Nurse": f"As a Nurse working for {request.years_ahead} years, I want to tell you - caring for people is both rewarding and challenging. Science courses are crucial, so focus on Biology and Chemistry. But also develop emotional resilience and teamwork skills. You'll need them!",
            "Graphic Designer": f"From my career as a Graphic Designer, I can say creativity and technical skills need to grow together. Start using design software now - Photoshop, Figma, Adobe Suite. But remember, design is about solving problems for people, not just making things look pretty.",
            "Business Analyst": f"As a Business Analyst, I analyze how to improve business processes and technology. Start by understanding how businesses work, develop strong analytical skills, and learn Excel thoroughly. Clear communication is your superpower!",
        }
        
        response_text = fallback_responses.get(request.career, f"That's a great question! As a {request.career}, I've learned so much over these {request.years_ahead} years. What aspect interests you most?")
        
        return {"response": response_text}
    except Exception as e:
        print(f"Chatbot Error: {e}")
        return {"response": f"I apologize for the technical difficulty. Please try again. Error: {str(e)}", "error": str(e)}








if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
