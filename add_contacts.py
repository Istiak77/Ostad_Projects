import re
from save_all_contacts import save_all_contacts

def add_contacts(all_contacts):
    while True:
        name = input("Enter contact name: ").lower()
        if not name.isdigit() and name.strip():
            break
        else:
            print("Invalid name. Please enter a valid name.")

    while True:
        number = input("Enter contact phone number: ")
        if number.isdigit():
            if not any(contact['number'] == number for contact in all_contacts):
                break
            else:
                print("This phone number is already associated with another contact.")
        else:
            print("Invalid phone number. Please enter digits only.")

    while True:
        email = input("Enter an email: ")
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(email_regex, email):
            break
        else:
            print("Invalid email format. Please try again.")

    address = input("Provide an address: ")

    contact = {
        "name": name,
        "number": number,
        "email": email,
        "address": address,
    }

    all_contacts.append(contact)
    save_all_contacts(all_contacts)
    print("Contact added successfully")

    return all_contacts


def search_contacts(all_contacts):

    query = input("Enter name or phone number to search: ")
    for contact in all_contacts:
        if contact['name'].lower() == query or contact['number'] == query:
            print(f"Contact found: Name: {contact['name']}, Phone: {contact['number']}, Email: {contact['email']}")
            return

    print("No contact found with that name or phone number.")

def delete_contact(all_contacts):

    query = input("Enter name or phone number of the contact to delete: ").lower()
    for contact in all_contacts:
        if contact['name'].lower() == query or contact['number'] == query:
            all_contacts.remove(contact)
            print(f"Contact deleted: Name: {contact['name']}")
            return
    print("No contact found with that name or phone number.")

def modify_contact(all_contacts):
    
    if not all_contacts:
        print("No contacts found.")
        return all_contacts

    name_to_search = input("Enter the name of the contact you want to modify: ")
    contact_to_modify = None

    for contact in all_contacts:
        if contact['name'].lower() == name_to_search.lower():
            contact_to_modify = contact
            break

    if not contact_to_modify:
        print(f"No contact found with the name '{name_to_search}'.")
        return all_contacts

    new_name = input(f"Enter new name (Leave blank to keep {contact_to_modify['name']}): ")
    if new_name:
        contact_to_modify['name'] = new_name

    new_number = input(f"Enter new phone number (Leave blank to keep {contact_to_modify['number']}): ")
    if new_number:
        if not new_number.isdigit():
            print("Invalid phone number. Please enter a valid number with digits only.")
        else:
            contact_to_modify['number'] = new_number

    new_email = input(f"Enter new email (Leave blank to keep {contact_to_modify['email']}): ")
    if new_email:
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(email_regex, new_email):
            contact_to_modify['email'] = new_email
        else:
            print("Invalid email format.")

    new_address = input(f"Enter new address (Leave blank to keep {contact_to_modify['address']}): ")
    if new_address:
        contact_to_modify['address'] = new_address

    return all_contacts

