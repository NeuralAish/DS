import pandas as pd

# Load dataset
df = pd.read_csv("iris.csv")

# Summary statistics
print("Summary Statistics:")
print(df.describe())

# Group by species (if exists)
if 'Species' in df.columns:
    grouped = df.groupby('Species').mean()
    print("\nGrouped Data:")
    print(grouped)