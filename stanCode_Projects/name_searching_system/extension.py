"""
File: extension.py
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10890537
Female Number: 7939153
---------------------------
2000s
Male Number: 12975692
Female Number: 9207577
---------------------------
1990s
Male Number: 14145431
Female Number: 10644002
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names' + year + '.html'
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, features="html.parser")
        targets = soup.find_all('tbody')
        total_male = 0
        total_female = 0

        for target in targets:
            all_td = target.text
            lists = all_td.split()             # ['serial', 'male_name', 'male_number', 'female_name', 'female_number']
            for i in range(22):                # pop out the redundancy in the end of the list
                lists.pop()

            for i in range(len(lists)):
                lst = lists[i]
                if i % 5 == 2:                          # determine whether the value is male_number
                    male_numbers = ''
                    for j in range(len(lst)):
                        male_number = lst[j]
                        if male_number.isdigit():       # remove the ',' between the digit
                            male_numbers += male_number
                    total_male += int(male_numbers)
                elif i % 5 == 4:                        # determine whether the value is female_number
                    female_numbers = ''
                    for j in range(len(lst)):
                        female_number = lst[j]
                        if female_number.isdigit():     # remove the ',' between the digit
                            female_numbers += female_number
                    total_female += int(female_numbers)
        print(f'Male Number: {total_male}\nFemale Number: {total_female}')


if __name__ == '__main__':
    main()
