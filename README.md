
## Demographic Data Analysis
Project Overview
This project analyzes demographic data from the "adult.csv" dataset using Python and the Pandas library.
The main goal is to extract meaningful statistics about different groups of people based on their race, education, work hours, income, and more.

The core functionality is implemented in the function calculate_demographic_data() inside the demographic_data_analyzer.py file.

## Features / What This Project Does
Counts the number of individuals in each race category.

Calculates the average age of men.

Finds the percentage of people with a Bachelor's degree.

Calculates the percentage of individuals with advanced education (Bachelors, Masters, Doctorate) earning more than $50K.

Calculates the percentage of individuals without advanced education earning more than $50K.

Determines the minimum number of hours worked per week.

Calculates the percentage of high earners (>50K) among those who work the minimum hours.

Identifies the country with the highest percentage of people earning more than $50K.

Finds the most common occupation for high earners in India.

## Files in the Project
demographic_data_analyzer.py - Contains the main function that performs the data analysis.

adult.csv - The dataset used for analysis (make sure this file is in the same directory).

test_module.py - Contains automated tests that verify the correctness of the analysis function.

README.md - This file



## How to Run the Project
Make sure you have Python installed.
# Install required packages (if needed):
pip install pandas

# Run the main file:
python main.py

# To run unit tests:
python test_module.py

## Notes
Results are rounded to the nearest tenth, as required.
You can test the output in main.py before running the tests.
The dataset must be named adult.csv and placed in the same folder.


