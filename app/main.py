import socket  # noqa: F401


def main():

    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    print("HTTP Server is running and listening for connection on port 4221")

    try:
        while True:
            client_connection, client_address = server_socket.accept()
            print(f"Connection established with {client_address}")

            request = client_connection.recv(1024).decode('utf-8')
            if request:
                print(f"Received request:\n{request}")

                method, target = request.splitlines().split()[0:2]

                if method == "GET" and target == "/":
                    response = "HTTP/1.1 200 OK\r\n\r\n"
                else:
                    response = "HTTP/1.1 404 Not Found\r\n\r\n"

            else:
                response = "HTTP/1.1 400 Bad Request\r\n\r\n"
                print("No request received.")

            client_connection.sendall(response.encode('utf-8'))

    except KeyboardInterrupt:
        print("\nServer is shutting down...")
    finally:
        server_socket.close()
        print("Server shut down.")


if __name__ == "__main__":
    main()
