import mysql.connector
import tkinter as tk
from tkinter import messagebox

# Function to create table
def create_table(conn):
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Employee (
                empno INT PRIMARY KEY,
                EmpName VARCHAR(255),
                Salary FLOAT,
                DateOfJoining DATE)''')
    conn.commit()

# Function to insert a new record
def insert_record(conn, empno, empname, salary, doj):
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO Employee (empno, EmpName, Salary, DateOfJoining)
                VALUES (%s, %s, %s, %s)''', (empno, empname, salary, doj))
    conn.commit()

# Function to update a record
def update_record(conn, empno, field, new_value):
    cursor = conn.cursor()
    cursor.execute('''UPDATE Employee SET {}=%s WHERE empno=%s'''.format(field), (new_value, empno))
    conn.commit()

# Function to delete a record
def delete_record(conn, empno):
    cursor = conn.cursor()
    cursor.execute('''DELETE FROM Employee WHERE empno=%s''', (empno,))
    conn.commit()

def print_records(conn):
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM Employee''')
    records = cursor.fetchall()
    for record in records:
        print(record)
    print("\n")

def main():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="student"
    )
    create_table(conn)

    def on_insert():
        try:
            insert_record(conn, int(empno_entry.get()), empname_entry.get(), float(salary_entry.get()), doj_entry.get())
            messagebox.showinfo("Success", "Record inserted successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def on_update():
        try:
            update_record(conn, int(empno_update_entry.get()), field_update_entry.get(), new_value_update_entry.get())
            messagebox.showinfo("Success", "Record updated successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def on_delete():
        try:
            delete_record(conn, int(empno_delete_entry.get()))
            messagebox.showinfo("Success", "Record deleted successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def read_records():
        print_records(conn)

    # GUI Setup
    root = tk.Tk()
    root.title("Employee Database Management")
    root.geometry("450x550")

    # tk.Label(root, text="Employee Database Management", font=("Helvetica", 16)).pack(pady=10)
    # Insert Record Section
    tk.Label(root, text="Insert Record", font=("Helvetica", 12)).place(x=20, y=10)

    tk.Label(root, text="Employee Number:").place(x=20, y=40)
    empno_entry = tk.Entry(root)
    empno_entry.place(x=200, y=40)

    tk.Label(root, text="Employee Name:").place(x=20, y=70)
    empname_entry = tk.Entry(root)
    empname_entry.place(x=200, y=70)

    tk.Label(root, text="Salary:").place(x=20, y=100)
    salary_entry = tk.Entry(root)
    salary_entry.place(x=200, y=100)

    tk.Label(root, text="Date of Joining (YYYY-MM-DD):").place(x=20, y=130)
    doj_entry = tk.Entry(root)
    doj_entry.place(x=200, y=130)

    insert_button = tk.Button(root, text="Insert Record", command=on_insert, bg="lightblue", fg="black")
    insert_button.place(x=150, y=170)

    # Update Record Section
    tk.Label(root, text="Update Record", font=("Helvetica", 12)).place(x=20, y=220)

    tk.Label(root, text="Employee Number:").place(x=20, y=250)
    empno_update_entry = tk.Entry(root)
    empno_update_entry.place(x=200, y=250)

    tk.Label(root, text="Field to Update:").place(x=20, y=280)
    field_update_entry = tk.Entry(root)
    field_update_entry.place(x=200, y=280)

    tk.Label(root, text="New Value:").place(x=20, y=310)
    new_value_update_entry = tk.Entry(root)
    new_value_update_entry.place(x=200, y=310)

    update_button = tk.Button(root, text="Update Record", command=on_update, bg="lightgreen", fg="black")
    update_button.place(x=150, y=350)

    # Delete Record Section
    tk.Label(root, text="Delete Record", font=("Helvetica", 12)).place(x=20, y=400)

    tk.Label(root, text="Employee Number:").place(x=20, y=430)
    empno_delete_entry = tk.Entry(root)
    empno_delete_entry.place(x=200, y=430)

    delete_button = tk.Button(root, text="Delete Record", command=on_delete, bg="lightcoral", fg="black")
    delete_button.place(x=150, y=470)

    read_data_button = tk.Button(root, text="Print Records", command=read_records, bg="lightcoral", fg="black")
    read_data_button.place(x=150, y=520)

    root.mainloop()

if __name__ == "__main__":
    main()
