contacts = []


def add_contact(name, email, phone_number):
    new_contact = {
        "name": name,
        "email": email,
        "phone_number": phone_number
    }
    contacts.append(new_contact)
    print('Contact added successfully!')


def view_contacts():
    if not contacts:
        print('There are no contacts')
    else:
        print('Contact Lists:')

    for contact in contacts:
        print(f"{contacts.index(contact) + 1} name: {contact["name"]}, email: {contact["email"]}, phone number: {contact["phone_number"]}")


def update_contact(name, new_email, new_phone_number):
    for contact in contacts:
        if contact["name"] == name:
            contact["email"] = new_email
            contact["phone_number"] = new_phone_number
            print('Contact updated successfully!')
            return
    
    print(f'{name} not found')


def delete_contact(name):
    for contact in contacts:
        if contact["name"] == name:
            contacts.remove(contact)
            print("Contact deleted successfully!")
            break

    else:
        print(f"{name} not found")