# Day 4 Task
# Will It Fit, and May I Use?
# Memory estimation, quantization and context-length comparison

BYTES_PER_PARAM = {
    "FP16": 2.00,
    "BF16": 2.00,
    "Q8_0": 1.00,
    "Q6_K": 0.81,
    "Q5_K_M": 0.68,
    "Q4_K_M": 0.57,
    "Q3_K_M": 0.43,
}

KV_GB_PER_B_PER_1K = 0.02
OVERHEAD = 1.10


def estimate(params_b, precision="Q4_K_M", context_k=8):
    """
    Estimate model memory.

    params_b   : Parameters in billions
    precision  : Quantization / precision type
    context_k  : Context length in thousands of tokens

    Returns:
        weights_gb
        kv_gb
        total_gb
    """

    if precision not in BYTES_PER_PARAM:
        raise ValueError(
            f"Unknown precision '{precision}'. "
            f"Choose from {list(BYTES_PER_PARAM.keys())}"
        )

    # Model weights
    weights_gb = params_b * BYTES_PER_PARAM[precision]

    # KV cache
    kv_gb = params_b * context_k * KV_GB_PER_B_PER_1K

    # Runtime overhead
    total_gb = (weights_gb + kv_gb) * OVERHEAD

    return weights_gb, kv_gb, total_gb


def verdict(total_gb, available_gb):
    """
    Decide whether the estimated model memory fits
    within available memory.
    """

    if total_gb <= available_gb * 0.70:
        return "fits comfortably"

    if total_gb <= available_gb:
        return "fits, but tight"

    return "does NOT fit"


def report(name, params_b, precision, context_k, available_gb):
    """
    Print one model's memory estimation.
    """

    weights, kv, total = estimate(
        params_b,
        precision,
        context_k
    )

    result = verdict(total, available_gb)

    print(
        f"{name:<24}"
        f"{params_b:>6.1f}B  "
        f"{precision:<8}"
        f"ctx {context_k:>4}K  "
        f"weights {weights:>6.2f} GB  "
        f"KV {kv:>6.2f} GB  "
        f"total {total:>6.2f} GB  "
        f"-> {result}"
    )


# ---------------------------------------------------------
# MAIN PROGRAM
# ---------------------------------------------------------

if __name__ == "__main__":

    # Change this according to your machine
    AVAILABLE_GB = 8.0

    print("=" * 100)
    print("DAY 4 - MODEL MEMORY ESTIMATION")
    print("=" * 100)

    print(f"\nAvailable memory: {AVAILABLE_GB} GB\n")

    # -----------------------------------------------------
    # 1. Four relevant model configurations
    # -----------------------------------------------------

    print("MODEL MEMORY ESTIMATES")
    print("-" * 100)

    report(
        "Small model",
        1.5,
        "Q4_K_M",
        8,
        AVAILABLE_GB
    )

    report(
        "Mid model Q4",
        8.0,
        "Q4_K_M",
        8,
        AVAILABLE_GB
    )

    report(
        "Mid model FP16",
        8.0,
        "FP16",
        8,
        AVAILABLE_GB
    )

    report(
        "Large model",
        30.0,
        "Q4_K_M",
        8,
        AVAILABLE_GB
    )

    # -----------------------------------------------------
    # 2. Context length experiment
    # -----------------------------------------------------

    print("\n")
    print("CONTEXT LENGTH EXPERIMENT")
    print("-" * 100)

    print("Same model: 8B")
    print("Same quantization: Q4_K_M\n")

    for context_k in (4, 8, 16, 32, 64, 128):

        report(
            "8B model",
            8.0,
            "Q4_K_M",
            context_k,
            AVAILABLE_GB
        )

    # -----------------------------------------------------
    # 3. Quantization experiment
    # -----------------------------------------------------

    print("\n")
    print("QUANTIZATION EXPERIMENT")
    print("-" * 100)

    print("Same model: 8B")
    print("Same context: 8K\n")

    for precision in (
        "Q3_K_M",
        "Q4_K_M",
        "Q5_K_M",
        "Q6_K",
        "Q8_0",
        "FP16"
    ):

        report(
            "8B model",
            8.0,
            precision,
            8,
            AVAILABLE_GB
        )

    print("\n")
    print("=" * 100)
    print("ESTIMATION COMPLETE")
    print("=" * 100)