"""Level 2 - Intermediate: Task 3 (Descriptive Statistics) and Task 4 (Most Preferred Investment Avenue)"""
import pandas as pd, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

df = pd.read_csv("dataset.csv")

# ---------- Task 3: Descriptive Statistics ----------
num_cols = df.select_dtypes("number").columns.tolist()
stats = df[num_cols].agg(["mean", "median", "std"]).T.round(2)
stats.columns = ["Mean", "Median", "Std Dev"]
print("TASK 3: DESCRIPTIVE STATISTICS\nNumerical columns:", num_cols, "\n")
print(stats)
stats.to_csv("outputs/task3_descriptive_statistics.csv")
print("\nFull describe():\n", df[num_cols].describe().round(2))

# ---------- Task 4: Most Preferred Investment Avenue ----------
freq = df["Avenue"].value_counts()
pct = (freq / freq.sum() * 100).round(1)
result = pd.DataFrame({"count": freq, "percent": pct})
print("\nTASK 4: MOST PREFERRED INVESTMENT AVENUE\n", result)
print(f"\nMost preferred: {freq.idxmax()} ({freq.max()} of {len(df)} respondents, {pct.max()}%)")
result.to_csv("outputs/task4_preferred_avenue.csv")

# Bonus: mean rank per avenue (rank 1 = most preferred)
rank_cols = ["Mutual_Funds","Equity_Market","Debentures","Government_Bonds","Fixed_Deposits","PPF","Gold"]
mean_rank = df[rank_cols].mean().sort_values().round(2)
print("\nAverage preference rank (1 = most preferred):\n", mean_rank)

fig, ax = plt.subplots(1, 2, figsize=(12, 4.5))
bars = ax[0].bar(freq.index, freq.values, color="#4C72B0"); ax[0].bar_label(bars)
ax[0].set_title("Most Preferred Investment Avenue"); ax[0].tick_params(axis="x", rotation=20)
ax[0].set_ylabel("Respondents")
bars = ax[1].barh(mean_rank.index[::-1], mean_rank.values[::-1], color="#55A868"); ax[1].bar_label(bars)
ax[1].set_title("Average Rank by Avenue (lower = preferred)")
plt.tight_layout(); plt.savefig("outputs/task4_investment_avenue.png", dpi=150)
