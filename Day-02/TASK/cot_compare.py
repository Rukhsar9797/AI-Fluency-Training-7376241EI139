"""Day 2: Direct Prompting vs Chain-of-Thought."""

from config import client, MODEL, banner


QUESTIONS = [

    # 1. Energy cost calculation
    (
        "A motor operates at 5 kW for 6 hours per day. "
        "If the electricity tariff is Rs. 8 per kWh, "
        "what is the daily operating cost?"
    ),

    # 2. Temperature trend
    (
        "A motor normally operates at 50°C. "
        "During three consecutive observations, its temperature "
        "is 52°C, 61°C and 72°C. "
        "What trend do you observe and what should an operator investigate?"
    ),

    # 3. Sensor logic
    (
        "Three sensors report temperatures of 48°C, 51°C and 75°C. "
        "The normal operating limit is 60°C. "
        "Which sensor reading requires attention?"
    )
]


DIRECT_PROMPT = """
You are an industrial equipment monitoring assistant.

Give only the final answer.
Do not show your reasoning.
"""


COT_PROMPT = """
You are an industrial equipment monitoring assistant.

Solve the problem step by step.
Number each step.
Show calculations where appropriate.

After the steps, write:
Final Answer: <answer>
"""


def ask(system_prompt, question):

    response = client.chat.completions.create(
        model=MODEL,

        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": question
            }
        ],

        temperature=0
    )

    return response.choices[0].message.content.strip()


if __name__ == "__main__":

    banner("DAY 2 — DIRECT PROMPTING VS CHAIN-OF-THOUGHT")

    for number, question in enumerate(QUESTIONS, start=1):

        print("=" * 72)

        print(f"QUESTION {number}:")
        print(question)

        print("\n--- WITHOUT CoT ---")
        print(ask(DIRECT_PROMPT, question))

        print("\n--- WITH CoT ---")
        print(ask(COT_PROMPT, question))

        print()