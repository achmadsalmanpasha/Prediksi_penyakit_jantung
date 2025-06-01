import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

df = pd.read_csv("heart.csv")
X = df[['age', 'chol', 'trestbps', 'thalach']]
y = df['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

def predict_heart_disease(age, chol, bp, hr):
    return model.predict([[age, chol, bp, hr]])[0]
