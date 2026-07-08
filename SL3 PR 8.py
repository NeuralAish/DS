import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = sns.load_dataset('titanic')

# Plot histogram
plt.hist(df['fare'].dropna())
plt.xlabel("Fare")
plt.ylabel("Frequency")
plt.title("Fare Distribution")
plt.show()
