# Module2Challenge
# Loan Qualifier Application

This project was developed by request of the lending software company, BizOps. In order to simplify their system for their customer base, this code offers their consumers the ability to see which loan companies they qualify for after answering a few questions surrounding their personal financial situation. The consumer then has the option to save their results into a .csv file.

---

## Technologies

The technologies used to run this project included Visual Studio Code (version 1.64.2) and the programming language Python (version 3.7). Built in modules/functions used included csv, sys, fire, questionary, and Path from pathlib. This project was built on a Macbook Pro version 12.2.1.


## Installation Guide

In this section, you should include detailed installation notes containing code blocks and screenshots.

First, the user will want to make sure that the appropriate libraries are installed, including sys, fire,questionary, and pathlib.

https://github.com/arfylarfy/Module2Challenge_/blob/master/data/Screen%20Shots/Import%20modules_libraries%20screenshot.png

---

## Usage

This projects utilizes multiple modules then links and combines tham to form a complete system to enable re-usability and minimize duplication.

To use the loan qualifier application simply clone the repository and run the app.py with: python app.

In your terminal, it will ask you to provide a path to the "daily_rate_sheet" where the loan information is stored.

##include screen shot

The user will then be prompted to answer several questions including inquiries about their credit score, current amount of monthly debt, total monthly income, desired loan amount, as well as the home's value.

##insert screen shot

The application will then tell you how many loans you qualify for. If none, you will be informed and exit the system. 

##insert screen shot

If you have qualifying loans, it will inform you of how many you qualify for and then prompt the user with a yes or no question asking if they would like to save the list of qualifying loans to a .csv file.
If the user chooses no, the system responds with "Thank you. Have a nice day." If the user chooses yes, the system responds with "The qualifying loans have been saved into a .csv file. Have a nice day." The user will then be able to access their saved .csv file with their qualifying loans.

##insert 2 screen shots (one with no and one with yes)

## Contributors

In this section, list all the people who contribute to this project. You might want recruiters or potential collaborators to reach you, so include your contact email and, optionally, your LinkedIn or Twitter profile.

---

## License

When you share a project on a repository, especially a public one, it's important to choose the right license to specify what others can and can't with your source code and files. Use this section to include the license you want to use.
