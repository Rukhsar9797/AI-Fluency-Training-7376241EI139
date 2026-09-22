from private_data import STUDENT_DATA


def workflow(question):

    question = question.lower()

    if "cgpa" in question:
        return f"CGPA: {STUDENT_DATA['cgpa']}"

    if "attendance" in question:
        return f"Attendance: {STUDENT_DATA['attendance']}%"

    if "scholarship" in question:

        if (
            STUDENT_DATA["cgpa"] >= 8.0
            and STUDENT_DATA["attendance"] >= 75
        ):
            return "Eligible for scholarship."

        return "Not eligible for scholarship."

    if "fee" in question:

        fee = STUDENT_DATA["pending_fees"]

        scholarship = STUDENT_DATA["scholarship_percentage"]

        final_fee = fee * (1 - scholarship / 100)

        return f"Fee after scholarship: ₹{final_fee:.2f}"

    return "Sorry, this question is not covered by the predefined rules."


if __name__ == "__main__":

    question = (
        "Am I eligible for the scholarship?"
    )

    print("\n=== RULE-BASED WORKFLOW ===\n")
    print("Question:", question)
    print("\nAnswer:")
    print(workflow(question))