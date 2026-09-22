"""Tools available to the AI agent."""

from private_data import STUDENT_DATA


def get_student_record(student_id: str) -> str:
    """Retrieve private student information."""

    if student_id != STUDENT_DATA["student_id"]:
        return "Student record not found."

    return (
        f"Name: {STUDENT_DATA['name']}\n"
        f"CGPA: {STUDENT_DATA['cgpa']}\n"
        f"Attendance: {STUDENT_DATA['attendance']}%\n"
        f"Semester: {STUDENT_DATA['semester']}\n"
        f"Total Credits: {STUDENT_DATA['total_credits']}\n"
        f"Scholarship: {STUDENT_DATA['scholarship_percentage']}%\n"
        f"Pending Fees: ₹{STUDENT_DATA['pending_fees']}"
    )


def calculate_fee_after_scholarship() -> str:
    """Calculate pending fee after the student's scholarship."""

    fee = STUDENT_DATA["pending_fees"]
    scholarship = STUDENT_DATA["scholarship_percentage"]

    final_fee = fee * (1 - scholarship / 100)

    return f"₹{final_fee:.2f}"


def check_scholarship_eligibility() -> str:
    """Check whether the student satisfies scholarship conditions."""

    cgpa = STUDENT_DATA["cgpa"]
    attendance = STUDENT_DATA["attendance"]

    if cgpa >= 8.0 and attendance >= 75:
        return "Eligible for scholarship."

    return "Not eligible for scholarship."


TOOL_FUNCTIONS = {
    "get_student_record": get_student_record,
    "calculate_fee_after_scholarship": calculate_fee_after_scholarship,
    "check_scholarship_eligibility": check_scholarship_eligibility,
}


TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_student_record",
            "description": "Retrieve private academic information for a student.",
            "parameters": {
                "type": "object",
                "properties": {
                    "student_id": {
                        "type": "string"
                    }
                },
                "required": ["student_id"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "calculate_fee_after_scholarship",
            "description": "Calculate the student's pending fee after scholarship.",
            "parameters": {
                "type": "object",
                "properties": {}
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "check_scholarship_eligibility",
            "description": "Check scholarship eligibility using CGPA and attendance.",
            "parameters": {
                "type": "object",
                "properties": {}
            }
        }
    }
]