# 🏥 Life Expectancy Predictor

A machine learning-powered web application that predicts life expectancy categories (Low/Medium/High) based on key health and economic indicators.
📋 Table of Contents
- [Features](#-features)
- [Technologies](#-technologies)
- [Installation](#-installation)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Model Details](#-model-details)
- [Deployment](#-deployment)

  ## ✨ Features
- 🧠 ML-powered predictions using Decision Tree algorithm
- 🌍 Web-based interface for easy access
- 📱 Responsive design for all devices
- ✅ Input validation and error handling
- 🚀 One-click deployment ready

## 🛠️ Technologies
- **Backend**: Python, Flask
- **Machine Learning**: scikit-learn, pandas, NumPy
- **Frontend**: HTML5, CSS3
- **Deployment**: Render, Gunicorn
- **Model Persistence**: Pickle

## 🚀 Installation
### Prerequisites
- Python 3.8+
- pip package manager
  ## 💻 Usage
1. Start the Flask server:
2. Open `http://localhost:5000` in your browser
3. Enter values for:
   - Adult Mortality (per 1000)
   - Infant Deaths (per 1000)
   - GDP per capita
   - Average BMI
4. Get instant life expectancy prediction

**Sample Input:**
Adult Mortality: 250
Infant Deaths: 60
GDP: 5000
BMI: 20

## 📁 Project Structure
.
├── app.py # Flask application
├── model.pkl # Trained ML model
├── requirements.txt # Dependencies
├── Procfile # Deployment config
├── README.md # Documentation
│
├── templates/ # HTML templates
│ └── index.html
│
└── static/ # Static assets
└── style.css
## 🧠 Model Details
- **Algorithm**: Decision Tree Classifier
- **Features**:
  - Adult Mortality
  - Infant Deaths
  - GDP
  - BMI
- **Classes**: Low/Medium/High (quantile-based)
- **Accuracy**: ~85% (training data)

## 🌐 Deployment
Deployed on Render:  
[![Render](https://img.shields.io/badge/Render-Deployed-success)](https://your-render-app-url.onrender.com)

**Deployment Steps:**
1. Fork this repository
2. Create a Render account
3. Connect your GitHub repository
4. Set build command: `pip install -r requirements.txt`
5. Set start command: `gunicorn app:app`
