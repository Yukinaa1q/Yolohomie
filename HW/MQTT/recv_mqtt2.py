import paho.mqtt.client as mqtt
import time

MQTT_SERVER = "mqtt.ohstem.vn"
MQTT_PORT = 1883
MQTT_USERNAME = "thinhdadn"
MQTT_PASSWORD = "hehe"
MQTT_TOPIC_PUB = MQTT_USERNAME + "/feeds/V2"
MQTT_TOPIC_SUB = MQTT_USERNAME + "/feeds/V2/#"  # Using "#" to subscribe to all subtopics under "V2"


def mqtt_connected(client, userdata, flags, rc):
    print("Connected succesfully!!")
    client.subscribe(MQTT_TOPIC_SUB)


def mqtt_subscribed(client, userdata, mid, granted_qos):
    print("Subscribed to Topic!!!")


def mqtt_recv_message(client, userdata, message):
    if message.topic == f"{MQTT_TOPIC_PUB}/light":
        print("Received message " + message.payload.decode("utf-8")
            + " on topic '" + message.topic
            # + "' with QoS " + str(message.qos)
            )
    # # elif message.topic == f"{MQTT_TOPIC_PUB}/humidity":
    #     print("Received message " + message.payload.decode("utf-8")
    #         + " on topic '" + message.topic  + "\n"
    #         # + "' with QoS " + str(message.qos)
    #         )



mqttClient = mqtt.Client()
mqttClient.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
mqttClient.connect(MQTT_SERVER, int(MQTT_PORT), 60)


# Register mqtt events
mqttClient.on_connect = mqtt_connected
mqttClient.on_subscribe = mqtt_subscribed
mqttClient.on_message= mqtt_recv_message

mqttClient.loop_start()

while True:
    time.sleep(1000)
