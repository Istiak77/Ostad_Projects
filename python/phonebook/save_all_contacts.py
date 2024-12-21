import csv
import os 


def save_all_contacts(all_contacts):
    project_folder = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(project_folder, "all_contacts.csv")

    with open(file_path, "w") as fp:
        fp.write("Name,Phone Number,Email,Address\n")
        for contact in all_contacts:
            line = f"{contact['name']},{contact['number']},{contact['email']},{contact['address']}\n"
            fp.write(line)



def load_contacts():
    contacts = []

    project_folder = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(project_folder, "all_contacts.csv")

    if os.path.exists(file_path):
        with open(file_path, "r") as fp:
            reader = csv.DictReader(fp)
            for row in reader:
                contact = {
                    "name": row["Name"],
                    "number": row["Phone Number"],
                    "email": row["Email"],
                    "address": row["Address"]
                }
                contacts.append(contact)
    else:
        print("\nNo contacts found.\n")

    return contacts