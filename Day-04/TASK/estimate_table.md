# Memory Estimate Table

## Machine

Available memory: **8 GB**

The estimates use the Day 4 memory formula:

```text
Weights (GB) = Parameters (B) × Bytes per parameter

KV Cache (GB) = Parameters (B) × Context (K) × 0.02

Total (GB) = (Weights + KV Cache) × 1.10