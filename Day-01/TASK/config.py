import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

PROVIDER = os.getenv("PROVIDER", "groq").strip().lower()

if PROVIDER == "groq":
    BASE_URL = "https://api.groq.com/openai/v1"
    API_KEY = os.getenv("GROQ_API_KEY")
    MODEL = os.getenv("MODEL", "openai/gpt-oss-120b")

else:
    raise SystemExit("Use PROVIDER=groq for this task.")

if not API_KEY:
    raise SystemExit("GROQ_API_KEY is missing from .env")

client = OpenAI(
    base_url=BASE_URL,
    api_key=API_KEY
)