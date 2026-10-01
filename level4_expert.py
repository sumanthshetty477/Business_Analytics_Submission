"""Level 4 - Expert: Task 7 (Information Sources), Task 8 (Investment Duration),
Task 9 (Expectations), Task 10 (Correlation Analysis)"""
import pandas as pd, numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("dataset.csv")

# ---------- Task 7: Common Information Sources ----------
vc = df["Source"].value_counts()
res = pd.DataFrame({"count": vc, "percent": (vc/len(df)*100).round(1)})
print("TASK 7: INFORMATION SOURCES\n", res)
res.to_csv("outputs/task7_information_sources.csv")
fig, ax = plt.subplots(figsize=(8, 4.5))
bars = ax.bar(vc.index, vc.values, color="#8172B2"); ax.bar_label(bars)
ax.set_title("Common Sources of Investment Information"); ax.tick_params(axis="x", rotation=15)
plt.tight_layout(); plt.savefig("outputs/task7_information_sources.png", dpi=150)

# ---------- Task 8: Investment Duration ----------
# Duration is categorical, so each band is converted to a midpoint (in years):
duration_map = {"Less than 1 year": 0.5, "1-3 years": 2.0, "3-5 years": 4.0, "More than 5 years": 6.0}
df["duration_years"] = df["Duration"].map(duration_map)
dcount = df["Duration"].value_counts().reindex(list(duration_map))
print("\nTASK 8: INVESTMENT DURATION\n", dcount)
print(f"Average duration (band midpoints): {df['duration_years'].mean():.2f} years")
print(f"Median duration: {df['duration_years'].median():.2f} years | Mode: {df['Duration'].mode()[0]}")
dcount.to_frame("count").to_csv("outputs/task8_investment_duration.csv")
fig, ax = plt.subplots(figsize=(8, 4.5))
bars = ax.bar(dcount.index, dcount.values, color="#C44E52"); ax.bar_label(bars)
ax.axhline(0, color="k", lw=.5)
ax.set_title(f"Investment Duration (avg ≈ {df['duration_years'].mean():.2f} yrs)")
plt.tight_layout(); plt.savefig("outputs/task8_investment_duration.png", dpi=150)

# ---------- Task 9: Expectations from Investments ----------
vc = df["Expect"].value_counts()
res = pd.DataFrame({"count": vc, "percent": (vc/len(df)*100).round(1)})
print("\nTASK 9: EXPECTED RETURNS\n", res)
res.to_csv("outputs/task9_expectations.csv")
fig, ax = plt.subplots(figsize=(6, 4.5))
bars = ax.bar(vc.index, vc.values, color="#CCB974"); ax.bar_label(bars)
ax.set_title("Expected Returns from Investments"); ax.set_ylabel("Respondents")
plt.tight_layout(); plt.savefig("outputs/task9_expectations.png", dpi=150)

# ---------- Task 10: Correlation Analysis ----------
# Expected returns band -> midpoint (%)
expect_map = {"10%-20%": 15, "20%-30%": 25, "30%-40%": 35}
df["expected_return_pct"] = df["Expect"].map(expect_map)
cols = ["age", "duration_years", "expected_return_pct"]
corr = df[cols].corr(method="pearson").round(3)
print("\nTASK 10: CORRELATION (Pearson)\n", corr)
print("\nSpearman:\n", df[cols].corr(method="spearman").round(3))
corr.to_csv("outputs/task10_correlation_matrix.csv")

fig, ax = plt.subplots(1, 3, figsize=(15, 4.5))
sns.heatmap(corr, annot=True, cmap="coolwarm", vmin=-1, vmax=1, ax=ax[0]); ax[0].set_title("Correlation Heatmap")
for a, (x, y) in zip(ax[1:], [("age", "duration_years"), ("age", "expected_return_pct")]):
    jit = lambda s: s + np.random.default_rng(0).normal(0, .04*s.std(), len(s))
    a.scatter(jit(df[x]), jit(df[y]), alpha=.7)
    m, b = np.polyfit(df[x], df[y], 1); xs = np.linspace(df[x].min(), df[x].max(), 10)
    a.plot(xs, m*xs+b, "r--"); a.set_xlabel(x); a.set_ylabel(y)
    a.set_title(f"{x} vs {y} (r={df[x].corr(df[y]):.2f})")
plt.tight_layout(); plt.savefig("outputs/task10_correlation.png", dpi=150)
