import models.owner as owner

def list_owners():
    """Function to list all owners."""
    owners = owner.Owner.get_all()
    if not owners:
        print("No owners found.")
    else:
        print("List of Owners:")
        for o in owners:
            print(f"Owner ID: {o.id}, Name: {o.name}, Address: {o.address}, Phone Number: {o.phone_number}")

# Call the function to list owners
list_owners()
