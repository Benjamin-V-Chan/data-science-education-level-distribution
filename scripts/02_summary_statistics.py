import pandas as pd

# Load cleaned dataset
df = pd.read_csv("outputs/cleaned_data.csv")

# Compute summary statistics
summary_stats = df.groupby("Highest level of education completed")["Percentage distribution of persons"].describe()

# Save summary statistics
summary_stats.to_csv("outputs/summary_statistics.csv")
