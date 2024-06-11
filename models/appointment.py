from database.db_helper import execute_query, fetch_all, fetch_one

class Appointment:
    @staticmethod
    def create(date, time, pet_id, vet_id):
        query = "INSERT INTO Appointment (date, time, pet_id, vet_id) VALUES (?, ?, ?, ?)"
        execute_query(query, (date, time, pet_id, vet_id))

    @staticmethod
    def delete(appointment_id):
        query = "DELETE FROM Appointment WHERE id = ?"
        execute_query(query, (appointment_id,))

    @staticmethod
    def get_all():
        query = "SELECT * FROM Appointment"
        return fetch_all(query)

    @staticmethod
    def find_by_id(appointment_id):
        query = "SELECT * FROM Appointment WHERE id = ?"
        return fetch_one(query, (appointment_id,))

