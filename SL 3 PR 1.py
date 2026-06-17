import seaborn as sns
import pandas as pd

# Load dataset
df = sns.load_dataset('Titanic')

# Show first 5 rows
print("First 5 Rows:")
print(df.head())

# Step 3: Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Step 4: Fill missing values (forward fill method)
df.fillna(method='ffill', inplace=True)

# Step 5: Convert 'Sex' column to category type
if 'Sex' in df.columns:
    df['Sex'] = df['Sex'].astype('category')

# Step 6: Display dataset information after cleaning
print("\nDataset Info After Cleaning:")
print(df.info())