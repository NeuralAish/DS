import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = sns.load_dataset('titanic')

# Create boxplot
sns.boxplot(x='sex', y='age', data=df)

# Title
plt.title("Age Distribution by Gender")

# Display plot
plt.show()