import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="RooT#123",
    database="student_db"
)

cursor = conn.cursor()

roll_no = input("Enter roll number to update: ")
new_marks = int(input("Enter new marks: "))

# update result automatically
result = "Pass" if new_marks >= 40 else "Fail"

query = """
UPDATE students
SET marks = %s, result = %s
WHERE roll_no = %s
"""

cursor.execute(query, (new_marks, result, roll_no))
conn.commit()

if cursor.rowcount > 0:
    print("Student updated successfully")
else:
    print("Student not found")

cursor.close()
conn.close()