"""
vsdev. / Vladislav Slugin / ver. 24.07.2024
It implements a simple password manager with encryption using the Fernet symmetric encryption method.
"""

import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter.scrolledtext import ScrolledText
from cryptography.fernet import Fernet, InvalidToken
import os
import webbrowser

# Generate a key and save it to a file if it doesn't exist
def generate_key():
    if not os.path.exists('key.key'):
        key = Fernet.generate_key()
        with open('key.key', 'wb') as key_file:
            key_file.write(key)

# Load the key from a file
def load_key():
    with open('key.key', 'rb') as key_file:
        return key_file.read()

# Encrypt the password
def encrypt_password(password, cipher):
    return cipher.encrypt(password.encode()).decode()

# Decrypt the password
def decrypt_password(encrypted_password, cipher):
    try:
        return cipher.decrypt(encrypted_password.encode()).decode()
    except InvalidToken:
        return None

# Save the password
def save_password():
    site = site_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    comment = comment_entry.get("1.0", tk.END).strip()
    if site and username and password:
        encrypted_password = encrypt_password(password, cipher)
        with open('passwords.txt', 'a') as f:
            f.write(f"{site}:{username}:{encrypted_password}:{comment}\n")
        site_entry.delete(0, tk.END)
        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
        comment_entry.delete("1.0", tk.END)
        load_passwords()
        messagebox.showinfo("Info", "Password saved successfully!")

# Load the passwords
def load_passwords():
    listbox.delete(0, tk.END)
    if os.path.exists('passwords.txt'):
        with open('passwords.txt', 'r') as f:
            passwords = f.readlines()
        for entry in passwords:
            parts = entry.strip().split(':', 3)
            if len(parts) == 4:
                site, username, encrypted_password, comment = parts
            else:
                site, username, encrypted_password = parts
                comment = ""
            decrypted_password = decrypt_password(encrypted_password, cipher)
            if decrypted_password is not None:
                listbox.insert(tk.END, f"{site} | {username} | {'*' * len(decrypted_password)} | {comment}")

# Copy the password to the clipboard
def copy_password():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        with open('passwords.txt', 'r') as f:
            passwords = f.readlines()
        parts = passwords[index].strip().split(':', 3)
        site, username, encrypted_password, comment = parts[0], parts[1], parts[2], parts[3] if len(parts) == 4 else ""
        decrypted_password = decrypt_password(encrypted_password, cipher)
        if decrypted_password is not None:
            root.clipboard_clear()
            root.clipboard_append(decrypted_password)
            messagebox.showinfo("Info", "Password copied to clipboard!")

# Open the website
def open_website():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        with open('passwords.txt', 'r') as f:
            passwords = f.readlines()
        parts = passwords[index].strip().split(':', 3)
        site = parts[0]
        webbrowser.open(f"http://{site}")

# Delete the password
def delete_password():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        with open('passwords.txt', 'r') as f:
            passwords = f.readlines()
        del passwords[index]
        with open('passwords.txt', 'w') as f:
            f.writelines(passwords)
        load_passwords()
        messagebox.showinfo("Info", "Password deleted successfully!")

# Create the main window
root = tk.Tk()
root.title("SecurePass Manager by vsdev. / Vladislav Slugin / ver. 24.07.2024")

# Create the key and cipher
generate_key()
key = load_key()
cipher = Fernet(key)

# Headers for columns
headers = tk.Label(root, text="Website | Username | Password | Comment", font=('Helvetica', 9))
headers.pack()

# Interface
frame = tk.Frame(root)
frame.pack(pady=6)


listbox = tk.Listbox(frame, width=100)
listbox.pack()

load_button = tk.Button(root, text="Load Passwords", command=load_passwords)
load_button.pack(side=tk.LEFT, padx=10)

copy_button = tk.Button(root, text="Copy Password", command=copy_password)
copy_button.pack(side=tk.LEFT, padx=10)

open_button = tk.Button(root, text="Open Website", command=open_website)
open_button.pack(side=tk.LEFT, padx=10)

delete_button = tk.Button(root, text="Delete Password", command=delete_password)
delete_button.pack(side=tk.LEFT, padx=10)

site_label = tk.Label(root, text="Website:")
site_label.pack()

site_entry = tk.Entry(root, width=50)
site_entry.pack()

username_label = tk.Label(root, text="Username:")
username_label.pack()

username_entry = tk.Entry(root, width=50)
username_entry.pack()

password_label = tk.Label(root, text="Password:")
password_label.pack()

password_entry = tk.Entry(root, show='*', width=50)
password_entry.pack()

comment_label = tk.Label(root, text="Comment:")
comment_label.pack()

comment_entry = ScrolledText(root, height=4, width=50)
comment_entry.pack()

save_button = tk.Button(root, text="Save Password", command=save_password)
save_button.pack(pady=10)

# Start the application
load_passwords()
root.mainloop()
