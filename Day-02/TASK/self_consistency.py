"""Day 2: Self-consistency experiment."""

from collections import Counter

from config import client, MODEL, banner


QUESTION = """
A motor operates at 5 kW for 6 hours per day.
The electricity tariff is Rs. 8 per kWh.

What is the daily operating cost?

Give the final answer clearly.
"""


def ask(temperature):

    response = client.chat.completions.create(
        model=MODEL,

        messages=[
            {
                "role": "system",
                "content": (
                    "You are an industrial energy monitoring assistant. "
                    "Solve the calculation carefully."
                )
            },
            {
                "role": "user",
                "content": QUESTION
            }
        ],

        temperature=temperature
    )

    return response.choices[0].message.content.strip()


if __name__ == "__main__":

    banner("DAY 2 — SELF CONSISTENCY")

    answers = []

    print("QUESTION:")
    print(QUESTION)

    print("\n--- Temperature = 0.7 ---\n")

    for i in range(5):

        answer = ask(0.7)

        answers.append(answer)

        print(f"Run {i + 1}:")
        print(answer)
        print()

    counts = Counter(answers)

    print("--- MOST COMMON RESPONSE ---")

    most_common = counts.most_common(1)[0]

    print(most_common[0])

    print("\nOccurrences:", most_common[1])

    print("\n--- Temperature = 0 ---")

    deterministic_answer = ask(0)

    print(deterministic_answer)