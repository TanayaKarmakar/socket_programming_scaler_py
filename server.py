import argparse
import socket

def run_server(server_host: str, server_port: int) -> None:
    # Step 1 - Create a socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Step 2 - bind to a host
    server_socket.bind((server_host, server_port))

    # Step 3 - Start Listen on port
    server_socket.listen() # Blocking call
    print(f'Listening on {server_port}')

    # Step 4 - Accept connection
    connection, address = server_socket.accept()
    print(f'Connection from {connection.getsockname()} to {connection.getpeername()}')

    # Step 5 - Receive Data
    data = server_socket.recv(1024)
    print(f'Received {data}')

    # Step 6 - Send data
    connection.sendall(data.upper())

    connection.close()
    server_socket.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Echo client')
    parser.add_argument('-H', '--host', help = 'Server Host', default='127.0.0.1', type=str)
    parser.add_argument('-p', '--port', help = 'Server Port', required=True, type=int)

    #Parse arguments
    args = parser.parse_args()
    host, port = args.host, args.port
    run_server(host, port)

