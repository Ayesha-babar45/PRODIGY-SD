import json

class ContactManager:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone_number, email):
        self.contacts[name] = {'phone_number': phone_number, 'email': email}
        print(f"Contact {name} added successfully.")

    def view_contacts(self):
        if self.contacts:
            print("Your Contacts:")
            for name, info in self.contacts.items():
                print(f"Name: {name}, Phone: {info['phone_number']}, Email: {info['email']}")
        else:
            print("You don't have any contacts yet.")

    def edit_contact(self, name, phone_number, email):
        if name in self.contacts:
            self.contacts[name] = {'phone_number': phone_number, 'email': email}
            print(f"Contact {name} updated successfully.")
        else:
            print(f"Contact {name} not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact {name} deleted successfully.")
        else:
            print(f"Contact {name} not found.")

    def save_contacts_to_file(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.contacts, file)
            print("Contacts saved successfully.")

    def load_contacts_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                self.contacts = json.load(file)
                print("Contacts loaded successfully.")
        except FileNotFoundError:
            print("Contacts file not found.")

if __name__ == "__main__":
    contact_manager = ContactManager()

    while True:
        print("\nContact Management System Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Save Contacts to File")
        print("6. Load Contacts from File")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email address: ")
            contact_manager.add_contact(name, phone_number, email)
        elif choice == '2':
            contact_manager.view_contacts()
        elif choice == '3':
            name = input("Enter name of contact to edit: ")
            phone_number = input("Enter new phone number: ")
            email = input("Enter new email address: ")
            contact_manager.edit_contact(name, phone_number, email)
        elif choice == '4':
            name = input("Enter name of contact to delete: ")
            contact_manager.delete_contact(name)
        elif choice == '5':
            filename = input("Enter filename to save contacts: ")
            contact_manager.save_contacts_to_file(filename)
        elif choice == '6':
            filename = input("Enter filename to load contacts: ")
            contact_manager.load_contacts_from_file(filename)
        elif choice == '7':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")
