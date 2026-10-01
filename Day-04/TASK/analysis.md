# Day 4 Task — Will It Fit, and May I Use?

## Agentic AI: Foundations and Open-Source Practice

---

# 1. Scenario Statement

## Scenario

I plan to run an open-weight language model locally as an **Industrial Energy and Equipment Monitoring Assistant**.

The assistant will be used to:

- Summarise industrial equipment reports
- Answer questions about motor operating conditions
- Perform simple energy calculations
- Analyse temperature and operating trends
- Support tool-based workflows
- Assist with local equipment-monitoring experiments

The model will primarily be used by **myself for academic and project development**.

## Machine

Available memory:

**8 GB**

## Memory Budget

The model should preferably use no more than the available 8 GB memory.

A model that uses a large percentage of the available memory will be considered a tight fit because the operating system and other applications also require memory.

## Licensing Situation

The model must have a licence that permits the intended use.

For this academic scenario, I will verify the exact model licence and its conditions before using a model in a public GitHub project or commercial application.

Therefore, the decision is based on two separate questions:

1. **Will the model fit in memory?**
2. **Am I permitted to use the model for the intended purpose?**

---

# 2. Aim

The aim of this task is to determine whether an open model can run within an 8 GB memory budget and whether its licence and capabilities are appropriate for the industrial monitoring scenario.

The analysis considers model weights, quantization, KV cache, context length, model cards and licensing.

The memory estimate is used as a planning tool before downloading a model.

---

# 3. Memory Formula

The Day 4 memory formula is:

```text
Weights (GB) = Parameters (B) × Bytes per parameter

KV Cache (GB) = Parameters (B) × Context (K tokens) × 0.02

Total (GB) = (Weights + KV Cache) × 1.10