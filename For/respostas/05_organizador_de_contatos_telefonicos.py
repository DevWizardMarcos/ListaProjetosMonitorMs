# filepath: c:\Users\INFINITY SCHOOL\Desktop\Lista De Exercios Do Monitor Marrcos\For\05_organizador_de_contatos_telefonicos.py

class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

class ContactOrganizer:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone):
        new_contact = Contact(name, phone)
        self.contacts.append(new_contact)
        print(f"Contact {name} added.")

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                return contact
        return None

    def display_contacts(self):
        if not self.contacts:
            print("No contacts available.")
            return
        for contact in self.contacts:
            print(f"Name: {contact.name}, Phone: {contact.phone}")

def main():
    organizer = ContactOrganizer()
    
    while True:
        print("\nContact Organizer")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Display Contacts")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter contact phone: ")
            organizer.add_contact(name, phone)
        elif choice == '2':
            name = input("Enter contact name to search: ")
            contact = organizer.search_contact(name)
            if contact:
                print(f"Found: Name: {contact.name}, Phone: {contact.phone}")
            else:
                print("Contact not found.")
        elif choice == '3':
            organizer.display_contacts()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()