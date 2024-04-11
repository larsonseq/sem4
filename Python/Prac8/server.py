import socket

s = socket.socket()
print("Socket created")

# Bind to a specific address and port
s.bind(('localhost', 9999))

# Listen for incoming connections, with a maximum of 3 clients in the q 
s.listen(3)
print("Waiting for connection")

while True:
    # Accept a connection, get the client socket and address
    c, addr = s.accept()
    print("Connected:", addr)
    
    # Send a welcome message to the client
    c.send(bytes("Welcome", 'utf-8'))
    
    # Receive data from the client (assuming the client sends a name) 
    name = c.recv(1024).decode()
    print("Client name:", name)
    
    txt = c.recv(1024).decode()
    print(f"Message from {name} is {txt}")
    
    c.send(bytes(f"Thanks {name}, received your message", 'utf-8'))
    
    # Close the client socket
    c.close()
