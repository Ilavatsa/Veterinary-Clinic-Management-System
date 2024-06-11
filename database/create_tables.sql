-- Create the Owner table
CREATE TABLE Owner (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    address TEXT NOT NULL,
    phone_number TEXT NOT NULL
);

-- Create the Pet table
CREATE TABLE Pet (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    species TEXT NOT NULL,
    age INTEGER NOT NULL,
    owner_id INTEGER,
    vet_id INTEGER,
    FOREIGN KEY (owner_id) REFERENCES Owner(id),
    FOREIGN KEY (vet_id) REFERENCES Veterinarian(id)
);

-- Create the Veterinarian table
CREATE TABLE Veterinarian (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    specialty TEXT NOT NULL,
    phone_number TEXT NOT NULL
);

-- Create the Appointment table
CREATE TABLE Appointment (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    time TEXT NOT NULL,
    pet_id INTEGER,
    vet_id INTEGER,
    FOREIGN KEY (pet_id) REFERENCES Pet(id),
    FOREIGN KEY (vet_id) REFERENCES Veterinarian(id)
);

-- Create the Treatment table
CREATE TABLE Treatment (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT NOT NULL,
    cost REAL NOT NULL,
    appointment_id INTEGER,
    FOREIGN KEY (appointment_id) REFERENCES Appointment(id)
);

-- Create the MedicalRecord table
CREATE TABLE MedicalRecord (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    record_date TEXT NOT NULL,
    details TEXT NOT NULL,
    pet_id INTEGER,
    FOREIGN KEY (pet_id) REFERENCES Pet(id)
);

