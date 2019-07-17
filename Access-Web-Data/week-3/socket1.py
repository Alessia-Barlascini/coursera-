import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                      # create the portal
mysock.connect(('data.pr4e.org', 80))                                           # find the receiver
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()            # ask for something
mysock.send(cmd)                                                                # se the request

while True:
    data = mysock.recv(512)                     # ask for the first 512 characters
    if len(data) < 1:                           # if there's no data break
        break
    print(data.decode())                 # print the data decoded

mysock.close()                                  # close the portal
