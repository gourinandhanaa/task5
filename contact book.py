contacts = []

def add_contact():
    name = input("Enter contact name: ")
    phone_number = input("Enter phone number: ")
    email = input("Enter email address: ")
    address = input("Enter address: ")
    contact = {
        "name": name,
        "phone_number": phone_number,
        "email": email,
        "address": address
    }
    contacts.append(contact)
    print("Contact added successfully!")

def view_contact_list():
    if contacts:
        print("Contact List:")
        for index, contact in enumerate(contacts, start=1):
            print(f"{index}. {contact['name']} - {contact['phone_number']}")
    else:
        print("No contacts found.")

def search_contact():
    search_term = input("Enter name or phone number to search: ")
    found_contacts = []
    for contact in contacts:
        if search_term.lower() in contact['name'].lower() or search_term in contact['phone_number']:
            found_contacts.append(contact)
    if found_contacts:
        print("Search Results:")
        for index, contact in enumerate(found_contacts, start=1):
            print(f"{index}. {contact['name']} - {contact['phone_number']}")
    else:
        print("No matching contacts found.")

def update_contact():
    search_term = input("Enter name or phone number of contact to update: ")
    for contact in contacts:
        if search_term.lower() in contact['name'].lower() or search_term in contact['phone_number']:
            print("Contact found. Enter new details:")
            contact['name'] = input("Enter new name: ")
            contact['phone_number'] = input("Enter new phone number: ")
            contact['email'] = input("Enter new email address: ")
            contact['address'] = input("Enter new address: ")
            print("Contact updated successfully.")
            return
    print("Contact not found.")

def delete_contact():
    search_term = input("Enter name or phone number of contact to delete: ")
    for contact in contacts:
        if search_term.lower() in contact['name'].lower() or search_term in contact['phone_number']:
            contacts.remove(contact)
            print("Contact deleted successfully.")
            return
    print("Contact not found.")

def main():
    while True:
        print("\nContact Management System\n")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contact_list()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__== "__main__":
    main()