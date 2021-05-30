import serial
import time

#Tutorial: https://www.instructables.com/id/Interface-Python-and-Arduino-with-pySerial/

baudRate = 9600
serialRead = serial.Serial("COM7", baudRate) #Create connection on serial port

counter = 32

def readFromSerial(bytes):
    firstString = serialRead.read(bytes)
    return firstString

def printSerialReading(bytes):
    for i in range(bytes):
        serialReading = readFromSerial(1)
        print(str(time.time()) + "Raw -> " + str(serialReading) + " | Decoded -> " + str(serialReading.decode('Latin-1')))
    print("\n")

print(serialRead.isOpen())
while True:
    print("Input String: ")
    stringToWrite = str(input()).encode('Latin-1')
    serialRead.write(stringToWrite)
    print("Writing: " + stringToWrite.hex())
    serialRead.flush()
    printSerialReading(10)
    serialRead.flush()
    print(""),

    