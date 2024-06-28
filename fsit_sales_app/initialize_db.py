import sqlite3

# Connect to SQLite database (it will create the database if it doesn't exist)
conn = sqlite3.connect('fsit_sales_database.db')
cursor = conn.cursor()

# Read the SQL file
with open('SalesDatabase.sql', 'r') as file:
    sql_script = file.read()

# Execute the SQL script to create tables and insert data
cursor.executescript(sql_script)

# Commit the changes and close the connection
conn.commit()
conn.close()
