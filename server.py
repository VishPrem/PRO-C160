import socket
from threading import Thread

IP_ADDRESS = "127.0.0.1"
PORT = 8050
SERVER = None
BUFFER_SIZE = 4096
clients = {}

def acceptConnections():
    global SERVER, clients

    while True:
        client, addr = SERVER.accept()
        print(client.addr)

def setup():
    global PORT, SERVER, IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS, PORT))

    SERVER.listen(100)

    print("\t\t\t\tSERVER IS WAITING FOR INCOMMING CONNECTIONS . . .")
    print("\n")

    acceptConnections()

setup_thread = Thread(target=setup)
setup_thread.start()