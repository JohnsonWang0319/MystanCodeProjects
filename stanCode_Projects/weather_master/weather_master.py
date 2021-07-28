"""
File: weather_master.py
Name: Johnson
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

EXIT = -1


def main():
    print('stanCode \"Weather Master 4.0"!')
    next_temp = int(input('Next Temperature: (or ' + str(EXIT) + ' to quit)? '))
    if next_temp == EXIT:           # if user input EXIT number, we will print 'No temperatures were entered'
        print('No temperatures were entered.')
    else:
        maximum = next_temp
        minimum = next_temp
        if next_temp < 16:          # if the first weather is a cold day, we will set the 'cold_days' to 1
            cold_days = 1
        else:
            cold_days = 0
        count_days = 1
        total_temp = next_temp

        while True:
            next_temp = int(input('Next Temperature: (or ' + str(EXIT) + ' to quit)? '))
            if next_temp == EXIT:
                break
            if next_temp > maximum: # compare which is bigger, the previous 'next_temp' or the one that we type
                maximum = next_temp
            if next_temp < minimum: # compare which is smaller, the previous 'next_temp' or the one that we type
                minimum = next_temp
            if next_temp < 16:      # if the next temperature is below 16, we will add one more day to 'cold_days'
                cold_days += 1
            if next_temp != EXIT:   # we count the times of 'next temperature', so that we can calculate the average
                count_days += 1
            if next_temp != EXIT:   # we add all the 'next temperature' together
                total_temp = total_temp + next_temp

        print('Highest temperature = ' + str(maximum))
        print('Lowest temperature = ' + str(minimum))
        print('Average = ' + str(total_temp / count_days))
        print(str(cold_days) + ' cold day(s)')


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
    main()
