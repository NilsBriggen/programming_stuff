import socket

def start_server(port):
    #Get the host's local ip. This is the complicated verison
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()

    print(f"Connect with Ip: {ip} and Port: {port}")

    #receive data from server
    with socket.create_server((ip, port)) as server:
        while True:
            client, address = server.accept()
            print(f"Connection from {address}")
            data = client.recv(1024)
            print(f"Received {data.decode()}")
            client.send(b"Hello from server")
            client.close()
start_server(56465)