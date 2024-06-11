
from database.db_helper import execute_query, fetch_all, fetch_one

class MedicalRecord:
    @staticmethod
    def create(record_date, details, pet_id):
        query = "INSERT INTO MedicalRecord (record_date, details, pet_id) VALUES (?, ?, ?)"
        execute_query(query, (record_date, details, pet_id))

    @staticmethod
    def delete(medical_record_id):
        query = "DELETE FROM MedicalRecord WHERE id = ?"
        execute_query(query, (medical_record_id,))

    @staticmethod
    def get_all():
        query = "SELECT * FROM MedicalRecord"
        return fetch_all(query)

    @staticmethod
    def find_by_id(medical_record_id):
        query = "SELECT * FROM MedicalRecord WHERE id = ?"
        return fetch_one(query, (medical_record_id,))
