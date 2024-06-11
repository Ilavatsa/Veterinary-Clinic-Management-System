import sqlite3

def create_database():
    conn = sqlite3.connect('vet_clinic.db')
    cursor = conn.cursor()

    with open('database/create_tables.sql', 'r') as f:
        sql_script = f.read()

    cursor.executescript(sql_script)
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_database()
