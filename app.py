from flask import Flask, request, render_template
import joblib
import pandas as pd

app = Flask(__name__)
model = joblib.load('insurance_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    input_data = {
        'age': int(request.form['age']),
        'bmi': float(request.form['bmi']),
        'children': int(request.form['children']),
        'sex_male': 1 if request.form['sex'] == 'male' else 0,
        'smoker_yes': 1 if request.form['smoker'] == 'yes' else 0,
        'region_northwest': 0,
        'region_southeast': 0,
        'region_southwest': 0
    }

    region = request.form['region']
    if f"region_{region}" in input_data:
        input_data[f"region_{region}"] = 1

    df = pd.DataFrame([input_data])
    prediction = model.predict(df)[0]
    return render_template('index.html', prediction=f"Estimated cost: ${prediction:.2f}")

if __name__ == '__main__':
    app.run(debug=True)
