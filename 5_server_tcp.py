from socket import*
serverName=gethostname()
serverPort=12000
serverSocket=socket(AF_INET,SOCK_STREAM)
serverSocket.bind((serverName,serverPort))
serverSocket.listen(1)
print("The Server is ready to recieve")
while(1):
    count=0
    conn,addr=serverSocket.accept()
    fname_word=conn.recv(1024).decode()
    l1=[]
    l1=fname_word.split(" ")
    file=open(l1[0],"r")
    contents=file.read(1024)
    l2=[]
    l2=contents.split(" ")
    for i in l2:
        if(l1[1]==i):
            count+=1
    print(count)
    conn.send(str(count).encode('utf8'))
    file.close()
    conn.close()
