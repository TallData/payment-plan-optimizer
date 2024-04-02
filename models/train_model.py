import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
import joblib

# Load the dataset
df = pd.read_csv('data/raw/synthetic_debt_data.csv')

# Encode categorical variables
label_encoder = LabelEncoder()
df['Repayment_Strategy'] = label_encoder.fit_transform(df['Repayment_Strategy'])

# Splitting the features and target variable
X = df.drop('Repayment_Strategy', axis=1)
y = df['Repayment_Strategy']

# Split the data into training, validation, and test sets
X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.3, random_state=42)
X_validate, X_test, y_validate, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

# Initialize and train the decision tree model
dtree = DecisionTreeClassifier(random_state=42)
dtree.fit(X_train, y_train)

# Predict on the validation set
y_pred_validate = dtree.predict(X_validate)

# Calculate accuracy
validate_accuracy = accuracy_score(y_validate, y_pred_validate)
print(f"Validation Accuracy: {validate_accuracy:.2f}")

# Save the trained model
joblib.dump(dtree, 'models/model_file.pkl')
