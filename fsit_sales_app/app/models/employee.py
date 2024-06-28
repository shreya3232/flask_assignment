import sqlite3

def get_employee_data():
    conn = sqlite3.connect('fsit_sales_database.db')
    cursor = conn.cursor()
    
    query = """
    SELECT e.employeeNumber, e.lastName, e.firstName, e.extension, e.email, e.officeCode, e.jobTitle,
           o.city, o.phone, e.reportsTo, r.lastName AS reportToLastName, r.firstName AS reportToFirstName
    FROM employees e
    LEFT JOIN employees r ON e.reportsTo = r.employeeNumber
    LEFT JOIN offices o ON e.officeCode = o.officeCode;
    """
    
    cursor.execute(query)
    rows = cursor.fetchall()
    
    employees = []
    for row in rows:
        employee = {
            "employeeNumber": row[0],
            "lastName": row[1],
            "firstName": row[2],
            "extension": row[3],
            "email": row[4],
            "officeCode": row[5],
            "jobTitle": row[6],
            "city": row[7],
            "phone": row[8],
            "reportsTo": row[9],
            "reportToLastName": row[10],
            "reportToFirstName": row[11]
        }
        employees.append(employee)
    
    conn.close()
    return {"data": employees}
