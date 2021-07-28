"""
File: hailstone.py
Name: Johnson
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    print('This program computes Hailstone sequences.\n')
    number = int(input('Enter a number: '))
    count_times = 0                     # set 'count_times' as zero, and we will add 1 in each WHILE LOOP
    while True:
        if number == 1:                 # if user type 1 or the number becomes to 1, the loop will break
            break
        if number % 2 == 1:             # if the number is odd, we will make 3n+1
            print(str(number), end='')  # to show the previous number first, we need to print 'number' before calculate
            count_times += 1            # add 1 to 'count_times'
            number = int(3 * number + 1)# use 'int' to exclude the case '.0'
            print(' is odd, so I make 3n+1: ' + str(number))
        if number % 2 == 0:             # if the number is even, we will take half
            print(str(number), end='')  # to show the previous number first, we need to print 'number' before calculate
            count_times += 1            # add 1 to 'count_times'
            number = int(number / 2)    # use 'int' to exclude the case '.0'
            print(' is even, so I take half: ' + str(number))
    print('It took ' + str(count_times) + ' steps to reach 1.')


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
    main()
