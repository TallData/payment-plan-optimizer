from flask import Blueprint, render_template, request
import joblib

# Load the trained model (adjust the path as necessary based on your project structure)
model = joblib.load('path/to/models/model_file.pkl')  # Adjust the path as necessary

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/optimize-plan', methods=['POST'])
def optimize_plan():
    data = request.form
    initial_debt = float(data.get('initial_debt', 0))
    interest_rate = float(data.get('interest_rate', 0))
    monthly_income = float(data.get('monthly_income', 0))
    monthly_expenses = float(data.get('monthly_expenses', 0))
    additional_payment = float(data.get('additional_payment', 0))
    minimum_payment_percentage = float(data.get('minimum_payment_percentage', 0))
    
    # Prepare the data for the model (ensure this matches the model's expected input format)
    input_data = [[initial_debt, interest_rate]]  # Adjust this based on your actual model inputs
    
    # Use the model to make a prediction
    prediction = model.predict(input_data)
    
    # Here, you can convert the prediction to a more readable form if necessary
    
    return render_template('result.html', optimization_result=prediction[0])