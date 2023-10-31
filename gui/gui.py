import tkinter as tk
from tkinter import messagebox
import socket

# Server configuration
SERVER_HOST = '127.0.0.1'  # Replace with the server's IP address
SERVER_PORT = 12345  # Use the same port as the server

# Client socket setup
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_HOST, SERVER_PORT))

# Function to handle publish button click
def publish_file():
    local_name = local_name_entry.get()
    file_name = file_name_entry.get()
    command = f"publish {local_name} {file_name}"
    client_socket.send(command.encode())
    response = client_socket.recv(1024).decode()
    messagebox.showinfo("Publish Result", response)

# Create the main window
root = tk.Tk()
root.title("File Sharing Application")

# Create GUI components
tk.Label(root, text="Local Name:").pack()
local_name_entry = tk.Entry(root)
local_name_entry.pack()

tk.Label(root, text="File Name:").pack()
file_name_entry = tk.Entry(root)
file_name_entry.pack()

publish_button = tk.Button(root, text="Publish", command=publish_file)
publish_button.pack()

# Start the GUI main loop
root.mainloop()

# Close the client socket when the GUI is closed
client_socket.close()
