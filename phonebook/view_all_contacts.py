def view_all_contacts(all_contacts):
    if all_contacts !=[]:
        for contact in all_contacts:
            print(f"\nName: {contact['name']}\nNumber: {contact['number']}\nEmail: {contact['email']}\nAddress: {contact['address']}\n")

    else:
        print("\nNo contacts found\n")