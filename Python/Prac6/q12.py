import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
# Establishing a MySQL connection
mycon = mysql.connector.connect(host="localhost", username='root', password='root', database="student")
# Checking the connection status
if mycon:
    print("Connection Successful")
else:
    print("Connection Unsuccessful")
# Creating a cursor
mycursor = mycon.cursor()

def add_record():
    name = name_var.get()
    pid = int(pid_entry.get())

    try:
        mycursor.execute("INSERT INTO Student VALUES (%s, %s)", (name, pid))
        mycon.commit()
        print("Record successfully added")
    except Exception:
        print("Something went wrong!")
   
# Function to read records
def read_record():
    mycursor.execute("SELECT * FROM Student")
    data = mycursor.fetchall()
    for row in data:
        print(row)

def update_record():
    name = name_var.get()
    pid = int(pid_entry.get())
    try:
        mycursor.execute("UPDATE Student SET Pid = %s WHERE Name = %s", (pid, name))
        mycon.commit()
        print("PID of the given name has been successfully updated")

    except Exception:
        print("Something went wrong")

# Function to delete a record
def delete_record():
    name = name_var.get()
    pid = int(pid_entry.get())
    try:
        mycursor.execute("DELETE FROM Student WHERE Name %s AND Pid = %s", (name, pid))
        mycon.commit()
        print("Data for the student with the given name and PID has been successfully deleted")

    except Exception:
        print("something went wrong!")

# Creating the main window
window = tk.Tk()
window.geometry("400x450+600+200")
window.configure (bg="grey")
window.title("Signup Form")

# Creating and placing labels, buttons, and entry widgets
tk. Label (text='Registration Form', height="2", bg='yellow', font=("Calibri", 16)).pack()

name_label = tk.Label(window, text="Name", bg='grey', font=("Calibri", 20))
name_label.place(x=20, y=75, width=100)
name_var = tk.StringVar()
name_entry = ttk.Entry(window, width=30, textvariable=name_var)
name_entry.place(x=125, y=85)

pid_label = tk.Label(window, text="PID", bg='grey',font=("Calibri", 20))
pid_label.place(x=20, y=150, width=100)
pid_var = tk.StringVar()
pid_entry = ttk.Entry(window, width=30, textvariable=pid_var)
pid_entry.place(x=125, y=160)

add_button = tk. Button(window, text="Add Record", bg='red', font=('Calibri', 12, 'bold'),justify="center", command=add_record)
add_button.place (x=150, y=200)
read_button = tk.Button(window, text="Read Record", bg='red', font=('Calibri', 12, 'bold'),justify="center", command=read_record)
read_button.place (x=150, y=250)
update_button = tk.Button(window, text="Update Record", bg='red', font=('Calibri', 12, 'bold'),justify="center", command=update_record)
                         
update_button.place(x=150, y=300)
delete_button = tk.Button(window, text="Delete Record", bg='red', font=('Calibri', 12, 'bold'),justify="center", command=delete_record)
delete_button.place(x=150, y=350)
# Running the main loop
window.mainloop()
