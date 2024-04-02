from flask import Blueprint, render_template, request

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/optimize-plan', methods=['POST'])
def optimize_plan():
    data = request.form
    initial_debt = data.get('initial_debt')
    interest_rate = data.get('interest_rate')
    # Process the rest of the fields similarly
    
    # Here, you'd include the logic for optimizing the payment plan based on the inputs

    return render_template('result.html', optimization_result="Your optimized plan details here.")
