Veterinary Clinic Management System
This Python CLI Application is designed to manage a veterinary clinic system. Users can interactively manage pets, their owners, and veterinarians within a clinic database using Object-Relational Mapping (ORM) methods.

Features
Manage pets, owners, and veterinarians.
Perform CRUD operations on pets, owners, and veterinarians.
View relationships between pets, owners, and veterinarians.
Search for objects by specific attributes.
Input validation and error handling to ensure data integrity. 

Database Interaction 
The SQLite database was managed using SQLAlchemy ORM.
Three main model classes: Pet, Owner, and Veterinarian.
One-to-many relationships are established between the Owner and Pet, and between the Veterinarian and Pet.
Command-Line Interface
The CLI provides interactive menus allowing users to navigate through options for each class (Owner, Pet, and Veterinarian):

Create an object (e.g., add a new pet, owner, or veterinarian).
Delete an object (e.g., remove a pet, owner, or veterinarian from the database).
Display all objects (e.g., list all pets, owners, or veterinarians).
View related objects (e.g., list all pets owned by a specific owner or all pets under a specific veterinarian's care).
Find an object by attribute (e.g., search for a pet by name, an owner by phone number, or a veterinarian by specialty).
Input Validation and Error Handling
User input is validated to ensure data integrity and informative error messages are provided for invalid operations or inputs. Users are kept within the application loop until they choose to exit.

Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your enhancements.

License
This project is licensed under the MIT License.