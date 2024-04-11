import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def submit():
    name = name_var.get()
    address = address_var.get()
    email = email_var.get()
    contact = contact_var.get()
    if not name or not address or not email or not contact or not select_year.get() or \
        not (cricket_var.get() or football_var.get() or tennis_var.get()) or not country_val.get() or \
           not age_select.get():
        messagebox.showerror("Error", "Please Enter All Fields!!")
    
    elif len(contact) != 10 or not contact.isdigit():
        messagebox.showerror("Error", "Please Enter a 10 Digit Numeric Contact Number")

    elif '@' not in email:
        messagebox.showerror("Error", "Please Enter a Valid Email Address")
    
    else:
        messagebox.showinfo("Thank you!!", "Thank you For Your Response")

root = tk.Tk()
root.geometry("500x600")
root.resizable(False, False)
root.title('Registration Form')

# Styles
style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 12))
style.configure("TEntry", font=("Helvetica", 12))

# Name
name_label = ttk.Label(root, text="Name:")
name_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
name_var = tk.StringVar()
e_name = ttk.Entry(root, textvariable=name_var, width=30)
e_name.grid(row=0, column=1, padx=10, pady=10)

# Address
address_label = ttk.Label(root, text="Address:")
address_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
address_var = tk.StringVar()
e_address = ttk.Entry(root, textvariable=address_var, width=30)
e_address.grid(row=1, column=1, padx=10, pady=10)

# Email
email_label = ttk.Label(root, text="Email:")
email_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")
email_var = tk.StringVar()
e_email = ttk.Entry(root, textvariable=email_var, width=30)
e_email.grid(row=2, column=1, padx=10, pady=10)

# Contact
contact_label = ttk.Label(root, text="Contact:")
contact_label.grid(row=3, column=0, padx=10, pady=10, sticky="e")
contact_var = tk.StringVar()
e_contact = ttk.Entry(root, textvariable=contact_var, width=30)
e_contact.grid(row=3, column=1, padx=10, pady=10)

# Class
class_year_label = ttk.Label(root, text="Class:")
class_year_label.grid(row=4, column=0, padx=10, pady=10, sticky="e")
select_year = tk.StringVar()
class_years = ["FE", "SE", "TE", "BE"]
class_year_frame = ttk.Frame(root)
class_year_frame.grid(row=4, column=1, columnspan=2, padx=10, pady=10)
for i, year in enumerate(class_years):
    ttk.Radiobutton(class_year_frame, text=year, value=year, variable=select_year).grid(row=0, column=i, padx=5, pady=5)

# Sports
sports_label = ttk.Label(root, text="Sports:")
sports_label.grid(row=5, column=0, padx=10, pady=10, sticky="e") 
cricket_var = tk.IntVar()
football_var = tk.IntVar()
tennis_var = tk.IntVar()
ttk.Checkbutton(root, text="Cricket", variable=cricket_var).grid(row=5, column=1, padx=10, pady=10)
ttk.Checkbutton(root, text="Football", variable=football_var).grid(row=5, column=2, padx=10, pady=10)
ttk.Checkbutton(root, text="Tennis", variable=tennis_var).grid(row=5, column=3, padx=10, pady=10)

# Country
country_label = ttk.Label(root, text="Country:")
country_label.grid(row=6, column=0, padx=10, pady=10, sticky="e") 
country_val = tk.StringVar()
countries = ttk.Combobox(root, textvariable=country_val, state='readonly', width=27)
countries['values'] = ('India', 'USA', 'China', 'Russia', 'Australia', 'UK', 'Germany')
countries.current(0)
countries.grid(row=6, column=1, columnspan=3, padx=10, pady=10)

# Age
age_label = ttk.Label(root, text="Age:")
age_label.grid(row=7, column=0, padx=10, pady=10, sticky="e") 
age_select = ttk.Spinbox(root, from_=0, to=100, width=27)
age_select.grid(row=7, column=1, columnspan=3, padx=10, pady=10)

# Submit
submit_button = ttk.Button(root, text="Submit", command=submit)
submit_button.grid(row=8, column=0, columnspan=4, pady=20)

root.mainloop()
