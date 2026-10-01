"""
Day 5, Part C: Call the REST API directly and measure what you get.

Contains:
1. Local Ollama configuration (commented out)
2. Groq API configuration (active)
"""

import os
import json
import time
import requests
from dotenv import load_dotenv


# Load variables from .env
load_dotenv()


# ============================================================
# 1. LOCAL OLLAMA CONFIGURATION (Commented Out)
# ============================================================

# BASE = "http://localhost:11434"
# MODEL = "qwen2.5:1.5b"          # Change to the model you pulled
# PROMPT = "In three sentences, explain what an AI agent is."


# def list_models():
#     """GET /api/tags - show models stored locally."""
#
#     response = requests.get(
#         f"{BASE}/api/tags",
#         timeout=30
#     )
#
#     tags = response.json()
#
#     print("Models on disk:")
#
#     for model in tags.get("models", []):
#         size_gb = model.get("size", 0) / 1e9
#         print(
#             f"   {model['name']:<28} "
#             f"{size_gb:5.2f} GB"
#         )


# def loaded_models():
#     """GET /api/ps - show models currently loaded in memory."""
#
#     response = requests.get(
#         f"{BASE}/api/ps",
#         timeout=30
#     )
#
#     running = response.json().get("models", [])
#
#     if not running:
#         print("Nothing is loaded in memory.")
#
#     for model in running:
#         print(
#             f"   loaded: {model['name']} "
#             f"{model.get('size', 0) / 1e9:5.2f} GB"
#         )


# def generate_once(model=MODEL, prompt=PROMPT):
#     """POST /api/generate with stream=false."""
#
#     start = time.time()
#
#     response = requests.post(
#         f"{BASE}/api/generate",
#         json={
#             "model": model,
#             "prompt": prompt,
#             "stream": False
#         },
#         timeout=300
#     ).json()
#
#     elapsed = time.time() - start
#     tokens = response.get("eval_count", 0)
#
#     print(
#         f"\n[generate] {elapsed:.1f} s "
#         f"for {tokens} tokens "
#         f"({tokens / elapsed if elapsed else 0:.1f} tokens/s)"
#     )
#
#     print(
#         response.get("response", "").strip()[:300]
#     )


# def chat_streaming(model=MODEL, prompt=PROMPT):
#     """POST /api/chat with streaming and measure TTFT."""
#
#     start = time.time()
#     first_token_at = None
#     pieces = []
#
#     with requests.post(
#         f"{BASE}/api/chat",
#         json={
#             "model": model,
#             "messages": [
#                 {
#                     "role": "user",
#                     "content": prompt
#                 }
#             ],
#             "stream": True
#         },
#         stream=True,
#         timeout=300
#     ) as response:
#
#         for line in response.iter_lines():
#
#             if not line:
#                 continue
#
#             chunk = json.loads(line)
#
#             piece = (
#                 chunk
#                 .get("message", {})
#                 .get("content", "")
#             )
#
#             if piece and first_token_at is None:
#                 first_token_at = time.time() - start
#
#             pieces.append(piece)
#
#     total = time.time() - start
#     text = "".join(pieces)
#
#     print(
#         f"\n[chat, streaming] "
#         f"TTFT {first_token_at:.2f} s | "
#         f"total {total:.1f} s | "
#         f"{len(text)} characters"
#     )
#
#     print(text.strip()[:300])


# def openai_compatible_ollama(model=MODEL, prompt=PROMPT):
#     """POST /v1/chat/completions using local Ollama."""
#
#     response = requests.post(
#         f"{BASE}/v1/chat/completions",
#         headers={
#             "Authorization": "Bearer ollama"
#         },
#         json={
#             "model": model,
#             "messages": [
#                 {
#                     "role": "user",
#                     "content": prompt
#                 }
#             ],
#             "temperature": 0
#         },
#         timeout=300
#     ).json()
#
#     print("\n[/v1/chat/completions]")
#
#     print(
#         response["choices"][0]["message"]["content"]
#         .strip()[:300]
#     )


# ============================================================
# 2. GROQ API CONFIGURATION (ACTIVE)
# ============================================================

BASE = "https://api.groq.com/openai/v1"

# Read all model names from .env
MODEL = os.getenv(
    "MODEL",
    "openai/gpt-oss-120b"
)

MODEL2 = os.getenv(
    "MODEL2",
    "qwen/qwen3-32b"
)

MODEL3 = os.getenv(
    "MODEL3",
    "meta-llama/llama-prompt-guard-2-86m"
)

MODEL4 = os.getenv(
    "MODEL4",
    "whisper-large-v3"
)

PROMPT = "In three sentences, explain what an AI agent is."

API_KEY = os.getenv("GROQ_API_KEY")


# Check API key
if not API_KEY:
    print("Error: GROQ_API_KEY not found in .env file.")
    raise SystemExit(1)


# ============================================================
# 3. GROQ REST API FUNCTION
# ============================================================

def openai_compatible_groq(model=MODEL4, prompt=PROMPT):
    """
    POST /v1/chat/completions

    Uses the Groq REST API directly.
    """

    print(f"Calling Groq API with model: {model}...")

    start = time.time()

    try:
        response = requests.post(
            f"{BASE}/chat/completions",

            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            },

            json={
                "model": model,
                "messages": [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                "temperature": 0
            },

            timeout=30
        )

        elapsed = time.time() - start

        print(
            f"\n[/v1/chat/completions] "
            f"Response in {elapsed:.2f}s:"
        )

        # Convert response to JSON
        data = response.json()

        # Successful response
        if "choices" in data:

            answer = (
                data["choices"][0]["message"]["content"]
                .strip()
            )

            print(answer)

        # Error response
        else:

            print(
                "Error or unexpected response:"
            )

            print(
                json.dumps(
                    data,
                    indent=2
                )
            )

    except requests.exceptions.RequestException as error:

        print(
            f"\nRequest failed: {error}"
        )


# ============================================================
# 4. MAIN PROGRAM
# ============================================================

if __name__ == "__main__":

    # --------------------------------------------------------
    # Local Ollama - currently disabled
    # --------------------------------------------------------

    # list_models()
    # generate_once()
    # chat_streaming()
    # openai_compatible_ollama()
    # print()
    # loaded_models()


    # --------------------------------------------------------
    # Groq API - active
    # --------------------------------------------------------

    openai_compatible_groq()