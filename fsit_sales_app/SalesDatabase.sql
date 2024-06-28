-- Create employees table
CREATE TABLE employees (
    employeeNumber INTEGER PRIMARY KEY,
    lastName TEXT NOT NULL,
    firstName TEXT NOT NULL,
    extension TEXT NOT NULL,
    email TEXT NOT NULL,
    officeCode INTEGER NOT NULL,
    reportsTo INTEGER,
    jobTitle TEXT NOT NULL,
    FOREIGN KEY (reportsTo) REFERENCES employees(employeeNumber)
);

-- Create offices table
CREATE TABLE offices (
    officeCode INTEGER PRIMARY KEY,
    city TEXT NOT NULL,
    phone TEXT NOT NULL
);

-- Insert some sample data into employees
INSERT INTO employees (employeeNumber, lastName, firstName, extension, email, officeCode, reportsTo, jobTitle) VALUES
(1056, 'Patterson', 'Mary', 'x4611', 'mpatterso@classicmodelcars.com', 1, 1002, 'VP Sales'),
(1076, 'Firrelli', 'Jeff', 'x9273', 'jfirrelli@classicmodelcars.com', 1, 1002, 'VP Marketing');

-- Insert some sample data into offices
INSERT INTO offices (officeCode, city, phone) VALUES
(1, 'San Francisco', '+1 650 219 4782');
  