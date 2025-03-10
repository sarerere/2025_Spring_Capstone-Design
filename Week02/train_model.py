from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib

# Load Iris dataset
iris = load_iris()
X = iris.data[:, :2]  # Use only sepal length and sepal width
y = (iris.target != 0) * 1  # Binary classification: Iris Setosa vs. others

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LogisticRegression()
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, "iris_model.pkl")
