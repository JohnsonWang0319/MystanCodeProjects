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
    secret_num = int(input('Secret number: '))
    ciph_str = input('What\'s the ciphered string? ')
    ciph_str = ciph_str.upper()
    deciph_str = decipher(secret_num, ciph_str)
    print('The deciphered string is: ' + str(deciph_str))


def decipher(secret_num, ciph_str):
    tail = ALPHABET[len(ALPHABET)-secret_num:]
    head = ALPHABET[:len(ALPHABET)-secret_num:]
    new_order = ''
    new_order = new_order + tail
    new_order = new_order + head
    location = []
    for i in range(len(ciph_str)):
        location.append(new_order.find(ciph_str[i]))
    ans = ''
    for i in range(len(location)):
        if location[i] == -1:
            ans = ans + ciph_str[i]
        else:
            ans = ans + ALPHABET[location[i]]
    return ans




#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
