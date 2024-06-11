from database.db_helper import execute_query, fetch_all, fetch_one

class Pet:
    @staticmethod
    def create(name, species, age, owner_id, vet_id):
        query = "INSERT INTO Pet (name, species, age, owner_id, vet_id) VALUES (?, ?, ?, ?, ?)"
        execute_query(query, (name, species, age, owner_id, vet_id))

    @staticmethod
    def delete(pet_id):
        query = "DELETE FROM Pet WHERE id = ?"
        execute_query(query, (pet_id,))

    @staticmethod
    def get_all():
        query = "SELECT * FROM Pet"
        return fetch_all(query)

    @staticmethod
    def find_by_id(pet_id):
        query = "SELECT * FROM Pet WHERE id = ?"
        return fetch_one(query, (pet_id,))

