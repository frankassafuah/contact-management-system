
from modules import *

def main():
    while True:
        print('1. Add contact')
        print('2. View contacts')
        print('3. Update contact')
        print('4. Delete contact')
        print('5. Exit')

        choice = input("Enter your choice: ")

        match choice:
            case '1':
                name = input('Enter name: ')
                email = input('Enter email: ')
                phone_number = input('Enter phone number: ')
                add_contact(name, email, phone_number)
            
            case '2':
                view_contacts()
            
            case '3':
                name_to_update = input('Enter the contact name to update: ')
                new_email = input('Enter new email: ')
                new_phone_number = input("Enter new phone number: ")
                update_contact(name_to_update, new_email, new_phone_number)

            case '4':
                name_to_delete = input('Enter the contact name to delete: ')
                delete_contact(name_to_delete)
            
            case '5':
                print('Bye!')
                break
            
            case _:
                print('Invalid input')

main()