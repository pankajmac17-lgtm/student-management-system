import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="RooT#123",
        database="student_db"
    )

def add_student():
    conn = connect_db()
    cursor = conn.cursor()

    name = input("Enter name: ")
    roll_no = input("Enter roll no: ")
    marks = int(input("Enter marks: "))

    result = "Pass" if marks >= 40 else "Fail"

    query = "INSERT INTO students (name, roll_no, marks, result) VALUES (%s, %s, %s, %s)"
    
    try:
        cursor.execute(query, (name, roll_no, marks, result))
        conn.commit()
        print("Student added successfully")
    except:
        print("Error: Roll number might already exist")

    cursor.close()
    conn.close()

def view_student():
    conn = connect_db()
    cursor = conn.cursor()

    roll_no = input("Enter roll no: ")

    cursor.execute("SELECT * FROM students WHERE roll_no = %s", (roll_no,))
    results = cursor.fetchall()

    if results:
        for row in results:
            print(row)
    else:
        print("No student found")

    cursor.close()
    conn.close()

def update_student():
    conn = connect_db()
    cursor = conn.cursor()

    roll_no = input("Enter roll no: ")
    marks = int(input("Enter new marks: "))

    result = "Pass" if marks >= 40 else "Fail"

    query = "UPDATE students SET marks=%s, result=%s WHERE roll_no=%s"
    cursor.execute(query, (marks, result, roll_no))
    conn.commit()

    if cursor.rowcount > 0:
        print("Updated successfully")
    else:
        print("Student not found")

    cursor.close()
    conn.close()

def delete_student():
    conn = connect_db()
    cursor = conn.cursor()

    roll_no = input("Enter roll no: ")

    cursor.execute("DELETE FROM students WHERE roll_no=%s", (roll_no,))
    conn.commit()

    if cursor.rowcount > 0:
        print("Deleted successfully")
    else:
        print("Student not found")

    cursor.close()
    conn.close()

# main menu loop
while True:
    print("\n1. Add Student")
    print("2. View Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_student()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice")