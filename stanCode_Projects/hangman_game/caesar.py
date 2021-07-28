"""
File: caesar.py
Name: JOHNSON
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    '''
    I did the 'ceasar_Lite' by using LIST, it was more simple and easy!!
    '''
    secret_num = int(input('Secret number: '))
    ciph_str = input('What\'s the ciphered string? ')
    ciph_str = ciph_str.upper()
    deciph_str = decipher(secret_num, ciph_str)
    print('The deciphered string is: ' + str(deciph_str))



def decipher(secret_num, ciph_str):
    '''
    :param secret_num: int, the user will enter the number that the ALPHABET will move left.
    :param ciph_str: str, the user will enter the cipher.
    :return: str, the string that is decipher!
    '''
    tail = ALPHABET[len(ALPHABET)-secret_num:]
    head = ALPHABET[:len(ALPHABET)-secret_num:]
    new_order = ''
    new_order = new_order + tail
    new_order = new_order + head

    location = ''           # save the word location in the new order
    non_alph = ''           # save the non alphabet element
    for i in range(len(ciph_str)):
        location = location + str(new_order.find(ciph_str[i])) + ','
        if ciph_str[i].isalpha() == True:
            non_alph = non_alph + '*' * len(str(new_order.find(ciph_str[i])) + '*')
        else:
            non_alph = non_alph + ciph_str[i] * 2 + '*'

    ans = ''                # those for loop will process the string in the 'location' and 'non_alph'
    for j in range(len(location)):
        if location[j] == '-':
            ans = ans + non_alph[j]
        elif location[j] == ',':
            ans = ans
        elif location[j - 1].isdigit() == True:
            ans = ans
        elif location[j + 1].isdigit() == False:
            if location[j - 1] == '-':
                ans = ans
            else:
                ans = ans + ALPHABET[int(location[j])]
        else:
            double = int(location[j]) * 10 + int(location[j + 1])
            ans = ans + ALPHABET[double]

    return ans










#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
