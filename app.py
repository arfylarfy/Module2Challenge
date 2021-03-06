"""Loan Qualifier Application.
This is a command line application to match applicants with qualifying loans.
Example:
    $ python app.py
"""

# import built-in modules/functions

import csv
import sys
import fire
import questionary
from pathlib import Path

# import input/output functions from fileio
from qualifier.utils.fileio import load_csv, save_csv

# import debt to income and loan to value calculators from calculators
from qualifier.utils.calculators import (
    calculate_monthly_debt_ratio,
    calculate_loan_to_value_ratio,
)

# import filters for loan app

from qualifier.filters.max_loan_size import filter_max_loan_size
from qualifier.filters.credit_score import filter_credit_score
from qualifier.filters.debt_to_income import filter_debt_to_income
from qualifier.filters.loan_to_value import filter_loan_to_value

# function for input of banking data from csv file entered on command line
def load_bank_data(): 

    csvpath = questionary.text("Enter a file path to a rate-sheet (.csv):").ask()
    csvpath = Path(csvpath)
    if not csvpath.exists():
        sys.exit(f"Oops! Can't find this path: {csvpath}")

    return load_csv(csvpath)

# function for input of applicant data from command line
def get_applicant_info():
    credit_score = questionary.text("What's your credit score?").ask()
    debt = questionary.text("What's your current amount of monthly debt?").ask()
    income = questionary.text("What's your total monthly income?").ask()
    loan_amount = questionary.text("What's your desired loan amount?").ask()
    home_value = questionary.text("What's your home value?").ask()

    credit_score = int(credit_score)
    debt = float(debt)
    income = float(income)
    loan_amount = float(loan_amount)
    home_value = float(home_value)

    return credit_score, debt, income, loan_amount, home_value

# function for filtering bank list for qualifying loans
def find_qualifying_loans(bank_data, credit_score, debt, income, loan, home_value):
  

    # Calculate the monthly debt ratio
    monthly_debt_ratio = calculate_monthly_debt_ratio(debt, income)
    print(f"The monthly debt to income ratio is {monthly_debt_ratio:.02f}")

    # Calculate loan to value ratio
    loan_to_value_ratio = calculate_loan_to_value_ratio(loan, home_value)
    print(f"The loan to value ratio is {loan_to_value_ratio:.02f}.")

    # Run qualification filters
    bank_data_filtered = filter_max_loan_size(loan, bank_data)
    bank_data_filtered = filter_credit_score(credit_score, bank_data_filtered)
    bank_data_filtered = filter_debt_to_income(monthly_debt_ratio, bank_data_filtered)
    bank_data_filtered = filter_loan_to_value(loan_to_value_ratio, bank_data_filtered)

    
    print(f"Found {len(bank_data_filtered)} qualifying loans")

    return bank_data_filtered
    

#function to save list of qualifying loans using command line input
def save_qualifying_loans(qualifying_loans):
    
    if len(qualifying_loans) == 0:
        sys.exit(f"You do not qualify for any loans.")

    else:
        action = questionary.select("Would you like to save a new .csv file with your qualifying bank loans?", choices=["yes", "no"]).ask()
        if action == "no":
            sys.exit(f"Thank you, have a nice day!")
        else:
            if action == 'yes'
                csvpath = questionary.text("Please enter a filepath for the saved data: (qualifying_loans.csv)").ask()
                save_csv(Path(csvpath), qualifying_loans)
                print("The qualifying loans have been saved into a .csv file. Have a nice day.")


        
        




# Main fuction for running the script
def run():

    # Load the latest Bank data
    bank_data = load_bank_data()

    # Get the applicant's information
    credit_score, debt, income, loan_amount, home_value = get_applicant_info()

    # Find qualifying loans
    qualifying_loans = find_qualifying_loans(
        bank_data, credit_score, debt, income, loan_amount, home_value
    )

    # Save qualifying loans
    save_qualifying_loans(qualifying_loans)


if __name__ == "__main__":
    fire.Fire(run)
