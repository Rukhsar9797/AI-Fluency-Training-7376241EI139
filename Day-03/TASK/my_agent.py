"""Day 3: ReAct agent - intentionally without safety guards."""

import json

from config import client, MODEL, banner
from my_tools import TOOLS, TOOL_FUNCTIONS


SYSTEM_PROMPT = """
You are an Industrial Energy and Equipment Monitoring Assistant.

You have two tools:

1. read_webpage
2. calculator

Always use read_webpage when the user asks about information
contained in an equipment report.

Always use calculator for arithmetic.

Never guess equipment values.

Return a final answer after completing the required tool calls.
"""


def agent(question, max_steps=10, verbose=True):

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
            temperature=0
        )

        message = response.choices[0].message

        # Final answer
        if not message.tool_calls:

            return message.content.strip()

        # Add assistant tool call
        messages.append(
            {
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
            }
        )

        # Execute tools
        for call in message.tool_calls:

            name = call.function.name

            try:

                arguments = json.loads(
                    call.function.arguments or "{}"
                )

                function = TOOL_FUNCTIONS.get(name)

                if function is None:

                    result = (
                        f"Unknown tool: {name}. "
                        f"Available tools: "
                        f"{list(TOOL_FUNCTIONS)}"
                    )

                else:

                    result = function(**arguments)

            except json.JSONDecodeError as error:

                result = f"Invalid JSON arguments: {error}"

            except TypeError as error:

                result = f"Tool argument error: {error}"

            except Exception as error:

                result = f"Tool error: {error}"

            if verbose:

                print(
                    f"Step {step}: "
                    f"{name}({arguments}) -> "
                    f"{str(result)[:200]}"
                )

            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": call.id,
                    "content": str(result)
                }
            )

    return "Stopped after maximum steps."


if __name__ == "__main__":

    banner("DAY 3 - UNGUARDED REACT AGENT")

    question = """
    Read equipment_report.html.

    Find the rated power of Motor M1 and its current operating power.
    Then calculate the percentage of rated power currently being used.

    Also calculate the daily energy cost when the motor operates
    for 6 hours per day at Rs. 8 per kWh.

    Finally, comment on whether the temperature readings show
    a rising trend.
    """

    print("QUESTION:")
    print(question)

    print("\nANSWER:")

    print(agent(question))