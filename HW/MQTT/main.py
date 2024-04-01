# from adafruit_mqtt import Adafruit_MQTT
#pip install paho-mqtt==1.6.1
import paho.mqtt.client as mqtt
import time
import random
# from detect import * 
from uart import *


# def received(payload):
#     print("Receive payload from main:",payload)


# client = Adafruit_MQTT()
# new_client.setRecvCallBack(received)

counter = 5

while True:
    counter = counter - 1
    if counter <= 0:
        counter = 5
    uart_write(f"{counter}")
    #     print("ai result:",ai_result)
    #     client.publish("ai",ai_result)
        
    readSerial()
    time.sleep(2)