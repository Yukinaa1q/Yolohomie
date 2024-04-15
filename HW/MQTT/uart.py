import serial.tools.list_ports
import time
import mqtt

def getPort():
    ports = serial.tools.list_ports.comports()
    N = len(ports)
    commPort = "None"
    for i in range(0, N):
        port = ports[i]
        strPort = str(port)
        if "usb" in strPort:
            splitPort = strPort.split(" ")
            commPort = (splitPort[0])
    return commPort
    # return "COM3"
    # return "/dev/tty.usbserial-2130"
    # return "/dev/ttys014"




def write_data(data):
    ser.write(str(data).encode())
    print("Write data to COM:",data)
    pass

def processData(client, data):
    data = data.replace("!", "")
    data = data.replace("#", "")
    splitData = data.split(":")
    print(splitData)
    if splitData[1] == "T":
        client.publish("temp", splitData[2])
    elif splitData[1] == "H":
        client.publish("humi", splitData[2])
    elif splitData[1] == "L":
        client.publish("light", splitData[2])
        
mess = ""
def readSerial(client,ser):
    bytesToRead = ser.inWaiting()
    if (bytesToRead > 0):
        global mess
        mess = mess + ser.read(bytesToRead).decode("UTF-8")
        # print(mess)
        while ("#" in mess) and ("!" in mess):
            start = mess.find("!")
            end = mess.find("#")
            # print(mess[start:end + 1])
            processData(client, mess[start:end + 1])
            if (end == len(mess)):
                mess = ""
            else:
                mess = mess[end+1:]
                

def main():
    pass

    # while True:


if __name__ == "uart":
    if getPort() != "None":
        ser = serial.Serial( port=getPort(), baudrate=115200)
        print(ser)
