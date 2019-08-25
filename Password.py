import random
from itertools import combinations
import sys

new_list = []


def introductions_function():
    # instructions
    print('''
──────▄▀▀▄────────────────▄▀▀▄────
─────▐▒▒▒▒▌──────────────▌▒▒▒▒▌───
─────▌▒▒▒▒▐─────────────▐▒▒▒▒▒▐───
────▐▒▒▒▒▒▒▌─▄▄▄▀▀▀▀▄▄▄─▌▒▒▒▒▒▒▌──
───▄▌▒▒▒▒▒▒▒▀▒▒▒▒▒▒▒▒▒▒▀▒▒▒▒▒▒▐───
─▄▀▒▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▌───
▐▒▒▒▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐───
▌▒▒▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▌──
▒▒▐▒▒▒▒▒▒▒▒▒▄▀▀▀▀▄▒▒▒▒▒▄▀▀▀▀▄▒▒▐──
▒▒▌▒▒▒▒▒▒▒▒▐▌─▄▄─▐▌▒▒▒▐▌─▄▄─▐▌▒▒▌─
▒▐▒▒▒▒▒▒▒▒▒▐▌▐█▄▌▐▌▒▒▒▐▌▐█▄▌▐▌▒▒▐─
▒▌▒▒▒▒▒▒▒▒▒▐▌─▀▀─▐▌▒▒▒▐▌─▀▀─▐▌▒▒▒▌
▒▌▒▒▒▒▒▒▒▒▒▒▀▄▄▄▄▀▒▒▒▒▒▀▄▄▄▄▀▒▒▒▒▐
▒▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▄▄▄▒▒▒▒▒▒▒▒▒▒▒▐
▒▌▒▒▒▒▒▒▒▒▒▒▒▒▀▒▀▒▒▒▀▒▒▒▀▒▀▒▒▒▒▒▒▐
▒▌▒▒▒▒▒▒▒▒▒▒▒▒▒▀▒▒▒▄▀▄▒▒▒▀▒▒▒▒▒▒▒▐
▒▐▒▒▒▒▒▒▒▒▒▒▀▄▒▒▒▄▀▒▒▒▀▄▒▒▒▄▀▒▒▒▒▐
▒▓▌▒▒▒▒▒▒▒▒▒▒▒▀▀▀▒▒▒▒▒▒▒▀▀▀▒▒▒▒▒▒▐
▒▓▓▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▌
▒▒▓▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▌─
▒▒▓▓▀▀▄▄▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐──
▒▒▒▓▓▓▓▓▀▀▄▄▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▄▄▀▀▒▌─
▒▒▒▒▒▓▓▓▓▓▓▓▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▒▒▒▒▒▐─
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▌
▒▒▒▒▒▒▒█▒█▒█▀▒█▀█▒█▒▒▒█▒█▒█▒▒▒▒▒▒▐
▒▒▒▒▒▒▒█▀█▒█▀▒█▄█▒▀█▒█▀▒▀▀█▒▒▒▒▒▒▐
▒▒▒▒▒▒▒▀▒▀▒▀▀▒▀▒▀▒▒▒▀▒▒▒▀▀▀▒▒▒▒▒▒▐
█▀▄▒█▀▄▒█▀▒█▀█▒▀█▀▒█▒█▒█▒█▄▒█▒▄▀▀▐
█▀▄▒█▀▄▒█▀▒█▄█▒▒█▒▒█▀█▒█▒█▀██▒█▒█▐
▀▀▒▒▀▒▀▒▀▀▒▀▒▀▒▒▀▒▒▀▒▀▒▀▒▀▒▒▀▒▒▀▀▐
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐
    ''')


# a list of words that will help find the correct password
words = ['admin','ADMIN', '0000', 'administrator', 'user', 'qwerty', 'azerty', '123456', 'password', '123456789', '1','2','3','4','Qwerty','0']


def use_list():
    use = input('''Do you want to use an already existing list to make it easier? (yes/no). 
    >''').lower()
    if use == "yes":
        for item in words:
            new_list.append(item)
    elif use == "no":
        pass


# input command
def command_function(list_name):
    print('''To add words to the list, write
            >>>add
    When you are done, write 
            >>>done''')
    while True:
        command = input('>>> ').lower()
        if command == "add":
            list_name.append(input("Add word : "))
            print('Word added')
        elif command == "done":
            break


def output():
    out = input('''Write the output txt file here
(/Desktop/passwords.txt)
    >''')
    return out


# opening (and creating) a text file, "w" means overwrite I can use "a" to keep the words every time I run the program
# output = open("passwords.txt", "w")


# printing the words, faster way but I have to finish it for a better output

def potential_password(list_name, output):
    for item in list_name:
        print(item, file=output)

    words_count = range(len(list_name))

    for item in words_count:
        for item2 in words_count:
            print(list_name[item] + list_name[item2], file=output)

    for item in words_count:
        for item2 in words_count:
            print(list_name[item2] + list_name[item], file=output)

    for item in words_count:
        for item2 in words_count:
            for item3 in words_count:
                print(list_name[item] + list_name[item2] + list_name[item3], file=output)

    for item in words_count:
        for item2 in words_count:
            for item3 in words_count:
                print(list_name[item] + list_name[item3] + list_name[item2], file=output)

    for item in words_count:
        for item2 in words_count:
            for item3 in words_count:
                print(list_name[item2] + list_name[item] + list_name[item3], file=output)

    for item in words_count:
        for item2 in words_count:
            for item3 in words_count:
                print(list_name[item2] + list_name[item3] + list_name[item], file=output)

    for item in words_count:
        for item2 in words_count:
            for item3 in words_count:
                print(list_name[item3] + list_name[item2] + list_name[item], file=output)

    for item in words_count:
        for item2 in words_count:
            for item3 in words_count:
                print(list_name[item3] + list_name[item] + list_name[item2], file=output)
    # closing the txt file
    output.close()


# main program


introductions_function()
use_list()
command_function(new_list)
potential_password(new_list, output=open(output(), "w"))
sys.exit("check your output file.")











'''
    for item in words_count:
        for item2 in words_count:
            for item3 in words_count:
                for item4 in words_count:
                    print(list_name[item] + list_name[item2] + list_name[item3] + list_name[item4], file=output)


oi = ['haleluja', 'oibruvsupmate']
'''

# another way but the problem is that it takes too much time and the output is either tuples or list +notepad file size gets more than 5gb
'''
for i in words_count:
    c = set(combinations(words,i))
    for item in c:
       print(item, file=output)
'''

'''
lezim nchouf kifech naamel loop wa7ad'ha tasna3 for item in words_count 7asb 3dad el words_count ou wa7ad'ha tasna3 item(noumrou) ou tzid +words[item(noumrou)]
'''