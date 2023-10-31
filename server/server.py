import socket
import threading

# Server configuration
SERVER_HOST = '127.0.0.1'  # Listen on all available interfaces
SERVER_PORT = 12345  # Choose any available port

# Dictionary to store available files and their owners
files = {}

# Function to handle client connections
def handle_client(client_socket, address):
    client_socket.send("Welcome to the File Sharing Server!".encode())

    while True:
        command = client_socket.recv(1024).decode()

        if command.startswith("publish"):
            # Handle file publishing: publish lname fname
            parts = command.split()
            if len(parts) == 3:
                local_name, file_name = parts[1], parts[2]
                files[file_name] = local_name
                client_socket.send(f"File '{file_name}' published successfully.".encode())
            else:
                client_socket.send("Invalid 'publish' command format. Use: publish lname fname".encode())

        elif command.startswith("fetch"):
            # Handle file fetching: fetch fname
            file_name = command.split()[1]
            if file_name in files:
                client_socket.send(f"File '{file_name}' is available from {files[file_name]}.".encode())
            else:
                client_socket.send(f"File '{file_name}' not found.".encode())

        elif command.startswith("discover"):
            # Handle file discovery: discover hostname
            hostname = command.split()[1]
            client_files = [file for file, owner in files.items() if owner == hostname]
            if client_files:
                client_socket.send(f"Files available from {hostname}: {', '.join(client_files)}".encode())
            else:
                client_socket.send(f"No files found from {hostname}.".encode())

        elif command.startswith("ping"):
            # Handle live check: ping hostname
            hostname = command.split()[1]
            if hostname in [owner for owner in files.values()]:
                client_socket.send(f"{hostname} is live.".encode())
            else:
                client_socket.send(f"{hostname} is not found.".encode())

        else:
            client_socket.send("Invalid command. Please try again.".encode())

        if not command:
            print(f"[*] Connection closed by {address[0]}:{address[1]}")
            break

    client_socket.close()

# Main server function
def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((SERVER_HOST, SERVER_PORT))
    server_socket.listen(5)
    print(f"[*] Listening on {SERVER_HOST}:{SERVER_PORT}")

    while True:
        client_socket, address = server_socket.accept()
        print(f"[*] Accepted connection from {address[0]}:{address[1]}")

        # Create a new thread to handle client
        client_handler = threading.Thread(target=handle_client, args=(client_socket, address))
        client_handler.start()

if __name__ == "__main__":
    main()
