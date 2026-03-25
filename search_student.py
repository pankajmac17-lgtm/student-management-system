import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="RooT#123",
    database="student_db"
)

cursor = conn.cursor()

# input from user
roll_no = input("Enter roll number to search: ")

# query
query = "SELECT * FROM students WHERE roll_no = %s"
cursor.execute(query, (roll_no,))

results = cursor.fetchall()

# check if data exists
if results:
    print("Students Found:")
    for row in results:
        print(row)
else:
    print("No student found")

cursor.close()
conn.close()