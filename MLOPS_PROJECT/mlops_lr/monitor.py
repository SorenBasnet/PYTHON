import pandas as pd


df = pd.read_csv("predictions.csv")


print("\n==============================")
print("       MODEL MONITOR")
print("==============================")

print(f"\nTotal predictions: {len(df)}")

print(
    f"Average latency: "
    f"{df['latency_ms'].mean():.3f} ms"
)

print(
    f"P95 latency: "
    f"{df['latency_ms'].quantile(0.95):.3f} ms"
)

print(
    f"Prediction rate: "
    f"{df['prediction'].mean() * 100:.2f}%"
)

print(
    f"Average probability: "
    f"{df['probability'].mean():.3f}"
)

print("\nPrediction distribution:")

print(
    df["prediction"]
    .value_counts()
    .sort_index()
)
