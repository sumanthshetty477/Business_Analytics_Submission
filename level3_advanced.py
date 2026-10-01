"""Level 3 - Advanced: Task 5 (Reasons for Investment) and Task 6 (Savings Objectives)"""
import pandas as pd, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

df = pd.read_csv("dataset.csv")

# ---------- Task 5: Reasons for Investment ----------
reason_cols = {"Equity": "Reason_Equity", "Mutual Funds": "Reason_Mutual",
               "Bonds": "Reason_Bonds", "Fixed Deposits": "Reason_FD"}
print("TASK 5: REASONS FOR INVESTMENT")
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
rows = []
for ax, (name, col) in zip(axes.ravel(), reason_cols.items()):
    vc = df[col].value_counts()
    top = vc.iloc[0]
    print(f"\n{name}:\n", pd.DataFrame({"count": vc, "percent": (vc/len(df)*100).round(1)}))
    for r, c in vc.items():
        rows.append({"Investment": name, "Reason": r, "Count": c, "Percent": round(c/len(df)*100, 1)})
    bars = ax.bar(vc.index, vc.values, color="#4C72B0"); ax.bar_label(bars)
    ax.set_title(f"Why invest in {name}?"); ax.tick_params(axis="x", rotation=15)
plt.tight_layout(); plt.savefig("outputs/task5_reasons_for_investment.png", dpi=150)
pd.DataFrame(rows).to_csv("outputs/task5_reasons_summary.csv", index=False)

# ---------- Task 6: Savings Objectives ----------
col = "What are your savings objectives?"
vc = df[col].value_counts()
res = pd.DataFrame({"count": vc, "percent": (vc/len(df)*100).round(1)})
print("\nTASK 6: SAVINGS OBJECTIVES\n", res)
res.to_csv("outputs/task6_savings_objectives.csv")

fig, ax = plt.subplots(figsize=(7, 5))
ax.pie(vc.values, labels=vc.index, autopct="%1.1f%%", startangle=90,
       colors=["#4C72B0", "#DD8452", "#55A868"])
ax.set_title("Main Savings Objectives")
plt.tight_layout(); plt.savefig("outputs/task6_savings_objectives.png", dpi=150)
