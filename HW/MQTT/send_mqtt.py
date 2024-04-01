#pip install paho-mqtt==1.6.1
import paho.mqtt.client as mqtt
import time

MQTT_SERVER = "mqtt.ohstem.vn"
MQTT_PORT = 1883
MQTT_USERNAME = "thinhdadn"
MQTT_PASSWORD = "hehe"
MQTT_TOPIC_PUB1 = MQTT_USERNAME + "/feeds/V2/humidity"
MQTT_TOPIC_PUB2 = MQTT_USERNAME + "/feeds/V2/temperature"
MQTT_TOPIC_PUB3 = MQTT_USERNAME + "/feeds/V2/light"
MQTT_TOPIC_PUB4 = MQTT_USERNAME + "/feeds/V2/door"

MQTT_TOPIC_SUB = MQTT_USERNAME + "/feeds/V2"


def mqtt_connected(client, userdata, flags, rc):
    print("Connected succesfully!!")
    client.subscribe(MQTT_TOPIC_SUB)

def mqtt_subscribed(client, userdata, mid, granted_qos):
    print("Subscribed to Topic!!!")

# # def mqtt_recv_message(client, userdata, message):
#     print("Received: ", message.payload.decode("utf-8"))
#     print(" Received message " + message.payload.decode("utf-8")
#           + " on topic '" + message.topic
#           + "' with QoS " + str(message.qos))

def mqtt_published(client, userdata, mid):
    print("Message published with mid: " + str(mid))

mqttClient = mqtt.Client()
mqttClient.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
mqttClient.connect(MQTT_SERVER, int(MQTT_PORT), 60)

#Register mqtt events
mqttClient.on_connect = mqtt_connected
mqttClient.on_subscribe = mqtt_subscribed
# mqttClient.on_message = mqtt_recv_message
mqttClient.on_publish = mqtt_published

mqttClient.loop_start()

counter = 5
while True:
    time.sleep(1)
    if counter == 0 :
        counter = 5
    counter -= 1   
    # if counter < 5 : 
    mqttClient.publish(MQTT_TOPIC_PUB1, counter)
    mqttClient.publish(MQTT_TOPIC_PUB2, counter*2)
    mqttClient.publish(MQTT_TOPIC_PUB3, counter*3)
    mqttClient.publish(MQTT_TOPIC_PUB4, counter*4)