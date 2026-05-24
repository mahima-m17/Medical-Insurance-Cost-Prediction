import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

df = pd.read_csv("insurance.csv")
df = pd.get_dummies(df, drop_first=True)

X = df.drop('charges', axis=1)
y = df['charges']

model = LinearRegression()
model.fit(X, y)

joblib.dump(model, 'insurance_model.pkl')
