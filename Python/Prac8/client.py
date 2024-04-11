import socket

c = socket.socket()
c.connect(('localhost', 9999))

# Receive and print the welcome message from the server 
print(c.recv(1024).decode())

# Get user input for the name
name = input("Enter your name: ")
txt = input("Enter a message you want to send to the server: ")

# Send the name to the server 
c.send(bytes(name, 'utf-8'))
c.send(bytes(txt, 'utf-8'))

print(c.recv(1024).decode())

# Close the client socket 
c.close()
