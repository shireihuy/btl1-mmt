import socket

# Server configuration
SERVER_HOST = '127.0.0.1'  # Replace with the server's IP address
SERVER_PORT = 12345  # Use the same port as the server

def publish_file(client_socket):
    local_name, file_name = input("Enter local file name and desired file name (lname fname): ").split()
    command = f"publish {local_name} {file_name}"
    client_socket.send(command.encode())
    print(client_socket.recv(1024).decode())

def fetch_file(client_socket):
    file_name = input("Enter the file name to fetch: ")
    command = f"fetch {file_name}"
    client_socket.send(command.encode())
    print(client_socket.recv(1024).decode())

def discover_files(client_socket):
    host_name = input("Enter the hostname to discover files: ")
    command = f"discover {host_name}"
    client_socket.send(command.encode())
    print(client_socket.recv(1024).decode())

def ping_host(client_socket):
    host_name = input("Enter the hostname to ping: ")
    command = f"ping {host_name}"
    client_socket.send(command.encode())
    print(client_socket.recv(1024).decode())

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_HOST, SERVER_PORT))

    # Receive the welcome message from the server
    print(client_socket.recv(1024).decode())

    while True:
        # Get user command
        command = input("Enter a command (publish/fetch/discover/ping/exit): ")

        # Send the appropriate command to the server
        if command == "publish":
            publish_file(client_socket)
        elif command == "fetch":
            fetch_file(client_socket)
        elif command == "discover":
            discover_files(client_socket)
        elif command == "ping":
            ping_host(client_socket)
        elif command == "exit":
            client_socket.close()
            print("Goodbye!")
            break
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
