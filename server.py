<<<<<<< HEAD
import socket  
import threading      #Import modules
import time
#################

#### Declaring variables ####
HEADER = 64 #Header in bytes
PORT = 15200 #Port number
SERVER = socket.gethostbyname(socket.gethostname()) #Gets device's Ipv4 address
ADDR = (SERVER, PORT)
FORMAT = 'utf-8' #Format protocol set to 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
clients = []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
for i in range(25): #Loops following commands x25 times
    try:
        server.bind(ADDR) #Creating actual server
    except Exception:
        print('[SERVER-SIDE ERROR] Couldn\'t start SERVER : ' + "x" + i)
        time.sleep(1)
################# Ta mere la pute. Pk tu regardes ?   

def broadcast(full_message): #Function that broadcasts messages to all clients
    for client in clients: #Iterate through all clients
        client.send(full_message.encode(FORMAT)) #Encode, using utf-8 protocol, and then send message to client
        
def handle_client(client, addr, nickname): #Manages client data
    print(f"[NEW CONNECTION] {addr} connected under username : {nickname}.")
    connected = True #Sets connected to TRUE
    clients.append(client)
    try:
        while connected: #While connected is TRUE, it will execute following code:
            msg_length = client.recv(HEADER).decode(FORMAT) #Recieves encoded message
            if msg_length:
                msg_length = int(msg_length)                     #Decodes message sent by client
                msg = client.recv(msg_length).decode(FORMAT) 
                if msg == DISCONNECT_MESSAGE: #if user sends 'DISCONNECT_MESSAGE'
                    clients.remove(client)   #Remove client from 'clients' list
                    connected = False #Sets 'connected' variable to False
                    
                broadcast(f"[{nickname}] {msg}") #Broadcasts to all clients the full message using 'broadcats()' function
                
        client.close() #Close connection between server and client if connected == False
    except Exception: #On exception raise, following code is executed
        client.send("[SERVER-SIDE] An error has occured".encode(FORMAT)) #If an error occurs this message is sent to the client that raised the error.

def start():
    
    server.listen() #Listen to all connections
    print(f"[LISTENNING] Server is listennig on : {socket.gethostname()} : {SERVER}") #Prints out DEBUG info
    while True: #Always Loop
        client, addr = server.accept() #Stores ever new client's Ip address and port number
        client.send("GET_username".encode(FORMAT)) #Sends 'GET_username' request to client
        nickname = client.recv(2048).decode(FORMAT) #Stores client's 'GET_username' response
        thread = threading.Thread(target=handle_client, args=(client, addr, nickname))
        thread.start() #Runs a new thread : 'handle_client()'
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}") #Prints out active connections count

=======
import socket  
import threading      #Import modules
import time
#################

#### Declaring variables ####
HEADER = 64 #Header in bytes
PORT = 15200 #Port number
SERVER = socket.gethostbyname(socket.gethostname()) #Gets device's Ipv4 address
ADDR = (SERVER, PORT)
FORMAT = 'utf-8' #Format protocol set to 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
clients = []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
for i in range(25): #Loops following commands x25 times
    try:
        server.bind(ADDR) #Creating actual server
    except Exception:
        print('[SERVER-SIDE ERROR] Couldn\'t start SERVER : ' + "x" + i)
        time.sleep(1)
################# Ta mere la pute. Pk tu regardes ?   

def broadcast(full_message): #Function that broadcasts messages to all clients
    for client in clients: #Iterate through all clients
        client.send(full_message.encode(FORMAT)) #Encode, using utf-8 protocol, and then send message to client
        
def handle_client(client, addr, nickname): #Manages client data
    print(f"[NEW CONNECTION] {addr} connected under username : {nickname}.")
    connected = True #Sets connected to TRUE
    clients.append(client)
    try:
        while connected: #While connected is TRUE, it will execute following code:
            msg_length = client.recv(HEADER).decode(FORMAT) #Recieves encoded message
            if msg_length:
                msg_length = int(msg_length)                     #Decodes message sent by client
                msg = client.recv(msg_length).decode(FORMAT) 
                if msg == DISCONNECT_MESSAGE: #if user sends 'DISCONNECT_MESSAGE'
                    clients.remove(client)   #Remove client from 'clients' list
                    connected = False #Sets 'connected' variable to False
                    
                broadcast(f"[{nickname}] {msg}") #Broadcasts to all clients the full message using 'broadcats()' function
                
        client.close() #Close connection between server and client if connected == False
    except Exception: #On exception raise, following code is executed
        client.send("[SERVER-SIDE] An error has occured".encode(FORMAT)) #If an error occurs this message is sent to the client that raised the error.

def start():
    
    server.listen() #Listen to all connections
    print(f"[LISTENNING] Server is listennig on : {socket.gethostname()} : {SERVER}") #Prints out DEBUG info
    while True: #Always Loop
        client, addr = server.accept() #Stores ever new client's Ip address and port number
        client.send("GET_username".encode(FORMAT)) #Sends 'GET_username' request to client
        nickname = client.recv(2048).decode(FORMAT) #Stores client's 'GET_username' response
        thread = threading.Thread(target=handle_client, args=(client, addr, nickname))
        thread.start() #Runs a new thread : 'handle_client()'
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}") #Prints out active connections count

>>>>>>> 9f340a19be38713a6dcfd027b0a88cb933fb2da0
start() #Runs 'start()' function