# Agentic AI: Foundations and Open-Source Practice

## Day 3 Lab — Build a ReAct Agent from Scratch

This lab builds a ReAct agent in plain Python using two tools:

- Calculator
- Web-page / local-file reader

The agent is deliberately tested against failure modes and then improved using safety guards.

## Aim

To implement a ReAct agent loop with tool calling, deliberately trigger common agent failure modes, and add guards to make the agent safer and more reliable.

## Objectives

By completing this lab, the following concepts are demonstrated:

1. Tool registry and JSON tool schemas
2. ReAct: Reason → Act → Observe
3. Calculator tool
4. Web-page and local-file reader
5. Deliberate agent failure testing
6. Repeat detection
7. Output truncation
8. Budget / cost protection
9. Graceful tool-error handling

## Tools

### 1. Calculator

The calculator evaluates basic arithmetic expressions using Python's AST module.

Example:

```text
(12000 + 18000) * 0.9
