from database.db_helper import execute_query, fetch_all, fetch_one

class Treatment:
    @staticmethod
    def create(description, cost, appointment_id):
        query = "INSERT INTO Treatment (description, cost, appointment_id) VALUES (?, ?, ?)"
        execute_query(query, (description, cost, appointment_id))

    @staticmethod
    def delete(treatment_id):
        query = "DELETE FROM Treatment WHERE id = ?"
        execute_query(query, (treatment_id,))

    @staticmethod
    def get_all():
        query = "SELECT * FROM Treatment"
        return fetch_all(query)

    @staticmethod
    def find_by_id(treatment_id):
        query = "SELECT * FROM Treatment WHERE id = ?"
        return fetch_one(query, (treatment_id,))

