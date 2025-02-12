import pandas as pd

# Load cleaned dataset
df = pd.read_csv("outputs/cleaned_data.csv")

# Group by year and compute mean percentage for each education level
trends = df.groupby(["Year", "Highest level of education completed"])["Percentage distribution of persons"].mean().reset_index()

# Save trends analysis
trends.to_csv("outputs/trends_analysis.csv", index=False)
