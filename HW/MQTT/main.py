# from adafruit_mqtt import Adafruit_MQTT
#pip install paho-mqtt==1.6.1
import paho.mqtt.client as mqtt
import time
import random
from mqtt import *
from uart import *


# def received(feed_id,payload):
#     print(f"Receive feed_id from :",feed_id)
#     print(f"Receive payload from :",payload)
#     if feed_id == "thinhdadn/feeds/V2/door":
#         if payload == "0":
#             # write_data(1)
#             print("receive 0")
#         if payload == "1":
#             print("receive 1")
#             # write_data(2)
#     # elif feed_id == "nutnhan2":
#     #     if payload == "0":
#     #         write_data(3)
#     #     if payload == "1":
#     #         write_data(4)
#     pass


client = MQTTController("mqtt.ohstem.vn", 1883, "thinhdadn", "hehe",
                                        "thinhdadn/feeds/V2/humidity", 
                                        "thinhdadn/feeds/V2/temperature",
                                        "thinhdadn/feeds/V2/light", 
                                        "thinhdadn/feeds/V2/door",
                                        "thinhdadn/feeds/V2/#")

# receive callback 
# client.setRecvCallBack(received)




counter = 4

while True:
    time.sleep(2)
    readSerial(client,ser)

    if counter == 0:
        counter = 4
    counter -= 1
    client.publish("door", counter)

# while True:
#     counter = counter - 1
#     if counter <= 0:
#         counter = 5
#     # print("Counter:",counter)
#     # uart_write(f"{counter}")
#     #     print("ai result:",ai_result)
#     #     client.publish("ai",ai_result)
        
#     # readSerial()
#     time.sleep(1)