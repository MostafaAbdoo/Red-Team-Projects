# referance : https://dev.to/rajatrajputdev/tcp-chatroom-in-python-5g66
import socket , threading # for communication and multithreading

# our server data
host = '127.0.0.1' # localhost address
port = 4444 # free port of your choice

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # 1st parameter indicates we are using an internet socket not unix (local socket)
# and the socend parameter indicates we are using TCP protocol
server.bind((host,port))
server.listen() # start listening for incoming connection

# store clinets data
clients = []
nicknames = []

# sending messages to all clients
def broadcast(message):
    for client in clients:
        client.sendall(message)

# to handle the client while the connection is open until the client closes the connection
def handle(client):
    while True :
        try:
            message = client.recv(1024)
            broadcast(message)

        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname=nicknames[index]
            broadcast('{} left!'.format(nickname).encode('ascii'))
            nicknames.remove(nickname)
            break

# receiving function
def receive():
    while True:
        # Accept Connection
        client, address = server.accept()
        print("Connected with {}".format(str(address)))

        # Request And Store Nickname
        client.sendall('NAME'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        # Print And Broadcast Nickname
        print("Nickname is {}".format(nickname))
        broadcast("{} joined!".format(nickname).encode('ascii'))
        client.sendall('Connected to server!'.encode('ascii'))

        # Start Handling Thread For Client
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

receive()
