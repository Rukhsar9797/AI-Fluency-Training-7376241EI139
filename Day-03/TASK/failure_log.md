# Day 3 Failure Log

## Scenario

Industrial Energy & Equipment Monitoring Assistant.

The agent reads an equipment report and uses a calculator to perform energy and equipment calculations.

## Failure 1: Repeating Tool Calls

### Observation

An agent can repeatedly request the same tool with the same arguments.

### Cause

There is no mechanism to remember previously executed tool calls.

### Fix

The guarded agent stores a tool-call signature and blocks repeated calls.

---

## Failure 2: Hallucinated Tool Call

### Observation

The LLM may request a tool that is not present in the tool registry.

Example:

```text
get_motor_temperature()