""" SlowLoris.py - A simple implementation of the lightweight DOS attack. """

""" Ethan Ruchotzke """
""" CprE 530 - Final Paper """
""" Fall 2021 """

from socket import *


with socket(AF_INET, SOCK_STREAM) as sock:
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.connect(("127.0.0.1", 8080))

    # Send a request
    request = f"GET /thread HTTP/1.1\r\n\r\n".encode()
    sock.sendall(request)

    # Receive response
    response = ""
    while True:
        recv = sock.recv(1024)
        if recv == b'':
            break
        response += recv.decode()
    print(response)
