
CREATE DATABASE IF NOT EXISTS HospitalManagement;

USE HospitalManagement;

CREATE TABLE Departments (
    DepartmentID INT PRIMARY KEY,
    Name VARCHAR(50) NOT NULL,
    Location VARCHAR(100) NOT NULL
);

CREATE TABLE Doctors (
    DoctorID INT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Specialization VARCHAR(50),
    Phone VARCHAR(15),
    DepartmentID INT,
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID)
);

CREATE TABLE Patients (
    PatientID INT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Age INT,
    Gender VARCHAR(10),
    Phone VARCHAR(15)
);

CREATE TABLE Appointments (
    AppointmentID INT PRIMARY KEY,
    Date DATE NOT NULL,
    Time TIME NOT NULL,
    Status VARCHAR(20),
    DoctorID INT,
    PatientID INT,
    FOREIGN KEY (DoctorID) REFERENCES Doctors(DoctorID),
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID)
);

-- DUMMY DATAS
INSERT INTO Departments VALUES (1, 'Cardiology', 'First Floor');
INSERT INTO Departments VALUES (2, 'Orthopedics', 'Second Floor');
INSERT INTO Departments VALUES (3, 'Neurology', 'Third Floor');
INSERT INTO Departments VALUES (4, 'Pediatrics', 'Ground Floor');
INSERT INTO Departments VALUES (5, 'Dermatology', 'Second Floor');


INSERT INTO Doctors VALUES (1, 'Dr. Smith', 'Cardiologist', '1234567890', 1);
INSERT INTO Doctors VALUES (2, 'Dr. Emily', 'Orthopedist', '0987654321', 2);
INSERT INTO Doctors VALUES (3, 'Dr. Alice', 'Neurologist', '1122334455', 3);
INSERT INTO Doctors VALUES (4, 'Dr. John', 'Pediatrician', '6677889900', 4);
INSERT INTO Doctors VALUES (5, 'Dr. Jane', 'Dermatologist', '5566778899', 5);


INSERT INTO Patients VALUES (1, 'Alice Johnson', 29, 'Female', '1231231234');
INSERT INTO Patients VALUES (2, 'Bob Williams', 45, 'Male', '4564564567');
INSERT INTO Patients VALUES (3, 'Charlie Brown', 35, 'Male', '7897897890');
INSERT INTO Patients VALUES (4, 'Diana Prince', 30, 'Female', '3213213214');
INSERT INTO Patients VALUES (5, 'Eva Green', 27, 'Female', '6546546543');


INSERT INTO Appointments VALUES (1, '2024-12-22', '09:00:00', 'Confirmed', 1, 1);
INSERT INTO Appointments VALUES (2, '2024-12-22', '10:00:00', 'Pending', 2, 2);
INSERT INTO Appointments VALUES (3, '2024-12-22', '11:00:00', 'Cancelled', 3, 3);
INSERT INTO Appointments VALUES (4, '2024-12-22', '12:00:00', 'Confirmed', 4, 4);
INSERT INTO Appointments VALUES (5, '2024-12-22', '01:00:00', 'Pending', 5, 5);
