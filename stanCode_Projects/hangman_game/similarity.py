"""
File: similarity.py
Name: JOHNSON
----------------------------
This program compares short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    dna = input('Please give me a DNA sequence to search: ')
    match = input('What DNA sequence would you like to match? ')
    dna = dna.upper()
    match = match.upper()
    ans = find_match(dna, match)
    print('The best match is ' + str(ans) + '.')


def find_match(dna, match):
    '''
    :param dna: str, the user will input the dna string.
    :param match: str, the user will input the small facture of dna.
    :return: str, the similar fracture in the long dna string.
    '''
    score_list = []                             # Through for loop, we can compare the original dna
    for i in range(len(dna) - len(match) + 1):  # with the fracture one and give each a score!
        score = 0
        for j in range(len(match)):
            if match[j] == dna[i + j]:
                score += 1
        score_list.append(score)

    maximum = score_list[0]                     # Find the biggest score, which is the most similar
    for num in score_list:                      # fracture of dna.
        if maximum <= num:
            maximum = num

    location = score_list.index(maximum)
    ans = dna[location:location+len(match)]
    return ans






###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
