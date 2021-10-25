#Huy Khoi Nguyen 500954699
import socket

#create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#bind the socket to the port on the localhost server
s.bind((socket.gethostname(), 5555))
#queqe = 5
s.listen(5)

#connect this to the other endpoint
clientsocket, address = s.accept()
print(f"Connection from {address} has been established!")
#send the message to the client
clientsocket.send(bytes("Welcome to the server!", "utf-8"))
print("Press number 1-5 to choose the speed")

while True:
    #recieve input from client
    data = clientsocket.recv(1024)
    if not data: break
    #print the input
    print(data)
clientsocket.close()