import os
import random

def get_response(prompt):
    """
    Simulates sending a prompt to an AI tool and returning the response.
    In a real scenario, this would call an API like OpenAI or Gemini.
    """
    # Placeholder for real AI logic
    # api_key = os.getenv("AI_API_KEY")
    # if not api_key:
    #     return "Error: API Key not found. Please set AI_API_KEY environment variable."
    
    responses = [
        f"That's an interesting question about '{prompt}'. Here is a simulated AI response.",
        f"I can help you with '{prompt}'. As an AI, I suggest looking into...",
        f"Processing request: '{prompt}'... Done!",
        "This is a mocked response from your custom library."
    ]
    return random.choice(responses)

def summarize_text(text):
    """
    Simulates summarizing a long text.
    """
    if len(text) < 50:
        return text
    return text[:50] + "... (summarized)"

def format_response(text):
    """
    Cleans or processes AI output before displaying.
    Converts newlines to <br> or handles markdown-like syntax if needed.
    """
    return text.strip().capitalize()
