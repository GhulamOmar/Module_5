"""
Program: average_input_scores.py
Author: Ghulam Omar
Last date modified: 09/22/2019
This program is  allows the users to put their first name, last name, age, and scores buy entering a negative
number the program stops, outputs and calculates the input numbers.
"""


# function definitions
def average(list):
    avg_scores = [] # list declaration.
    total = 0 # variables.
    score = 0
    print("Please enter a score, a negative number or (-1) to stop") # print message.
    first_name = input("Enter your first name: ") # asking for user inputs.
    last_name = input("Enter your last name :  ")
    age = input("Enter your age : ")
    while score != -1:  # -1 as a sentinel for the loop condition.
        try:  # try and Exception for string input.
            score = float(input(" please enter the score : "))  # asking for number of scores.
        except ValueError:
            print("Enter a number! ")  # error message for string input.

        if score < 0:
            break # executes the next line.
        avg_scores.append(score)
    total = sum(avg_scores)
    average = float(total) / len(avg_scores)  # calculation.
    print(last_name, ",", first_name, "age", age, "grade:", average)  # expected output.

    return average


if __name__ == '__main__':
    average(list)  # calling the function.
