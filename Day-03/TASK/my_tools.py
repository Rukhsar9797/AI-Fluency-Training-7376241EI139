"""Day 3: Tools for an Industrial Energy & Equipment Monitoring Agent."""

import ast
import operator
import os
import re


# ============================================================
# TOOL 1: SAFE CALCULATOR
# ============================================================

_OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.USub: operator.neg
}


def _evaluate(node):
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value

    if isinstance(node, ast.BinOp) and type(node.op) in _OPS:
        return _OPS[type(node.op)](
            _evaluate(node.left),
            _evaluate(node.right)
        )

    if isinstance(node, ast.UnaryOp) and type(node.op) in _OPS:
        return _OPS[type(node.op)](
            _evaluate(node.operand)
        )

    raise ValueError("Unsupported expression")


def calculator(expression: str) -> str:
    """
    Evaluate a basic arithmetic expression.

    Example:
    (5 * 6 * 8)
    """

    try:
        result = _evaluate(
            ast.parse(expression, mode="eval").body
        )

        return str(result)

    except Exception as error:
        return (
            f"Calculator error: {error}. "
            "Use only numbers and + - * / ** ( )."
        )


# ============================================================
# TOOL 2: WEB PAGE / LOCAL FILE READER
# ============================================================

TAG = re.compile(
    r"<(script|style)[^>]*>.*?</\1>|<[^>]+>",
    re.S | re.I
)

SPACES = re.compile(r"\s+")


def read_webpage(url: str, max_chars: int = 2000) -> str:
    """
    Read a web page or local HTML/text file.
    """

    try:

        # Read a real web page
        if url.startswith("http://") or url.startswith("https://"):

            import requests

            response = requests.get(
                url,
                timeout=10,
                headers={
                    "User-Agent": "AgenticAI-Lab/1.0"
                }
            )

            response.raise_for_status()

            raw = response.text

        # Read a local file
        elif os.path.exists(url):

            with open(
                url,
                encoding="utf-8",
                errors="ignore"
            ) as file:

                raw = file.read()

        else:

            return (
                f"Read error: '{url}' is not a URL "
                "and no such file exists."
            )

    except Exception as error:

        return (
            f"Read error: {type(error).__name__}: {error}"
        )

    # Remove HTML tags
    text = TAG.sub(" ", raw)

    # Normalize spaces
    text = SPACES.sub(" ", text).strip()

    # Prevent very large tool output
    if len(text) > max_chars:

        text = (
            text[:max_chars]
            + f" ... [truncated, {len(text)} characters total]"
        )

    return text or "Read error: no readable text found."


# ============================================================
# TOOL REGISTRY
# ============================================================

TOOL_FUNCTIONS = {
    "calculator": calculator,
    "read_webpage": read_webpage
}


TOOLS = [

    {
        "type": "function",
        "function": {

            "name": "calculator",

            "description":
                "Evaluate arithmetic expressions using "
                "+ - * / ** and brackets.",

            "parameters": {
                "type": "object",

                "properties": {
                    "expression": {
                        "type": "string",
                        "description":
                            "Arithmetic expression to calculate."
                    }
                },

                "required": ["expression"]
            }
        }
    },

    {
        "type": "function",
        "function": {

            "name": "read_webpage",

            "description":
                "Read a web page or a local HTML/text file "
                "and return its visible text.",

            "parameters": {
                "type": "object",

                "properties": {
                    "url": {
                        "type": "string",
                        "description":
                            "URL or local file name."
                    }
                },

                "required": ["url"]
            }
        }
    }
]


# ============================================================
# TOOL TESTS
# ============================================================

if __name__ == "__main__":

    print("Calculator test:")
    print(calculator("(5 * 6 * 8)"))

    print("\nPower test:")
    print(calculator("2 ** 10"))

    print("\nInvalid calculator test:")
    print(calculator("import os"))

    print("\nEquipment report test:")
    print(read_webpage("equipment_report.html")[:500])

    print("\nMissing file test:")
    print(read_webpage("no_such_file.html"))