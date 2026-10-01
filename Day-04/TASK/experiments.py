from vram_estimate import estimate, verdict


AVAILABLE_GB = 8.0

PARAMS = 8.0


def context_experiment():

    print("=" * 80)
    print("CONTEXT LENGTH EXPERIMENT")
    print("=" * 80)

    print(
        f"{'Context':<12}"
        f"{'Weights':<15}"
        f"{'KV Cache':<15}"
        f"{'Total':<15}"
        f"{'Fits?'}"
    )

    print("-" * 80)

    for context in (4, 8, 16, 32, 64, 128):

        weights, kv, total = estimate(
            PARAMS,
            "Q4_K_M",
            context
        )

        print(
            f"{context}K{'':<8}"
            f"{weights:<15.2f}"
            f"{kv:<15.2f}"
            f"{total:<15.2f}"
            f"{verdict(total, AVAILABLE_GB)}"
        )


def quantization_experiment():

    print("\n")
    print("=" * 80)
    print("QUANTIZATION EXPERIMENT")
    print("=" * 80)

    print(
        f"{'Precision':<15}"
        f"{'Weights':<15}"
        f"{'KV Cache':<15}"
        f"{'Total':<15}"
        f"{'Fits?'}"
    )

    print("-" * 80)

    precisions = [
        "Q3_K_M",
        "Q4_K_M",
        "Q5_K_M",
        "Q6_K",
        "Q8_0",
        "FP16"
    ]

    for precision in precisions:

        weights, kv, total = estimate(
            PARAMS,
            precision,
            8
        )

        print(
            f"{precision:<15}"
            f"{weights:<15.2f}"
            f"{kv:<15.2f}"
            f"{total:<15.2f}"
            f"{verdict(total, AVAILABLE_GB)}"
        )


if __name__ == "__main__":

    context_experiment()
    quantization_experiment()