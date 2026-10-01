"""Level 1 - Beginner: Task 1 (Data Overview) and Task 2 (Gender Distribution)"""
import io, pandas as pd, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

df = pd.read_csv("dataset.csv")

# ---------- Task 1: Data Overview ----------
buf = io.StringIO()
df.info(buf=buf)
info_text = buf.getvalue()
print("TASK 1: DATA OVERVIEW")
print("Rows, Columns:", df.shape)
print(info_text)
print("Missing values per column:\n", df.isna().sum())
print(df.head())
with open("outputs/task1_data_overview.txt", "w") as f:
    f.write(f"Rows: {df.shape[0]}  Columns: {df.shape[1]}\n\n{info_text}\n")
    f.write("Missing values:\n" + df.isna().sum().to_string() + "\n\nFirst 5 rows:\n" + df.head().to_string())

# ---------- Task 2: Gender Distribution ----------
counts = df["gender"].value_counts()
pct = (counts / counts.sum() * 100).round(1)
print("\nTASK 2: GENDER DISTRIBUTION\n", pd.DataFrame({"count": counts, "percent": pct}))

fig, ax = plt.subplots(1, 2, figsize=(10, 4.5))
colors = ["#4C72B0", "#DD8452"]
bars = ax[0].bar(counts.index, counts.values, color=colors)
ax[0].bar_label(bars)
ax[0].set_title("Gender Distribution (Bar)"); ax[0].set_ylabel("Number of respondents")
ax[1].pie(counts.values, labels=counts.index, autopct="%1.1f%%", colors=colors, startangle=90)
ax[1].set_title("Gender Distribution (Pie)")
plt.tight_layout(); plt.savefig("outputs/task2_gender_distribution.png", dpi=150)
