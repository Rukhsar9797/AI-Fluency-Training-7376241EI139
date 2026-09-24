# Agentic AI – Day 2 Task

## Smart Energy & Equipment Monitoring Assistant

This project compares three AI approaches for solving industrial energy and equipment-monitoring problems:

1. Direct Prompting
2. Chain-of-Thought (CoT)
3. ReAct (Reason + Act)

### Scenario

The assistant handles common industrial monitoring tasks such as:

- Calculating daily motor energy cost
- Analyzing temperature trends
- Detecting abnormal sensor readings
- Retrieving motor specifications using tools
- Comparing operating values with rated limits

### Example

A 5 kW motor operates for 6 hours/day at ₹8/kWh:

**Energy Cost = 5 × 6 × 8 = ₹240/day**

For Motor M1:

- Rated Power: 7.5 kW
- Rated Voltage: 415 V
- Normal Temperature Limit: 60°C

The ReAct agent retrieves these values using a tool before making the comparison.

### Approaches Compared

| Approach | Main Idea |
|---|---|
| Direct Prompting | Generates an answer directly |
| Chain-of-Thought | Breaks the problem into reasoning steps |
| ReAct | Reasons, uses tools, observes results, and continues |

### Self-Consistency

The same reasoning question is executed multiple times at a non-zero temperature to observe answer variation. The results are compared with temperature 0 to study consistency.

### Tools

The project uses:

- `get_motor_spec()` – retrieves motor specifications
- `calculate()` – performs arithmetic calculations

### Files

```text
Day_02/
├── config.py
├── tools.py
├── cot_compare.py
├── self_consistency.py
├── react_trace.py
├── analysis.md
├── requirements.txt
└── screenshots/
