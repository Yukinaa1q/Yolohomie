import paho.mqtt.client as mqtt
import time
import uart

class MQTTController:
    def __init__(self, server, port, username, password, topic_pub1, topic_pub2, topic_pub3, topic_pub4, topic_sub):
        self.MQTT_SERVER = server
        self.MQTT_PORT = port
        self.MQTT_USERNAME = username
        self.MQTT_PASSWORD = password
        self.MQTT_TOPIC_PUB1 = topic_pub1
        self.MQTT_TOPIC_PUB2 = topic_pub2
        self.MQTT_TOPIC_PUB3 = topic_pub3
        self.MQTT_TOPIC_PUB4 = topic_pub4
        self.MQTT_TOPIC_SUB = topic_sub
        self.mqttClient = mqtt.Client()
        self.mqttClient.username_pw_set(username, password)
        self.mqttClient.connect(server, int(port), 60)
        self.mqttClient.on_connect = self.mqtt_connected
        self.mqttClient.on_subscribe = self.mqtt_subscribed
        self.mqttClient.on_message= self.mqtt_recv_message

        # self.mqttClient.on_publish = self.mqtt_published
        self.mqttClient.loop_start()

    def mqtt_connected(self, client, userdata, flags, rc):
        print("Connected successfully!!")
        client.subscribe(self.MQTT_TOPIC_SUB)

    def mqtt_subscribed(self, client, userdata, mid, granted_qos):
        print("Subscribed to Topic!!!")

    # def mqtt_published(self, client, userdata, mid):
    #     print("Message published with mid: " + str(mid))
    
    def mqtt_recv_message(self,client, userdata, message):
        if message.topic == f"{self.MQTT_TOPIC_PUB4}":
            if(message.payload.decode("utf-8") == "0"):
                uart.write_data(1)
            elif(message.payload.decode("utf-8") == "1"):
                uart.write_data(2)
            elif(message.payload.decode("utf-8") == "2"):
                uart.write_data(3)
            elif(message.payload.decode("utf-8") == "3"):
                uart.write_data(4)
        print("Received message " + message.payload.decode("utf-8")
            + " on topic '" + message.topic
            # + "' with QoS " + str(message.qos)
        )
        # elif message.topic == f"{MQTT_TOPIC_PUB}/humidity":
        #     print("Received message " + message.payload.decode("utf-8")
        #         + " on topic '" + message.topic  + "\n"
        #         # + "' with QoS " + str(message.qos)
        #         )


    def publish(self,channel, data):
        if "humi" in channel:
            self.mqttClient.publish(self.MQTT_TOPIC_PUB1, data)
        elif "temp" in channel:
            self.mqttClient.publish(self.MQTT_TOPIC_PUB2, data)
        elif "light" in channel:
            self.mqttClient.publish(self.MQTT_TOPIC_PUB3, data)
        elif "door" in channel:
            self.mqttClient.publish(self.MQTT_TOPIC_PUB4, data)

# Example usage:
# def main():
#     pass
    # counter = 5
    # while True:
    #     time.sleep(1)
    #     if counter == 0:
    #         counter = 5
    #     counter -= 1
    #     mqtt_controller.publish_data(counter, counter*2, counter*3, counter*4)

# if __name__ == "main":
    # mqtt_controller = MQTTController("mqtt.ohstem.vn", 1883, "thinhdadn", "hehe",
    #                                     "thinhdadn/feeds/V2/humidity", 
    #                                     "thinhdadn/feeds/V2/temperature",
    #                                     "thinhdadn/feeds/V2/light", 
    #                                     "thinhdadn/feeds/V2/door",
    #                                     "thinhdadn/feeds/V2/#")
    # main()
