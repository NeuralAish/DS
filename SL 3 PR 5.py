import pandas as pd
from sklearn.linear_model import LogisticRegression

# Load dataset
df = pd.read_csv("ads.csv")

df.head(4)

# Select columns and clean data
df = df[['Age', 'Purchased']].dropna()

X = df[['Age']]
y = df['Purchased']

# Train model
model = LogisticRegression()
model.fit(X, y)

# Predict for all rows
predict = model.predict(X)

print(predict)

# Prediction
prediction = model.predict([[30]])

print("Prediction for Age 30:", prediction[0])