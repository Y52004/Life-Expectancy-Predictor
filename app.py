from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

# Create Flask app
app = Flask(__name__)

# Load your trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Home page route
@app.route('/')
def home():
    return render_template('index.html')

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from the form
        adult_mortality = float(request.form['adult_mortality'])
        infant_deaths = float(request.form['infant_deaths'])
        gdp = float(request.form['gdp'])
        bmi = float(request.form['bmi'])
        
        # Make prediction
        features = np.array([[adult_mortality, infant_deaths, gdp, bmi]])
        prediction = model.predict(features)[0]
        
        # Get confidence score
        confidence = max(model.predict_proba(features)[0]) * 100
        
        return render_template('index.html', 
                             prediction=prediction,
                             confidence=round(confidence, 1))
    
    except Exception as e:
        return render_template('index.html', 
                             error="Please enter valid numbers for all fields")

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
