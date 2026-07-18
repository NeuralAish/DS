from sklearn.datasets import load_iris
from sklearn.naive_bayes import GaussianNB

# Load dataset
data = load_iris()

X = data.data
y = data.target

#
model = GaussianNB()
model.fit(X, y)

# Predict for all rows
predict = model.predict(X)

print(predict)

# Prediction
prediction = model.predict([X[0]])

print("Predicted Class:", prediction[0])
