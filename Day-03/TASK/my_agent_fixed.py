"""Day 3: Guarded ReAct agent."""

import json

from config import client, MODEL, banner
from my_tools import TOOLS, TOOL_FUNCTIONS


SYSTEM_PROMPT = """
You are an Industrial Energy and Equipment Monitoring Assistant.

Available tools:

1. read_webpage
2. calculator

Rules:

- Use read_webpage for information stored in equipment reports.
- Use calculator for arithmetic.
- Never guess values from the report.
- Do not repeatedly call the same tool with the same arguments.
- Stop once the answer is complete.
"""


MAX_STEPS = 6
MAX_TOOL_OUTPUT = 2000
MAX_TOOL_CALLS = 8


def agent(question, verbose=True):

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

    previous_calls = set()
    total_tool_calls = 0

    for step in range(1, MAX_STEPS + 1):

        # ----------------------------------------------------
        # STEP GUARD
        # ----------------------------------------------------

        if step > MAX_STEPS:

            return "Stopped: maximum reasoning steps reached."

        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=TOOLS,
            temperature=0
        )

        message = response.choices[0].message

        # ----------------------------------------------------
        # FINAL ANSWER
        # ----------------------------------------------------

        if not message.tool_calls:

            return message.content.strip()

        # ----------------------------------------------------
        # STORE ASSISTANT TOOL CALL
        # ----------------------------------------------------

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

        # ----------------------------------------------------
        # TOOL EXECUTION
        # ----------------------------------------------------

        for call in message.tool_calls:

            total_tool_calls += 1

            # ------------------------------------------------
            # BUDGET GUARD
            # ------------------------------------------------

            if total_tool_calls > MAX_TOOL_CALLS:

                return (
                    "Stopped: tool-call budget exceeded."
                )

            name = call.function.name

            try:

                arguments = json.loads(
                    call.function.arguments or "{}"
                )

            except json.JSONDecodeError as error:

                result = (
                    f"Invalid JSON arguments: {error}"
                )

                messages.append(
                    {
                        "role": "tool",
                        "tool_call_id": call.id,
                        "content": result
                    }
                )

                continue

            # ------------------------------------------------
            # TOOL VALIDATION
            # ------------------------------------------------

            if name not in TOOL_FUNCTIONS:

                result = (
                    f"Unknown tool '{name}'. "
                    f"Available tools: "
                    f"{list(TOOL_FUNCTIONS)}"
                )

                messages.append(
                    {
                        "role": "tool",
                        "tool_call_id": call.id,
                        "content": result
                    }
                )

                continue

            # ------------------------------------------------
            # REPEAT DETECTION
            # ------------------------------------------------

            call_signature = (
                name,
                json.dumps(
                    arguments,
                    sort_keys=True
                )
            )

            if call_signature in previous_calls:

                result = (
                    "Repeated tool call detected. "
                    "Do not repeat the same action. "
                    "Use the previous observation."
                )

                print(
                    f"Step {step}: "
                    f"REPEAT BLOCKED -> {name}"
                )

                messages.append(
                    {
                        "role": "tool",
                        "tool_call_id": call.id,
                        "content": result
                    }
                )

                continue

            previous_calls.add(call_signature)

            # ------------------------------------------------
            # EXECUTE TOOL
            # ------------------------------------------------

            try:

                function = TOOL_FUNCTIONS[name]

                result = function(**arguments)

            except TypeError as error:

                result = (
                    f"Tool argument error: {error}"
                )

            except Exception as error:

                result = (
                    f"Tool error: {type(error).__name__}: "
                    f"{error}"
                )

            # ------------------------------------------------
            # OUTPUT TRUNCATION
            # ------------------------------------------------

            result = str(result)

            if len(result) > MAX_TOOL_OUTPUT:

                result = (
                    result[:MAX_TOOL_OUTPUT]
                    + "\n[Tool output truncated]"
                )

            if verbose:

                print(
                    f"Step {step}: "
                    f"{name}({arguments}) -> "
                    f"{result[:200]}"
                )

            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": call.id,
                    "content": result
                }
            )

    return "Stopped: maximum steps reached."


if __name__ == "__main__":

    banner("DAY 3 - GUARDED REACT AGENT")

    question = """
    Read equipment_report.html.

    Find the rated power of Motor M1 and its current operating power.
    Calculate the percentage of rated power currently being used.

    Calculate the daily energy cost for 6 hours of operation
    at Rs. 8 per kWh.

    Finally, determine whether the temperature readings
    show a rising trend.
    """

    print("QUESTION:")
    print(question)

    print("\nANSWER:")

    print(agent(question))