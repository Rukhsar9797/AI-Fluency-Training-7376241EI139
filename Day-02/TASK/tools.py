"""Tools for the Smart Energy and Equipment Monitoring Assistant."""

MOTOR_DATA = {
    "M1": {
        "rated_power": 7.5,
        "rated_voltage": 415,
        "normal_temperature": 60
    }
}


def get_motor_spec(motor_id):
    """Retrieve specifications for a motor."""

    motor_id = motor_id.strip().upper()

    motor = MOTOR_DATA.get(motor_id)

    if motor is None:
        return f"Motor {motor_id} not found."

    return (
        f"Motor: {motor_id}\n"
        f"Rated Power: {motor['rated_power']} kW\n"
        f"Rated Voltage: {motor['rated_voltage']} V\n"
        f"Normal Temperature Limit: {motor['normal_temperature']} °C"
    )


def calculate(expression):
    """Perform a basic mathematical calculation."""

    try:
        result = eval(
            expression,
            {"__builtins__": {}},
            {}
        )

        return str(result)

    except Exception as error:
        return f"Calculation error: {error}"


TOOL_FUNCTIONS = {
    "get_motor_spec": get_motor_spec,
    "calculate": calculate
}


TOOLS = [

    {
        "type": "function",
        "function": {
            "name": "get_motor_spec",
            "description": (
                "Retrieve the rated power, rated voltage and "
                "normal temperature limit of a motor."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "motor_id": {
                        "type": "string"
                    }
                },
                "required": ["motor_id"]
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "calculate",
            "description": "Calculate a mathematical expression.",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string"
                    }
                },
                "required": ["expression"]
            }
        }
    }
]