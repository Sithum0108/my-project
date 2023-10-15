import tkinter as tk

def register_student():
    name = name_entry.get()
    index_number = index_number_entry.get()
    department = department_entry.get()
    year = year_entry.get()

  

    result_label.config(text="Registration Successful")

# Create the main window
root = tk.Tk()
root.title("Student Registration")

# Create and place widgets
name_label = tk.Label(root, text="Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

indexl_number_label = tk.Label(root, text="Index Number:")
index_number_label.pack()
index_number_entry = tk.Entry(root)
index_number_entry.pack()

department_label = tk.Label(root, text="Department:")
department_label.pack()
department_entry = tk.Entry(root)
department_entry.pack()

year_label = tk.Label(root, text="Year:")
year_label.pack()
year_entry = tk.Entry(root)
year_entry.pack()

register_button = tk.Button(root, text="Register", command=register_student)
register_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

# Start the main loop
root.mainloop()
