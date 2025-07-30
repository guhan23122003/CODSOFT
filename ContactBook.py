contacts = []

while True:
    print("\nContact Manager")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == '1':
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        contact = {"name": name, "phone": phone, "email": email, "address": address}
        contacts.append(contact)
        print("Contact added.")

    elif choice == '2':
        if len(contacts) == 0:
            print("No contacts found.")
        else:
            print("\nContact List:")
            for i in range(len(contacts)):
                print(f"{i+1}. {contacts[i]['name']} - {contacts[i]['phone']}")

    elif choice == '3':
        query = input("Enter name or phone to search: ").lower()
        found = []
        for c in contacts:
            if query in c["name"].lower() or query in c["phone"]:
                found.append(c)
        if len(found) > 0:
            print("\nSearch Results:")
            for c in found:
                print("Name:", c["name"])
                print("Phone:", c["phone"])
                print("Email:", c["email"])
                print("Address:", c["address"])
                print("")
        else:
            print("No matching contacts found.")

    elif choice == '4':
        if len(contacts) == 0:
            print("No contacts to update.")
        else:
            for i in range(len(contacts)):
                print(f"{i+1}. {contacts[i]['name']} - {contacts[i]['phone']}")
            num = input("Enter contact number to update: ")
            if num.isdigit():
                idx = int(num) - 1
                if 0 <= idx < len(contacts):
                    contact = contacts[idx]
                    new_name = input(f"New name ({contact['name']}): ")
                    if new_name != "":
                        contact['name'] = new_name
                    new_phone = input(f"New phone ({contact['phone']}): ")
                    if new_phone != "":
                        contact['phone'] = new_phone
                    new_email = input(f"New email ({contact['email']}): ")
                    if new_email != "":
                        contact['email'] = new_email
                    new_address = input(f"New address ({contact['address']}): ")
                    if new_address != "":
                        contact['address'] = new_address
                    contacts[idx] = contact
                    print("Contact updated.")
                else:
                    print("Invalid contact number.")
            else:
                print("Invalid input.")

    elif choice == '5':
        if len(contacts) == 0:
            print("No contacts to delete.")
        else:
            for i in range(len(contacts)):
                print(f"{i+1}. {contacts[i]['name']} - {contacts[i]['phone']}")
            num = input("Enter contact number to delete: ")
            if num.isdigit():
                idx = int(num) - 1
                if 0 <= idx < len(contacts):
                    deleted = contacts.pop(idx)
                    print(f"Deleted contact: {deleted['name']}")
                else:
                    print("Invalid contact number.")
            else:
                print("Invalid input.")

    elif choice == '6':
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
