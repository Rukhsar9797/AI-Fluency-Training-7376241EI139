import json

from config import client, MODEL
from tools import TOOLS, TOOL_FUNCTIONS


SYSTEM_PROMPT = """
You are a student academic assistant.

You have access to private student information through tools.

Never guess private information.

Use get_student_record when you need academic information.

Use check_scholarship_eligibility when asked about scholarship eligibility.

Use calculate_fee_after_scholarship when asked about the final fee.

Student ID for the available record is STU001.
"""


def agent(question, max_steps=6):

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": question
        }
    ]

    for step in range(1, max_steps + 1):

        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=TOOLS,
            temperature=0,
            reasoning_effort="low"
        )

        message = response.choices[0].message

        # No more tools required
        if not message.tool_calls:
            return message.content.strip()

        # Add assistant tool-call message
        messages.append({
            "role": "assistant",
            "content": message.content or "",
            "tool_calls": [
                {
                    "id": call.id,
                    "type": "function",
                    "function": {
                        "name": call.function.name,
                        "arguments": call.function.arguments
                    }
                }
                for call in message.tool_calls
            ]
        })

        # Execute tools
        for call in message.tool_calls:

            name = call.function.name.split("<|channel|>")[0]

            arguments = json.loads(
                call.function.arguments or "{}"
            )

            function = TOOL_FUNCTIONS.get(name)

            if function:
                result = function(**arguments)
            else:
                result = f"Unknown tool: {name}"

            print(
                f"Step {step}: "
                f"{name}({arguments}) -> {result}"
            )

            messages.append({
                "role": "tool",
                "tool_call_id": call.id,
                "content": result
            })

    return "Maximum steps reached."


if __name__ == "__main__":

    question = (
        "What is my CGPA, am I eligible for the scholarship, "
        "and how much fee do I need to pay after the scholarship?"
    )

    print("\n=== AI AGENT ===\n")
    print("Question:", question)
    print("\nAgent execution:\n")

    answer = agent(question)

    print("\nFinal Answer:")
    print(answer)