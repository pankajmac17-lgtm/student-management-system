import mysql.connector

# connect to database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="RooT#123",        # add password if you set one
    database="student_db"
)

cursor = conn.cursor()

# student data
name = "Ganesh"
roll_no = "101"
marks = 85

# logic for result
result = "Pass" if marks >= 40 else "Fail"

# insert query
query = "INSERT INTO students (name, roll_no, marks, result) VALUES (%s, %s, %s, %s)"
values = (name, roll_no, marks, result)

cursor.execute(query, values)

# save changes
conn.commit()

print("Student inserted successfully")

# close connection
cursor.close()
conn.close()