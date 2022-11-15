import argparse
import socket

def connect_to_server(server_host: str, server_port: int) -> None:
    # Step1 - create a socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Step 2 - Connect to the server
    client_socket.connect((server_host, server_port))

    print(f'Connected from {client_socket.getsockname()} to {client_socket.getpeername()}')

    # Step 3 - Send data
    # TCP Segments
    client_socket.sendall(b'Hello World')

    # Step 4 - Receive Data
    data = client_socket.recv(1024)

    # Step 5 - Close socket
    print(f'Received {data}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Echo client')
    parser.add_argument('-H', '--host', help = 'Server Host', default='127.0.0.1', type=str)
    parser.add_argument('-p', '--port', help = 'Server Port', required=True, type=int)

    #Parse arguments
    args = parser.parse_args()
    host, port = args.host, args.port

    connect_to_server(host, port)