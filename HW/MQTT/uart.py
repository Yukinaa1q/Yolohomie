import serial.tools.list_ports
import time
import mqtt
from database import Database
from model import *
TEMP = None
HUMI = None
LIGHT = None
WATER = None
NAME = None

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
# def processData( data):
    global TEMP, HUMI, LIGHT, WATER, NAME
    data = data.replace("!", "")
    data = data.replace("#", "")
    splitData = data.split(":")
    # print(splitData[1])
    if splitData[1] == "T":
        client.publish("temperature", splitData[2])
        print("Temp: ", splitData[2])
        TEMP = splitData[2]
        
    elif splitData[1] == "H":
        client.publish("humidity", splitData[2])
        HUMI = splitData[2]
        print("Humi: ", HUMI)
    elif splitData[1] == "L":
        client.publish("light", splitData[2])
        LIGHT = splitData[2]
        print("Light: ", LIGHT)
        if TEMP is not None and HUMI is not None and LIGHT is not None:
            print("Data: ", TEMP, LIGHT, HUMI)

            db.insert_data(TEMP, LIGHT, HUMI)
            TEMP = None
            HUMI = None
            LIGHT = None

    elif splitData[1] == "CamOn":
        print("Getface")
        NAME = str(get_prediction()) #will use this to get name by AI
        # NAME = "hehe"
        print("Amt,Name: ",WATER, NAME)

    elif splitData[1] == "RejectFace":
        print("RejectFace")
        db.set_last_name()
    elif splitData[1] == "WaterAmt":
        print("Water amount: ", splitData[2])
        WATER = splitData[2]
        if WATER is not None and NAME is not None:
            print("Data: ", WATER, NAME)
            db.insert_waterpump(WATER, NAME)
            WATER = None
            NAME = None
        
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
                



    # while True:


if __name__ == "uart":
    if getPort() != "None":
        ser = serial.Serial( port=getPort(), baudrate=115200)
        print(ser)
    db = Database()
    

# if __name__ == "__main__":
    # db = Database()
    # processData("!1:T:25#")
    # processData("!1:H:26#")
    # processData("!1:L:27#")
    # processData("!1:L:27#")
    # processData("!1:CamOn:#")
    # processData("!1:WaterAmt:100#")
    # processData("!1:RejectFace:#")
    
    

