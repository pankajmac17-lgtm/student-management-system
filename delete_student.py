import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="RooT#123",
    database="student_db"
)

cursor = conn.cursor()

roll_no = input("Enter roll number to delete: ")

query = "DELETE FROM students WHERE roll_no = %s"
cursor.execute(query, (roll_no,))

conn.commit()

if cursor.rowcount > 0:
    print("Student deleted successfully")
else:
    print("Student not found")

cursor.close()
conn.close()