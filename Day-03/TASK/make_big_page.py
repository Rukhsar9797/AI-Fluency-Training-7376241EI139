"""Create a large HTML page for the Day 3 overflow experiment."""

text = """
Industrial Equipment Monitoring Data.
Motor M1 rated power is 7.5 kW.
Motor M1 rated voltage is 415 V.
Normal temperature limit is 60 C.
Current operating power is 6 kW.
"""

with open("big.html", "w", encoding="utf-8") as file:

    file.write("<html><body>")

    for _ in range(10000):
        file.write(f"<p>{text}</p>")

    file.write("</body></html>")

print("big.html created successfully.")