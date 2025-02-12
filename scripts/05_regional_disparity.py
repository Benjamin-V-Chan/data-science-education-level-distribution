import pandas as pd

# Load cleaned dataset
df = pd.read_csv("outputs/cleaned_data.csv")

# Separate rural and urban data
rural_data = df[df["Type of area"] == "Rural"]
urban_data = df[df["Type of area"] == "Urban"]

# Compute mean percentage for each education level by area type
rural_stats = rural_data.groupby("Highest level of education completed")["Percentage distribution of persons"].mean()
urban_stats = urban_data.groupby("Highest level of education completed")["Percentage distribution of persons"].mean()

# Combine into a single DataFrame
regional_disparity = pd.DataFrame({"Rural": rural_stats, "Urban": urban_stats})
regional_disparity["Difference"] = regional_disparity["Urban"] - regional_disparity["Rural"]

# Save disparity analysis
regional_disparity.to_csv("outputs/regional_disparity.csv")
