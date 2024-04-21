#pip install paho-mqtt==1.6.1
import paho.mqtt.client as mqtt
import time
import random
from mqtt import *
# from uart import *

#declare MQTT client
client = MQTTController("mqtt.ohstem.vn", 1883, "thinhdadn", "hehe",[],
                                        "thinhdadn/feeds/V2/#")


# start define your topics here
feedArray = ["humidity","temperature","sun","door","lights","fan"]

#assign topic to MQTTclient
for feed in feedArray:
    client.declare_topic(f"thinhdadn/feeds/V2/{feed}")
print(client.get_all_topics())


while True:
    pass
    # print("\nChoose your topic ")
    # for topic in feedArray:
    #     print(f"{feedArray.index(topic)} . {topic} ")
    # topicIdx = int(input("Enter topic number: "))
    # data = input("Enter data: ")

    #publish data to MQTT broker
    # client.publish(feedArray[topicIdx],data)
# while True:
#     counter = counter - 1
#     if counter <= 0:
#         counter = 5
#     # print("Counter:",counter)
#     # uart_write(f"{counter}")
#     #     print("ai result:",ai_result)
#     #     client.publish("ai",ai_result)
        
    # readSerial(client,ser)
    # time.sleep(1)