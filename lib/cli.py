# cli.py

def display_menu():
    """Display the menu options."""
    print("Veterinary Clinic Management System")
    print("1. Add new patient")
    print("2. View patient information")
    print("3. Update patient information")
    print("4. Delete patient")
    print("5. Exit")

def add_patient():
    """Function to add a new patient."""
    print("Adding new patient...")
    # Add code to handle adding a new patient

def view_patient():
    """Function to view patient information."""
    print("Viewing patient information...")
    # Add code to handle viewing patient information

def update_patient():
    """Function to update patient information."""
    print("Updating patient information...")
    # Add code to handle updating patient information

def delete_patient():
    """Function to delete a patient."""
    print("Deleting patient...")
    # Add code to handle deleting a patient

def cli():
    """Main function to run the CLI."""
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_patient()
        elif choice == '2':
            view_patient()
        elif choice == '3':
            update_patient()
        elif choice == '4':
            delete_patient()
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    cli()
