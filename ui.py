import tkinter as tk
from tkinter import messagebox

def login():
    username = entry_username.get()
    password = entry_password.get()

    # Check if username and password are correct (dummy check)
    if username == "admin" and password == "password":
        messagebox.showinfo("Login Successful", "Welcome, Admin!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Create the main window
root = tk.Tk()
root.title("Discussion Forum Login")
root.geometry("400x200")  # Set window size

# Set background color
root.configure(bg="#D3E1E8")

# Create padding rows and columns
for i in range(3):
    root.rowconfigure(i, weight=1)
for i in range(2):
    root.columnconfigure(i, weight=1)

# Username label and entry
label_username = tk.Label(root, text="Username:", bg="#D3E1E8")
label_username.grid(row=1, column=0, pady=5, sticky="e")  # Align label to the right
entry_username = tk.Entry(root)
entry_username.grid(row=1, column=1, pady=5, sticky="w")  # Align entry to the left

# Password label and entry
label_password = tk.Label(root, text="Password:", bg="#D3E1E8")
label_password.grid(row=2, column=0, pady=5, sticky="e")  # Align label to the right
entry_password = tk.Entry(root, show="*")
entry_password.grid(row=2, column=1, pady=5, sticky="w")  # Align entry to the left

# Login button
button_login = tk.Button(root, text="Login", command=login, bg="#001F3F", fg="white")
button_login.grid(row=3, column=0, columnspan=2, pady=10)

# Run the Tkinter event loop
root.mainloop()
