# Agentic AI: Foundations and Open-Source Practice

## Day 4 Lab — Will It Fit?

### Estimating Memory and Comparing Model Licences

This lab estimates the memory requirements of open models before downloading them and compares model cards and licences to determine which models are suitable for different hardware and use cases.

## Aim

To estimate model memory requirements, compare the estimates with actual memory usage, and evaluate four open models based on size, context, licence, and tool-calling support.

## Objectives

- Calculate model weight and KV-cache memory.
- Estimate total memory requirements.
- Understand the effect of context length.
- Understand the effect of quantization.
- Compare estimated memory with actual Ollama usage.
- Read model cards and identify licence information.
- Compare four open models.
- Make a justified model recommendation.

## Memory Formula

```text
Weights (GB) = Parameters (B) × Bytes per parameter

KV Cache (GB) = Parameters (B) × Context (K tokens) × 0.02

Total (GB) = (Weights + KV Cache) × 1.10
