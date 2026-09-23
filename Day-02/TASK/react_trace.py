"""Day 2: ReAct agent with tool usage."""

import json

from config import client, MODEL
from tools import TOOLS, TOOL_FUNCTIONS


QUESTION = (
    "Motor M1 is currently operating at 6 kW and 415 V. "
    "What is the rated power and rated voltage of Motor M1? "
    "Is the current operating power within its rated power limit?"
)


SYSTEM_PROMPT = """
You are an industrial equipment monitoring assistant.

You have access to tools containing motor specifications.

Never guess motor specifications.

Use get_motor_spec when you need motor information.

Use calculate when mathematical comparison is required.

For the user's question:

1. Identify what information is required.
2. Retrieve the motor specification using the tool.
3. Compare the operating power with the rated power.
4. Compare the operating voltage with the rated voltage.
5. Give a clear final answer.
"""


def agent(question, max_steps=8):

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

        if not message.tool_calls:

            return message.content.strip()

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
                f"Action = {name}({arguments})"
            )

            print(f"Observation = {result}\n")

            messages.append({
                "role": "tool",
                "tool_call_id": call.id,
                "content": result
            })

    return "Maximum steps reached."


if __name__ == "__main__":

    print("QUESTION:")
    print(QUESTION)

    print("\n--- ReAct Trace ---\n")

    answer = agent(QUESTION)

    print("\nFINAL ANSWER:")
    print(answer)