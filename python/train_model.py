import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib

data = pd.read_csv("obesity.csv")

X = data[["height", "weight", "age"]]

y = data["status"]

model = DecisionTreeClassifier()

model.fit(X, y)

joblib.dump(model, "model.pkl")

print("Model berhasil dibuat!")
