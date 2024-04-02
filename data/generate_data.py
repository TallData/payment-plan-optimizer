import pandas as pd
import numpy as np

# Set seed for reproducibility
np.random.seed(42)

# Generate synthetic data
num_records = 2000  # Number of records you want to generate
user_ids = range(1, num_records + 1)
initial_debt = np.random.uniform(3000, 100000, num_records).round(2)  # Debt between $3,000 and $100,000
monthly_income = np.random.uniform(2000, 15000, num_records).round(2)  # Monthly income between $2,000 and $7,000
monthly_expenses = monthly_income * np.random.uniform(0.3, 0.9, num_records).round(2)  # Expenses between 50% and 90% of income
additional_payment = np.random.uniform(0, 800, num_records).round(2)  # Additional payment between $0 and $500
repayment_strategies = np.random.choice(['Avalanche', 'Snowball', 'Highest Interest'], num_records)

# Increase the range and variability of interest_rate
interest_rate = np.random.uniform(3, 30, num_records).round(2)  # Wider range from 3% to 30%

# Introduce more variability into minimum_payment_percentage
# Using a distribution that might reflect real-life scenarios more closely
minimum_payment_percentage = np.random.normal(2.5, 0.5, num_records).clip(1.5, 3.5)


# Create DataFrame
df = pd.DataFrame({
    'User_ID': user_ids,
    'Initial_Debt': initial_debt,
    'Interest_Rate': interest_rate,
    'Minimum_Payment_Percentage': minimum_payment_percentage,
    'Monthly_Income': monthly_income,
    'Monthly_Expenses': monthly_expenses,
    'Additional_Payment': additional_payment,
    'Repayment_Strategy': repayment_strategies
})

# Save the DataFrame to a CSV file in the raw folder
output_path = 'raw/synthetic_debt_data.csv'
df.to_csv(output_path, index=False)

print(f"Data saved to {output_path}")
