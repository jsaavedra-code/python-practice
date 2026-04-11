# Welcome to my contact book app
# This app allows you to manage your contacts by adding, viewing, editing, and deleting them. 
# You can also list all your contacts at any time. 

# The contact book is implemented as a dictionary where the keys are the contact names and the values are dictionaries. 
# These dictionaries contain the phone number, email, and address of each contact.
# The app provides a simple menu-driven interface for users to interact with their contact book.

# The display_menu function shows the available options to the user.
def display_menu():
    print("Contact Book Menu:")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. List All Contacts")
    print("6. Exit")

# The add_contact function allows the user to add a new contact to the contact book.
def add_contact(contact_book):
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    if name in contact_book:
        print("Contact already exists.")
    else:
        contact_book[name] = {
        "phone": phone, 
        "email": email, 
        "address": address }
        print ("Contact added successfully.")

# The view_contact function allows the user to view the details of a specific contact by entering the contact's name.
def view_contact(contact_book):
    name = input("Enter contact name: ")

    if name in contact_book:
        contact = contact_book[name]
        print(f"Name: {name}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
        print(f"Address: {contact['address']}")
    else:
        print("Contact not found.")

# The edit_contact function allows the user to edit the details of an existing contact. 
# The user can choose to update the phone number, email, and address. 
# If the user leaves any field blank, that field will not be updated.
def edit_contact(contact_book):
    name = input("Enter contact name: ")

    if name in contact_book:
        contact = contact_book[name]

        new_phone = input("Enter new phone number: ")
        new_email = input("Enter new email: ")
        new_address = input("Enter new address: ")

        if new_phone != "":
            contact["phone"] = new_phone
        if new_email != "":
            contact["email"] = new_email
        if new_address != "":
            contact["address"] = new_address

        print("Contact updated successfully.")
    else:
        print("Contact not found.")

# The delete_contact function allows the user to delete a contact from the contact book by entering the contact's name.
# If the contact exists, it will be removed from the contact book. 
# If the contact does not exist, a message will be displayed indicating that the contact was not found.      
def delete_contact(contact_book):
    name = input("Enter contact name: ")

    if name in contact_book:
        del contact_book[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")
        
# The list_all_contacts function displays all the contacts in the contact book.
# If there are no contacts, it will display a message indicating that no contacts are available.
def list_all_contacts(contact_book):
    if not contact_book:
        print("No contacts available.")
    else:
        for name in contact_book:
            contact = contact_book[name]

            print(f"Name: {name}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
            print()


