# Write a program to prompt for a score between 0.0 and 1.0.
# If the score is out of range, print an error.
# If the score is between 0.0 and 1.0, print a grade using the following table:
# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
# If the user enters a value out of range, print a suitable error message and exit.
# For the test, enter a score of 0.85.

try:
    score = raw_input("Enter Score: ")
    S = float(score)
except:
    print "Please enter a numeric value between 0.0 and 1.0."
    quit()

if S >= 0.0 and S <= 1.0:
    if S >= 0.9:
        print "Your grade is A."
    elif S >= 0.8 and S <= 0.9:
        print "Your grade is B"
    elif S >= 0.7 and S <= 0.8:
        print "Your grade is C"
    elif S >= 0.6 and S <= 0.7:
        print "Your grade is D"
    else :
        print "Your grade is F"
else :
    print "Please enter a value between 0.0 and 1.0."
    quit()
