from socket import*
serverName=gethostname()
serverPort=12000
clientSocket=socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
fname=input("Enter file name and the word separated by space: ")
clientSocket.send(fname.encode())
contents=clientSocket.recv(1024).decode('utf8')

print(contents)
clientSocket.close()
