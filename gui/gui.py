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

# Function to handle fetch button click
def fetch_file():
    file_name = fetch_entry.get()
    command = f"fetch {file_name}"
    client_socket.send(command.encode())
    response = client_socket.recv(1024).decode()
    messagebox.showinfo("Fetch Result", response)

# Function to handle discover button click
def discover_files():
    hostname = discover_entry.get()
    command = f"discover {hostname}"
    client_socket.send(command.encode())
    response = client_socket.recv(1024).decode()
    messagebox.showinfo("Discover Result", response)

# Function to handle ping button click
def ping_host():
    hostname = ping_entry.get()
    command = f"ping {hostname}"
    client_socket.send(command.encode())
    response = client_socket.recv(1024).decode()
    messagebox.showinfo("Ping Result", response)

# Function to handle exit button click
def exit_application():
    client_socket.close()
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("File Sharing Application")

# Create GUI components for publish
tk.Label(root, text="Local Name:").pack()
local_name_entry = tk.Entry(root)
local_name_entry.pack()

tk.Label(root, text="File Name:").pack()
file_name_entry = tk.Entry(root)
file_name_entry.pack()

publish_button = tk.Button(root, text="Publish", command=publish_file)
publish_button.pack()

# Create GUI components for fetch
tk.Label(root, text="File Name to Fetch:").pack()
fetch_entry = tk.Entry(root)
fetch_entry.pack()

fetch_button = tk.Button(root, text="Fetch", command=fetch_file)
fetch_button.pack()

# Create GUI components for discover
tk.Label(root, text="Hostname to Discover:").pack()
discover_entry = tk.Entry(root)
discover_entry.pack()

discover_button = tk.Button(root, text="Discover", command=discover_files)
discover_button.pack()

# Create GUI components for ping
tk.Label(root, text="Hostname to Ping:").pack()
ping_entry = tk.Entry(root)
ping_entry.pack()

ping_button = tk.Button(root, text="Ping", command=ping_host)
ping_button.pack()

# Create exit button
exit_button = tk.Button(root, text="Exit", command=exit_application)
exit_button.pack()

# Start the GUI main loop
root.mainloop()
