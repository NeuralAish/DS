import pandas as pd

# Load dataset
df = pd.read_csv("Employee_Salary_Dataset.csv")

# Convert column to numeric (safe)
df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce')

# Remove missing values
df = df.dropna(subset=['Salary'])

# Calculate quartiles
Q1 = df['Salary'].quantile(0.25)
Q3 = df['Salary'].quantile(0.75)

IQR = Q3 - Q1

# Remove outliers
df_clean = df[
    (df['Salary'] >= Q1 - 1.5 * IQR) &
    (df['Salary'] <= Q3 + 1.5 * IQR)
]

# Display cleaned data
print("Cleaned Data:")
print(df_clean.head())