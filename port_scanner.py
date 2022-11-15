import socket
import argparse
from colorama import Fore, init

def is_port_open(host: str, port: int) -> bool:
    '''
        Try to connect to server
        If it can connect, port is open
    '''

    # Step1: Create a socket
    # Address family
    client_socket = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM #TCP
    )

    # Step2: Create a connection
    try:
        client_socket.connect((host, port))
    except:
        return False
    else:
        return True


if __name__ == '__main__':
    init()
    parser = argparse.ArgumentParser(description='Port Scanner')
    parser.add_argument('-H', '--host', help = 'Host to scan', required= True, type = str)
    parser.add_argument('-s', '--start', help = 'Starting port', default=1, type = int)
    parser.add_argument('-e', '--end', help = 'Ending port', default=1024, type = int)

    args = parser.parse_args()
    host, start, end = args.host, args.start, args.end

    for port in range(start, end):
        is_open = is_port_open(host, port)
        if not is_open:
            print(f'{Fore.RED} Port {port} is closed {Fore.RESET}')
            continue
        print(f'{Fore.GREEN} Port {port} is open {Fore.RESET}')


# python port_scanner.py --host 127.0.0.1 --start 6000 --end 7000

