#This is the main window code of the login

import tkinter as tk

def validate_login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "your_username" and password == "your_password":
        result_label.config(text="Login successful")
    else:
        result_label.config(text="Invalid username or password")

root = tk.Tk()
root.title("Main Window")

username_label = tk.Label(root, text="Username:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")  # Use 'show' to hide the password
password_entry.pack()

login_button = tk.Button(root, text="Login", command=validate_login)
login_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()

#Added by friend 
