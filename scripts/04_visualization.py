import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("outputs/cleaned_data.csv")

# Bar chart of education level distribution
education_distribution = df.groupby("Highest level of education completed")["Percentage distribution of persons"].mean()
education_distribution.plot(kind="bar", figsize=(10, 5), title="Average Education Distribution")
plt.xlabel("Education Level")
plt.ylabel("Percentage")
plt.xticks(rotation=45)
plt.savefig("outputs/education_distribution.png")

# Line plot of education trends over time
df_pivot = df.pivot_table(index="Year", columns="Highest level of education completed", values="Percentage distribution of persons", aggfunc="mean")
df_pivot.plot(figsize=(12, 6), title="Education Trends Over Time")
plt.xlabel("Year")
plt.ylabel("Percentage")
plt.legend(title="Education Level", bbox_to_anchor=(1.05, 1), loc="upper left")
plt.savefig("outputs/education_trends.png")