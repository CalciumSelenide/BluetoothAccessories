import bluetooth

serverMac = 'C2:F1:03:05:09:79'
serverPrt = 1

import sys

#import bluetooth


addr = serverMac

if len(sys.argv) < 2:
    print("No device specified. Searching all nearby bluetooth devices for "
          "the SampleServer service...")
else:
    addr = sys.argv[1]
    print("Searching for SampleServer on {}...".format(addr))

# search for the SampleServer service
#uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"
#service_matches = bluetooth.find_service(uuid=uuid, address=addr)

service_matches = bluetooth.find_service(address=addr)
#if len(service_matches) == 0:
#    print("Couldn't find the SampleServer service.")
#    sys.exit(0)

first_match = service_matches[0]
port = first_match["port"]
name = first_match["name"]
host = first_match["host"]

print(first_match)

print("Connecting to \"{}\" on {}".format(name, host))

# Create the client socket
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((host, 'RFCOMM'))

print("Connected. Type something...")
while True:
    data = input()
    if not data:
        break
    sock.send(data)

sock.close()
