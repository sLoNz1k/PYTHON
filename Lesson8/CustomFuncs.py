import os
import re

def show_contacts(file_name):
    os.system('CLS')
    with open(file_name, 'r') as file: 
        data = file.readlines()

        for contact in data :
            print(contact, end='')
    input('\nPress any key: ')

def add_contact(file_name):
    os.system('CLS')
    with open(file_name, 'a') as file:
        res = ''
        res += input('Input a name of contact: ') + ' '
        res += input('Input a surname of contact:') + ' '
        res += input('Input a phone number of contact:')

        file.write('\n' + res)
    input('Contact successfully add! Press any key for return')

def find_contact(file_name):
    os.system('CLS')
    target = input('Input a name of contact for searching: ')

    with open(file_name, 'r') as file: 
        contacts = file.readlines()

        for contact in contacts:                
            if target in contact:
                print(contact)
                break
        else :
            print('there is no contacts with this name.')

    input('press any key')


def delete_contact(file_name):
    # os.system('CLS')
    target = input('Input a name of contact for delete: ')

    with open(file_name, 'r') as file:
        contacts = file.readlines() 
    
        for i in range(len(contacts)):
            if target in contacts[i]:
                contacts.pop(i)
                print(contacts)
                convert = ''.join(str(x) for x in contacts)
                print(convert)
                file.write(convert)

                break

               # print('Successfully deleted!')
        else:
            print('there is no contact with this name!')
    input('press any key')
        

def drawing():
    print('1 - show contacts')
    print('2 - add contact')
    print('3 - search contact')
    print('4 - delete contact')
    print('6 - exit')

def main(file_name):
    while True:
        os.system('CLS')
        drawing()
        user_choice = int(input('Input a number from 1 to 6: '))

        if user_choice == 1:
            show_contacts(file_name)
        elif user_choice == 2:
            add_contact(file_name)
        elif user_choice == 3:
            find_contact(file_name)
        elif user_choice == 4:
            delete_contact(file_name)
        elif user_choice == 6:
            print('Have a nice day!\n')
            return

main("test.txt")