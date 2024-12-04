import add_contacts
import view_all_contacts
from add_contacts import search_contacts, delete_contact, modify_contact
from save_all_contacts import save_all_contacts
from save_all_contacts import load_contacts

all_contacts = load_contacts()

while True:
    print("=====================================\n")
    print("Welcome to Python Phonebook")
    print("1.Add a contact")
    print("2.View all contacts")
    print("3.Search for a contact")
    print("4.Delete a contact")
    print("5.Modify a contact")
    print("Press Q to quit\n")
    print("=====================================\n")

    menu = input("Select an option: ")

    if menu.upper() == "Q":
        save_all_contacts(all_contacts)
        print("Thanks for using Python Phonebook")
        break
    elif menu == "1":
        all_contacts = add_contacts.add_contacts(all_contacts)
    elif menu == "2":
        view_all_contacts.view_all_contacts(all_contacts)
    elif menu == "3":
        search_contacts(all_contacts)
    elif menu == "4":
         delete_contact(all_contacts)
    elif menu == "5":
        modify_contact(all_contacts)
    else:
        print("Choose a valid option")