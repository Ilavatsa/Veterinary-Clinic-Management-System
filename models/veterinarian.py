from database.db_helper import execute_query, fetch_all, fetch_one

class Veterinarian:
    @staticmethod
    def create(name, specialty, phone_number):
        query = "INSERT INTO Veterinarian (name, specialty, phone_number) VALUES (?, ?, ?)"
        execute_query(query, (name, specialty, phone_number))

    @staticmethod
    def delete(vet_id):
        query = "DELETE FROM Veterinarian WHERE id = ?"
        execute_query(query, (vet_id,))

    @staticmethod
    def get_all():
        query = "SELECT * FROM Veterinarian"
        return fetch_all(query)

    @staticmethod
    def find_by_id(vet_id):
        query = "SELECT * FROM Veterinarian WHERE id = ?"
        return fetch_one(query, (vet_id,))

