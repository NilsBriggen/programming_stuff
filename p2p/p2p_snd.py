import socket, time

#send file to server
def send_file(file_name, ip, port):
    with open(file_name, 'rb') as f:
        with socket.create_connection((ip, port)) as sock:
            while True:
                data = f.read(1024)
                if not data:
                    break
                sock.sendall(data)
            print("File sent")

#send message to server
def send_message(message, ip, port):
    with socket.create_connection((ip, port)) as sock:
        sock.sendall(message.encode())
        print("Message sent")

def start_client(port):
    time.sleep(1)
    ip = input("Enter Ip and Port seperated by a space: ")
    variant = input("Send file or message? (f/m): ").lower()
    if variant == "m":
        message = input("Enter message: ")
        send_message(message, ip, port)
    elif variant == "f":
        file_name = input("Enter path to file: ")
        send_file(file_name, ip, port)
    else:
        print("Invalid variant")