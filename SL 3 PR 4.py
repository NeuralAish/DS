import pandas as pd
from sklearn.linear_model import LinearRegression

# Load dataset
df = pd.read_csv("housing.csv")

# Select required columns and drop missing values
df = df[['RM', 'MEDV']].dropna()

X = df[['RM']]
y = df['MEDV']

# Train model
model = LinearRegression()
model.fit(X, y)

# Predict for all rows
Predict = model.predict(X)

print(Predict)

# Predict value
prediction = model.predict([[6]])

print("Predicted Price:", prediction[0])