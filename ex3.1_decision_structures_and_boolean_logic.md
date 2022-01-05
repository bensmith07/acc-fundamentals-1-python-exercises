# Lab Exercise 3
## Focus
1. Boolean expressions and operators 2. SimpleandNestedif-elsestructures

This lab maps to learning objectives 1, 2, and 3 for Competency Three - Write a Working Program that Uses Decision Structures and Boolean Logic Including the If, If-Else, If-Elif-Else Control Structure

# Part A: Building upon an Existing Solution

For this portion of the lab you will design the solution so that you perform some conditional tests. For this lab: you will reuse the program you wrote in Lab 2A. That means you will open the lab you wrote in the previous assignment and change it. You should NOT start from scratch. Also, all the requirements/prohibitions from the previous lab MUST also be included /omitted from this lab.

1. You will validate input to ensure that the user enters inputs within a certain range or larger than a certain minimum value. You will validate the inputs as follows: (LO 1, 2, 3)
    a. The user cannot enter a negative number for:
        i. Miles to kilometers
        ii. Gallons to liters
        iii. Pounds to kilograms
        iv. Inches to centimeters
    b. The user cannot enter a value above 1000 degrees for Fahrenheit to Celsius
    c. You MUST design a logical program exit. You may NOT use exit, break, quit, continue or system exit, or ANY OTHER forced exit. You may not use loops or functions or lists, or anything that has not yet been covered in this course. Do not use a menu. Use LOGIC to exit the program.
  
2. If the user enters an invalid value, then the program will issue an error message and terminate immediately. (Do NOT accept further data).
3. Save the program as firstname_lastname_Lab3a.py where you will replace firstname and lastname with your actual first and last name.
4. Test all conditions prior to submitting.

# Part B: Write Something New!

Write a complete and syntactically correct Python program to solve the following problem: You are the payroll manager for SoftwarePirates Inc. You have been charged with writing a package that calculates the monthly paycheck for the salespeople. Salespeople at SoftwarePirates get paid a base salary of $2000 per month. Beyond the base salary, each salesperson earns commission on the following scale:

[sales/commission scale table]

 The following additional conditions apply:
1. If a salesperson has taken more than 3 vacation days in a month, their pay gets reduced by $200
2. A salesperson earns a bonus only if they have been with the company for 3 months or more
3. For salespeople who have been with the company for 5 years or more and who have made sales greater than $100,000 an additional bonus of $1000 is added.
All input to the program will be interactive from the keyboard. The output of the program will include:

a. The name of the salesperson
b. Their longevity with the company
c. Their base salary
d. The commission earned(inDollars)
e. The bonus earned
f. Additional bonus earned (if any)
g. Deductions (if any)
h. A total gross paycheck
i. Your output should look like a paystub (NOT in paragraph format)
j. All currency should be formatted with a $ sign and 2 decimal places