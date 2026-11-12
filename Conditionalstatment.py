#########################################################################
###A conditional statement is a set of rules performed if a certain condition is met. 
####In Python, conditional statements are used to perform different actions based on 
####different conditions. 
###The most common conditional statements are `if`, `elif`, and `else`.
###########################################################################

age = 18
if age >= 18:
    print("You are eligible to vote.")

mark = 25
if mark >= 35:
    print("You have passed the exam.")
else:
    print("You have failed the exam.")

marks = 85

if marks >= 90:
    print("You have scored an A grade.")
elif marks >=  75:
    print("You have scored a B grade.")
elif marks >= 60:
    print("You have scored a C grade.")
else:
    print("You have failed the exam")

#Nested if statements are used when you have multiple conditions to check.
age = 20
citizen = True
if age >= 18:
    if citizen:
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote because you are not a citizen.")
else:
    print("You are not eligible to vote because you are underage.")