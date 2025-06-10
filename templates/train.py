import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import pickle
from google.colab import files
df = pd.read_csv('life_expectancy_classified.csv')

# Create classes if not already done
df['LifeExp_Class'] = pd.qcut(df['Life expectancy'], q=3, labels=['Low', 'Medium', 'High'])

# Prepare features and target using iloc
X = df.iloc[:, :4]  # Selects first 4 columns (Adult Mortality, infant deaths, GDP, BMI)
y = df.iloc[:, -1]  # Selects last column (LifeExp_Class)

# Split and train
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# Save the model as .pkl file
with open('life_expectancy_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model saved successfully as life_expectancy_model.pkl!")
# Download the .pkl file to your computer
from google.colab import files
files.download('life_expectancy_model.pkl')
