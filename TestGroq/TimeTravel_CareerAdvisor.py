from groq import Groq
import json
import os

# Initialize Groq client
client = Groq()

# RIASEC Career Database (can be loaded from external file)
# Format: {"career_name": {"realistic": %, "investigative": %, ...}, ...}
CAREER_DATABASE = {
    "Software Engineer": {
        "realistic": 40,
        "investigative": 60,
        "artistic": 10,
        "social": 20,
        "enterprising": 30,
        "conventional": 40
    },
    "Data Scientist": {
        "realistic": 30,
        "investigative": 80,
        "artistic": 15,
        "social": 25,
        "enterprising": 35,
        "conventional": 50
    },
    "Product Manager": {
        "realistic": 35,
        "investigative": 45,
        "artistic": 25,
        "social": 70,
        "enterprising": 75,
        "conventional": 55
    },
    "UX Designer": {
        "realistic": 30,
        "investigative": 40,
        "artistic": 75,
        "social": 60,
        "enterprising": 55,
        "conventional": 35
    },
    "Management Consultant": {
        "realistic": 45,
        "investigative": 60,
        "artistic": 20,
        "social": 75,
        "enterprising": 80,
        "conventional": 70
    },
    "Nurse": {
        "realistic": 60,
        "investigative": 55,
        "artistic": 25,
        "social": 85,
        "enterprising": 40,
        "conventional": 65
    },
    "Graphic Designer": {
        "realistic": 40,
        "investigative": 35,
        "artistic": 90,
        "social": 50,
        "enterprising": 60,
        "conventional": 45
    },
    "Business Analyst": {
        "realistic": 50,
        "investigative": 70,
        "artistic": 20,
        "social": 55,
        "enterprising": 65,
        "conventional": 75
    }
}

def load_career_database(filepath=None):
    """Load career database from JSON file if provided"""
    if filepath and os.path.exists(filepath):
        try:
            with open(filepath, 'r') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading career database: {e}")
            return CAREER_DATABASE
    return CAREER_DATABASE

def display_careers():
    """Display available careers for selection"""
    print("\n" + "="*60)
    print("AVAILABLE CAREERS - Select Your Field of Interest")
    print("="*60)
    for i, career in enumerate(CAREER_DATABASE.keys(), 1):
        print(f"{i}. {career}")
    print("="*60)

def get_career_choice():
    """Get career selection from user"""
    display_careers()
    while True:
        try:
            choice = int(input("\nEnter the number of your career choice: "))
            careers = list(CAREER_DATABASE.keys())
            if 1 <= choice <= len(careers):
                return careers[choice - 1]
            else:
                print(f"Please enter a number between 1 and {len(careers)}")
        except ValueError:
            print("Please enter a valid number")

def get_time_period():
    """Get time period selection from user"""
    print("\n" + "="*60)
    print("TIME TRAVEL - How Far Into Your Future?")
    print("="*60)
    print("1. 5 Years")
    print("2. 10 Years")
    print("3. 20 Years")
    print("="*60)
    
    while True:
        try:
            choice = int(input("\nEnter your choice (1-3): "))
            if choice == 1:
                return 5
            elif choice == 2:
                return 10
            elif choice == 3:
                return 20
            else:
                print("Please enter 1, 2, or 3")
        except ValueError:
            print("Please enter a valid number")

def generate_future_self_persona(career, years, riasec_scores):
    """Generate a detailed persona for the future self"""
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

def chat_with_future_self(career, years):
    """Main chatbot function - conversation with future self"""
    conversation_history = []
    riasec_scores = CAREER_DATABASE.get(career, {})
    
    persona = generate_future_self_persona(career, years, riasec_scores)
    
    print("\n" + "="*60)
    print(f"🚀 WELCOME TO YOUR FUTURE! 🚀")
    print(f"You are now talking to yourself in {years} years")
    print(f"Career: {career}")
    print("="*60)
    print("\nYour future self is ready to talk. Type 'quit' to exit.\n")
    
    # Initial greeting from future self
    initial_message = f"Hi! I'm you, {years} years from now, working as a {career}. I'm excited to share my journey with you and answer your questions about this career path!"
    print(f"Future You: {initial_message}\n")
    
    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() == 'quit':
            print("\n✨ Thank you for speaking with your future self! ✨")
            print("Remember: Your choices today shape who you become tomorrow.")
            break
        
        if not user_input:
            continue
        
        # Build conversation history
        conversation_history.append({
            "role": "user",
            "content": user_input
        })
        
        # Create system message with persona
        system_message = f"""{persona}

ADDITIONAL GUIDELINES:
- Always stay in character as the future professional version of the user
- Reference specific skills, experiences, or advice relevant to {career}
- When asked about regrets, be honest but constructive
- When asked about good decisions, explain the long-term impact
- When asked about skills to learn now, be specific (e.g., "Learn Python" not just "programming")
- Keep responses conversational and not too long (2-3 paragraphs max)
- Use "I" and "we" (your future self speaking to your current self)"""
        
        try:
            # Call Groq API with streaming
            response_text = ""
            print(f"Future You: ", end="", flush=True)
            
            # Prepare messages with system message first
            messages_with_system = [
                {"role": "system", "content": system_message}
            ] + conversation_history
            
            completion = client.chat.completions.create(
                model="openai/gpt-oss-120b",  # Using Groq's current model
                messages=messages_with_system,
                temperature=0.8,
                max_completion_tokens=1000,
                top_p=0.9,
                stream=True
            )
            
            # Stream the response
            for chunk in completion:
                if chunk.choices[0].delta.content:
                    response_text += chunk.choices[0].delta.content
                    print(chunk.choices[0].delta.content, end="", flush=True)
            
            print("\n")
            
            # Add assistant response to history
            conversation_history.append({
                "role": "assistant",
                "content": response_text
            })
            
        except Exception as e:
            print(f"Error communicating with AI: {e}")
            print("Let's try again...\n")
            conversation_history.pop()  # Remove the user message if API fails

def reverse_planning_mode():
    """Guide user through reverse planning from future to today"""
    print("\n" + "="*60)
    print("🎯 REVERSE PLANNING MODE")
    print("="*60)
    print("\nLet's work backward from your future success to today!")
    print("This will help you create a practical roadmap.\n")
    
    career = get_career_choice()
    years = get_time_period()
    
    # Generate reverse planning guidance
    riasec_scores = CAREER_DATABASE.get(career, {})
    
    reverse_plan_prompt = f"""Create a detailed reverse planning timeline for a high school student who wants to become a {career} professional in {years} years.

RIASEC Profile for {career}:
- Realistic: {riasec_scores.get('realistic', 50)}%
- Investigative: {riasec_scores.get('investigative', 50)}%
- Artistic: {riasec_scores.get('artistic', 50)}%
- Social: {riasec_scores.get('social', 50)}%
- Enterprising: {riasec_scores.get('enterprising', 50)}%
- Conventional: {riasec_scores.get('conventional', 50)}%

Please provide:
1. Where they should be at each milestone ({years} years, {years//2} years, 1 year, now)
2. Key skills needed at each stage
3. Education/certification path
4. Internship/experience recommendations
5. Specific actions they should take in the next 3 months

Format this as a clear, actionable roadmap that feels achievable."""

    try:
        print(f"\n📊 REVERSE PLANNING ROADMAP")
        print(f"Career: {career} | Timeline: {years} years")
        print("-"*60 + "\n")
        
        completion = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[
                {"role": "system", "content": "You are a helpful career advisor. Provide practical, actionable advice."},
                {"role": "user", "content": reverse_plan_prompt}
            ],
            temperature=0.7,
            max_completion_tokens=2000,
            stream=True
        )
        
        for chunk in completion:
            if chunk.choices[0].delta.content:
                print(chunk.choices[0].delta.content, end="", flush=True)
        
        print("\n")
        
    except Exception as e:
        print(f"Error generating reverse plan: {e}")

def main():
    """Main application loop"""
    print("\n" + "="*60)
    print("⏰ TIME-TRAVEL CAREER ADVISOR ⏰")
    print("Talk to Your Future Self")
    print("="*60)
    
    while True:
        print("\n1. Chat with Your Future Self")
        print("2. Reverse Planning (Future → Today)")
        print("3. Exit")
        
        choice = input("\nSelect an option (1-3): ").strip()
        
        if choice == "1":
            career = get_career_choice()
            years = get_time_period()
            chat_with_future_self(career, years)
        
        elif choice == "2":
            reverse_planning_mode()
        
        elif choice == "3":
            print("\n✨ Remember: Your future is shaped by the choices you make today! ✨\n")
            break
        
        else:
            print("Please enter 1, 2, or 3")

if __name__ == "__main__":
    main()
