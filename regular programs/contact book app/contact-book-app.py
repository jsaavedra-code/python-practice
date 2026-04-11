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
    name = input("Enter contact name: ")     # User inputs the contact name (used as dictionary key)
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    if name in contact_book:                 # Checks if the name already exists in the dictionary
        print("Contact already exists.")
    else:
        contact_book[name] = {               # Nested dictionary to store contact details
        "phone": phone,                      # Stores phone number under 'phone' key
        "email": email,                      # Stores email under 'email' key
        "address": address }                 # Stores address under 'address' key
        print("Contact added successfully.")


# The view_contact function allows the user to view the details of a specific contact by entering the contact's name.
def view_contact(contact_book):
    name = input("Enter contact name: ")

    if name in contact_book:
        contact = contact_book[name]             # Variable to store the nested dictionary of the contact details 
        print(f"Name: {name}")                   # Prints the contact name (key)
        print(f"Phone: {contact['phone']}")      # Accesses phone from nested dictionary
        print(f"Email: {contact['email']}")      # Accesses email from nested dictionary
        print(f"Address: {contact['address']}")  # Accesses address from nested dictionary
    else:
        print("Contact not found.")

# The edit_contact function allows the user to edit the details of an existing contact. 
# The user can choose to update the phone number, email, and address. 
# If the user leaves any field blank, that field will not be updated.
def edit_contact(contact_book):
    name = input("Enter contact name: ")

    if name in contact_book:
        contact = contact_book[name]        # Get reference to nested dictionary (not a copy)
        new_phone = input("Enter new phone number: ")
        new_email = input("Enter new email: ")
        new_address = input("Enter new address: ")

        if new_phone != "":                 # Update phone if user provided a value
            contact["phone"] = new_phone
        if new_email != "":                 # Update email if user provided a value
            contact["email"] = new_email
        if new_address != "":               # Update address if user provided a value
            contact["address"] = new_address

        print("Contact updated successfully.")
    else:
        print("Contact not found.")

# The delete_contact function allows the user to delete a contact from the contact book by entering the contact's name.
# If the contact exists, it will be removed from the contact book. 
# If the contact does not exist, a message will be displayed indicating that the contact was not found.      
def delete_contact(contact_book):
    name = input("Enter contact name: ")

    if name in contact_book:                 # Check if contact exists
        del contact_book[name]               # Delete the key and its nested dictionary
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")
        
# The list_all_contacts function displays all the contacts in the contact book.
# If there are no contacts, it will display a message indicating that no contacts are available.
def list_all_contacts(contact_book):
    if not contact_book:                    # Checks if dictionary is empty
        print("No contacts available.")
    else:
        for name in contact_book:                     # Loop through all keys (contact names)
            contact = contact_book[name]              # Get nested dictionary for each contact
            print(f"Name: {name}")                    # Print name (key)
            print(f"Phone: {contact['phone']}")       # Access phone
            print(f"Email: {contact['email']}")       # Access email
            print(f"Address: {contact['address']}")   # Access address
            print()                                   # Blank line for spacing

# The program runs in a loop, displaying the menu and prompting the user for their choice.
# Based on the user's input, the corresponding function is called to perform the desired action on the contact book.
# The loop continues until the user chooses to exit the program by entering 6.
contact_book = {}  # Main dictionary that stores all contacts

while True:   # Infinite loop to keep the program running until the user decides to exit
    display_menu()

    try:
        choice = int(input("Please enter a valid number from 1 to 6: "))
    except ValueError:   # Handles non-numeric input
        print("Invalid input. Please enter a number.")
        continue  # Restarts the loop to prompt the user again

    if choice == 1:
        add_contact(contact_book)           # Call add function
    elif choice == 2:
        view_contact(contact_book)          # Call view function
    elif choice == 3:
        edit_contact(contact_book)          # Call edit function
    elif choice == 4:
        delete_contact(contact_book)        # Call delete function
    elif choice == 5:
        list_all_contacts(contact_book)     # Call list function
    elif choice == 6:
        break                              # Exit loop → end program
    else:
        print("Invalid choice. Please try again.")  # Handles invalid menu options
