# TODO: Add error handeling
import socket
import threading
import sys


def SendMessage(my_socket, name):
    my_socket.send("{} has entered the chat room.".format(name).encode())

    while True:
        send_message = input()
        my_socket.send("{0}: {1}".format(name, send_message).encode())

def RecieveMessage(my_socket):
    while True:
        recv_message = my_socket.recv(1024)

        if recv_message.decode() == '':
            print("Server disconnected")
            my_socket.close()
            sys.exit()

        print(recv_message.decode())


if __name__ == '__main__':
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = input("Host: ")
    port = int(input("Port: "))

    try:
        my_socket.connect((host, port))
    except socket.error:
        print("Unable to connect.")
        sys.exit(0)

    try:
        name = input("What's your name? ")

        t1 = threading.Thread(target=SendMessage, args=(my_socket, name), daemon=True)
        t2 = threading.Thread(target=RecieveMessage, args=(my_socket,), daemon=True)

        t1.start()
        t2.start()

        t2.join()
    except:
        print("\nDisconnected from: {}".format(port))
        my_socket.send("{} disconnected".format(name).encode())
        my_socket.close()

