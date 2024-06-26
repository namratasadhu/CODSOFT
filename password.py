import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length):
    # Define the character set to include in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password of the specified length
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def generate_and_display_password():
    try:
        # Get the length input from the user
        password_length = int(length_entry.get())
        
        if password_length < 1:
            raise ValueError("Password length must be at least 1")
        
        # Generate the password
        global generated_password
        generated_password = generate_password(password_length)
        
        # Display the password
        result_label.config(text=f"Generated Password: {generated_password}")
    except ValueError as ve:
        messagebox.showerror("Invalid Input", f"Error: {ve}")

def accept_password():
    if generated_password:
        messagebox.showinfo("Password Accepted", f"Your password is: {generated_password}")
    else:
        messagebox.showwarning("No Password", "Please generate a password first.")

def reset():
    length_entry.delete(0, tk.END)
    result_label.config(text="")
    global generated_password
    generated_password = ""

# Initialize the generated password variable
generated_password = ""

# Create the main window
root = tk.Tk()
root.geometry("500x300")
root.configure(background="light green")
root.title("Random Password Generator")

# Create and place the widgets
tk.Label(root, text="Enter the desired password length:").pack(pady=10)
length_entry = tk.Entry(root)
#length_entry.grid(columnspan=4)
length_entry.pack(pady=5,)

generate_button = tk.Button(root, text="Generate Password", command=generate_and_display_password)
generate_button.pack(pady=10)

accept_button = tk.Button(root, text="Accept", command=accept_password)
accept_button.pack(pady=5)

reset_button = tk.Button(root, text="Reset", command=reset)
reset_button.pack(pady=5)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Run the application
root.mainloop()
