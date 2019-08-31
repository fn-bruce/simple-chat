import socket
import threading

clients = set()

def SendMessage(client, address):
    global clients

    while True:
        message = client.recv(1024)

        if message.decode() == '':
            print("{} disconnected".format(address))
            clients.remove(client)
            client.close()
            break

        for elem in clients:
            if elem != client:
                elem.send(message)


if __name__ == '__main__':
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '0.0.0.0'
    port = int(input("What port would you like to use? "))

    my_socket.bind((host, port))
    my_socket.listen(5)
    print("Listening...")

    try:
        while True:
            client, address = my_socket.accept()
            print("Connection established from: {}".format(address))

            if client not in clients:
                clients.add(client)

            threading.Thread(target=SendMessage, args=(client, address), daemon=True).start()
    except:
        print("\nServer disconnected")
        my_socket.close()
