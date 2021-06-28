import socket
import threading      #Import modules
#################

#### Declaring variables ####
HEADER = 64 #Header in bytes
PORT = 15200 #Port number
FORMAT = 'utf-8' #Encoding protocol
DISCONNECT_MESSAGE = "!DISCONNECT" #Disconnect message to get disconnected from server
SERVER = "SERVER_IP_HERE" #Server host's Ipv4 address
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client.connect(ADDR) #Connects to 'SERVER' using 'PORT'
except Exception: #On exception raise, the following code will be executed
    print(f"[CONNECTION FAILED] Coundn't connect to : {SERVER}") #Print Error Message

username = input("What is your username ? : ") #Asks for username and stores user's input in variable
#################

def send(msg):
    message = msg.encode(FORMAT) #Encodes message
    msg_length = len(message)  #Sets msg_length to message's length    
    send_length = str(msg_length).encode(FORMAT) #Encodes message length
    send_length += b' ' * (HEADER - len(send_length)) #Adds space to message_length variable until being equal to 'HEADER'
    client.send(send_length) #Sends encoded message length using 'utf-8' protocol
    client.send(message) #Sends encoded message using 'utf-8' protocol

###############################
def process_data():
    while True: #The following code will always be executed in a loop
        try:
            message = client.recv(2048).decode(FORMAT) #Gets the broadcasted message by Server
            if message == "GET_username": #If server's request == "GET_username", the followwing code is executed 
                client.send(username.encode(FORMAT))
            elif message: #If message is equal to something
                nickname = (message.split("["))[1].split("]")[0] #Get's username
                if nickname != username: #If username not equal to this client's server, the message is printed
                    print(f"{message}")
        except Exception: #If an exception is raised, the following code will be executed
            print("[CLIENT-SIDE] An error has occured Please refresh the program...")
    
###############################   
def process_input():
    print(': "!DISCONNECT" to leave chat room')
    while True: #The following code will always be executed in a loop
        thread = threading.Thread(target=process_data, args=())
        thread.start() #Runs a new thread : 'process_data()'
        msg = input("> ") #Asks for user's input (message) and stores it in a variable
        
        if (msg != DISCONNECT_MESSAGE) and (len(msg) > 0): #If message's length is greater than 0 and isn't equal to 'DISCONNECT_MESSAGE', the following code is executed
            send(msg) #Runs 'send()' function
        if msg == DISCONNECT_MESSAGE: #If user input (message) == DISCONNECT_MESSAGE, the following code is executed
            print("You left Session")
            break #Break the loop, stop it
    
process_input() #Runs 'process_input()' function