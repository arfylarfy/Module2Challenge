# Module2Challenge
# Loan Qualifier Application

This project was developed by request of the lending software company, BizOps. In order to simplify their system for their customer base, this code offers their consumers the ability to see which loan companies they qualify for after answering a few questions surrounding their personal financial situation. The consumer then has the option to save their results into a .csv file.

---

## Technologies

The technologies used to run this project included Visual Studio Code (version 1.64.2) and the programming language Python (version 3.7). Built in modules/functions used included csv, sys, fire, questionary, and Path from pathlib. This project was built on a Macbook Pro version 12.2.1.


## Installation Guide

First, the user will want to make sure that the appropriate libraries are installed, including sys, fire,questionary, and pathlib.

![Import libraries](https://github.com/arfylarfy/Module2Challenge_/blob/master/data/Screen%20Shots/Import%20modules_libraries%20screenshot.png)

---

## Usage

This projects utilizes multiple modules then links and combines them to form a complete system to enable re-usability and minimize duplication.

To use the loan qualifier application simply clone the repository and run the app.py with: python app.

In your terminal, it will ask you to provide a path to the "daily_rate_sheet" where the loan information is stored.

![Daily rate sheet pathway](https://github.com/arfylarfy/Module2Challenge_/blob/master/data/Screen%20Shots/csv%20pathway.png)

The user will then be prompted to answer several questions including inquiries about their credit score, current amount of monthly debt, total monthly income, desired loan amount, as well as the home's value.

![Questions](https://github.com/arfylarfy/Module2Challenge_/blob/master/data/Screen%20Shots/Questions%20screen%20shot.png)

The application will then tell you how many loans you qualify for. If none, you will be informed and exit the system. 

![0 qualifying loans](https://github.com/arfylarfy/Module2Challenge_/blob/master/data/Screen%20Shots/0%20qualifying%20loans.png)

If you have qualifying loans, it will inform you of how many you qualify for and then prompt the user with a yes or no question asking if they would like to save the list of qualifying loans to a .csv file.
If the user chooses no, the system responds with "Thank you. Have a nice day." If the user chooses yes, the system asks the user to choose a filepath. After filepath is chosen, the system responds with "The qualifying loans have been saved into a .csv file. Have a nice day." The user will then be able to access their saved .csv file with their qualifying loans.

![Do not save csv file](https://github.com/arfylarfy/Module2Challenge_/blob/master/data/Screen%20Shots/No%20to%20saving%20csv.png)
![Save csv file](https://github.com/arfylarfy/Module2Challenge/blob/master/data/Screen%20Shots/Save%20CSV%20file.png)

## Contributors

Aranda Furth, arandafurth@gmail.com

---

## License

Copyright 2022 Aranda Furth

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
