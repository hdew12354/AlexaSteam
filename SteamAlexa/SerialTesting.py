import serial
ser = serial.Serial('COM3', 9600)
x = ""
while True:
    x = ser.readline()
    print(x)
    if (x != ""):
        print("5")
    elif (x == "b'NEC: FF38C7\r\n'"):
        print("Sepcific")