import socket

serverMac = 'C2:F1:03:05:09:79'
serverPrt = 1

serverMac = 'E2:F1:03:05:09:79'
serverPort = 6

sock = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
sock.connect((serverMac, serverPrt))
sleep(5)
sock.close()
