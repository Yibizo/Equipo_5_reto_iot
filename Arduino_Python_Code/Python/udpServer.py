import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("0.0.0.0", 1337))

while True:
    try:
        data = s.recv(1024).decode('ascii').rstrip()
        data_split = data.split(";")
        hr = int(data_split[0].split(":")[1])
        milis = int(data_split[1].split(":")[1])

        print(hr, milis)
    except:
        continue