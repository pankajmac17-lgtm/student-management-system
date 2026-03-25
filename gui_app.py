import tkinter as tk
from tkinter import messagebox
import mysql.connector

# DB connection
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="RooT#123",  # 🔴 change this
        database="student_db"
    )

# ADD
def add_student():
    name = entry_name.get()
    roll_no = entry_roll.get()
    marks = entry_marks.get()

    if not name or not roll_no or not marks:
        messagebox.showerror("Error", "All fields required")
        return

    try:
        marks = int(marks)
    except:
        messagebox.showerror("Error", "Marks must be number")
        return

    result = "Pass" if marks >= 40 else "Fail"

    try:
        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO students (name, roll_no, marks, result) VALUES (%s, %s, %s, %s)",
            (name, roll_no, marks, result)
        )
        conn.commit()

        messagebox.showinfo("Success", "Student added successfully")

        entry_name.delete(0, tk.END)
        entry_roll.delete(0, tk.END)
        entry_marks.delete(0, tk.END)

    except mysql.connector.IntegrityError:
        messagebox.showerror("Error", "Roll number already exists")

    finally:
        cursor.close()
        conn.close()


# VIEW
def view_student():
    roll_no = entry_roll.get()

    if not roll_no:
        messagebox.showerror("Error", "Enter roll number")
        return

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students WHERE roll_no = %s", (roll_no,))
    result = cursor.fetchone()

    cursor.close()
    conn.close()

    if result:
        info = f"Name: {result[1]}\nRoll: {result[2]}\nMarks: {result[3]}\nResult: {result[4]}"
        messagebox.showinfo("Student Details", info)
    else:
        messagebox.showerror("Error", "Student not found")


# UPDATE
def update_student():
    roll_no = entry_roll.get()
    marks = entry_marks.get()

    if not roll_no or not marks:
        messagebox.showerror("Error", "Enter roll no and marks")
        return

    try:
        marks = int(marks)
    except:
        messagebox.showerror("Error", "Marks must be number")
        return

    result = "Pass" if marks >= 40 else "Fail"

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE students SET marks=%s, result=%s WHERE roll_no=%s",
        (marks, result, roll_no)
    )
    conn.commit()

    if cursor.rowcount > 0:
        messagebox.showinfo("Success", "Updated successfully")
    else:
        messagebox.showerror("Error", "Student not found")

    cursor.close()
    conn.close()


# DELETE
def delete_student():
    roll_no = entry_roll.get()

    if not roll_no:
        messagebox.showerror("Error", "Enter roll number")
        return

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM students WHERE roll_no=%s", (roll_no,))
    conn.commit()

    if cursor.rowcount > 0:
        messagebox.showinfo("Success", "Deleted successfully")
    else:
        messagebox.showerror("Error", "Student not found")

    cursor.close()
    conn.close()


# UI
root = tk.Tk()
root.title("Student Management System")
root.geometry("400x450")

tk.Label(root, text="Student Management System", font=("Arial", 14)).pack(pady=10)

tk.Label(root, text="Name").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Roll No").pack()
entry_roll = tk.Entry(root)
entry_roll.pack()

tk.Label(root, text="Marks").pack()
entry_marks = tk.Entry(root)
entry_marks.pack()

tk.Button(root, text="Add Student", command=add_student).pack(pady=5)
tk.Button(root, text="View Student", command=view_student).pack(pady=5)
tk.Button(root, text="Update Student", command=update_student).pack(pady=5)
tk.Button(root, text="Delete Student", command=delete_student).pack(pady=5)

tk.Button(root, text="Exit", command=root.quit).pack(pady=15)

root.mainloop()