"""
File: quadratic_solver.py
Name: Johnson
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
    print('stanCode Quadratic Solver!')
    a = int(input('Enter a: '))  	# The 'a' in the discriminant
    b = int(input('Enter b: '))  	# The 'b' in the discriminant
    c = int(input('Enter c: '))  	# The 'c' in the discriminant
    if (b * b) - (4 * a * c) < 0:	# 'No real roots' case
        print('No real roots!')
    elif (b * b) - (4 * a * c) > 0:	# '2 real roots' case
        print('Two roots: ' + str((- b + math.sqrt((b * b) - (4 * a * c))) / (2 * a)) + ', ' + str(
            (- b - math.sqrt((b * b) - (4 * a * c))) / 2 * a))
    else:							# 'double roots' case
        print('One roots: ' + str((- b + math.sqrt((b * b) - (4 * a * c))) / (2 * a)))


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
    main()
