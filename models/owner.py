from database.db_helper import execute_query, fetch_all, fetch_one

class Owner:
    @staticmethod
    def create(name, address, phone_number):
        query = "INSERT INTO Owner (name, address, phone_number) VALUES (?, ?, ?)"
        execute_query(query, (name, address, phone_number))

    @staticmethod
    def delete(owner_id):
        query = "DELETE FROM Owner WHERE id = ?"
        execute_query(query, (owner_id,))

    @staticmethod
    def get_all():
        query = "SELECT * FROM Owner"
        return fetch_all(query)

    @staticmethod
    def find_by_id(owner_id):
        query = "SELECT * FROM Owner WHERE id = ?"
        return fetch_one(query, (owner_id,))


