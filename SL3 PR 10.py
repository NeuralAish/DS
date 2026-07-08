import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Iris.csv")

df.head(3)

# Histograms
plt.figure(figsize=(10,5))

plt.subplot(2,2,1)
plt.hist(df['SepalLengthCm'])

plt.subplot(2,2,2)
plt.hist(df['SepalWidthCm'])

plt.subplot(2,2,3)
plt.hist(df['PetalLengthCm'])

plt.subplot(2,2,4)
plt.hist(df['PetalWidthCm'])

plt.show()

# Boxplot
df.plot(kind='box', figsize=(10,5))

plt.show()