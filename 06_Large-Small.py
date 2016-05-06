# THE TASK:
# 5.2 Write a program that repeatedly prompts a user for integer numbers until
# the user enters 'done'. Once 'done' is entered, print out the largest and
# smallest of the numbers. If the user enters anything other than a valid number
# catch it with a try/except and put out an appropriate message and ignore the
# number. Enter the numbers from the book for problem 5.1 and Match the desired
# output as shown.

# Intro
print "Enter a sequence of numbers by pressing 'Enter' after each number. Once you are done with inputting the numbers, type in 'Done'. After you have punched in 'Done', the program will show you the largest and the smallest number from the set you have entered. "
smallest = None
largest = None

# Start Loop
while True:
    num = raw_input("Enter a number: ")

# Handle the edge cases
    if num == 'Done' : break
    if len(num) < 1 : #Check for empty lines
        print "Please do not leave the line empty, enter a number."
        continue

# Convert input into numbers
    try:
        N = float(num)
    except:
        print "Please enter numeric values."
        continue

# Smallest evaluation
    if smallest is None :
        smallest = N
    elif N < smallest :
        smallest = N

# Largest evaluation
    if largest is None :
        largest = N
    elif N > largest :
        largest = N

# The Result
print "The smallest number is: " , smallest
print "The largest number is: " , largest
