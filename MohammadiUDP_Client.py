import socket
import time
import sys

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_address = ('localhost', 12000)
clientSocket.settimeout(1)
ping = 1

try:
    for ping in range(1, 11):
        start = time.time()
        outputData = 'Ping #' + str(ping) + " " + time.ctime(start)
        try:
            clientSocket.sendto(outputData.encode(), client_address)
            data, server = clientSocket.recvfrom(1024)
            print("Reply From 127.0.0.1: " + outputData)
            end = time.time()
            elapsed = end - start
            print("RTT:" + str(elapsed) + "seconds\n")
        except socket.timeout:
            print("#" + str(ping) + " Request Timed Out\n")

except IOError:
    print("System Error")
    print("Server Socket Not Found")
clientSocket.close()
sys.exit()
