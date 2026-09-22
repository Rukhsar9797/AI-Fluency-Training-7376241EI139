from config import client, MODEL

SYSTEM_PROMPT = """
You are a general student assistant.
You do not have access to any private student records.
Answer using only the information provided in the conversation.
Do not invent private academic information.
"""


def chatbot(question):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": question}
        ],
        temperature=0
    )

    return response.choices[0].message.content


if __name__ == "__main__":

    question = (
        "What is my CGPA and am I eligible for the scholarship? "
        "My student ID is STU001."
    )

    print("\n=== PLAIN LLM CHATBOT ===\n")
    print("Question:", question)
    print("\nAnswer:")
    print(chatbot(question))