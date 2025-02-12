import pandas as pd

# Load dataset
df = pd.read_csv("data/REPORT.csv")

# Drop irrelevant columns
columns_to_drop = ["ROWID"]
df = df.drop(columns=columns_to_drop)

# Handle missing values
df = df.fillna(0)

# Convert Year column to integer
df["YearCode"] = df["YearCode"].astype(int)

# Save cleaned dataset
df.to_csv("outputs/cleaned_data.csv", index=False)
