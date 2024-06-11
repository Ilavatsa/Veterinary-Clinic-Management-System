# cli.py

# Define a list to store patient records (each patient represented as a dictionary)
patients = []

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
    # Prompt user for patient details
    name = input("Enter patient's name: ")
    age = int(input("Enter patient's age: "))
    # Create a new patient record (represented as a dictionary)
    patient = {'name': name, 'age': age}
    # Append the patient record to the list of patients
    patients.append(patient)
    print("Patient added successfully.")

def view_patient():
    """Function to view patient information."""
    print("Viewing patient information...")
    if patients:
        for index, patient in enumerate(patients, start=1):
            print(f"Patient {index}: Name - {patient['name']}, Age - {patient['age']}")
    else:
        print("No patients found.")

def update_patient():
    """Function to update patient information."""
    print("Updating patient information...")
    view_patient()  # Display current patient information
    if patients:
        patient_index = int(input("Enter the index of the patient to update: ")) - 1
        if 0 <= patient_index < len(patients):
            # Prompt user for updated details
            name = input("Enter updated name: ")
            age = int(input("Enter updated age: "))
            # Update patient record
            patients[patient_index]['name'] = name
            patients[patient_index]['age'] = age
            print("Patient information updated successfully.")
        else:
            print("Invalid patient index.")
    else:
        print("No patients found.")

def delete_patient():
    """Function to delete a patient."""
    print("Deleting patient...")
    view_patient()  # Display current patient information
    if patients:
        patient_index = int(input("Enter the index of the patient to delete: ")) - 1
        if 0 <= patient_index < len(patients):
            # Delete patient record
            del patients[patient_index]
            print("Patient deleted successfully.")
        else:
            print("Invalid patient index.")
    else:
        print("No patients found.")

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
