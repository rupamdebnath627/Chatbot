from langchain_google_genai import ChatGoogleGenerativeAI
import os

def fetch_llm_model():
    google_api_key = os.environ['GOOGLE_API_KEY']
    model = None
    try:
        model = ChatGoogleGenerativeAI(
            model="gemini-2.0-flash",
            google_api_key=google_api_key,
            temperature=0,
            max_tokens=None,
            timeout=None,
            max_retries=2
        )
    except Exception:
        print("Failed to fetch model")

    return model