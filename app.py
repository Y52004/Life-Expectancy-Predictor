from flask import Flask, render_template, request
import pickle
import os
import numpy as np

app = Flask(__name__)

# Robust model path
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'model.pkl')
with open(MODEL_PATH, 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        adult_mortality = float(request.form['adult_mortality'])
        infant_deaths = float(request.form['infant_deaths'])
        gdp = float(request.form['gdp'])
        bmi = float(request.form['bmi'])
        features = np.array([[adult_mortality, infant_deaths, gdp, bmi]])
        prediction = model.predict(features)[0]
        return render_template('index.html', prediction=prediction)
    except Exception as e:
        return render_template('index.html', error="Please enter valid numbers for all fields")

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
