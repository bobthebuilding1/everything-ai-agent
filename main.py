import os
import sys
from google import genai

def run_ai_agent():
    # 1. Fetch the secure API key from environment variables
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("ERROR: GEMINI_API_KEY environment variable is missing.")
        sys.exit(1)
        
    print("🤖 Everything AI Agent waking up...")
    
    # 2. Initialize the AI Client
    client = genai.Client(api_key=api_key)
    
    # 3. Formulate the core prompt instructing the AI
    prompt = (
        "You are an omni-capable 'Everything AI' assistant running autonomously on GitHub. "
        "Provide a high-density, 3-bullet-point morning brief detailing how to systematically "
        "organize tasks, monitor markets, and track software code changes efficiently today."
    )
    
    # 4. Generate the response
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
        )
        print("\n=== AI AGENT DAILY BRIEF ===")
        print(response.text)
        print("============================\n")
        print("✅ Task executed successfully.")
    except Exception as e:
        print(f"Execution failed: {e}")

if __name__ == "__main__":
    run_ai_agent()
