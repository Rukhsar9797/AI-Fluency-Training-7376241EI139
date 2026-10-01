# Agentic AI: Foundations and Open-Source Practice

## Day 3 Lab — Build a ReAct Agent from Scratch, Break It on Purpose, Then Fix It

### Industrial Energy & Equipment Monitoring Assistant

This project implements a **ReAct (Reasoning + Acting) agent from scratch in Python** using tool calling.

The agent is designed for an industrial equipment-monitoring scenario where it reads an equipment report, performs calculations, and provides an analysis.

The project also intentionally demonstrates common agent failures and then fixes them using safety guards.

---

## Aim

To build a ReAct agent that can:

- Reason about a user query
- Select appropriate tools
- Execute tool calls
- Observe tool results
- Continue reasoning based on observations
- Produce a final answer

The project also demonstrates how an agent can fail through repeated tool calls, invalid tool calls, excessive output and uncontrolled execution.

---

## Scenario

The agent acts as an **Industrial Energy & Equipment Monitoring Assistant**.

It works with a report for **Motor M1** containing information such as:

- Rated power
- Rated voltage
- Current operating power
- Operating time
- Electricity tariff
- Temperature readings
- Normal temperature limit

Example task:

> Read the motor report and calculate the daily energy cost of Motor M1 after checking its rated power and temperature trend.

---

## Tools

### 1. `read_webpage()`

Reads information from:

- Local HTML files
- HTTP/HTTPS web pages

In this project, it is used to read the Motor M1 equipment report.

### 2. `calculator()`

Performs arithmetic calculations using a safe AST-based expression evaluator.

It is used for calculations such as:

```text
Daily energy = Power × Operating hours

Daily cost = Energy × Electricity tariff
