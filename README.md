# loan-coverage-eligibility-test-script
# Problem

To test a large number of loans, the current approach requires manually sending each loan value one by one using Postman. This process is time-consuming and prone to human error.

## Solution

This repository provides a Python script that automates the testing of loan values. It sends the loan values to the relevant API, validates the response, and compares it against the actual inventory data.


## Usage

- Step 1: Clone the Repository

- Step 2: 
Modify the Input CSV: 
Open the input.csv file and add the loan values in the first column. Each row should represent a separate loan.


- Step 3: Modify the inv Variable (Optional)
If needed, modify the inv variable in the script to match the specifics of your inventory data.

- Step 4: Run the Script
Execute the Python script eligibility.py to start the loan validation process

- Step 5: Review the Output
The script will generate an Excel sheet with the results of the loan validation. This sheet will contain the loan value, the response status, and more relevant details for each loan.
