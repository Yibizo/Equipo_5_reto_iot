import serial

ser = serial.Serial('COM5', 9600)
while True:
    lineBytes = ser.readline()
    line = lineBytes.decode("ascii").rstrip()
    hr_milis = line.split()
    hr = int(hr_milis[0].split(':')[1])
    milis = int(hr_milis[1].split(':')[1])
    print(hr, milis)